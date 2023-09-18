from Connection import Connection
from Task import Task

def main():

    conn = Connection()
    conn.create_table()

    #Menú
    home_screen = "\n================\
        \nLISTA DE TAREAS\
        \n================"
    menu = "\n1. Agregar una tarea\
        \n2. Mostrar tareas pendientes\
        \n3. Marcar tarea como terminada\
        \n4. Salir"
    
    print(home_screen)


    while True:

        
        print(menu)

        op = input("\nSeleccione una opción: ")
        
        while op not in "1234":
            op = input("Seleccione una opción válida: ")
        if op == "1":
            task_title = input("Ingresa la nueva tarea: ")
            task = Task(task_title)
            conn.add_task(task)
            input("\nPresione ENTER para continuar...")
        elif op == "2":
            conn.show_tasks()
            input("\nPresione ENTER para continuar...")
        elif op == "3":
            task_id = input("Ingresa el ID de la tarea terminada: ")
            conn.check_task(task_id)
            input("\nPresione ENTER para continuar...")
        elif op == "4":
            break

    print("\n---------------------\
          \nCreado por: Emilio Soto Andrade\
          \n---------------------")


if __name__ == "__main__":
    main()



    
