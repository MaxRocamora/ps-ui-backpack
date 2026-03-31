import pytest

pytest.importorskip('PySide6')

from PySide6.QtWidgets import QMainWindow, QMessageBox

from pyside_ui_backpack.dialogs import dialogs as dialogs_module


def test_custom_size_dialog_layout(qtbot):
    parent = QMainWindow()
    qtbot.addWidget(parent)

    dialog = dialogs_module.CustomSizeDialog(
        parent=parent,
        message='Example message',
        title='Example title',
        icon=dialogs_module.QStyle.SP_MessageBoxInformation,
    )
    qtbot.addWidget(dialog)

    assert dialog.windowTitle() == 'Example title'
    assert dialog.minimumWidth() >= 300
    assert dialog.minimumHeight() >= 200
    assert dialog.label.text() == 'Example message'
    assert dialog.button.text() == 'Close'


def test_dialog_helpers_use_exec_helper(monkeypatch, qtbot):
    parent = QMainWindow()
    qtbot.addWidget(parent)

    created = []

    def fake_exec(dialog):
        created.append(dialog)
        return 0

    monkeypatch.setattr(dialogs_module, '_exec_dialog', fake_exec)

    dialogs_module.inform_dialog(parent, 'info text', 'Info')
    dialogs_module.warning_dialog(parent, 'warn text', 'Warn')
    dialogs_module.inform_dialog_small(parent, 'small info', 'SmallInfo')
    dialogs_module.warning_dialog_small(parent, 'small warn', 'SmallWarn')

    assert len(created) == 4
    assert created[0].windowTitle() == 'Info'
    assert created[1].windowTitle() == 'Warn'
    assert isinstance(created[0], dialogs_module.CustomSizeDialog)
    assert isinstance(created[1], dialogs_module.CustomSizeDialog)
    assert isinstance(created[2], QMessageBox)
    assert isinstance(created[3], QMessageBox)
