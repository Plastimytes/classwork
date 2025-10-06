
#####Dictionaries
D={}
D['name']='Richard'
D['Job']='Student'
D['age']='21'

#Prnting the entire dictionary
print(f"{D}")

#Printing only one entity
print(D['name'])
print()
# we can also make dictionaries by passing to the dict type name 
Richard1 = dict(name='Richard', age=21, job='Student')
print(Richard1)
print()
#Another method
Richard2 = dict(zip(['name', 'age', 'job'],['Main','23','student']))
print(Richard2)
print()

#Nesting in dictionaries(Incase the information is alot)
Record={
    'name':{'first':'John', 'last':'Mark'},
    'jobs':["student",'Dev'],
    'age': 23
}
print(Record)
print()

#Print anything to do with the name
print(Record['name'])
print()

#Print the last name
print(Record['name']['last'])
print()

#Print the jobs
print(Record['jobs'])
print()

#Remove one job
print(Record['jobs'][-1])

#Add a job
New_Record=Record['jobs'].append('Mechanic')
print(New_Record)