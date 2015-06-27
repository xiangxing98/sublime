#看来你用的是python 3.x版本,input函数返回的是字符串,执行强制类型转换就行了
#guess = int(input("What's yer guess?"))
#运行这些python 2的例子,最好还是下载python 2.x,否则还会有很多不兼容的地方
num = 10
print ('Guess what I think?')
answer = int(input())

#result = answer<num
if answer<num:
    print ('too small?')
#print(result)

#result = answer>num
if answer>num:
    print ('too big?')
#print(result)

#result = answer==num
if answer==num:
    print ('equal?')
#print(result)

import random
secret = random.randint(1,99)
guess = 0
tries = 0
print ("AHOY! I'm the Dread Pirate Roberts, and I have a secret!")
print ("It is a number from 1 to 99. I'll give you 6 tries")
while guess != secret and tries < 6:
    guess = int(input("What's yer guess?"))
    if guess < secret:
        print ("Too low, ye scurvy dog")
    elif guess > secret:
        print ("Too high, landlubber!")
    tries = tries + 1
    if guess == secret:
        print ("Avast! Ye got it! Found my secret, ye did!")
    else:
        print ("No more guesses!Better luck next time, matey!")
        print ("The secret number was", secret)   
