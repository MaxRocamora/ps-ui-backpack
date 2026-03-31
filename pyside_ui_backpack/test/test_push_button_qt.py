import pytest

pytest.importorskip('PySide6')

from PySide6.QtWidgets import QMainWindow

from pyside_ui_backpack.css.colors import Colors
from pyside_ui_backpack.widgets.push_button import PushButton


def test_push_button_basic_properties(qtbot):
    """Test that the PushButton has the expected properties and styles."""
    main_window = QMainWindow()
    qtbot.addWidget(main_window)

    button = PushButton(
        parent=main_window,
        qt_name='test_button',
        text='Click me',
        size=(120, 30),
        color=Colors.BLUE,
        shadow=False,
    )
    qtbot.addWidget(button)

    assert button.objectName() == 'test_button'
    assert button.text() == 'Click me'
    assert button.minimumWidth() == 120
    assert button.minimumHeight() == 30
    assert button.maximumWidth() == 120
    assert button.maximumHeight() == 30
    assert button.graphicsEffect() is None
    assert Colors.BLUE.value.background_color in button.styleSheet()
    assert Colors.BLUE.value.foreground_color in button.styleSheet()


def test_push_button_shadow_enabled_creates_effect(qtbot):
    main_window = QMainWindow()
    qtbot.addWidget(main_window)

    button = PushButton(parent=main_window, shadow=True)
    qtbot.addWidget(button)

    assert button.graphicsEffect() is not None
