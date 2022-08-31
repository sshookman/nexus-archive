import os

INDEX_LENGTH = 5
TITLE_LENGTH = 15
PAGE_LENGTH = 3
LENGTH = 31

GATES_LOCATION = "archive/gates/"
GATES_TABLE = """
    [B]ACK
    [O]PEN (INDEX)

    +-------+-----------------+
    | INDEX |      TITLE      |
    +-------+-----------------+
{rows}    +-------+-----------------+
{controls}
"""
GATES_ROW = "    | {index} | {title} |\n"
CONTROLS_ROW = "    {prev}{page}{next}\n"
PREV_CONTROL = "<< [P]REV" #9
NEXT_CONTROL = "[N]EXT >>" #9
PAGE_DISPLAY = " {current}/{total} " #3 each

class ArchiveService:

    gates = None
    total_pages = None

    def __init__(self):
        self.gates = {}
        for root, dirs, files in os.walk(GATES_LOCATION):
            index = 0
            for filename in files:
                if (".sqlite" in filename):
                    index += 1
                    gate = filename.split(".")[0]
                    gate = gate.replace("_", " ")
                    self.gates[str(index)] = {
                        "title": gate.title(),
                        "file": filename
                    }
        self.total_pages = int(index / 25)

    def __resize(self, text, length, justify="left"):
        text = str(text)
        diff = length - len(text)
        if (diff > 0):
            padding = " "*diff
            if (justify == "left"):
                text = text + padding
            elif (justify == "right"):
                text = padding + text
        elif (diff < 0):
            text = text[:diff-3] + "..."
        return text

    def get_gatefile(self, index):
        return self.gates[str(index)]["file"]

    def get_page(self, page=1):
        rows = ""
        for gate_id in self.gates.keys():
            index = self.__resize(gate_id, INDEX_LENGTH)
            title = self.__resize(self.gates[gate_id]['title'], TITLE_LENGTH)
            row = GATES_ROW.format(index=index, title=title)
            rows += row

        prev_c = PREV_CONTROL if (page > 1) else " "*9
        next_c = NEXT_CONTROL if (page < self.total_pages) else " "*9
        current = self.__resize(page, 3, justify="right")
        total = self.__resize(self.total_pages, 3)
        page = PAGE_DISPLAY.format(current=current, total=total)
        controls = CONTROLS_ROW.format(prev=prev_c, page=page, next=next_c)

        return GATES_TABLE.format(rows=rows, controls=controls)
