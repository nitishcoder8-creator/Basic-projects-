game_1 = {'colour':'green','place':'space'}
game_2 = {'weapon':'laser','suit':'iron'}
game_3 = {'company':'chatgpt','smart':'genius'}

game = [game_1,game_2,game_3]
for gaming in game :
    print(f"{gaming}\n\n")  
    
aliens = []
for alien_num in range(20):
  new_alien = {'color':'green','speed':'slow','points':5}
  aliens.append(new_alien)
for all in aliens[:5] :
  print(f"{all} \n ..... .")
print(f"\n\nTotal number of aliens is {len(aliens)} .")