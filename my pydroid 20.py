scientist = {
'einstein':
    {'name':'albert',
    'age':67,
    'wife':'marry'
    },
'homi bhava':
    {
    'country':'bharat',
    'state':'bihar',
    'age':66
    },
'kalam':
    {
    'name':'APJ',
    'state':'tamilnadu',
    'age':79
    }
}
number_1 = 1
for great, science in scientist.items():
    print(f"\n{number_1}. The name of scientist is {great.upper()} .")
    number_1 += 1
    number_2 = 1
    for greatness, value in science.items():
        
        print(f"\t{number_2}. {greatness.title()} : {value}")     
        number_2 +=1