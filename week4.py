grade_one= {'Sami': [19, 18, 19.5, 30, 10], 'Ahmad': [15, 14, 16, 21, 7], 'Faris': [18, 19, 17, 26, 9], 'Salem': [20, 20, 19, 30, 10], 'Mahmoud': [12, 13, 11, 18, 7]}

grade_two= {'Lana': [17, 19, 20, 28, 9], 'Dina': [18.5, 19.5, 20, 29, 10], 'Maha': [20, 20, 18, 26, 9], 'Abeer': [16, 18, 19.5, 25, 8]}

grade_three= {'Rima': [18, 19, 18, 26, 9], 'Tala': [20, 20, 19, 29, 10], 'Lamar': [19, 20, 18, 26, 9], 'Rola': [15, 14, 16, 19, 7], 'Naya': [9, 6, 11, 14, 7], 'Dalal': [1, 5, 2, 6, 7], 'Ola': [19.5, 20, 20, 29.5, 10]}
grade={}
def student_name(grade):
    return list(grade.keys())
def student_score(grade,name):
    if name in grade  :
       l=grade.get(name)
       return sum(l[:4])
def student_count(grade) :
    return len(grade.keys())
while True:
    n=input(' choose one:student_name,student_score,student_count:= ')
    if n =='student_name' :
        num = input('enter class number one  or two or three : ')
        if num=='one':
            print(student_name(grade_one))
        elif num=='two':
            print(student_name(grade_two))
        else:
            print(student_name(grade_three))
        i =input('type:done if you finish or more to select function :')
        if i=='done':
            break
    elif n=='student_score':
         sn=input('student_name is:')
         num=(input('class number is  one or two or three :' ))
         if num=='one':
             print(student_score(grade_one,sn))
         elif num=='two':
             print(student_score(grade_two,sn))
         else:
             print(student_score(grade_three,sn))
         i =input('type:done if you finish or more to select function :')
         if i=='done':
             break
    else:
        c =input('enter class number : one or two or three :')
        if c=='one':
             print(student_count(grade_one))
        elif c=='two':
             print(student_count(grade_two))
        else:
             print(student_count(grade_three))
        i =input('type:done if you finish or more to select function :')
        if i=='done':
             break
