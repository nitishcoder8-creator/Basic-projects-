student_lang = {'arya':['hindi','sanskrit'],
'rubina':['english','tamil','kannad'],
'jacky':['french','german','hebrew'],
'kiara':['italvi','apanish','sindhi']
}
number = 1
for name, goal in student_lang.items():
   numer = 1
   print(f"\n{number}. {name.upper()}'s fav lang is:-")
   number += 1
   for lang in goal :
       print(f"\t {numer}. {lang} : this language commonly used in {lang} .")
       numer += 1   
                                               