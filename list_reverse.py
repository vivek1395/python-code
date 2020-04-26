list=['a','b','c','d']

# method-1 using slice operator
rev_list=list[::-1]
print(rev_list)

# method -2: using reverse function

list.reverse()
print(list)

# method-3: using loop

n=len(list)
rl=[]

for i in range(n):
    rl.append(list[n-i-1])
print(rl)

