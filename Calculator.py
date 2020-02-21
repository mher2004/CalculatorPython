#Calculator in Python
from colorama import init
from colorama import Fore, Back, Style
init()

print(Back.RED)
print(Fore.BLACK)

func=input("Yntreq gortsoxutyun@ (+,-,*,/): ")

print(Back.YELLOW)
print(Fore.BLACK)

a=float(input("Greq araji tiv@: "))
b=float(input("Greq erkrord tiv@: "))

print(Back.GREEN)
print(Fore.BLACK)

if func == "+":
    answ=a+b
    print("Answer: "+str(answ))

elif func == "-":
    answ=a-b
    print("Answer: "+str(answ))

elif func == "*":
    answ=a*b
    print("Answer: "+str(answ))

elif func == "/":
    answ=a/b
    print("Answer: "+str(answ))

else:
    print("Fuck your life")

input()
