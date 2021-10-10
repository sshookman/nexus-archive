import re

class PageManager():
    pages = None
    page = None

    def __init(self):
        self.pages = {
            "welcome": Page("Welcome!", {re.compile("^a(bout)?$"): "about"}),
            "about": Page("ABOUT", {re.compile("^b(ack)?$"): "welcome"})
        }
        self.page = self.pages["welcome"]

    def getPage(self, cmd=None):
        if (cmd is not None):
            page_name = self.page.route(cmd)
            self.page = self.pages[page_name]

        return self.page
