"""
En este archivo declaramos todos los módulos que se mostrarán en la aplicación.
La filtración de módulos que dependen de un usuario ocurre en otro lugar. Aquí
hacemos la declaración y los empaquetamos para que puedan intercambiarse en 
tiempo de ejecución
"""

from ..packages.moduibuilder import Module, Section
from ..content.purchase_module import purchase_content, inventory_content, providers_content
# from ..content.inventory_module import inventory_content ... todo su contenido

from typing import List
import flet as ft


# DECLARACIÓN DE MÓDULOS

module = Module

_purchase_module = module(
    'Compras',
    ft.icons.SHOP,
    Section(name='Compras', icon=ft.icons.SHOPPING_CART, content=purchase_content),
    Section(name='Inventario', icon=ft.icons.INVENTORY, content=inventory_content),
    Section(name='Proveedores', icon=ft.icons.PEOPLE, content=providers_content),
)

_inventory_module = module(
    'Inventario',
    ft.icons.INVENTORY,
    Section(name='Productos', icon=ft.icons.ARTICLE),
    Section(name='Categorías', icon=ft.icons.TAG),
    Section(name='Stock mínimo', icon=ft.icons.PRODUCTION_QUANTITY_LIMITS),
)

_customers_module = module(
    'Clientes',
    ft.icons.PEOPLE,
    Section(name='Clientes', icon=ft.icons.PEOPLE),
    Section(name='Grupos', icon=ft.icons.GROUP),
    Section(name='Descuentos', icon=ft.icons.DISCOUNT),
)
