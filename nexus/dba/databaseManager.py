import os
import re
import sys
import time
import shutil
import sqlite3

#TODO: Use SQLAlchemy - should make this much easier

class DatabaseManager:
    """
    Database management layer that is a wrapper around SQLAlchemy and SQLite3
    """

    db = None
    cursor = None

    def __init__(self, filename, voyager):
        # Create voyager directory if one does not exist already
        voyagerDir = f"archive/voyagers/{voyager}"
        if (os.path.isdir(voyagerDir) == False):
            print(f"Welcome new Voyager ({voyager})")
            os.mkdir(voyagerDir)

        # Copy gatefile to voyager directory if one does not exist already
        gateFile = f"archive/gates/{filename}"
        dbFile = f"{voyagerDir}/{filename}"
        if (os.path.isfile(dbFile) == False):
            print(f"Voyager ({voyager}) entering new Gate ({gateFile})")
            shutil.copyfile(gateFile, dbFile)

        print(f"Voyager ({voyager}) entering Gate ({dbFile})")
        self.db = sqlite3.connect(dbFile)
        self.cursor = self.db.cursor()

    def close(self):
        self.db.close()

    def __checkPaths(self, command, entityId):
        destination_id = entityId

        # TODO: Handle DB tables as classes ideally (not just tuples)
        rows = self.db.execute(f"SELECT regexp, destination_id FROM path WHERE entity_id = {entityId};")
        for row in rows:
            regexp = row[0]
            # TODO: re.match not returning simple bool
            if (regexp == "") | (re.match(regexp, command) == True):
                destination_id = row[1]

        return destination_id

    def getLocation(self, entityId):
        # TODO: Handle queries in a more streamlined manner
        rows = self.db.execute(f"SELECT description FROM location WHERE entity_id = {entityId};")
        for row in rows:
            location_description = row[0]

        return location_description

    def execute(self, command, entityId):

        # TODO: Handle things other than paths
        return self.__checkPaths(command, entityId)
