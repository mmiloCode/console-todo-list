import datetime

class Task:
    def __init__(self, title):
        self.title = title
        self.creation_date = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        self.is_checked = False