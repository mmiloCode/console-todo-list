import psycopg2

class Connection:
    def __init__(self):
        self.host = 'localhost'
        self.user = 'postgres'
        self.password = 'admin'
        self.db = 'todo_list'
        self.conn = None

    def connect(self):
        try:
            self.conn = psycopg2.connect(
                host = self.host,
                user = self.user,
                password = self.password,
                database = self.db
            )
        except Exception as e:
            print(e)


    
    def create_table(self):
        self.connect()
        try:
            query = """CREATE TABLE IF NOT EXISTS tasks(
                id SERIAL PRIMARY KEY,
                title TEXT NOT NULL,
                creation_date TIMESTAMP NOT NULL,
                is_checked BOOLEAN NOT NULL
            );"""
            cur = self.conn.cursor()
            cur.execute(query)
            self.conn.commit()
            cur.close()
        except Exception as e:
            print(e)
        self.disconnect()
    

    def add_task(self, task):
        self.connect()
        query = "INSERT INTO tasks (title, creation_date, is_checked) VALUES(%s, %s, %s);"
        data = (task.title, task.creation_date, task.is_checked)
        cur = self.conn.cursor()
        cur.execute(query, data)
        self.conn.commit()
        cur.close()
        self.disconnect()

        print("\nLa tarea ha sido creada con éxito!")


    def check_task(self, task_id):
        self.connect()
        try:
            cur = self.conn.cursor()
            cur.execute("SELECT * FROM tasks WHERE id = %s AND is_checked = FALSE", [task_id])
            res = cur.fetchone()
            if res is None:
                print("La tarea no existe")
            else:
                cur.execute("UPDATE tasks SET is_checked = TRUE WHERE id = %s", [task_id])
                self.conn.commit()
                print(f"\nTAREA TERMINADA: {res[1]}")
        except Exception as e:
            print(e)
        finally:
            cur.close()
        self.disconnect()
        



    def show_tasks(self):

        screen = "\n===================\
        \nTAREAS PENDIENTES\
        \n==================="

        self.connect()
        cur = self.conn.cursor()
        cur.execute("SELECT id, title, creation_date FROM tasks WHERE is_checked = FALSE;")
        results = cur.fetchall()
        print(screen)
        for row in results:
            print(f"ID: {row[0]} | {row[2]} | {row[1]}\
                  \n-----------------------------")
        cur.close()
        self.disconnect()


    
    def disconnect(self):
        if self.conn is not None:
            self.conn.close()

    

    