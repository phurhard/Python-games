import random
words=['crop','dogs','fat','fast','get','hat','dog','big']
print('Guess the hidden word \n')
print('From the list of words presented below\n',words)
print('\nNOTE:All words are in small letters')
HW=random.choice(words)
mat=len(HW)

print('The hidden word is a ',+mat,' letter word')
user=input('\n')
if user in words:
	print('Congratulations mate you got the correct answer\n')
	print(user)
else:
	print('Sorry the word you choosed is wrong try again\n')
	print('The hidden word is ',HW)