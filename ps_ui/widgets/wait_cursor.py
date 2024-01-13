from PySide2.QtWidgets import QApplication
from PySide2.QtCore import Qt


def wait_cursor(method):
    ''' qt wait cursor decorator '''

    def wrapper(*args, **kwargs):

        QApplication.setOverrideCursor(Qt.WaitCursor)
        QApplication.processEvents()

        r = method(*args, **kwargs)

        QApplication.restoreOverrideCursor()
        QApplication.processEvents()

        return r

    return wrapper
