favourite_lang = {'jen':'python','eric':'java','elisa':'C++',
'holki':'rubi'}
poll = ['jen','eric','resnick','halliday','tom']
for loop in poll :
    if loop in favourite_lang.items():
        print(f"{loop} thanking them .")
    else :
        print(f"{loop} inviting them to poll.")           