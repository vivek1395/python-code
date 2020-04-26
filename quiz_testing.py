q1='''1. How many states are there in India?
a.28
b.29
c.30
d.31'''

q2='''2. How many schedule-8 language in India?
a.22
b.23
c.8
d.16'''

q3='''3.Who is the President of India?
a. Pranav Mukharjee
b.Ramnath Kovind
c.Pratibha patil
d.Shankar Dyal Sharma'''

q4='''4.Who is the CEO of Accenture?
a.Jim Koob
b.Claire Kastler
c.Balu
d.Julie Sweet'''
q5='''5. Who is the CEO of Amazon?
a.Jim Koob
b.Tim Paine
c.Jeff Bejos
d.Martin Rolfsmeyer'''
q6='''Who has served as India's Prime minister
a.Jawahar Lal Nehru
b.Narender Modi
c.Rahul Gandhi
d.Indira Gandhi'''

import time,sys
questions={q1:'b',q2:'a',q3:'b',q4:'d',q5:'c',q6:('a','b','d')}
users={'vivek':'123','himadri':'345','rashmi':'1234','chandam':'101','uzwal':'54321'}
rem_time=300 # in seconds
name=input('Enter your name:')
if name in users:
    print('user authentication required!')
    password=input('enter your password:')
    if password==users[name]:
        print('user authentication verified.')
        time.sleep(2)
        print('Hello',name,'Welcome to quiz mania!')
    else:
        print("you have entered the wrong password,please entered the correct password.")
        sys.exit(0)
else:
    print('user',name, 'is not authorized to write this test')
    sys.exit(0)
time.sleep(3)
rule='''RULE: Before you start the quiz read the rules: for correct answer you will get 1 marks and for incorrect 
you will loose your 1 marks. if you skip the question you will get 0 marks.
 So here is your first question :'''
print(rule)
time.sleep(10)
score=0
total_correct_ans=0
total_incorrect_ans=0
l=len(questions)
t1=time.perf_counter()
for i in questions:
    print(i)
    t3=time.perf_counter()
    skip=input('Do you want to skip this question. answer in y/n:')
    if skip=='y':
        t5=time.perf_counter()
        skip_time=t5-t3
        print('time taken to skip this question is: {:5.2f} seconds'.format(skip_time))
        rem_time=rem_time - skip_time
        print('Time Left: {:5.2f} seconds'.format(rem_time))
        continue
    response=input('Please enter your answer in a/b/c/d:')
    if (len(response)==1):
        pass
    else:
        response=tuple(response)

    if questions[i]==response:
        print('your answer is correct, you got 1 point, good luck')
        score=score + 1
        total_correct_ans=total_correct_ans +1
        print('Your current score is:',score)
    else:
        print('your answer is incorrect,all the best')
        score=score -1
        total_incorrect_ans=total_incorrect_ans +1
        print('Your current score is:', score)
    t4=time.perf_counter()
    qt=t4-t3
    print('time taken to answer this question is:{:5.2f} seconds'.format(qt))
    rem_time=rem_time - qt
    print('Time Left:{:5.2f} seconds'.format(rem_time))

t2=time.perf_counter()
t=t2-t1
print('---------Here is your result---------------------')
print('Your total time taken to finish this quiz:{:5.2f} seconds'.format(t))
print('Your total score is:',score)
print('Your total correct number of answer is:',total_correct_ans)
print('Your total wrong answer is:',total_incorrect_ans)
uq =l - total_correct_ans - total_incorrect_ans
print('total no. of un-attempted question is:',uq)
if score==l:
    print('Congratulations!! your all answers are correct. You will get a chocolate .')
print('---------------------------------------------------')
print('Thank you so much',name,'to participate in the quiz')

print('Help me to improve this quiz, pls give a feedback/suggestion below:')
feedback= input('Type your feedback here:>>>')
print('Feedback from',name, 'is:',feedback)
print('**************Thank you for the feedback*******************')