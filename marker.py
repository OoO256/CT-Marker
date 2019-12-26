import os
import sys
from subprocess import check_output
import difflib
import re
import json

class Student:
    def __init__(self):
        self.name = ""
        self.id = 0
        self.right = False
        self.did_submissoin = False
        self.runtime_error = False
        self.answer = ""
        self.code = ""

def getAnswer(prob_input, path_solution):
    return check_output([sys.executable, path_solution],
                    input=prob_input,
                    universal_newlines=True)

def show(students, right_answer):
    for student in students:
        print(student.id, student.name)

        if student.right:
            print("정답")
        else:
            print("오답")
            if student.runtime_error:
                print("런타임 에러")
            else:
                d = difflib.Differ()
                result = list(d.compare(right_answer.splitlines(keepends=True), student.answer.splitlines(keepends=True)))
                sys.stdout.writelines(result)
        print("")
        print('-'*80)
        print("")

def mark(prob_input, path_assignments, path_solution, format):
    print('만든사람 이용욱, qjrmsktso2@gmail.com')
    print('채점 결과에 대해 어떠한 책임도 지지 않습니다.')
    print('\n'+'-'*80)

    students = []
    right_answer = getAnswer(prob_input, path_solution)

    for file in path_assignments:
        _, filename = os.path.split(file)
        
        ct_file_checker = re.compile("\[.{2,3}-\d{8}\](.*)\.py")
        if ct_file_checker.match(filename) == None:
            print(filename,": 컴퓨팅사고력 양식에 맞지 않습니다.")
            continue
        
        student = Student()
        student.name = re.search(r'\[(.*?)-', filename).group(0)[1:-1]
        student.id = re.search(r'-(.*?)\]', filename).group(0)[1:-1]
        student.code = open(file).readlines()

        try:
            if format == "Python":
                student.answer = check_output([sys.executable, file],
                    input=prob_input,
                    universal_newlines=True)
            elif format = "C":
                subprocess.run(["gcc", "-o", filename+".o", file])

    
            if right_answer == student.answer:
                student.right = True
            else:
                student.right = False

        except:
            student.right = False
            student.runtime_error = True

        students.append(student)
    
    print('\n'+'-'*80)    
    show(students, right_answer)