import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QTextEdit, QFileDialog, QMainWindow, QInputDialog, QPushButton


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.init_UI()


    def init_UI(self):
        grid = QGridLayout()
        self.setLayout(grid)


        grid.addWidget(QLabel('채점할 폴더 : '), 0, 0)
        grid.addWidget(QLabel('학생 정보 엑셀 파일 : '), 1, 0)
        grid.addWidget(QLabel('학생 수 : '), 2, 0)
        grid.addWidget(QLabel('입력 1 : '), 3, 0)
        grid.addWidget(QLabel('입력 2 : '), 4, 0)
        grid.addWidget(QLabel('입력 3 : '), 5, 0)
        grid.addWidget(QLabel('입력 3 : '), 6, 0)

        grid.addWidget(QLineEdit(), 0, 1)
        grid.addWidget(QLineEdit(), 1, 1)
        grid.addWidget(QLineEdit(), 2, 1)
        grid.addWidget(QTextEdit(), 3, 1)
        grid.addWidget(QTextEdit(), 4, 1)
        grid.addWidget(QTextEdit(), 5, 1)
        grid.addWidget(QTextEdit(), 6, 1)

        grid.addWidget(QPushButton('Show text', self), 0, 2)
        grid.addWidget(QPushButton('Show text', self), 1, 2)

        self.setWindowTitle('CT marker')
        self.setGeometry(300, 300, 300, 200)
        self.getDirectory()
        self.show()

        
    def getDirectory(self):
        file = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        print(file)
        return file

    def getTextInput(self):
        return QInputDialog.getText(self, 'Input Dialog', 'Enter your name:')

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
