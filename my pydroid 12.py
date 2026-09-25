programmer = {'eric':'python','qwel':'java',
'oliver':'rubi','hela':'C++'}
print("This is the following language :")
numer = 0
for name in programmer.keys():
    numer += 1
    if name == 'eric':
        print(f"{numer}. {name.upper()} - this is so bad.")
    elif name == 'oliver':
         print(f"{numer}. {name.upper()} - this is very bad.So i quit it.")
   
    else :
        print(f"{numer}. {name.upper()} - this is bad.")
     