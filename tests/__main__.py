import kiwimouse
import time

def square():
    """
    move mouse in square pattern
    """
    kiwimouse.move(0, 100)
    time.sleep(1)
    kiwimouse.move(-200, 0)
    time.sleep(1)
    kiwimouse.move(0, -100)
    time.sleep(1)
    kiwimouse.move(200, 0)

def click_left():
    """
    click left mouse button
    """
    kiwimouse.click()


if __name__ == '__main__':
    square()
    time.sleep(1)
    click_left()