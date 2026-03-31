from functools import wraps
from typing import Callable

try:
    from PySide2.QtCore import Qt  # type: ignore
    from PySide2.QtWidgets import QApplication  # type: ignore

    IS_PYSIDE2 = True
except ImportError:
    from PySide6.QtCore import Qt
    from PySide6.QtWidgets import QApplication

    IS_PYSIDE2 = False


def _resolve_wait_cursor():
    """Resolve wait cursor across Qt enum styles and monkeypatched test doubles."""
    cursor = getattr(Qt, 'WaitCursor', None)
    if cursor is not None:
        return cursor

    return Qt.CursorShape.WaitCursor


def wait_cursor(method: Callable) -> Callable:
    """Qt wait cursor decorator.

    Note:
        The wait cursor will be set for the duration of the method call.
        The method must be a function or a method of a class.

    Use QApplication.processEvents() to update the UI while the wait cursor is active.
    """

    @wraps(method)
    def wrapper(*args, **kwargs):
        QApplication.setOverrideCursor(_resolve_wait_cursor())
        QApplication.processEvents()

        try:
            r = method(*args, **kwargs)
        except Exception:
            raise
        finally:
            QApplication.restoreOverrideCursor()
            QApplication.processEvents()

        return r

    return wrapper
