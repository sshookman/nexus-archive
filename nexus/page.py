class Page():
    display = None
    routes = None

    def __init__(self, display, routes):
        self.display = display
        self.routes = routes

    def route(self, cmd):
        page = None
        for pattern, page_name in self.routes.items():
            if pattern.match(cmd):
                page = page_name

        return page
