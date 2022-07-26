import random
a=0
z=input('Number you want: ')
b=input('How many sides: ')
c=input('Go till: ')
list=[]
list.append(int(b))
#add numbers on dice
while int(b) >1:
    b = int(b) - 1

    list.append(b)
twenties=[]
for i in range(int(c)):
    a+=1
    number = random.choice(list)
    print(number)
    if number==int(z):
        twenties.append(number)
    else:
        pass
print('Amount of ' + z + ' rolled.')
print (len(twenties))
