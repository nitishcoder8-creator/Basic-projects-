rivers = {'amazon':'brazil','ganga':'bharat',
'moscowa':'russia'}
for river, states in rivers.items():
    print(f"\tThe {river.upper()} runs through {states.upper()}.\n")
print("Rivers included in dictionary.")
for water in rivers.keys():
    print(water.upper())
print("\n\nThe rivers present in country.")
for place in rivers.values():
    print(place.upper())
    