answer = input("Who was the first ever WWE Universal champion?: ")
if answer == "Finn Balor":
    print("You are right!")
else:
    print("You dead wrong!")

being_a_male = False
being_tall = True
if being_a_male and being_tall:
    print("You are a tall freakin' male.")
elif being_a_male and not being_tall:
    print("You're a short male.")
elif not being_a_male and being_tall:
    print("You're tall, but you're not masculine enough.")
else:
    print("You're not tall and masculine enough!")

def max(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
print(max(2, 3, 1))



