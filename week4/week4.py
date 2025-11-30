 # // TASK 31//

list1=["domates","biber","patlıcan"]
print(list1)
print(list1[0])
print(">List length is 3")
list1.pop(1)
print(list1)

        # // TASK 32//
mylist=["domates","biber","patlıcan"]
print(f"{mylist}")
mylist[0]="karahindiba"
print(f"{mylist}")


        #// TASK 33//

skrt=[]
myflag=True

while myflag:
    listmat=input("Please enter an input")
    skrt.append(listmat)

    if listmat=="exit": 
        myflag=False
        print(f"{skrt}")

        #//TASK 34//

mylist=["Mahmut","Heisenberg","Agent47","Geodude","Kratos"]
for i in mylist:
    print(i)

    #//TASK 35//


metin=input("please enter an input.")
for i in metin:
    print(i)

    #//TASK 36//


rawpoints=[1,2,1,3]
totalpoints=0
for i in rawpoints:
    totalpoints+=i
 
 
print(f"Total {totalpoints} have been earned.")


        #//TASK 37//

rawpoints=[1, -2, 1, 3, -5, 7, 0]
totalpoints=0

for i in rawpoints:
    if i >0:
        totalpoints+=i

print(f"Total {totalpoints} have been earned.")

        #//TASK 38//

num=int(input(">please input table size"))
for satir in range(num):
    print("|_|" *num )
    #//task 39//

myflag=True
while myflag:
    sprhei=int(input("Spruce height"))
    if sprhei<0:
        print("Please enter a positive nnumber.")
    else:
        for i in range(sprhei):
            spaces=sprhei - i -1
            stars=2 * i + 1
            print(" "* spaces + "*" * stars )
            myflag=False

print(" " * (sprhei - 1) + "*")
