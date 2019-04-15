import os
import sys
from openpyxl import load_workbook
from subprocess import check_output

num_std = 55
prob_answer = ''

def get_students_info():
    wb = load_workbook('student_info.xlsx')
    sheet = wb['excel']

    name_list = [sheet['B'+str(i+3)].value for i in range(num_std)]
    id_list = [sheet['C'+str(i+3)].value for i in range(num_std)]

    print("name list : ", name_list)
    print("id list : ", id_list)

    num_std
    
    return zip(name_list, id_list)

def getAnswer(prob_input):
    return check_output([sys.executable, './answer.py' ],
                    input=prob_input,
                    universal_newlines=True)


if __name__ == '__main__':
    print('만든사람 이용욱, qjrmsktso2@gmail.com')
    print('채점 결과에 대해 어떠한 책임도 지지 않습니다.')
    print('\n'+'-'*80)
    
    prob_input = input('체점할 입력을 입력해주세요 : ')
    path_assignments = input('과제 파일의 경로를 문자열의 마지막에 \ 문자 없이 입력해주세요 : ')
    print('\n'+'-'*80)
    
    runtime_error_list = []
    wrong_dict = {}
    not_submit_list = []

    
    file_list = os.listdir(path_assignments)

    info = get_students_info();

    for name, id in info:
        print(name, '학생 : ', id)

        target_file = ''
        for file in file_list:
            if (('H4_1_'+id) in file):
                target_file = file

       
        if(target_file == ''):
            not_submit_list.append(name)
            print('미제출!')
        
        else:
            prob_answer = getAnswer(prob_input)

            try:
                output = check_output([sys.executable, path_assignments+'/'+target_file],
                    input=prob_input,
                    universal_newlines=True)
        
                if (prob_answer == output):
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
        print(answer, end='')
        print(prob_answer, end='')
        
