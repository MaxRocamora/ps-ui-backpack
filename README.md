# ps-ui-backpack
 PySide UI Utilities

## Installation

```bash
pip install ps-ui-backpack
```

## Usage

### Widgets

```python
from ps_ui_backpack import widgets, Colors

widgets.PushButton(parent, 'qt_name', (120, 21) , Colors.blue)

```

### Dialogs

```python
from ps_ui_backpack import dialogs

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

### Utils

Wait Cursor decorator

```python
from ps_ui_backpack import wait_cursor

@wait_cursor
def long_running_function():
    pass
```
