aliens = []
for alien_num in range(0,30):
    new_aliens = {'colour':'green','speed':'slow','points':5}
    aliens.append(new_aliens)
for alien in aliens[0:3]:
    if alien['colour'] == 'green':
        alien['colour'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    
    elif alien['colour'] == 'yellow':
        alien['colour'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 20  
for alien in aliens[0:5]:
    print(alien)