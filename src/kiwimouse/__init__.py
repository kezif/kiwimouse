import ctypes
from functools import wraps
from time import sleep

# Constants for the mouse button names
LEFT = "left"
MIDDLE = "middle"
RIGHT = "right"
PRIMARY = "primary"
SECONDARY = "secondary"

# Mouse Scan Code Mappings
MOUSEEVENTF_MOVE = 0x0001
MOUSEEVENTF_LEFTDOWN = 0x0002
MOUSEEVENTF_LEFTUP = 0x0004
MOUSEEVENTF_RIGHTDOWN = 0x0008
MOUSEEVENTF_RIGHTUP = 0x0010
MOUSEEVENTF_MIDDLEDOWN = 0x0020
MOUSEEVENTF_MIDDLEUP = 0x0040

# copy from pyautogui
FAILSAFE = True
FAILSAFE_POINTS = [(0, 0)]
PAUSE = 0.1


def failSafeCheck():
    if FAILSAFE and tuple(_position()) in FAILSAFE_POINTS:
        raise FailSafeException(
            "kiwiMouse fail-safe triggered from mouse moving to a corner of the screen. To disable this fail-safe, set kiwimouse.FAILSAFE to False. DISABLING FAIL-SAFE IS NOT RECOMMENDED."
        )


def _position():
    """Returns the current xy coordinates of the mouse cursor as a two-integer
    tuple by calling the GetCursorPos() win32 function.

    Returns:
      (x, y) tuple of the current xy coordinates of the mouse cursor.
    """
    cursor = ctypes.wintypes.POINT()
    ctypes.windll.user32.GetCursorPos(ctypes.byref(cursor))
    return (cursor.x, cursor.y)


def _genericKiwiMouseChecks(wrappedFunction):
    """
    A decorator that calls failSafeCheck() before the decorated function and
    _handlePause() after it.
    """

    @wraps(wrappedFunction)
    def wrapper(*args, **kwargs):
        failSafeCheck()
        returnVal = wrappedFunction(*args, **kwargs)
        _handlePause(kwargs.get("_pause", True))
        return returnVal

    return wrapper


def _handlePause(_pause):
    if _pause:
        assert isinstance(PAUSE, int) or isinstance(PAUSE, float)
        sleep(PAUSE)


class FailSafeException(Exception):
    pass


# end of paste


@_genericKiwiMouseChecks
def click(button=PRIMARY, duration=0.1, _pause=True):
    """
    Send mouse up and down inputs using win32 mouse_event api
    """
    ev_up, ev_down = None, None
    if button == PRIMARY or button == LEFT:
        ev_up, ev_down = MOUSEEVENTF_LEFTUP, MOUSEEVENTF_LEFTDOWN
    elif button == MIDDLE:
        ev_up, ev_down = MOUSEEVENTF_MIDDLEUP, MOUSEEVENTF_MIDDLEDOWN
    elif button == SECONDARY or button == RIGHT:
        ev_up, ev_down = MOUSEEVENTF_RIGHTUP, MOUSEEVENTF_RIGHTDOWN

    if not ev_up or not ev_down:
        raise ValueError(
            'button arg to _click() must be one of "left", "middle", or "right", not %s'
            % button
        )

    ctypes.windll.user32.mouse_event(ev_down)
    sleep(duration)
    ctypes.windll.user32.mouse_event(ev_up)


_genericKiwiMouseChecks


def move(x, y, _pause=True):
    """
    Move mouse by using win32 mouse_event api
    """
    ctypes.windll.user32.mouse_event(
        MOUSEEVENTF_MOVE, ctypes.c_long(x), ctypes.c_long(y)
    )


moveRel = move
