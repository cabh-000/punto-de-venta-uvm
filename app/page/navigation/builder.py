from typing import List
import flet as ft


class Rail(ft.NavigationDestination):

    def __init__(self, name: str, icon: str) -> None:
        super().__init__()
        self.label = name
        self.icon = icon
    

class Section(ft.NavigationDrawerTheme):
    
    def __init__(
            self,
            name: str = 'Undefined',
            icon: str = ft.icons.NOT_ACCESSIBLE,
            content: ft.Control = ft.Column(controls=[ft.Text('None')])
    ) -> None:
        super().__init__()
        self._name = name
        self._icon = icon
        self._content = content
    
    @property
    def content(self) -> ft.Control:
        return self._content
    
    def __repr__(self):
        return f'{self.__class__.__name__}(name={self._name})'
    
    def build(self) -> ft.NavigationDrawerDestination:
        return ft.NavigationDrawerDestination(
            label=self._name,
            icon=self._icon,
        )
    

class Module:
    """
    Las aplicaciones para las que está pensado este framework son aplicaciones en las que se debe
    navegar entre módulos globales y secciones más detalladas. Esta clase representa un módulo en la aplicación
    que consta de ``Rail`` y una lista de ``Section`` que permitirán la nevegación entre módulos y secciones.

    ### Argumentos

    - ``name (str)``: El nombre del módulo.
    - ``icon (str)``: El ícono que represent
    - ``sections (List[Section])``: Las secciones que pertenecen al módulo.

    ### Propiedades

    - ``name (str)``: El nombre del módulo.
    - ``rail (Rail)``: El ``Rail`` que representa el módulo en el ``ft.NavigationBar``.
    - ``sections (List[Section])``: Las secciones que pertenecen al módulo.

    Podemos acceder a las propiedades con el uso de @property como accesores.
    Para renderizar el ``Rail`` deberemos llamar al método ``build`` de la clase ``Rail``.
    De esta forma podremos usarlo en el ``ft.NavigationBar``.

    En el caso de la lista de secciones, tendremos que iterar primeramente la lista de 
    secciones del módulo y llamar al método ``build`` de cada una de las secciones.
    Es preferible usar comprensión de listas para este propósito.

    ``[section.build() for section in module.sections]``

    ### Declaración de módulos 

    Para lograr la modularidad en una aplicación, es importante separar los módulos en archivos separados 
    donde podamos identificar claramente que estamos creando un módulo con ciertas secciones para la aplicación.
    Podemos declarar esta intención de la siguiente manera:

    ```python

    PurchaseModule = Module(
        'Compras',
        ft.icons.SHOP,
        Section('Compras', ft.icons.SHOPPING_CART),
        Section('Inventario', ft.icons.INVENTORY),
        Section('Proveedores', ft.icons.PEOPLE),
    )
    ```
    """

    all: List['Module'] = []

    def __init__(self, name: str, icon: str, *sections: Section) -> None:
        if not sections:
            sections = (
                Section(),
                Section(),
                Section(),
            )
        self._name = name
        self._rail = Rail(name, icon)
        self._sections = sections
        Module.all.append(self)
        # NOTE: Usar Module, en lugar de self, permite el acceso global, incluso a las subclases.
        # Si una subclase heredara de Model y estamos usando self, entonces la subclase no tendría acceso
        # a la lista de módulos. Por eso se usa Module en lugar de self.
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def rail(self) -> Rail:
        """Debe llamar al método ``build`` para obtener el objeto ``ft.NavigationDestination``."""
        return self._rail
    
    @property
    def sections(self) -> tuple[Section, ...]:
        """ 
        Se debe desempaquetar y luego llamar al método ``build`` para obtener el
        objeto ``ft.NavigationDrawerDestination``.
        """
        return self._sections
    
    def __repr__(self) -> str:
        return f'Module(name={self.name}, sections={self._sections})'
