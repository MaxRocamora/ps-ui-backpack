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

dialogs.warning_dialog(parent, 'error_message', 'title')

```

### CSS

```python
from ps_ui_backpack import utils
```

### Utils

Wait Cursor decorator

```python
from ps_ui_backpack import wait_cursor

@wait_cursor
def long_running_function():
    pass
```
