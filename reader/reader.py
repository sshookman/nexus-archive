import re
import sys
import time
import sqlite3

# TODO: Most of these details need to be stored, loaded, and passed in from elsewhere
voyager = "sshookman"
gate = "test"
player = "Harkken"
PREFS_DEFAULT = {
    "render_speed": 0.04
}

class DatabaseManager:

    db = None
    cursor = None

    def __init__(self, databaseFile):
        self.db = sqlite3.connect(databaseFile)
        self.cursor = self.db.cursor()

    def close(self):
        self.db.close()

    def __checkPaths(self, command, entity_id):
        destination_id = entity_id

        # TODO: Handle DB tables as classes ideally (not just tuples)
        rows = self.db.execute(f"SELECT regexp, destination_id FROM path WHERE entity_id = {entity_id};")
        for row in rows:
            regexp = row[0]
            # TODO: re.match not returning simple bool
            if (regexp == "") | (re.match(regexp, command) == True):
                destination_id = row[1]

        return destination_id
    
    def getLocation(self, entity_id):
        # TODO: Handle queries in a more streamlined manner
        rows = self.db.execute(f"SELECT description FROM location WHERE entity_id = {entity_id};")
        for row in rows:
            location_description = row[0]

        return location_description

    def executeCommand(self, command, entity_id):

        # TODO: Handle things other than paths
        return self.__checkPaths(command, entity_id)

class Reader:

    dbm = None
    prefs = None

    def __init__(self, gate, prefs=None):
        self.prefs = prefs if (prefs is not None) else PREFS_DEFAULT
        self.dbm = DatabaseManager(gate)

    def start(self):
        # TODO: The state of the player (entity_id as current location) should be stored directly in DB
        entity_id = 1
        while entity_id != 3:
            location = self.dbm.getLocation(entity_id)
            self.render(location)
            command = input(f"\n\n{player} >> ")
            entity_id = self.dbm.executeCommand(command, entity_id)

        self.dbm.close()

    def render(self, message):
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(self.prefs["render_speed"])

reader = Reader(f"archive/voyagers/{voyager}/{gate}/{player}.sqlite")
reader.start()
