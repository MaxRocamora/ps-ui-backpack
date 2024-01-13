from PySide2.QtWidgets import QMessageBox, QSizePolicy, QMainWindow


# def event(self, event):
#     self.setMinimumHeight(100)
#     self.setMaximumHeight(100)
#     self.setMinimumWidth(200)
#     self.setMaximumWidth(200)


def inform_dialog(parent: QMainWindow, message: str, title: str = ''):
    ''' open qt dialog box with a warning message '''
    msg_box = QMessageBox(parent)
    msg_box.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    msg_box.setStyleSheet("background: rgba(40, 40, 40, 255);")
    msg_box.setIcon(QMessageBox.Information)
    msg_box.setInformativeText(message)
    msg_box.setWindowTitle(title)
    msg_box.setStandardButtons(QMessageBox.Close)
    msg_box.exec_()


def warning_dialog(parent: QMainWindow, error_message: str, title: str = ''):
    ''' open qt dialog box with a warning message '''
    msg_box = QMessageBox(parent)
    msg_box.setStyleSheet("background: rgba(40, 40, 40, 255);")
    msg_box.setIcon(QMessageBox.Warning)
    msg_box.setText(error_message)
    msg_box.setWindowTitle(title)
    msg_box.setStandardButtons(QMessageBox.Close)
    msg_box.exec_()
