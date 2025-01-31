import sqlite3

class TaskManager:
    def __init__(self, db_name='tasks.db'):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT,
                is_completed BOOLEAN NOT NULL DEFAULT 0
            )
        ''')
        self.connection.commit()
        
    def add_task(self, title, description):
        self.cursor.execute('''       
                INSERT INTO tasks (title,description) VALUES (?, ?)
''', (title,description))
        
        self.connection.commit()
        
    def get_all_tasks(self):
        self.cursor.execute("SELECT * FROM tasks")
        return self.cursor.fetchall()
    
    
    def get_task_by_id(self,task_id):
        self.cursor.execute("SELECT * FROM tasks WHERE id = ?", (task_id,))
        tas = self.cursor.fetchone()
        print(tas)
        
    def complete_task(self,task_id):
        self.cursor.execute("UPDATE tasks SET is_completed = 1 WHERE id = ?", (task_id,))
        self.connection.commit()
        
    # def delete_task(self,task_id):
    #     self.cursor.execute("DELETE FROM tasks WHERE id = ?",(task_id))
    #     self.connection.commit()
    
    def delete_task(self, task_id):
        self.cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
        self.connection.commit()
        
task_manager = TaskManager()
# task_manager.add_task("Програмист","Работает с компьюторами")
# task_manager.add_task("Пожарный","Работает против пожара")
# task_manager.add_task("Полицейский","Работает против приступников")
# task_manager.add_task("Учитель","Работает с учениками ")

tasks = task_manager.get_all_tasks()
for task in tasks:
    print(task)
    
# task_manager.complete_task(1)
# task_manager.delete_task(2)
