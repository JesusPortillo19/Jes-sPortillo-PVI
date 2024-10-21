import flet as ft

def main(page: ft.Page):
    page.window_width = 600
    page.window_height = 400
    page.title = "Lista de compras"

    # Crear un campo de texto para la entrada
    new_task = ft.TextField(hint_text="¿Qué necesitas comprar?", width=300)
    editing_task = None  # Variable para saber si estamos editando una tarea

    # Función para agregar o modificar una tarea
    def add_clicked(e):
        nonlocal editing_task
        if new_task.value:  # Asegúrate de que el campo no esté vacío
            if editing_task:  # Si estamos editando, actualizamos la tarea
                editing_task.label = new_task.value
                editing_task = None  # Reiniciamos el estado de edición
            else:  # Si no, creamos una nueva tarea
                task = ft.Checkbox(label=new_task.value)
                
                # Crear botones de modificar y eliminar para cada tarea
                modify_button = ft.IconButton(
                    icon=ft.icons.CREATE,  # Icono de modificar 
                    on_click=lambda e, t=task: modify_task(t)
                )
                
                delete_button = ft.IconButton(
                    icon=ft.icons.DELETE,  # Icono de eliminar
                    on_click=lambda e, t=task: delete_task(task_row)
                )
                
                # Añadir la tarea y los botones en una fila (Row)
                task_row = ft.Row([task, modify_button, delete_button])
                page.add(task_row)

            # Limpiar el campo de entrada y enfocar nuevamente
            new_task.value = ""
            new_task.focus()
            page.update()

    # Función para modificar una tarea
    def modify_task(task):
        nonlocal editing_task
        new_task.value = task.label  # Pasar el valor de la tarea al campo de texto
        editing_task = task  # Guardar referencia a la tarea que se está editando
        new_task.focus()
        page.update()

    # Función para eliminar una tarea
    def delete_task(task_row):
        page.controls.remove(task_row)  # Eliminar la fila completa que contiene la tarea
        page.update()

    # Logo y texto del encabezado
    logo = ft.Image(src="C:\\Users\\Owner\\OneDrive\\Documents\\TP PROGRAMACIONVl\\jp.jpg", width=500, height=400)
    
    header_text = ft.Text("Bienvenidos a la App de Lista de Compras", size=20, weight=ft.FontWeight.BOLD)

    # Organizar el encabezado en una columna
    header = ft.Column([
        logo,
        header_text
    ], alignment="center")

    # Agregar elementos a la aplicación
    page.add(
        header,
        ft.Divider(height=20),  # Agrega un divisor
        ft.Row([
            new_task,
            ft.IconButton(icon=ft.icons.ADD, on_click=add_clicked)  # Botón agregar con icono
        ])
    )

# Ejecutar la aplicación
ft.app(target=main)
