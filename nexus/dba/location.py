class Location():
    entity_id = None
    display = None
    paths = None

    def __init__(self, entity_id, display, paths):
        self.entity_id = entity_id
        self.display = display
        self.paths = paths
