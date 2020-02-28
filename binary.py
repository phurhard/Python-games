#creating a decimal to binary converter
'''
steps to do i.e algorithm
1 start import math module
2.take userut from user
3.get the moduli remainder 
4 use a for loop 
5. print the moduli of the numbers till the last number
'''
'''
written by Phoenixx $ Maverick
20/02/2020
12:05 am
V1.0
V2 will be GUI
'''
print('''\nA simple program to convert any  number in base 10  into its equivalent 
binary format \n''')
user =int(input("Enter the number: "))
bina_num=[]
while user!=0:

    if user % 2 ==0:
        
        bina_num.append('0')
        user=int(user/2)
        continue
    elif user%2 == 1:
        bina_num.append('1')
        user=int(user/2)
        continue
    elif user == 1:
        bina_num.append('1')
        bina_num.append('1')
        break
output=[]
for a in range(0,len(bina_num)):
	output.append(bina_num[a])

print('THE BINARY FORMAT  IS ',(output[::-1]))
print('''\n___________phoenixx__________\n
_____phurhardeen@gmail.com_________
-----------phurhard@github.com---++--''')