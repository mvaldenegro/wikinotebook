from PySide2.QtCore import QObject, SIGNAL, QDir, QSettings
from PySide2.QtWidgets import QMainWindow, QToolBar, QTextEdit, QVBoxLayout, QWidget
from PySide2.QtWidgets import QComboBox, QSizePolicy, QSystemTrayIcon, QMenu
from PySide2.QtWidgets import QInputDialog, QApplication
from PySide2.QtGui import QIcon, QFontDatabase, QKeySequence, QPixmap

import pathlib, os

from .MarkdownRenderer import MarkdownRenderer
from .NoteManager import Note, Notebook, NotebookManager
from .config import ORGANIZATION_STR

BASIC_TITLE = "Wiki Notebook"

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self, parent=None)
        self.settings = QSettings(ORGANIZATION_STR)
        self.toolbar = self.createToolBar()

        self.widget = QWidget(self)
        self.layout = QVBoxLayout(self.widget)
        self.layout.setContentsMargins(1, 1, 1, 1)
        self.currentWidget = None

        self.editor = QTextEdit()
        self.editor.setAcceptRichText(False)

        font = QFontDatabase.systemFont(QFontDatabase.FixedFont)
        fs = int(self.settings.value("fontSize", 13))
        font.setPointSize(fs)

        self.editor.setFont(font)
        self.preview = MarkdownRenderer()

        self.layout.addWidget(self.toolbar)
        self.widget.setLayout(self.layout)

        self.showWidget(self.editor)

        self.addToolBar(self.toolbar)
        self.setCentralWidget(self.widget)

        self.setWindowTitle(BASIC_TITLE)

        self.nbManager = NotebookManager()        

        self.currentNotebook = None
        self.currentNote = None
        self.dirty = False

        self.editor.document().modificationChanged.connect(self.editorModified)

        self.updateUI()

        if len(self.nbManager.notebooks()) > 0:
            self.switchNotebook(self.nbManager.notebooks()[0].name)

        self.createTrayIcon()
        
        self.readConfig()

    def closeEvent(self, event):        
        self.nbManager.writeConfig()
        self.writeConfig()

        QMainWindow.closeEvent(self, event)

    def showWidget(self, w):
        if self.currentWidget is not None:
            self.currentWidget.hide()
            self.layout.removeWidget(self.currentWidget)
            
        self.layout.addWidget(w)        
        #self.layout.update()
        self.currentWidget = w
        self.currentWidget.show()

    def createToolBar(self):
        toolbar = QToolBar()

        act = toolbar.addAction(QIcon.fromTheme("document-new"), "Create a new note", self.newNote)
        act.setShortcut(QKeySequence.New)
        toolbar.addAction(QIcon.fromTheme("folder-new"), "Create a new notebook", self.newNotebook)
        toolbar.addSeparator()

        act = toolbar.addAction(QIcon.fromTheme("document-save"), "Save changes to current note", self.saveNote)
        act.setShortcut(QKeySequence.Save)
        toolbar.addAction(QIcon.fromTheme("document-send"), "Export current note")
        toolbar.addSeparator()

        toolbar.addAction(QIcon.fromTheme("format-text-bold"), "Bold")
        toolbar.addAction(QIcon.fromTheme("format-text-italic"), "Italic")
        toolbar.addAction(QIcon.fromTheme("format-text-underline"), "Underline")

        self.headingsCombo = QComboBox()
        self.headingsCombo.addItem("H1")
        self.headingsCombo.addItem("H2")
        self.headingsCombo.addItem("H3")
        self.headingsCombo.addItem("H4")
        self.headingsCombo.addItem("H5")
        self.headingsCombo.addItem("H6")

        toolbar.addWidget(self.headingsCombo)
        toolbar.addSeparator()

        toolbar.addAction(QIcon.fromTheme("format-list-unordered"), "Insert bulleted list")
        toolbar.addAction(QIcon.fromTheme("format-list-ordered"), "Insert numbered list")
        toolbar.addAction(QIcon.fromTheme("insert-link"), "Inserts a link")
        toolbar.addSeparator()

        self.editableAction = toolbar.addAction(QIcon.fromTheme("edit"), "Toggle edit or markdown visualizer")
        self.editableAction.setCheckable(True)
        self.editableAction.setChecked(True)
        self.editableAction.setShortcut(QKeySequence("Ctrl+E"))
        QObject.connect(self.editableAction, SIGNAL('triggered(bool)'), self.editTriggered)

        toolbar.addAction(QIcon.fromTheme("system-search"), "Search")

        self.notebooksCombo = QComboBox()
        self.notebooksCombo.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.notebooksCombo.addItem(QIcon.fromTheme("folder"), "Create new notebook")

        self.notesCombo = QComboBox()
        self.notesCombo.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)

        QObject.connect(self.notebooksCombo, SIGNAL("activated(QString)"), self.switchNotebook)
        QObject.connect(self.notesCombo, SIGNAL("activated(QString)"), self.switchNote)

        self.spacer = QWidget()
        self.spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)

        toolbar.addWidget(self.spacer)
        toolbar.addWidget(self.notebooksCombo)
        toolbar.addWidget(self.notesCombo)

        return toolbar

    def createTrayIcon(self):
        path = os.path.join(pathlib.Path(__file__).parent.absolute(), "icons/notes.svg")
        icon = QIcon(QPixmap(path))
        
        self.trayIcon = QSystemTrayIcon(icon, self)
        self.trayMenu = None

        QObject.connect(self.trayIcon, SIGNAL("activated(QSystemTrayIcon::ActivationReason)"), self.trayIconActivated)

        self.populateTrayMenu()
        self.trayIcon.show()

    def trayIconActivated(self, reason):
        if reason != QSystemTrayIcon.Trigger:
            return

        if self.isVisible():
            self.savedGeometry = self.saveGeometry()
            self.hide()
        else:
            self.show()
            self.activateWindow()
            self.restoreGeometry(self.savedGeometry)

    def populateTrayMenu(self):
        del self.trayMenu
        self.trayMenu = QMenu()

        self.trayMenu.addAction(QIcon.fromTheme("folder-new"), "Create a new notebook", self.newNotebook)
        self.trayMenu.addSeparator()

        for notebook in self.nbManager.notebooks():
            nbMenu = self.trayMenu.addMenu(QIcon.fromTheme("folder"), notebook.name)
            
            nbMenu.addAction(QIcon.fromTheme("document-new"), "Create a new note", self.newNote)
            nbMenu.addSeparator()

            for note in notebook.notes():
                nbMenu.addAction(QIcon.fromTheme("text-x-generic"), note.name)

        self.trayMenu.addSeparator()
        self.trayMenu.addAction(QIcon.fromTheme("application-exit"), "&Quit", QApplication.instance().quit)

        self.trayIcon.setContextMenu(self.trayMenu)

    def editTriggered(self, checked):
        if checked:
            self.showWidget(self.editor)
        else:
            self.preview.displayMarkdown(self.editor.toPlainText())
            self.showWidget(self.preview)            

    def readConfig(self):
        if self.settings.contains("geometry"):
            geometry = self.settings.value("geometry")
            self.restoreGeometry(geometry)

    def writeConfig(self):
        geometry = self.saveGeometry()
        
        self.settings.setValue("geometry", geometry)

    def updateUI(self):
        self.notebooksCombo.clear()

        for notebook in self.nbManager.notebooks():
            self.notebooksCombo.addItem(QIcon.fromTheme("folder"), notebook.name)

        if self.currentNotebook is not None:
            self.notesCombo.clear()

            for note in self.currentNotebook.notes():
                self.notesCombo.addItem(QIcon.fromTheme("text-x-generic"), note.name)

        if self.currentNotebook is not None and self.currentNote is not None:
            title = BASIC_TITLE + " - {}/{}".format(self.currentNotebook.name, self.currentNote.name)

            if self.dirty:
                title += " (Modified)"
        else:
            title = BASIC_TITLE

        self.setWindowTitle(title)

    def switchNotebook(self, notebookName):        
        self.currentNotebook = self.nbManager.notebook(notebookName)
        self.updateUI()

        # If notebook not empty, switch to first note.
        if len(self.currentNotebook.notes()) > 0:
            self.switchNote(self.currentNotebook.notes()[0].name)
        # If not, request creation of a new note
        else:
            self.newNote()

        self.notebooksCombo.setCurrentText(notebookName)

    def switchNote(self, noteName):
        self.currentNote = self.currentNotebook.note(noteName)
        self.editor.setPlainText(self.currentNote.contents)
        self.preview.displayMarkdown(self.currentNote.contents)

        self.updateUI()

        self.notesCombo.setCurrentText(noteName)

    def newNotebook(self):
        name, ok = QInputDialog.getText(self, "Notebook name", "How would you like your notebook to be named?")

        if ok:
            storagePath = QDir.homePath() + "/.config/wikinotebook/" + name

            nb = self.nbManager.createNewNotebook(name, storagePath)
            self.switchNotebook(nb.name)

    def newNote(self):
        if self.currentNotebook is None:
            return

        name, ok = QInputDialog.getText(self, "Note name", "How would you like your note to be named?")

        if ok:
            note = self.currentNotebook.createNewNote(name)
            self.switchNote(note.name)

    def saveNote(self):
        self.currentNote.contents = self.editor.toPlainText()
        self.currentNote.save()

        self.dirty = False
        self.editor.document().setModified(False)
        self.updateUI()

    def editorModified(self, changed):
        self.dirty = changed
        self.updateUI()