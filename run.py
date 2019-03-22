import sys

from PySide2.QtWidgets import QApplication
from wikinotebook import MainWindow

if __name__ == "__main__":

    app = QApplication(sys.argv)
    app.setApplicationName("wikinotebook")

    mw = MainWindow()
    mw.show()

    sys.exit(app.exec_())
