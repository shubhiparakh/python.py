'''
num1 = int(input("enter first number"))
num2 = int(input("enter second number"))
print("sum of number is ", num1+ num2)

d1 = {}
print(type(d1))
d2= []
print(type(d2))
d3 = ()
print(type(d3))

mystring  = "i am like not bharat, i have heart and i love him "
print(len(mystring))
print(mystring[0:9])
print(mystring[0:6:3])
print(mystring[2:51:9])"
print(mystring[:])

mystring  = "bharat i have heart and i love him"
print(mystring)
print(mystring.isalpha())

mystring  = "i am like not bharat, i have heart and i love him "
print(mystring.endswith("love him "))
print(mystring.count("i"))
print(mystring.count(" "))
print(mystring.upper())


numbers = [90, 45, 23, 7, 2, 1]

print(numbers)
numbers[1] = 98
print(numbers)
print(numbers[1:9])

print(len(numbers))



tp = (1, )
print(tp)


dict = {"love": "bonding", "hate": "not liked by other person", "friendship":"best thing in world", "relationship":"timepass"}
print("enter any of the word u want to search")
print(dict[input()])

s = set()
#print(type(s))
#l = [1, 4, 5, 6]
#print(l)
s.add(1)
s.add(34)
s1 = s.intersection({34, 4, 5, 6})
print(s, s1 )
print(len(s))
print(max(s))


v1= 20
v2= 40
v3= int(input("enter the number"))
if v3>v2:
    print("greater")
elif v3==v2:
    print("equal")
else:
    print("lesser")

list = [1, 2, 3, 4, 6, 7]
print(5 not in list)
if 7 not in list:
    print("yes its not in the list")
else:
    print("statement is false")



age= int(input("enter your age"))
if age<1 and age>18:
    print("you cant drive!")
elif age==18:
    print("sorry, we cant decide, it depends on u")
elif age>18 and age<90:
    print("can drive")
else:
    print("enter a valid age")




list2 = [["bharat", 4], ["keshu", 2], ["abhi", 3], ["rahul", 1]]

for item, lollypop in list2:
    print("item", "lollypop")
    print(item, lollypop)



items = [1, 2, 3, 4, 5, 6, 7, "kites", "birds"]
for item in items:
    if str(item).isnumeric() and item>6:
        print(item)



while (True):
    num = int(input("enter the number"))
    if num>100:
        print("congrats u have entered a num greater than 100")
        break
    else:
       print("try again")
       continue




n=18
no_of_guesses = 1
print("you can guess 9 times")
while(no_of_guesses<=9):
    num=int(input("enter your guess"))
    if num>n:
        print("enter a lower number")
    elif num<n:
        print("enter a greater number")
    else:
        print("you won the game")
        print(no_of_guesses, "no of guesses you took to win")
    print("no of guesses left", 9-no_of_guesses)
    no_of_guesses +=1
if no_of_guesses>9:
    print("game over")

'''





'''
print("enter first number")
num1 = input()
print("enter other number")
num2= input()
try:
    print("the sum of these numbers is", int(num1)+int(num2))
except Exception as e:
    print(e)
print("this line is so important")


f = open("ekta.txt")
content = f.read()
print(content)
f.close()

f = open("ekta1.txt","a")
a= f.write("you are so sweet with beautiful hairs\n")
print(a)
f.close()
'''




i=1
n = int(input("enter number whose star pattern u want to print"))
b = bool(int(input("enter how you want to print? normal or reverse")))
if b ==1:
    print("normal star pattern")
    while i<n:
        print("*" * i, i)
        i +=1
elif b==0:
    print("reverse star pattern")
    while i<n:
        print("*" * (n-1), n)
        n=n-1
else:
    print("out of range")




































