# En el contexto del punto de venta (tienda) se manejan los siguientes eventos:
# - handle_on_tap: Evento tap de la barra de búsqueda (si existe)
# - handle_on_change: Evento de búsqueda en tiempo real
# - handle_on_add_button_click: Evento de click en el botón de la tarjeta
# - handle_on_card_button_click: Evento de click en el botón de la tarjeta
# - handle_on_remove_button_click: Evento de click en el botón de la tarjeta (de la lista de compra)
# - handle_on_clear_button_click: Evento de click en el botón de limpiar la lista de compra
# - handle_on_process_button_click: Evento de click en el botón de procesar la compra

# TODO: Evitar que se agreguen productos (cards) duplicados en la lista de compra: Esto debe estar listo antes de implementar el evento para procesar la compra
# TODO: Calculo del total de la compra
# TODO: Implementar funciones en la base de datos para que al procesar la compra, se actualice el inventario
# TODO: Guardar la compra en la base de datos
# TODO: Permitir que los productos puedan ser ordenados en función de ciertas propiedades
# TODO: Permitir que los productos puedan ser filtrados en función de ciertas propiedades

import flet as ft

from business_classes.Product                           import Product
from components.ProductList                             import ProductList
from components.ShoppingCart                            import ShoppingCart
from controllers.dto_controllers.product_dto_controller import ProductDTOController
from components.product_cards                           import ProductCard, ProductCardFactory, CardType


# HANDLERS ---------------------------------------------------------------------


def handler_on_remove_button_card_click(event: ft.ControlEvent): # Al presionar en el botón de remover
    button = event.control
    card: ProductCard = button.data['card']
    shopping_cart.remove_product_card(card)
    shopping_cart.update()

def handler_on_add_button_card_click(event: ft.ControlEvent): # Al presionar en el botón de añadir
    button = event.control
    product: Product = button.data['product']
    card: ProductCard = cards_factory.create_product_card(
        product=product,
        card_type=CardType.SELLING,
        on_button_card_click=handler_on_remove_button_card_click
    )
    shopping_cart.add_product_card(card)
    shopping_cart.update()

def handler_on_clear_button_click(event: ft.ControlEvent): # Al presionar en el botón de limpiar
    shopping_cart.clear_product_list_cards()
    shopping_cart.update()

def handler_on_process_button_click(event: ft.ControlEvent): # Al presionar en el botón de procesar
    pass

def handler_on_searcher_tap(event: ft.ControlEvent): # Al presionar en la barra de búsqueda
    searcher.close_view('')
    product_list_view.product_cards = [
        cards_factory.create_product_card(
            product=product,
            card_type=CardType.DISPLAY,
            on_button_card_click=handler_on_add_button_card_click
        ) for product in product_controller.get_all()
    ]
    product_list_view.update()

def handle_on_searcher_change(event: ft.ControlEvent): # Al cambiar el texto en la barra de búsqueda
    search_term = searcher.value
    results = product_controller.search(str(search_term))
    if results:
        product_list_view.product_cards = [
            cards_factory.create_product_card(
                product=product,
                card_type=CardType.DISPLAY,
                on_button_card_click=handler_on_add_button_card_click
            ) for product in results
        ]
        product_list_view.update()

# CONTEXT ----------------------------------------------------------------------
cards_factory = ProductCardFactory()
product_controller = ProductDTOController()

searcher = ft.SearchBar( # Barra de búsqueda
    bar_hint_text='Buscar producto',
    height=40,
    bar_leading=ft.Icon(ft.icons.SEARCH, size=20),
    on_tap=handler_on_searcher_tap,
    on_change=handle_on_searcher_change
)
product_list_view = ProductList()
product_list_view.product_cards = [
    cards_factory.create_product_card(
        product=product,
        card_type=CardType.DISPLAY,
        on_button_card_click=handler_on_add_button_card_click
    ) for product in product_controller.get_all()
]
shopping_cart = ShoppingCart(
    on_clear_button_click=handler_on_clear_button_click
)

# SHAPE CONTENT-----------------------------------------------------------------

StoreShape = ft.ResponsiveRow( # Capa general de la vista
    [
        ft.Column( # Capa de búsqueda y productos
            [
                ft.Container( # Capa de búsqueda
                    height=50,
                    content=searcher,
                ),
                ft.Container( # Capa de productos
                    content=product_list_view,
                    expand=True,
                ),
            ],
            col=7.5,
        ),
        ft.Container( # Capa de formulario
            content=shopping_cart,
            expand=True,
            col=4.5,
        ),
    ],
    spacing=0,
)
