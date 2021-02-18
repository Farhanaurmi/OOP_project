class stu():
    def __init__(self,di):
        self.di=di
    def student_due(self,clas):
        self.clas=clas
        if clas>=1 and clas<=3:
            return 2000
        if clas>=4 and clas<=8:
            return 4000
        if clas>=9 and clas<=10:
            return 6000

class dent():
    def __init__(self,di):
        self.di=di

    def student_grade(self,student_numbers):
        self.students_numbers=student_numbers
        total=count=0
        for i in student_numbers:
            total=total+i
            count=count+1
        avg=total/count
        if avg>=80 and avg<=100:
            return 'A+'
        elif avg>=70:
            return 'A'
        elif avg>=60:
            return 'A-'
        elif avg>=50:
            return 'B'
        elif avg>=33:
            return 'C'
        else:
            return 'F'

class user(stu,dent):
    def __init__(self,dic):
        super().__init__(dic)
        self.dic=dic
        

    def output(self):
        for i,j in self.dic.items():
            if i==query_name:
                for k in j:
                    yield k
                

dic={}
N=int(input())
for i in range (N):
    name,*line=input().split()
    age_class=list(map(int,line))
    dic[name]=age_class
query_name=input('Enter name: ')
query=user(dic)
while(1):
    number=int(input('\nEnter number:\n1.Age and Class\n2.Student due\n3.Student grade\n4.Exit\n'))
    if number==1:
        li=list(query.output())
        print(f'Age = {li[0]}\nClass = {li[1]}')
    elif number==2:
        li=list(query.output())
        print(f'Student due: {query.student_due(li[1])}')
    elif number==3:
        sub=int(input('Enter total subject number: '))
        sub_numbers=list(map(int,input().split()))
        print(f'Student grade: {query.student_grade(sub_numbers)}')
    elif number==4:
        break