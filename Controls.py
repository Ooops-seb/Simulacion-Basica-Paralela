import flet as ft

class Process():
    
    def play_event(e):
        print("Play_button pressed")
        
    def pause_event(e):
        print("stop_button pressed")

    def stop_event(e):
        print("stop_button pressed")
    
    play_button_enable = False
    pause_button_enable = False
    stop_button_enable = True
    
    play_button = ft.IconButton(
        icon=ft.icons.PLAY_ARROW,
        icon_color="blue",
        icon_size=25,
        tooltip="Iniciar",
        on_click=play_event,
        disabled = play_button_enable,
    )
    
    pause_button = ft.IconButton(
        icon=ft.icons.PAUSE,
        icon_color="blue",
        icon_size=25,
        tooltip="Pausar",
        on_click=pause_event,
        disabled = pause_button_enable,
    )
    
    stop_button = ft.IconButton(
        icon=ft.icons.STOP,
        icon_color="red",
        icon_size=25,
        tooltip="Detener",
        on_click=stop_event,
        disabled = stop_button_enable,
    )
    
    def __init__(self, count:int) -> ft.Container:
        ft.Container(
            ft.Column(
                [
                    ft.Text(value=f"Proceso: {count}"),
                    ft.Container(
                        ft.Row(
                            [
                                self.play_button,
                                self.pause_button,
                                self.stop_button,
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                        border=ft.border.all(1, '#FFFFFF'),
                        border_radius=ft.border_radius.all(10),
                    ),
                    ft.Container(
                        ft.Column(
                            [
                                ft.Text(value="Procesando..."),
                                ft.Text(value="Procesando..."),
                                ft.Text(value="Procesando..."),
                                ft.Text(value="Procesando..."),
                                ft.Text(value="Procesando..."),
                                ft.Text(value="Procesando..."),
                                ft.Text(value="Procesando..."),
                                ft.Text(value="Procesando..."),
                                ft.Text(value="Procesando..."),
                                ft.Text(value="Procesando..."),
                                ft.Text(value="Procesando..."),
                                ft.Text(value="Procesando..."),
                            ],
                            width = 300,
                            scroll=ft.ScrollMode.AUTO,
                            alignment=ft.MainAxisAlignment.CENTER
                        ),
                        height=200,
                        bgcolor='#262626',
                        border=ft.border.all(1, '#383838'),
                        border_radius=ft.border_radius.all(10),
                    ),
                    ft.Text(value=f"Velocidad: x{count}"),
                    ft.Container(
                        ft.Row(
                            [
                                ft.Text(value="Estado:"),
                                ft.Text(value="estado...")
                            ],
                            alignment=ft.MainAxisAlignment.START,
                        ),
                        margin=10,
                    ),
                ],
                spacing=10,
                alignment=ft.MainAxisAlignment.START,
            ),
            padding=20,
            width=300,
            bgcolor='#262626',
            border=ft.border.all(1, '#B21200'),
            border_radius=ft.border_radius.all(10),
            margin=20,
        )