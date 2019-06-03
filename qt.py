import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QTextEdit, QFileDialog, QMainWindow, QInputDialog, QPushButton

class MyApp(QWidget):

    def __init__(self):
        super().__init__()

        self.buttons = {}
        self.buttons['hw'] = QPushButton('...', self)
        self.buttons['excel'] = QPushButton('...', self)
        self.buttons['mark'] = QPushButton('체점하기', self)

        self.buttons['hw'].clicked.connect(self.get_path_hw)
        self.buttons['excel'].clicked.connect(self.get_path_excel)
        self.buttons['mark'].clicked.connect(self.mark)


        self.lines = {}
        self.lines['hw'] = QLineEdit()
        self.lines['excel'] = QLineEdit()
        self.lines['num'] = QLineEdit()

        self.inputs = []
        self.inputs.append(QTextEdit())
        self.inputs.append(QTextEdit())
        self.inputs.append(QTextEdit())
        self.inputs.append(QTextEdit())

        self.path_hw = ''
        self.path_excel = ''
        self.num_stu = 0

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
        grid.addWidget(QLabel('입력 4 : '), 6, 0)
        grid.addWidget(self.buttons['mark'], 7, 0)

        grid.addWidget(self.lines['hw'], 0, 1)
        grid.addWidget(self.lines['excel'], 1, 1)
        grid.addWidget(self.lines['num'], 2, 1)
        grid.addWidget(self.inputs[0], 3, 1)
        grid.addWidget(self.inputs[1], 4, 1)
        grid.addWidget(self.inputs[2], 5, 1)
        grid.addWidget(self.inputs[3], 6, 1)

        grid.addWidget(self.buttons['hw'], 0, 2)
        grid.addWidget(self.buttons['excel'], 1, 2)

        self.setWindowTitle('CT marker')
        self.setGeometry(300, 300, 300, 200)
        self.resize(600, 400)
        self.show()

    def getTextInput(self):
        return QInputDialog.getText(self, 'Input Dialog', 'Enter your name:')

    def get_path_hw(self):
        self.path_hw = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.lines['hw'].setText(self.path_hw)

    def get_path_excel(self):
        self.path_excel = str(QFileDialog.getOpenFileName(self,"get_path_excel", "" ,"Excel Files (*.xlsx)")[0])
        self.lines['excel'].setText(self.path_excel)

    def mark(self):
        string_stu = self.lines['num'].text()
        try:
            self.num_stu = int(string_stu)
        except:
            print("잘못된 학생수입니다.")
            pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
