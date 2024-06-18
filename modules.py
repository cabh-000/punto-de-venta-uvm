from flet import icons as icon
from package_navigation.Module import Module, Section
from inventory_view.view_section import ContentStockSectionShape as ProductSection
from suppliers_view.view_section import ContentStockSectionShape as SupplierSection
from purchase_view.context import shape
from store_view.context import StoreShape


Module(
    'Compras',
    icon.SHOPPING_CART,
    Section(label='Proveedores', icon=icon.PEOPLE, content=SupplierSection()),
    Section(label='Compras', icon=icon.SHOPPING_BAG, content=shape),
)

Module(
    'Punto de venta', # Module name
    icon.POINT_OF_SALE_SHARP, # Module icon
    Section(label='Tienda', icon=icon.STOREFRONT,content=StoreShape),
    Section(label='Inventario', icon=icon.INVENTORY, content=ProductSection()),
    Section(label='Ventas', icon=icon.SAILING_SHARP),
)
