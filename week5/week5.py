#//TASK 40//

city=input("which city")
rep=int(input(">How many repetition for 'li' "))
word="li"
print(city + word *rep+"lerle")

        #//TASK 41//

fword=input("first word")
sword=input("second word")
fwordlen=len(fword)
swordlen=len(sword)
if fwordlen ==swordlen:
    print("The length is same.")

elif fwordlen>swordlen:
    print(f"{fword}")
else:
    print(f"{sword}")

    #//TASK 42//

word=input("Your input")
print(f"*{word}*")

    #//TASK 43//

word=input("your input")
mark=len(word)
print(word)
print("_"*mark)

    #//TASK 44//

word=input("your input")
maxlength=18
orta=maxlength-len(word)
solorta=orta//2
sağorta=orta-solorta
ortalama= ">"*solorta+word+"<"*sağorta
print("_"*18)
print(ortalama)
print("_"*18)

    #//TASK 45//
word=input("your word")
num1=int(input("enter a number"))
num2=int(input("enter  another number"))
print(word[num1:num2])

    #//TASK 46//


word=input("your word")
num1=int(input("enter a number"))
print(word[0:num1])

    #//TASK 47 //
word=input("your word")
num1=int(input("enter a number"))
print(word[num1:])

    #//TASK 48//

word=input("your word:")
let=input("which letter")

if let in word:
    print("found")
else:
    print("not found")


    #//TASK 49//

word=input("your word:")
let=input("which letter")

if let in word:
    print("found")
else:
    print("not found")