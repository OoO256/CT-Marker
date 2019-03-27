import os
import sys
from openpyxl import load_workbook
from subprocess import check_output

num_std = 56
info = load_workbook('student_info.xlsx')

sheet = info['Sheet1']

name_list = [sheet['B'+str(i+3)].value for i in range(num_std)]
id_list = [sheet['C'+str(i+3)].value for i in range(num_std)]
    
print("name list : ", name_list)
print("id list : ", id_list)

file_list = os.listdir('./')

wrong_list = []
not_submit_list = []

for name, id in zip(name_list, id_list):
    print(name, '학생 : ', id)

    target_file = ''
    for file in file_list:
        if (('H1_1_'+id) in file):
            target_file = file

       
    if(target_file == ''):
        not_submit_list.append(name)
        print('미제출!')
        
    else:
        prob_input =  '' # \n'.join(['loop', 'pool'])
        prob_answer = "현재가격(원) : 41800\n보유수량(주) : 60\n매수금액(원) : 2532000\n평균가(원) : 42200.0\n수익률(%) : -0.95\n"
 
        output = check_output([sys.executable, './'+target_file],
                      input=prob_input,
                      universal_newlines=True)
        
        if (prob_answer == output):
            print('정답')
        else:
            print('오답')
            wrong_list.append(name);

print("미제출리스트 : ",not_submit_list)
print("오답리스트 : ",wrong_list)
