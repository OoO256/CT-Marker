import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QTextEdit, QFileDialog, QPushButton
import marker

class MyApp(QWidget):

    def __init__(self):
        super().__init__()

        self.lines = {}
        self.inputs = []

        self.path_assignments = []
        self.path_solution = ''

        self.init_UI()

    def init_UI(self):
        self.grid = QGridLayout()
        self.setLayout(self.grid)

        self.addLine(0, 'submit', '체점할 파일들 : ', 'line', button='선택',  callback=self.get_path_hw)
        self.addLine(1, 'solution', '정답 코드 파일 : ', 'line', button='선택', callback=self.get_path_solution)
        self.addLine(2, 'input1', '입력 1 : ', 'text')
        self.addLine(3, 'input1', '입력 2 : ', 'text')
        self.addLine(4, 'input1', '입력 3 : ', 'text')
        self.addLine(5, 'input1', '입력 4 : ', 'text')

        '''
        combo = QComboBox(self)
        combo.addItem("과제 형식 선택")
        combo.addItem("Python")
        combo.addItem("C")
        combo.activated[str].connect(self.on_combo_changed)
        self.grid.addWidget(combo, 6, 0)
        '''

        btn_mark = QPushButton('채점', self)
        btn_mark.clicked.connect(self.mark)
        self.grid.addWidget(btn_mark, 6, 1)

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
            btn = QPushButton(button, self)
            self.grid.addWidget(btn, idx, 2)

            btn.clicked.connect(callback)

    def get_path_hw(self):
        caption = 'Open file'
        directory = '../'
        filter_mask = "Python/C files (*.py *.pyw *.c *.cpp)"
        self.path_assignments = QFileDialog.getOpenFileNames(None, caption, directory, filter_mask)[0]
        self.lines['submit'].setText("got it!")

    def get_path_solution(self):
        self.path_solution = str(QFileDialog.getOpenFileName(self, "get_path_solution", "", "Python/C files (*.py *.pyw *.c *.cpp)")[0])
        self.lines['solution'].setText(self.path_solution)

    def mark(self):

        for i in range(4):
            if self.inputs[i].toPlainText() is '':
                break

            prob_inputs = self.inputs[i].toPlainText().split('//')
            prob_inputs = '\n'.join(prob_inputs)
            # ??

            marker.mark(prob_input=prob_inputs, path_assignments = self.path_assignments, path_solution = self.path_solution)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
