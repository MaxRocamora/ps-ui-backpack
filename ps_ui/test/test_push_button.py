import sys
from PySide2.QtWidgets import QApplication
from PySide2.QtWidgets import QMainWindow

from ps_ui.css.colors import Colors
from ps_ui.widgets.push_button import PushButton


if __name__ == '__main__':
    # create a qt application
    app = QApplication(sys.argv)

    # create a main window
    main_window = QMainWindow()

    # set the size of the main window
    main_window.setMinimumSize(400, 600)
    main_window.setMaximumSize(400, 600)

    main_window.show()

    # create a push button for every color in Colors
    for index, color in enumerate(Colors):
        push_button = PushButton(main_window, f'push_button {index}', (100, 30), color, True)
        push_button.setText(color.name)
        push_button.move(20, 20 + (index * 40))
        push_button.show()

    # start the event loop
    sys.exit(app.exec_())