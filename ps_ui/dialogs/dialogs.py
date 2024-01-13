import sys
from PySide2.QtWidgets import QApplication
from PySide2.QtWidgets import QMessageBox, QSizePolicy, QMainWindow


def inform_dialog(parent: QMainWindow, message: str, title: str = ''):
    ''' open qt dialog box with a warning message '''
    msg_box = QMessageBox(parent)
    msg_box.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    msg_box.setStyleSheet("background: rgba(40, 40, 40, 255); color: rgba(255, 255, 255, 255);")
    msg_box.setIcon(QMessageBox.Information)
    msg_box.setInformativeText(message)
    msg_box.setWindowTitle(title)
    msg_box.setStandardButtons(QMessageBox.Close)
    msg_box.setMinimumHeight(100)
    msg_box.setMaximumHeight(100)
    msg_box.setMinimumWidth(200)
    msg_box.setMaximumWidth(200)
    msg_box.exec_()


def warning_dialog(parent: QMainWindow, error_message: str, title: str = ''):
    ''' open qt dialog box with a warning message '''
    msg_box = QMessageBox(parent)
    msg_box.setStyleSheet("background: rgba(40, 40, 40, 255); color: rgba(255, 255, 255, 255);")
    msg_box.setIcon(QMessageBox.Warning)
    msg_box.setText(error_message)
    msg_box.setWindowTitle(title)
    msg_box.setStandardButtons(QMessageBox.Close)
    msg_box.exec_()


if __name__ == '__main__':
    # create a qt application

    app = QApplication(sys.argv)

    # create a main window
    main_window = QMainWindow()
    main_window.show()

    inform_dialog(main_window, 'this is an inform dialog', 'Title for inform dialog')
    warning_dialog(main_window, 'this is a warning dialog', 'Title for warning dialog')
