import string
import random

letter= string.printable
password= []

print("This is password generator")

password_lenght= int(input("Enter How many digits of password do you want: "))
for _ in range(password_lenght-1):
 random_letter= random.choice(letter)
 password.append(random_letter)

passw= ''.join(password)
print(f"Your password is {passw}")