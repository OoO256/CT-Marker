import os
import sys


students = [
    # write names or ids of student that you keep exist
]

files = os.listdir(os.getcwd())

for file in files:
    if file == os.path.basename(__file__):
        continue

    is_my_student = False
    for student in students:
        if student in file:
            is_my_student = True
            break
    
    if is_my_student is False:
        os.remove(file)
