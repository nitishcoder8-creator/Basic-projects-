student = {'name':'Ankit','class':'10th',
'subject':['maths','science','economics','hindi'],
'friends':['shila','sarita','holki']
}
print(f"\nThe name of {student['name']}'s subject are : ")    

for numer, loop in enumerate(student['subject'],start = 1) :
    print(f"{numer}. {loop.upper()}")                    
    
