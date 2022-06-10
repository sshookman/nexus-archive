import sqlite3

class DatabaseManager:

    db = None
    cursor = None

    def __init__(self, databaseFile):
        self.db = sqlite3.connect(databaseFile)
        self.cursor = self.db.cursor()

    def close():
        self.db.close()
    
    def getLocation(self):
        return "TEMP TEST PAGE"

    def execute(self, command):
        rows = db.execute("SELECT * FROM location WHERE location_id == 0")
        for row in rows:
            print(rows)

        return 1
