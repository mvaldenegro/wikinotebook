from PySide2.QtCore import QObject, Property, Signal
from PySide2.QtWebEngineWidgets import QWebEngineView, QWebEnginePage
from PySide2.QtWebChannel import QWebChannel

class MarkdownDocument(QObject):
    def __init__(self):
        QObject.__init__(self)
        self.textVal = str()

    def readText(self):
        return self.textVal

    def setText(self, val):
        self.textVal = val
        self.textChanged.emit(val)

    textChanged = Signal(str)
    text = Property(str, readText, setText, notify=textChanged)

class MarkdownRenderer(QWebEngineView):
    def __init__(self, parent=None):
        QWebEngineView.__init__(self, parent)

        self.channel = QWebChannel(self)
        self.document = MarkdownDocument()
        self.channel.registerObject("content", self.document)

        self.page().setWebChannel(self.channel)
        self.setUrl("qrc:/index.html")

    def displayMarkdown(self, mdText):
        self.document.setText(mdText)
        print("Displaying MD: {}".format(self.document.text))