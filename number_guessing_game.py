import random
random_number=random.randint(1,100)
count=0
while count < 9999:
    user_input=int(input("Enter your number: "))
    count=count+1
    if user_input==random_number:
        print(f"Congrats you won in {count} tries")
        break
    elif user_input <  random_number:
         print(f'Guess above {user_input}')
    elif user_input > random_number:
         print(f'Guess below {user_input}')
