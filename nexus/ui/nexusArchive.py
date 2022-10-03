import os
import re
from enum import Enum
from ..conf import TITLE
from ..dba.databaseManager import DatabaseManager
from .messageSystem import MessageSystem
from ..dbm.voyager.voyagerService import VoyagerService
from ..archive.archiveService import ArchiveService
from ..util.logging import NexusLogger

LOGGER = NexusLogger(__name__)

class NexusArchive:

    address = None
    messageSystem = None
    archiveService = None
    username = None
    database = None

    def __init__(self, socket, address):
        self.address = address
        self.messageSystem = MessageSystem(socket)
        self.archiveService = ArchiveService()

    def __title(self):
        self.messageSystem.clear()
        self.messageSystem.send(TITLE)

    def __login(self):
        self.__title()

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

    def __select_gate(self, page=0):
        self.__title()

        page = self.archiveService.get_page(page=page)
        self.messageSystem.send(page)

        cmd = self.messageSystem.prompt()
        cmd = cmd.lower()
        #TODO: Handle commands more flexibly
        if (cmd == "p"):
            return self.__select_gate(max(page-1, 0))
        elif (cmd == "n"):
            return self.__select_gate(page+1)
        elif (cmd == "b"):
            return self.__select_gate(0)
        elif (cmd.startswith("o")):
            gatefile = self.archiveService.get_gatefile(1)
            self.database = DatabaseManager(gatefile, self.username)

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
            self.__login()
            self.__select_gate()
            self.__enter_gate()

        except Exception as exc:
            LOGGER.info(f"Voyager {self.address} Encountered an Error:\n{exc}")
            self.messageSystem.send("Something Went Wrong!\n")
            self.messageSystem.send(f"{exc}")

        finally:
            LOGGER.info(f"Voyager {self.address} Returned Home. Closing Connection")
            self.messageSystem.send("Carry On, Inrepid Voyager!\n")

