'''
PHURHARDEEN(PHOENIX💸🔥)
day of the week:write a program that takes a date as input and prints the day of the week that date falls i  .your program shld take in 3 command lines :m> month, y>year ,d>day.
for m 1=january,2=february and so on
for d 0=sunday,1=monday and so on
use the formula for gregorian calender
Yo = Y - ( 14 - m ) / 12
X= Yo + ( Yo / 4 ) - ( Yo / 100 ) + ( Yo / 400 )
Mo = M + 12 * ( ( 14 - M ) / 12 ) - 2)
Do =(D + X + ( 31 * M / 12 ) ) % 7
Algorithm
1.start
2take 3 inputs and store them accordinly
3.make a dictionary of values with resoective keys
4.use formular to calculate the day
5.test the code 
6....debug
'''
#update nd catch errors eg errors of alphabet in month,unsupported date for day,using less than 4 digits for year
print('''DAY FINDER!!! FIND THE DAY WHICH THAT DATE FALLS ON😉😉😉''')
Day=int(input("\nEnter the date u wish to calculate: \nin format dd: "))
if Day>31:
	print('INVALID DATE SELECTION')
	Day=int(input('\nEnter date : '))
Montth=input("\nEnter the month\n in words e.g March  mm: ")
Year=input("Enter the year \n in format yyyy: ")
if len(Year)<4:
	print('YEAR MUST BE FOUR DIGITS\n')
	Year=input("Enter the year \n in format yyyy: ")
#Month values
months={'January':1,'February':2,'March':3,'April':4,'May':5,'June':6,'July':7,'August':8,'September':9,'October':10,'November':11,'December':12}
days={0:'Sunday',1:'Monday',2:'Tuesday',3:'Wednessday',4:'Thursday',5:'Friday',6:'Saturday'}
#calculation
Year=int(Year)
Month=int(months[Montth])
Yo = int(Year - ( 14 - Month ) / 12)
X=int( Yo +  Yo / 4  -  Yo / 100  +  Yo / 400 )
Mo = int(Month + 12 * ( ( 14 - Month ) / 12 ) - 2)
Do =int((Day + X + ( 31 * Mo/ 12 ) ) % 7)
day=days[Do]
print('The day ',+Day, Montth, Year ,'is  :',day )