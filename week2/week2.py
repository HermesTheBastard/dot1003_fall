#// TASK 11//

temp=float(input(">Please type in a temperature"))
ans1=((temp - 32) *5/9)
print(f"{temp} Fahrenheit is equal to: {ans1}.")
if ans1 < 0:
    print("Brr, Its cold out here.")

#//TASK 12//
hour=float(input("Hourly wage"))
hournum=float(input("Working hours"))
days=(input("Day of the week"))
ans=(hour*hournum)
ans2=(hour*hournum*2)

if days== ("saturday"):
    print(f"daily wage is {ans2}")
elif days in ["monday","tuesday","wednesday","thursday","friday","sunday"]:
    print(f"daily wage is{ans}")

else:
     print("Invalid day please enter a valid day name." )
     #//TASK 12//

age=float(input("How old are you?"))
if age<18 :
    print(">You can’t play Dark Souls")
elif age>44:
    print("You are too old for this sh*t")
else:
    print(">Here is Dark Souls. Lol")

    #//TASK 13//
    fnumber=float(input("Type the first number."))
snumber=float(input("Type the second number."))

if fnumber>snumber:
    print("First number is greater")
elif fnumber<snumber:
    print("Second number is greater")
else:
    print("These numbers are equal to each other")

    #//TASK 14//
fword=input("Type the first word.")
sword=input("Type the second word.")

if fword>sword:
    print(f"{fword} comes last")
elif sword>fword:
    print(f"{sword} comes last")
else:
    print(">These are same!")

    #//TASK 15//

com=input("Which community do you belong to?")
if com==("NCR"):
    print(">You’re belong to Fallout Universe.")
elif com in ["Brotherhood of Steel","Caesar’s Legion","Great Khans","Vault Dweller"]:
    print(">Nope, you are not belong to Fallout Lore")
else:
    print("You entered a invalid community.")

   #//TASK 16 //
poi=int(input(">How many points [0-100]:"))

if poi<0:
    print("you what?")
elif poi >=0 and poi <=49 :
    print("Fail.")
elif poi >=50 and poi<=59 :
    print("1")
elif poi >= 60 and poi<=69 :
    print("2")
elif poi >= 70 and poi<= 79 :
    print("3")
elif poi >= 80 and poi<= 89 :
    print("4")
elif poi>=90 and poi <=100 :
    print("5")
else:
    print("impossible!!!!")
    #// TASK 17 //

num=int(input(">Enter number:"))
if num % 3 == 0 and num % 5 == 0 :
    print("FizzBuzz")
elif num % 3 == 0:
    print("Fizz")
elif  num % 5 == 0:
    print("Buzz")
else:
    print("Try another number.")

     #//TASK 18 //
number = int(input("Please type in a number: "))

if number <= 0:
    print("The number is negative or zero")
elif number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")
    #//TASK 19//
year=int(input(">Please type in a year:"))
if year  % 4 == 0 and year %100 !=0:
    print(">That year is a leap year.") 
elif year %4 == 0 and year% 100 == 0 and year % 400 == 0:
    print(">That year is a leap year.")
else:
    print(">That year is not a leap year.")
    #//TASK 20 //
def name(arg1):
    print(f"Hello {arg1}")
name("Gordon")
