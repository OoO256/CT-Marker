import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QTextEdit, QFileDialog, QMainWindow, QInputDialog, QPushButton
import marker


class MyApp(QWidget):

    def __init__(self):
        super().__init__()

        self.buttons = {}
        self.buttons['mark'] = QPushButton('mark', self)
        self.buttons['mark'].clicked.connect(self.mark)
        self.lines = {}
        self.inputs = []

        self.path_hw = ''
        self.path_excel = ''
        self.path_solution = ''
        self.num_stu = 0

        self.init_UI()


    def init_UI(self):
        self.grid = QGridLayout()
        self.setLayout(self.grid)

        self.addLine(0, 'submit', '체점할 폴더 : ', 'line', button='선택',  callback=self.get_path_hw)
        self.addLine(1, 'filename', '파일명 양식 : ', 'line')
        self.addLine(2, 'excel', '학생 정보 엑셀 파일 : ', 'line', button='선택', callback=self.get_path_excel)
        self.addLine(3, 'num_stu', '학생 수 : ', 'line')
        self.addLine(4, 'solution', '정답 코드 파일 : ', 'line', button='선택', callback=self.get_path_solution)
        self.addLine(5, 'input1', '입력 1 : ', 'text')
        self.addLine(6, 'input1', '입력 2 : ', 'text')
        self.addLine(7, 'input1', '입력 3 : ', 'text')
        self.addLine(8, 'input1', '입력 4 : ', 'text')
        self.grid.addWidget(self.buttons['mark'], 9, 0)

        self.setWindowTitle('CT marker')
        self.setGeometry(300, 300, 300, 200)
        self.resize(600, 400)
        self.show()

    
    def addLine(self, idx, name, text, box = 'line', button = None, callback = None):
        self.grid.addWidget(QLabel(text), idx, 0)

        if box is 'line':
            self.lines[name] = QLineEdit()
            self.grid.addWidget(self.lines[name], idx, 1)
        elif box is 'text':
            self.inputs.append(QTextEdit())
            self.grid.addWidget(self.inputs[len(self.inputs) - 1], idx, 1)

        if button is not None:
            self.buttons[name] = QPushButton(button, self)
            self.grid.addWidget(self.buttons[name], idx, 2)

            self.buttons[name].clicked.connect(callback)

    def get_path_hw(self):
        self.path_hw = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.lines['submit'].setText(self.path_hw)

    def get_path_excel(self):
        self.path_excel = str(QFileDialog.getOpenFileName(self,"get_path_excel", "" ,"Excel Files (*.xlsx)")[0])
        self.lines['excel'].setText(self.path_excel)

    def get_path_solution(self):
        self.path_solution = str(QFileDialog.getOpenFileName(self, "get_path_solution", "", "Python Files (*.py)")[0])
        self.lines['solution'].setText(self.path_solution)

    def mark(self):
        string_stu = self.lines['num_stu'].text()
        try:
            self.num_stu = int(string_stu)
        except:
            print("잘못된 학생수입니다.")
            pass

        file_form = self.lines['filename'].text()
        for i in range(4):
            if self.inputs[i].toPlainText() is '':
                break

            prob_inputs = self.inputs[i].toPlainText().split('//')
            prob_inputs = '\n'.join(prob_inputs)

            marker.mark(prob_input=prob_inputs, path_hw = self.path_hw, path_excel = self.path_excel, path_solution = self.path_solution, hw_filename = file_form, num_std = self.num_stu)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
