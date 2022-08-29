import os
import re
from enum import Enum
from ..conf import TITLE
from ..dba.databaseManager import DatabaseManager
from .messageSystem import MessageSystem
from ..dbm.voyager.voyagerService import VoyagerService

class NexusArchive:

    address = None
    messageSystem = None
    username = None
    database = None

    def __init__(self, socket, address):
        self.address = address
        self.messageSystem = MessageSystem(socket)

    def __title(self):
        self.messageSystem.clear()
        self.messageSystem.send(TITLE)

    def __login(self):
        voyagerService = VoyagerService()

        is_auth = False
        while (is_auth == False):
            username = self.messageSystem.prompt(prompt="Username")
            voyager = voyagerService.read(username)

            if (voyager is not None):
                password = self.messageSystem.prompt(prompt="Password")
                is_auth = voyager.authenticate(password)

                if (is_auth == False):
                    self.messageSystem.send("Incorrect Password - Authentication Failed")
            else:
                is_valid = False
                while (is_valid == False):
                    password = self.messageSystem.prompt(prompt="Create a Password")
                    password_check = self.messageSystem.prompt(prompt="Re-Enter the Password")
                    is_valid = password == password_check

                voyagerService.create(username, password)
                is_auth = True

        voyagerService.close()
        self.username = username

    def __select_gate(self):
        # Create and Use ArchiveService
        gates = {}
        for root, dirs, files in os.walk("archive/gates/"):
            index = 0
            for filename in files:
                if (".sqlite" in filename):
                    index += 1
                    gate = filename.split(".")[0]
                    gate = gate.replace("_", " ")
                    gates[str(index)] = {
                        "title": gate.title(),
                        "file": filename
                    }

        self.messageSystem.clear()
        self.messageSystem.send(TITLE)
        self.messageSystem.send("GATEWAYS:\n")
        for gate_id in gates.keys():
            self.messageSystem.send(f"[{gate_id}] {gates[gate_id]['title']}\n")

        self.messageSystem.send("\nSelect a Gate ID: ")
        gateId = self.messageSystem.recieve()

        if (gateId in gates.keys()):
            gatefile = gates[gateId]["file"]
            self.database = DatabaseManager(gatefile, self.username)
        else:
            self.__select_gate()

    def __enter_gate(self, entityId=1):

        page = self.database.getLocation(entityId) 
        self.messageSystem.clear()
        self.messageSystem.type(page)

        command = self.messageSystem.prompt(username=self.username)
        entityId = self.database.execute(command, entityId)

        if (entityId != 0):
            self.__enter_gate(entityId)

    def start(self):

        try:
            self.__title()
            self.__login()
            self.__select_gate()
            self.__enter_gate()

        except Exception as exc:
            print(f"Voyager {self.address} Encountered an Error:\n{exc}")
            self.messageSystem.send("Something Went Wrong!\n")
            self.messageSystem.send(f"{exc}")

        finally:
            print(f"Voyager {self.address} Returned Home. Closing Connection")
            self.messageSystem.send("Carry On, Inrepid Voyager!\n")

