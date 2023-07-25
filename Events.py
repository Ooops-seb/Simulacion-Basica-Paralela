from flet import (
    Page,
    AlertDialog,
    Text,
    ElevatedButton,
    OutlinedButton,
    MainAxisAlignment,
    ElevatedButton,
    BottomSheet,
    TextField,
    Checkbox,
    Container,
    Column
)

class EventHandlers:
    
    def __init__(self, page: Page):
        self.page = page
        self.confirm_dialog = AlertDialog(
            modal=True,
            title=Text("Por favor confirma"),
            content=Text("Estas seguro de cerrar la aplicación?"),
            actions=[
                ElevatedButton("Si", on_click=self.yes_click),
                OutlinedButton("No", on_click=self.no_click),
            ],
            actions_alignment=MainAxisAlignment.END,
        )
        
        self.bs = BottomSheet(
            Container(
                Column(
                    [
                        Text("Ingreso de datos"),
                        TextField(label="Tiempo de procesamiento"),
                        TextField(label="Velocidad de procesamiento"),
                        Checkbox(label="Colorear texto", value=False),
                        ElevatedButton("Crear proceso", on_click=self.add_event),
                    ],
                    tight=True,
                ),
                padding=10,
            ),
        )
        self.page.overlay.append(self.bs)
        self.page.update()
    
    def minimize_event(self, e):
        self.page.window_minimized = True
        self.page.update()

    def close_window(self, e):
        self.page.dialog = self.confirm_dialog
        self.confirm_dialog.open = True
        self.page.update()

    def yes_click(self, e):
        self.page.window_destroy()

    def no_click(self, e):
        self.confirm_dialog.open = False
        self.page.update()
        
    def yes_click(self, e):
        self.page.window_destroy()

    def no_click(self, e):
        self.confirm_dialog.open = False
        self.page.update()
        
    def show_bs(self, e):
        self.bs.open = True
        self.bs.update()

    def close_bs(self, e):
        self.bs.open = False
        self.bs.update()
    
    def add_event(self, e):
        print("Add Event clicked")
        
    def play_event(self, e):
        print("Play Event clicked")
        
    def pause_event(self, e):
        print("Pause Event clicked")

    def stop_event(self, e):
        print("Stop Event clicked")
        
    def delete_event(self, e):
        print("Delete Event clicked")