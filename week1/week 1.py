#// TASK 1//
print("Robins will wear their feathery fire;")
print("Whistling their whims on a low fence -wire")
print("And not one will know of the war")
print("not one")

#//TASK 2//
#hours in a week
print(7*24)
print(60*24*7)
print(60*24*60*7)

# //TASK 3//
name=input(">What is your name?")
email=input(">What is your email adress?") 
nickname=input(">What is your nickname?")  

print("\n## Let's review your information ##")
print(">Your name:",name)
print("Your email:",email)
print("Your nickname:",nickname)

# // TASK 4 //
name="MSA"
age="31"
city="Vegas"

print(f"\n Hi ,{name} , you are {age} years old. You live in {city}.")

# // TASK 5//
name="MSA"
age="18"
skill1="pyhton"
level1="beginner"
skill2="2d artist"
level2="beginner"
lower="2000"
upper="3000"

print(f"\n my name is {name} , I am {age} years old.\n My skills are \n -{skill1} ({level1}) \n -{skill2} ({level2}) \n My salary expectation is {lower}-{upper} euros/month.s" ),

#// TASK 6//#
num1= 3
num2= 5
ans1 = (num2+num1)
ans2= (num1 - num2)
ans3= (num1 * num2)
ans4= (num1 / num2)
print(f"The results are\n 1>{ans1} \n2>{ans2}\n 3>{ans3} \n 4<{ans4} ")

#// TASK 7 //
weight=float(input("What is your body weight in kg?"))
height=float(input("How tall are you in m?"))
ans= (weight/(height*height))
print(f"Your BMI is {ans}.")

#// TASK 8// 

gamename= "Half-Life"
year=float(input("Which year your game released?"))
currentyear=2025
ans=(currentyear - year)
print(f"{gamename} is {ans} years old.")

#// TASK 9//
number1 = int(input("Please type in the first number: "))
number2 = int(input("Please type in the second number: "))
number3 = int(input("Please type in the third number: "))
product = (number1 * number2 * number3)
print(f"The product is, {product}")

#//TASK10//
kafeterya=float(input(">How many times a week do you eat at the student cafeteria?"))
yemek=float(input(">The price of a typical student lunch?"))
alışv=float(input(">How much money do you spend on groceries in a week?"))
week=7
Month=30
ans1=((kafeterya*yemek+alışv)/week)
ans2=((kafeterya*yemek+alışv))
ans3=((kafeterya*yemek+alışv)/week*Month)
print(f"Daily expanses:{ans1}")
print(f"Weekly expanses:{ans2}")
print(f"Monthly expanses.{ans3}")