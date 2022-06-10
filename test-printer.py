import time
import sys

SPEED_FAST = 0.05
SPEED_MEDIUM = 0.10
SPEED_SLOW = 0.20

def writer(message, delay=SPEED_MEDIUM):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

msg = """
A deep, loud noise merges with your dream and startles you back into concoiusness. There is no
memory of the noise or the dream anymore. There is only a faint imprint in your mind of where they
once resided.

“What the…”

The smell of lavender gently wafts around the you as you hoist your body up from the floor.
"""

writer(msg)
