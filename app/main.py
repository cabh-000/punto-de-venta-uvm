import flet as ft

from page.navigation.navigation_components import NavigationComponentsFactory
from page.navigation.builder import Module
from page.modules import (
    purchase_module,
    inventory_module,
    pos_module,
    sales_module,
)


def main(page: ft.Page):

    page.theme_mode = ft.ThemeMode.LIGHT  # Se remplaza por las preferencias de usuario
    page.scroll = ft.ScrollMode.AUTO
    page.window_maximized = True
    
    modules = Module.all
    factory = NavigationComponentsFactory(modules)

    page.navigation_bar = factory.build_navigation_bar()
    page.appbar         = factory.build_appbar()
    page.drawer         = factory.build_drawer()
    
    factory.build_content(page)

    page.update()

ft.app(target=main)
