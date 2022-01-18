from __future__ import unicode_literals
import sys
from PySide6 import QtCore, QtWidgets, QtGui
from shutil import move
import youtube_dl

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.text = QtWidgets.QLabel("Enter link to video", alignment=QtCore.Qt.AlignCenter)
        self.link = QtWidgets.QLineEdit()
        self.message = QtWidgets.QLabel(alignment = QtCore.Qt.AlignCenter)
        self.destination = QtWidgets.QLabel('', alignment=QtCore.Qt.AlignCenter)

        self.choose = QtWidgets.QPushButton('Choose Destination')
        
        self.button = QtWidgets.QPushButton("Download")
        
        
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.link)
        self.layout.addWidget(self.choose)
        self.layout.addWidget(self.destination)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.message)

        self.choose.clicked.connect(self.chooseDir)
        self.button.clicked.connect(self.magic)

    
    def chooseDir(self):
        destination = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Destination')
        return self.destination.setText(destination)

    @QtCore.Slot()
    def magic(self):
        #try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.cache.remove()
            meta = ydl.extract_info(self.link.text(), download=True)
        title = meta['title']
        _id = meta['id']
        fileName = f'{title}-{_id}.mp3'
        outFile = f'{title}.mp3'
        destination = self.destination.text() + '/' + outFile
        move(fileName, destination)
        
        self.message.setText('Downloaded Audio Successfully.')
        #except:
            #self.message.setText('There was an error. Please check your request.')

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    app.setApplicationName('FluYT Downloader')
    app.setApplicationDisplayName('FluYT')
    
#<a href="https://www.flaticon.com/free-icons/boat" title="boat icons">Boat icons created by max.icons - Flaticon</a>    
    app.setWindowIcon(QtGui.QIcon('./pirate-ship.png'))

    widget = MyWidget()
    widget.resize(400, 100)
    widget.show()

    sys.exit(app.exec())