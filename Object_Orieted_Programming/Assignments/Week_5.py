#ENCAPSULATION-Bundling data and how it's viewed
class Student:
    def __init__(self, name):
        self.name = name        #Public
        self._gpa =3.9          #Protected= ONE UNDER SCORE
        self.__password ="1234" #Private = TWO UNDER SCORES
          
     
        
Stud1=Student("Richard")
print(f" Sudent name = {Stud1.name}\n Student gpa = {Stud1._gpa}\n Student password")
print()
#Change name to Alberrt
Stud1.name='Albert'
print(f" Sudent name = {Stud1.name}\n Student gpa = {Stud1._gpa}\n Student password = ")
print()
#Change GPA
Stud1._gpa=4.5    
print(f" Sudent name = {Stud1.name}\n Student gpa = {Stud1._gpa}\n Student password = ")