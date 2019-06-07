import os
import sys
from openpyxl import load_workbook
from subprocess import check_output
import difflib
from pprint import pprint

def get_students_info(path_excel, num_std):
    wb = load_workbook(path_excel)
    sheet = wb['excel']

    name_list = [sheet['B'+str(i+3)].value for i in range(num_std)]
    id_list = [sheet['C'+str(i+3)].value for i in range(num_std)]

    print("name list : ", name_list)
    print("id list : ", id_list)
    
    return zip(name_list, id_list)

def getAnswer(prob_input, path_solution):
    return check_output([sys.executable, path_solution],
                    input=prob_input,
                    universal_newlines=True,
                    shell=True,
                    encoding='utf-8')

def mark(prob_input, path_hw, path_excel, path_solution, hw_filename, num_std):
    print('만든사람 이용욱, qjrmsktso2@gmail.com')
    print('채점 결과에 대해 어떠한 책임도 지지 않습니다.')
    print('\n'+'-'*80)
    
    runtime_error_list = []
    wrong_dict = {}
    not_submit_list = []
    
    file_list = os.listdir(path_hw)

    info = get_students_info(path_excel, num_std)

    for name, id in info:
        print(name, '학생 : ', id)

        target_file = ''
        for file in file_list:
            if hw_filename.format(id=id, name=name) in file:
                target_file = file
       
        if target_file == '':
            not_submit_list.append(name)
            print('미제출!')
        
        else:
            prob_answer = getAnswer(prob_input, path_solution)

            try:
                output = check_output([sys.executable, path_hw+'/'+target_file],
                    input=prob_input,
                    universal_newlines=True,
                    encoding='utf-8')
        
                if prob_answer == output:
                    print('정답')
                else:
                    print('오답')
                    wrong_dict[name] = output
                    
            except:
                print('runtime error')
                runtime_error_list.append(name)
    
    print('\n'+'-'*80)
    print("런타임 에러 리스트 : ",runtime_error_list)
    print("미제출리스트 : ",not_submit_list)
    print("오답리스트 : ",wrong_dict.keys())
    
    print('\n'+'-'*80)
    print('오답을 학생 이름, 답안, 정답 순으로 출력합니다')
    for name, answer in wrong_dict.items():
        print()
        print('-'*20)
        print(name)
        #print(answer)
        #print(prob_answer)

        d = difflib.Differ()
        result = list(d.compare(answer.splitlines(keepends=True), prob_answer.splitlines(keepends=True)))
        pprint(result)