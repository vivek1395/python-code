q={'q1':{'a'},'q2':{'b'},'q3':{'a','b'},'q4':{'a','b','d'},'q5':{'d'}}
print(q['q3'])


for i in q:
    response=set(input('Please enter your answer in a/b/c/d:'))
    if response==q[i]:
        print('correct')
    else:
        print('Incorrect')