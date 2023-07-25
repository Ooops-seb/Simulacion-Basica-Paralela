from flet import (
    Page,
    IconButton,
    Row,
    Column,
    Text,
    Container,
    MainAxisAlignment,
    Image,
    icons,
    border
)
from Events import EventHandlers

class Index:
    
    def __init__(self, page: Page):
        
        self.page = page
        self.event_handler = EventHandlers(page)
        
        self.window_buttons = Container(
            Row(
                [
                    IconButton(
                        icon=icons.MINIMIZE,
                        icon_color="gray",
                        icon_size=20,
                        tooltip="Minimizar",
                        on_click=self.event_handler.minimize_event
                    ),
                    IconButton(
                        icon=icons.CLOSE,
                        icon_color="red",
                        icon_size=20,
                        tooltip="Cerrar",
                        on_click=self.event_handler.close_window,
                    ),
                ],
                spacing=0,
            )
        )
        
        title_bar = Container(
            Row(
                [
                    Text(
                        value='Proyecto final | Computación Paralela'                    
                    ),
                    self.window_buttons,
                ],
                spacing=0,
                alignment=MainAxisAlignment.SPACE_BETWEEN,
            ),
            border=border.all(1, '#2E4C06'),
            bgcolor='#162504',
            margin=-10,
            padding=0,
        )
        
        header = Container(
            Row(
                [
                    Image(
                        src='../assets/img/logo-espe.png',
                        width=100,
                        height=100,
                    ),
                    Column(
                        [
                            Text(value='Universidad de las Fuerzas Armadas', font_family='Allura', scale=3),
                            Text(value='ESPE - Sede Latacunga', font_family='Poppins', scale=1),
                        ],
                    ),
                    Image(
                        src='../assets/img/logo-software.png',
                        width=100,
                        height=100,
                    ),
                ],
                alignment=MainAxisAlignment.SPACE_BETWEEN,
            ),
            padding=10,
        )
        
        #Botones de control de procesos
        add_button = IconButton(
            icon=icons.ADD,
            icon_color="gray",
            icon_size=25,
            tooltip="Agregar proceso",
            on_click=self.event_handler.show_bs,
            #disabled = add_button_enable,
        )
        
        delete_button = IconButton(
            icon=icons.DELETE_SHARP,
            icon_color="red",
            icon_size=25,
            tooltip="Eliminar",
            on_click=self.event_handler.delete_event,
            #disabled = delete_button_enable,
        )
        
        play_button = IconButton(
            icon=icons.PLAY_ARROW,
            icon_color="blue",
            icon_size=25,
            tooltip="Iniciar",
            on_click=self.event_handler.play_event,
            #disabled = play_button_enable,
        )
        
        pause_button = IconButton(
            icon=icons.PAUSE,
            icon_color="blue",
            icon_size=25,
            tooltip="Pausar",
            on_click=self.event_handler.pause_event,
            #disabled = pause_button_enable,
        )
        
        stop_button = IconButton(
            icon=icons.STOP,
            icon_color="red",
            icon_size=25,
            tooltip="Detener",
            on_click=self.event_handler.stop_event,
            #disabled = stop_button_enable,
        )
        
        process_controls = Container(
            Row(
                [
                    Text(value="Control de procesos:", font_family="Poppins"),
                    add_button,
                    delete_button,
                ],
                alignment=MainAxisAlignment.CENTER,
            ),
        )
        
        body_content = Container(
            Column(
                [
                    process_controls,
                ],
                alignment=MainAxisAlignment.SPACE_BETWEEN,
            ),
            #border=ft.border.all(1, '#383838'),
            #border_radius=ft.border_radius.all(10),
            padding=20,
        )
        
        self.app_content = Container(
            Column(
                [
                    title_bar,
                    header,
                    body_content
                ],
            ),
        )