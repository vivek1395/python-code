q={'q1':'a','q2':'b','q3':('a','b'),'q4':('a','b','d'),'q5':'d'}
print(q)
score=0

for i in q:
    r=input('enter your response:')
    if len(r)==1:
        print(len(r))
        pass
    else:
        r=tuple(r)
    print('length of response is:',len(r))
    print('the number of answer is:',len(q[i]))
    j=0
    q_score=0
    if len(r)==len(q[i]):
        pass
        while(len(r)>j):
            if (r[j] in q[i]):
                q_score=1
                print(r[j],q[i],'correct:',q_score)
            else:
                q_score=-1
                print(r[j], q[i], 'incorrect:',q_score)
                break
            j=j+1
    elif len(r)==0:
        q_score=0
    else:
        q_score=-1
    if (q_score==1):
        print('Correct, Well done!!, You got 1 marks')
    elif (q_score==0):
        print('You have skipped the question and got 0 marks')
    else:
        print('Incorrect')

    score=score + q_score
    print('Your current score is:',score)

'''t=tuple(input('enter your value:'))
print(t)'''
print('score',score)
