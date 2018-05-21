import sys

from PySide2.QtWidgets import QApplication

from WMainWindow import WMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = WMainWindow()
    main_window.show()
    sys.exit(app.exec_())
