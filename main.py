import flet as ft

process_items = []
count = 0
add_button_enable = False
play_button_enable = False
pause_button_enable = False
stop_button_enable = True
delete_button_enable = True

def main(page: ft.Page):
    global add_button_enable, pause_button_enable, stop_button_enable, delete_button_enable, play_button_enable
    
    page.fonts = {
        "Allura": "..\\assets\\fonts\\Allura-Regular.ttf",
        "Poppins": "..\\assets\\fonts\\Poppins-Regular.ttf"
    }

    page.window_title_bar_hidden = True
    page.window_prevent_close = True
    page.window_maximized = True
    page.auto_scroll = True
    page.window_center()
    
    ##EVENTOS
    def add_event(e):
        global count, delete_button_enable
        if (count >= 0):
            count+=1
            process_items.append(
                ft.Container(
                    ft.Column(
                        [
                            ft.Text(value=f"Proceso: {count}"),
                            ft.Container(
                                ft.Row(
                                    [
                                        play_button,
                                        pause_button,
                                        stop_button,
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
            )
            if(count == 0):
                delete_button_enable = True
            if (count > 0):
                delete_button_enable = False
            delete_button.disabled = delete_button_enable
            delete_button.update()
            process_container.update()
            close_bs()
            show_snack_bar('Proceso agregado!')

    def play_event(e):
        page.update()
        
    def pause_event(e):
        page.update()

    def stop_event(e):
        page.update()

    def delete_event(e):
        global count, delete_button_enable
        count-=1
        del process_items[0]
        
        if(count == 0):
            delete_button_enable = True
            
        delete_button.disabled = delete_button_enable
        delete_button.update()
        process_container.update()
        show_snack_bar('Proceso eliminado!')
        
    def minimize_event(e):
        page.window_minimized = True
        page.update()

    def close_window(e):
        page.dialog = confirm_dialog
        confirm_dialog.open = True
        page.update()

    def yes_click(e):
        page.window_destroy()

    def no_click(e):
        confirm_dialog.open = False
        page.update()
    
    def show_snack_bar(msg):
        page.snack_bar = ft.SnackBar(ft.Text(f"{msg}"))
        page.snack_bar.open = True
        page.snack_bar.duration = int(1000)
        page.update()
        
    def close_alert(e):
        load_data_modal.open = False
        page.update()

    def load_data_modal_event(e):
        page.dialog = load_data_modal
        load_data_modal.open = True
        page.update()
    
    def show_bs(e):
        bs.open = True
        bs.update()

    def close_bs():
        bs.open = False
        bs.update()

    bs = ft.BottomSheet(
        ft.Container(
            ft.Column(
                [
                    ft.Text("Ingreso de datos"),
                    ft.TextField(label="Tiempo de procesamiento"),
                    ft.TextField(label="Velocidad de procesamiento"),
                    ft.Checkbox(label="Colorear texto", value=False),
                    ft.ElevatedButton("Crear proceso", on_click=add_event),
                ],
                tight=True,
            ),
            padding=10,
        ),
        open=True,
    )
    page.overlay.append(bs)
    
    load_data_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text("Atento!"),
        content=ft.Text("Hay campos sin ser ingresados"),
        actions=[
            ft.TextButton("Cerrar", on_click=close_alert),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )
    
    page.snack_bar = ft.SnackBar(
        content=ft.Text("Proceso agregado!"),
        action="Alright!",
    )
    
    confirm_dialog = ft.AlertDialog(
        modal=True,
        title=ft.Text("Por favor confirma"),
        content=ft.Text("Estas seguro de cerrar la aplicación?"),
        actions=[
            ft.ElevatedButton("Si", on_click=yes_click),
            ft.OutlinedButton("No", on_click=no_click),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )
    
    header = ft.Container(
        ft.Row(
            [
                ft.Image(
                    src='..\\assets\\img\\logo-espe.png',
                    width=100,
                    height=100,
                ),
                ft.Column(
                    [
                        ft.Text(value='Universidad de las Fuerzas Armadas', font_family='Allura', scale=3),
                        ft.Text(value='ESPE - Sede Latacunga', font_family='Poppins', scale=1),
                    ],
                ),
                ft.Image(
                    src='..\\assets\\img\\logo-software.png',
                    width=100,
                    height=100,
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        ),
        padding=10,
    )
    
    window_buttons = ft.Container(
        ft.Row(
            [
                ft.IconButton(
                    icon=ft.icons.MINIMIZE,
                    icon_color="gray",
                    icon_size=20,
                    tooltip="Minimizar",
                    on_click=minimize_event
                ),
                ft.IconButton(
                    icon=ft.icons.CLOSE,
                    icon_color="red",
                    icon_size=20,
                    tooltip="Cerrar",
                    on_click=close_window,
                ),
            ],
            spacing=0,
        )
    )
    
    title_bar = ft.Container(
        ft.Row(
            [
                ft.Text(
                    value='Proyecto final | Computación Paralela'                    
                ),
                window_buttons,
            ],
            spacing=0,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        ),
        border=ft.border.all(1, '#2E4C06'),
        bgcolor='#162504',
        margin=-10,
        padding=0,
    )
    
    add_button = ft.IconButton(
        icon=ft.icons.ADD,
        icon_color="gray",
        icon_size=25,
        tooltip="Agregar proceso",
        on_click=show_bs,
        disabled = add_button_enable,
    )
    
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
    
    delete_button = ft.IconButton(
        icon=ft.icons.DELETE_SHARP,
        icon_color="red",
        icon_size=25,
        tooltip="Eliminar",
        on_click=delete_event,
        disabled = delete_button_enable,
    )
    
    process_controls = ft.Container(
        ft.Row(
            [
                ft.Text(value="Control de procesos:", font_family="Poppins"),
                add_button,
                delete_button,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
    )
    
    process_container = ft.Row(
        height=500,
        controls=process_items,
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=10,
        wrap=True,
        auto_scroll=True,
        scroll=ft.ScrollMode.AUTO,
    )
    
    body_content = ft.Container(
         ft.Column(
            [
                process_controls,
                process_container,
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        ),
        #border=ft.border.all(1, '#383838'),
        #border_radius=ft.border_radius.all(10),
        padding=20,
    )
    
    app_content = ft.Container(
        ft.Column(
            [
                title_bar,
                header,
                body_content,
            ],
        ),
    )
    
    page.add(app_content)

if __name__ == '__main__':
    ft.app(target=main)

#HOT RELOAD: flet run main.py -d