import flet as ft
import time
import datetime
import threading
import random

process_items = []
count = 0
add_button_enable = False
delete_button_enable = True

def main(page: ft.Page):
    global add_button_enable, delete_button_enable
    
    page.fonts = {
        "Allura": "..\\assets\\fonts\\Allura-Regular.ttf",
        "Poppins": "..\\assets\\fonts\\Poppins-Regular.ttf"
    }

    page.window_title_bar_hidden = True
    page.window_prevent_close = True
    page.window_maximized = True
    page.auto_scroll = True
    page.window_center()
    
    concurrency_sem = threading.Semaphore(3)
    
    class ProcessView():
        
        def run_process(self, e):
            self.sem.acquire()
            print("Play Clicked")
            self.running = True
            inicio = datetime.datetime.now()
            self.state.value = "En ejecución"
            self.proccess_item.border = ft.border.all(1, 'yellow')
            
            for i in range(self.numero_datos):
                hora = datetime.datetime.now().strftime("%H:%M:%S")
                if(self.color):
                    r = random.randint(0, 255)
                    g = random.randint(0, 255)
                    b = random.randint(0, 255)
                    color_hex = "#{:02X}{:02X}{:02X}".format(r, g, b)
                    text = ft.Text(value=f"{i+1}: Procesando {hora}", color=color_hex)
                else:
                    text = ft.Text(value=f"{i+1}: Procesando {hora}")
                self.process_texts.append(text)
                time.sleep(1/self.velocidad)
                self.final_time.value = f"Tiempo estimado: {(datetime.datetime.now() - inicio).total_seconds()}s"
                self.proccess_item.update()
            
            self.proccess_item.border = ft.border.all(1, 'green')
            self.state.value = "Completado"
            self.page.update()
            self.sem.release()

        def play_event(self, e):
            thread = threading.Thread(target=self.run_process)
            thread.start()

        def stop_event(self, e):
            self.sem.acquire()
            print("Stop Clicked")
            self.running = False
            self.proccess_item.border = ft.border.all(1, '#B21200')
            self.state.value = "Detenido"
            self.process_texts = []
            self.counter = 0
            self.proccess_item.update()
            self.page.update()
            self.sem.release()
        
        def __init__(self, page: ft.Page, sem: threading.Semaphore, count: int, velocidad: int, numero_datos: int, color: bool):
            
            self.sem = sem
            self.page = page
            self.count = count
            self.numero_datos = numero_datos
            self.velocidad = velocidad
            self.color = color
            self.final_time = 0
            
            self.running = False 
            self.counter = 0
            self.process_texts = []
                
            self.play_button = ft.IconButton(
                icon=ft.icons.PLAY_ARROW,
                icon_color="blue",
                icon_size=25,
                tooltip="Iniciar",
                on_click=self.run_process,
            )
            self.stop_button = ft.IconButton(
                icon=ft.icons.STOP,
                icon_color="red",
                icon_size=25,
                tooltip="Detener",
                on_click=self.stop_event,
            )

            
        def build(self):
            self.state = ft.Text(value="No iniciado")
            self.process_container = ft.Container(
                            ft.Column(
                                self.process_texts,
                                width = 300,
                                scroll=ft.ScrollMode.AUTO,
                                alignment=ft.MainAxisAlignment.CENTER,
                                auto_scroll=True,
                            ),
                            padding=10,
                            height=200,
                            bgcolor='#262626',
                            border=ft.border.all(1, '#383838'),
                            border_radius=ft.border_radius.all(10),
                        )
            self.final_time = ft.Text(value=f"Tiempo estimado: {int(self.final_time)}s")
            self.proccess_item = ft.Container(
                ft.Column(
                    [
                        ft.Text(value=f"Proceso: {self.count}"),
                        ft.Text(value=f"Cantidad de datos a procesar: {int(self.numero_datos)}"),
                        ft.Container(
                            ft.Row(
                                [
                                    self.play_button,
                                    self.stop_button,
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                            ),
                            border=ft.border.all(1, '#FFFFFF'),
                            border_radius=ft.border_radius.all(10),
                        ),
                        self.process_container,
                        ft.Text(value=f"Velocidad: x{self.velocidad}"),
                        ft.Container(
                            ft.Row(
                                [
                                    ft.Text(value="Estado:"),
                                    self.state
                                ],
                                alignment=ft.MainAxisAlignment.START,
                            ),
                            margin=10,
                        ),
                        self.final_time,
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
            return self.proccess_item
    
    ##EVENTOS
    def add_event(e):
        try:        
            global count, delete_button_enable
            if (count >= 0):
                count+=1
                process = ProcessView(
                    page,
                    concurrency_sem,
                    int(count),
                    int(sd_velocidad.value),
                    int(sd_datos.value),
                    ck_colorear.value
                )
                widget = process.build()
                process_items.append(widget)
                if(count == 0):
                    delete_button_enable = True
                if (count > 0):
                    delete_button_enable = False
                delete_button.disabled = delete_button_enable
                delete_button.update()
                process_container.update()
                close_bs()
                page.snack_bar.duration = int(1000)
                show_snack_bar(f'Proceso agregado! {count}')
                
        except Exception as ex:
            close_bs()
            page.snack_bar.duration = int(3000)
            show_snack_bar(f'Error en los datos {ex}')

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
        page.update()
        
    def close_alert(e):
        load_data_modal.open = False
        page.update()
    
    def show_bs(e):
        bs.open = True
        bs.update()

    def close_bs():
        bs.open = False
        bs.update()

    #BS
    sd_velocidad = ft.Slider(min=0, max=20, divisions=20, label="x{value}")
    sd_datos = ft.Slider(min=0, max=1000, divisions=50, label="{value}")
    ck_colorear = ft.Checkbox(label="Colorear texto", value=False)
    bs = ft.BottomSheet(
        ft.Container(
            ft.Column(
                [
                    ft.Text("Ingreso de datos"),
                    ft.Text("Cantidad de datos"),
                    sd_datos,
                    ft.Text("Velocidad de procesamiento (dato por segundo)"),
                    sd_velocidad,
                    ft.Text("Colorear texto"),
                    ck_colorear,
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