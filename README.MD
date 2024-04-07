# KiwiMouse
Simulate mouse movement in 3d games using this package.

# Dependencies
Windows has no dependencies. The Win32 extensions do not need to be installed.

# Example Usage
##  Mouse Control
The x, y coordinates used by kiwimouse are relative to the current mouse position. The x coordinates increase going to the right (just as in mathematics) but the y coordinates increase going down (the opposite of mathematics). Keep in mind that in 3d games mouse movement is not correlated 1:1 to the monitor pixel position. 

Main focus of this package was to give the ability to control the mouse in the game window. All mouse events are sent to the active window.

```
import kiwimouse
kiwimouse.click(button='right')  # click right mouse button
kiwimouse.move(0, -500)  # move mouse up 500 px
kiwimouse.click(button='left')  # click left mouse button
kiwimouse.move(0, 500)  # move mouse down 500 px
```
![ultrakill example](https://github.com/kezif/kiwimouse/assets/11709254/0e0d7868-c8b5-48c0-add0-0151edb8feec)

Dy default after each operation `time.sleep(.1)` is executed. You can change it by altering `kiwimouse.PAUSE` value

# Documentation
The `mouse event` windows documentation could be found at [link](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-mouse_event)

# Testing

To run the supplied tests: first setup a virtualenv. Then you can pip install this project in an editable state by doing `pip install -e .`. This allows any edits you make to these project files to be reflected when you run the tests. Run the test file with `python3 tests`.

I have been testing with ULTRAKILL to confirm that these inputs work with DirectX games.

# Features Implemented

* Fail Safe Check (as in pyautogui)
* move(x,y) / moveRel(x,y)
* click()

# Features NOT Implemented
* move to specific pixel on screen
