import os
import sys
import subprocess
from subprocess import Popen
import difflib
import re
import json
import pdb

class Student:
    def __init__(self):
        self.name = ""
        self.id = 0
        self.right = False
        self.did_submissoin = False
        self.runtime_error = False
        self.answer = ""
        self.code = ""

def format(path):
    return path.split('.')[-1].lower()

def get_output(path, input):
    f = format(path)

    if f == "py":
        try:
            return subprocess.check_output([sys.executable, path],
            input = input,
            universal_newlines=True)
        except:
            raise Exception("에러")

    elif f == "c":
        try:
            subprocess.check_call(u'gcc "' + path + '" -o "' + path[:-2] + '.exe"')
        except:
            raise Exception("컴파일 에러")

        try:
            p = subprocess.run(u'"'+path[:-2] + '.exe"', stdout=subprocess.PIPE, input=input, universal_newlines=True, timeout=15)

            if p.stderr != None:
                raise Exception("런타임 에러")
        except:
            raise Exception("런타임 에러")

        return p.stdout

def show(students, right_answer, skip_code=True):
    for student in students:
        print(student.id, student.name)
        if skip_code == False:
            print("학생 코드", "-"*75)
            print(student.code)
            print("-"*80)
        
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

def mark(prob_input, path_assignments, path_solution):
    # print('만든사람 이용욱, qjrmsktso2@gmail.com')
    print('채점 결과에 대해 어떠한 책임도 지지 않습니다.')
    print('\n'+'-'*80)

    students = []
    try:
        right_answer = get_output(path_solution, prob_input)
    except Exception as e:
        print('솔루션', e)
        return

    for file in path_assignments:
        _, filename = os.path.split(file)

        ct_file_checkers = [re.compile("\w{2,3}-\d{8}.*.py"),re.compile("\d{8}-\w{2,3}.*.py")]
        print(filename)
        if ct_file_checkers[0].match(filename) == None and ct_file_checkers[1].match(filename) == None:
            print(filename,": 파일명 양식이 맞지 않습니다.")
            continue
        
        student = Student()
        student.name = re.search(r'(.*?)-', file).group(0)[:-1]
        student.id = re.search(r'-(.*?)\_', file).group(0)[1:-1]
        student.code = "".join(open(file, encoding='UTF8').readlines())
        #student.code = "".join(open(file).readlines())

        try:
            student.answer = get_output(file, prob_input)
            student.right = (right_answer == student.answer)

        except Exception as e:
            student.right = False
            student.runtime_error = True

        students.append(student)
    
    print('\n'+'-'*80)    
    show(students, right_answer)