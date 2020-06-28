#!/bin/python3

import sys

from PySide2.QtWidgets import QApplication
from PySide2.QtGui import QIcon, QPixmap
from wikinotebook import MainWindow

import pathlib, os

if __name__ == "__main__":

    app = QApplication(sys.argv)
    app.setApplicationName("wikinotebook")

    path = os.path.join(pathlib.Path(__file__).parent.absolute(), "wikinotebook/icons/notes.svg")
    icon = QIcon(QPixmap(path))
    app.setWindowIcon(icon)

    mw = MainWindow()
    mw.show()

    sys.exit(app.exec_())
