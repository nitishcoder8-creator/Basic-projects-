comlang = {'jok':'python',
'rol':'java',
'heli':'c++',
'kling':'C'
}
enemy = ['jok','rol']
for name ,loop in comlang.items() :
    if name in enemy :
        print(f"hi {name.upper()},\n\ti know you lang {loop.upper()} .")