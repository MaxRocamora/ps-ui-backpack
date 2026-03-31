import pytest

pytest.importorskip('PySide6')

import pyside_ui_backpack.widgets.wait_cursor as wait_cursor_module


class DummyQt:
    WaitCursor = object()


class DummyApp:
    calls = []

    @staticmethod
    def setOverrideCursor(cursor):
        DummyApp.calls.append(('set', cursor))

    @staticmethod
    def processEvents():
        DummyApp.calls.append(('process', None))

    @staticmethod
    def restoreOverrideCursor():
        DummyApp.calls.append(('restore', None))


def test_wait_cursor_wraps_success(monkeypatch):
    monkeypatch.setattr(wait_cursor_module, 'Qt', DummyQt)
    monkeypatch.setattr(wait_cursor_module, 'QApplication', DummyApp)
    DummyApp.calls = []

    @wait_cursor_module.wait_cursor
    def do_work(value):
        return value * 2

    assert do_work(3) == 6
    assert DummyApp.calls[0] == ('set', DummyQt.WaitCursor)
    assert DummyApp.calls[-2:] == [('restore', None), ('process', None)]


def test_wait_cursor_wraps_exception(monkeypatch):
    monkeypatch.setattr(wait_cursor_module, 'Qt', DummyQt)
    monkeypatch.setattr(wait_cursor_module, 'QApplication', DummyApp)
    DummyApp.calls = []

    @wait_cursor_module.wait_cursor
    def fail():
        raise RuntimeError('boom')

    with pytest.raises(RuntimeError, match='boom'):
        fail()

    assert DummyApp.calls[0] == ('set', DummyQt.WaitCursor)
    assert DummyApp.calls[-2:] == [('restore', None), ('process', None)]
