# 문제 1 : 성적 출력하기
D = {'Bob': [92, 85, 65], 'Joe': [100, 90, 75], 'Anne': [95, 90, 90], 'Jane': [55, 60, 65]} #국어, 영어, 수학의 성적이다.
print ("name quiz   mid final")
print ("---------------------")
for k, v in D.items() :
    print ("{:6s}{:3d}{:6d}{:6d}".format(k, v[0], v[1], v[2]))
print()


# 문제 2 : 리스트에 평균 추가하여 출력하기
for k, v in D.items() :
    avg = int (sum(v)/3)   #평균은 정수형으로 변환한다.
    v.append(avg)
print ("name quiz   mid final   avg")
print ("---------------------------")
for k, v in D.items() :
    print ("{:6s}{:3d}{:6d}{:6d}{:6d}".format(k, v[0], v[1], v[2], v[3]))
print()


# 문제 3 : 리스트에 학점 추가하여 출력하기
for k, v in D.items() :
    if v[3] >= 90 :
        grade = "A"
    elif v[3] >= 80 :
        grade = "B"
    elif v[3] >= 70 :
        grade = "C"
    else :
        grade = "D"
    v.append(grade)
print ("name quiz   mid final   avg grade")
print ("---------------------------------")
for k, v in D.items() :
    print ("{:6s}{:3d}{:6d}{:6d}{:6d}{:>6s}".format(k, v[0], v[1], v[2], v[3], v[4]))
print()


# 문제 4 : 추가 학생을 입력받아서 학점까지 출력하기
while(True):
    student = input ("학생의 이름과 성적을 입력하시오.(엔터입력은 종료) \n예)david 53 75 48 : ").split()
    if len(student) > 0:
        a, b, c, d = student
        b = int(b) ; c = int(c) ; d = int(d)
    
        avg = int((b+c+d)/3)
        if avg >= 90 :
            grade = "A"
        elif avg >= 80 :
            grade = "B"
        elif avg >= 70 :
            grade = "C"
        else :
            grade = "D"
        D[a] = [b, c, d, avg, grade]
        print ("name quiz   mid final   avg grade")
        print ("---------------------------------")
        for k, v in D.items() :
            print ("{:6s}{:3d}{:6d}{:6d}{:6d}{:>6s}".format(k, v[0], v[1], v[2], v[3], v[4]))
        print()
    else : break


