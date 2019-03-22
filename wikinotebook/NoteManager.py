from PySide2.QtCore import QFile, QDir, QTextStream, QSettings

MARKDOWN_EXT = "md"
MARKDOWN_PATTERN = "*.md"

def readMarkdownFile(fileName):
    inFile = QFile(fileName)

    if not inFile.open(QFile.ReadOnly | QFile.Text):
        inFile.close()

        print("Couldn't read {}".format(fileName))

        return ""

    stream = QTextStream(inFile)
    contents = stream.readAll()
    inFile.close()

    return contents

class Note:
    def __init__(self, name, backingStoragePath, contents=""):
        self.name = name
        self.contents = contents
        self.backingStoragePath = backingStoragePath

    def save(self):
        outFile = QFile(self.backingStoragePath)

        if not outFile.open(QFile.WriteOnly | QFile.Text):
            outFile.close()

            return False

        stream = QTextStream(outFile)
        stream << self.contents

        outFile.close()

class Notebook:
    def __init__(self, name, localStoragePath):
        self.name = name
        self.localStoragePath = localStoragePath

        self.allNotes = []
        self.loadNotesMetadata()

    def loadNotesMetadata(self):
        localDir = QDir(self.localStoragePath)

        noteFileInfos = localDir.entryInfoList([MARKDOWN_PATTERN], QDir.Files | QDir.NoDotAndDotDot)

        for noteFileInfo in noteFileInfos:
            absPath = noteFileInfo.absoluteFilePath()

            name = noteFileInfo.baseName()
            contents = readMarkdownFile(absPath)

            self.allNotes.append(Note(name, absPath, contents))

            print("Loaded note {} from {}".format(name, absPath))

    def notes(self):
        return self.allNotes

    def note(self, name):
        for note in self.notes():
            if note.name == name:
                return note
        
        raise KeyError(name)

    def createNewNote(self, name):
        outFileName = name + ".md"        
        backingFileName = self.localStoragePath + "/" + outFileName

        outFile = QFile(backingFileName)
        outFile.open(QFile.NewOnly | QFile.Text)
        outFile.close()

        note = Note(name, backingFileName)
        note.save()
        self.allNotes.append(note)

        return note

from .config import ORGANIZATION_STR

class NotebookManager:
    def __init__(self):
        self.settings = QSettings(ORGANIZATION_STR)        
        self.allNotebooks = []

        self.readConfig()

    def notebook(self, name):
        for notebook in self.allNotebooks:
            if notebook.name == name:
                return notebook
        
        raise KeyError(name)

    def notebooks(self):
        return self.allNotebooks

    def createNewNotebook(self, name, storagePath):
        ok = QDir(storagePath).mkpath(".")
        nb = Notebook(name, storagePath)

        self.allNotebooks.append(nb)
        self.writeConfig()

        return nb

    def readConfig(self):
        notebookCount = self.settings.beginReadArray("notebooks")

        for i in range(notebookCount):
            self.settings.setArrayIndex(i)
            name = self.settings.value("name")
            storagePath = self.settings.value("storagePath")

            self.allNotebooks.append(Notebook(name, storagePath))

        self.settings.endArray()

    def writeConfig(self):
        #self.settings.beginGroup("notebooks")

        self.settings.beginWriteArray("notebooks")
        for i, notebook in enumerate(self.allNotebooks):
            self.settings.setArrayIndex(i)
            self.settings.setValue("name", notebook.name)
            self.settings.setValue("storagePath", notebook.localStoragePath)

        self.settings.endArray()
        self.settings.sync()
        #self.settings.endGroup()