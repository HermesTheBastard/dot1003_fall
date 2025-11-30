#//TASK 21//
def name(arg1):
    return f"Hello {arg1}"
print(name("Gordon"))

    #//TASK 22//
def sum( a,b ):
    return a+b
print(sum(3,2))

    #//TASK 23//
def greeting(arg1):
    return f"Hello,{arg1}"
print(greeting("Gordon freeman"))
print(greeting("Anrew Ryan"))
      #//TASK 24//
def mean(a,b,c):
    return ((a+b+c) /3)
print(mean(1,2,3))

     # //TASK 25//

myflag = True

while myflag:
    name = input("Say my name: ")
    if name == "heisenberg":
        myflag = False
        print("You're goddamn right!")

        #// TASK 26 //
myflag=True
fpass=input("Please enter your password.")

while myflag:
     spass=input("Enter your password again")
     if fpass!= spass:
          print(">They are not same.")
     elif fpass == spass :
          myflag = False
          print(">Your password matches and account created successfully")

        #//TASk 27//

num=int(input("Please type a number."))
if num <0:
    print("Please type a positive number.")
else:
    while num>0:
        print(f"{num}")
        num -=1
print("Kaboom!!")

        #// TASK 28//

password="Mahmut123"
trial=3
while trial>0:
     pass1=(input("Please type your password."))
     if pass1==password:
        print("Welcome.")
     else:
          trial-=1
          if trial>0:
            print("Incorrect password , try again.")
          else:
            print("IncorrectPassword. Exterminate...")
