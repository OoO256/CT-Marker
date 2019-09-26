import os
import sys
from subprocess import check_output
import difflib
import re
import json


def getAnswer(prob_input, path_solution):
    return check_output([sys.executable, path_solution],
                    input=prob_input,
                    universal_newlines=True,
                    shell=True,
                    encoding='utf-8')

def mark(prob_input, path_hw, path_solution):
    print('만든사람 이용욱, qjrmsktso2@gmail.com')
    print('채점 결과에 대해 어떠한 책임도 지지 않습니다.')
    print('\n'+'-'*80)
    
    runtime_error_list = []
    wrong_dict = {}
    not_submit_list = []

    prob_answer = getAnswer(prob_input, path_solution)
    for file in os.listdir(path_hw):
        ct_file_checker = re.compile("\[.{2,3}-\d{8}\](.*)\.py")
        if ct_file_checker.match(file) == None:
            print(file,": 컴퓨팅사고력 양식에 맞지 않습니다.")
            continue
        
        name = re.search(r'\[(.*?)-', file).group(0)[1:-1]
        id = re.search(r'-(.*?)\]', file).group(0)[1:-1]        

        try:
            output = check_output([sys.executable, path_hw+'/'+file],
                input=prob_input,
                universal_newlines=True)
    
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
        result = list(d.compare(prob_answer.splitlines(keepends=True), answer.splitlines(keepends=True)))
        sys.stdout.writelines(result)

if __name__ == "__main__":

    if ".config.json" in os.listdir():
        print("이전 설정이 있습니다.")
        with open(".config.json") as f:
            config = json.load(f)
            print("prob_input : ", config['marker']['prob_input'])
            print("path_hw : ", config['marker']['path_hw'])
            print("path_solution : ", config['marker']['path_solution'])
            same = input("똑같이 진행하시겠습니까? [Y/N]")
            if same.lower() == 'y':
                mark(config['marker']['prob_input'], config['marker']['path_hw'], config['marker']['path_solution'])
    else:
        prob_input = input("prob_input")
        path_hw = input("path_hw")
        path_solution = input("path_solution")

        config = {}
        config['marker'] = {
            'prob_input' : prob_input,
            'path_hw' : path_hw,
            'path_solution' : path_solution
        }
        with open(".config.json", 'w') as outfile:
            json.dump(config, outfile, ensure_ascii = False, indent=4)