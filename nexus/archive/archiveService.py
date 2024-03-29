import os
import math

INDEX_LENGTH = 5
TITLE_LENGTH = 35
PAGE_LENGTH = 3
LENGTH = 31
GATES_PER_PAGE = 10

GATES_LOCATION = "archive/gates/"
GATES_TABLE = """
    [B]ACK
    [O]PEN (INDEX)

    +-------+-------------------------------------+
    | INDEX |                TITLE                |
    +-------+-------------------------------------+
{rows}    +-------+-------------------------------------+
{controls}
"""
GATES_ROW = "    | {index} | {title} |\n"
CONTROLS_ROW = "    {prev}{page}{next}\n"
PREV_CONTROL = "<< [P]REV" #9
NEXT_CONTROL = "[N]EXT >>" #9
PAGE_DISPLAY = " {current}/{total} " #3 each

class ArchiveService:
    """
    This class provides a mechanism for finding the different gates within the archive.
    """

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
        self.total_pages = int(math.ceil(index / GATES_PER_PAGE))

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

    def get_page(self, page=0):
        rows = ""
        start = page*GATES_PER_PAGE + 1
        end = min(start+GATES_PER_PAGE, len(self.gates)+1)
        for gate_id in range(start, end):
            gate_id = str(gate_id)
            index = self.__resize(gate_id, INDEX_LENGTH)
            title = self.__resize(self.gates[gate_id]['title'], TITLE_LENGTH)
            row = GATES_ROW.format(index=index, title=title)
            rows += row

        prev_c = PREV_CONTROL if (page > 1) else " "*9
        next_c = NEXT_CONTROL if (page < self.total_pages) else " "*9
        current = self.__resize(page+1, 3, justify="right")
        total = self.__resize(self.total_pages, 3)
        page = PAGE_DISPLAY.format(current=current, total=total)
        controls = CONTROLS_ROW.format(prev=prev_c, page=page, next=next_c)

        return GATES_TABLE.format(rows=rows, controls=controls)
