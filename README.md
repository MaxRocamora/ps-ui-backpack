[![PyPI Supported Python Versions](https://img.shields.io/pypi/pyversions/pyside-ui-backpack.svg?style=flat-square&logo=appveyor)](https://pypi.python.org/pypi/pyside-ui-backpack/)
[![PyPI version](https://badge.fury.io/py/pyside-ui-backpack.svg?style=flat-square&logo=appveyor)](https://badge.fury.io/py/pyside-ui-backpack)
[![Message](https://img.shields.io/badge/python--backpack-python-blue?style=flat-square&logo=appveyor)](https://github.com/MaxRocamora/ps-ui-backpack)


# ps-ui-backpack
 PySide UI Utilities

Some shared PySide2 UI utilities for Maya/Houdini/Nuke Qt Tools

## Installation

```bash
pip install pyside-ui-backpack
```

## Usage

### Widgets

```python
from ps_ui import widgets, Colors

widgets.PushButton(parent, 'qt_name', 'Click Me' , (120, 21) , Colors.BLUE)

```

### Dialogs

```python
from ps_ui import dialogs

dialogs.inform_dialog(parent, 'message', 'title')
dialog.inform_dialog_small(parent, 'message', 'title')
dialogs.warning_dialog(parent, 'error_message', 'title')
dialogs.warning_dialog(parent, 'error_message', 'title')

```

### CSS

```python
from ps_ui import style_push_button, Colors

# style a button widget
button = QPushButton(main_window)
style_push_button(main_window, button, Colors.BLUE)

```

### Colors

Colors.py contains a list of colors

```python
from ps_ui import Colors

Colors.DISABLED Colors.BLUE, Colors.RED, Colors.GREEN, Colors.YELLOW, ...
Colors.DARK_BLUE, Colors.DARK_RED, Colors.DARK_GREEN, Colors.DARK_YELLOW, ...
Colors.BG_BLUE, Colors.BG_RED, Colors.BG_GREEN, Colors.BG_YELLOW, ...
```

![Push Button](img/button_colors.png)

### Utils

Wait Cursor decorator

```python
from ps_ui import wait_cursor

@wait_cursor
def long_running_function():
    pass
```
