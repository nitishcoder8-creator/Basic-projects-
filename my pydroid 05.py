current_users = [' kilo ' , ' admin ' , ' loki ' , ' poli ' , ' roki ' , ' moli ' , ' oli ']
new_users = [' moli ' , ' oli ' , ' poli ' , ' noni ' , ' mini ' , ' romi ']
for user in current_users :
    if user in new_users :
        print("\n\tThe person will need to enter a new user name .")
    else :
        print("\n\tThe user name is available .")