from random import randint

def main(chance):
  
  random_number= randint(1,100)
  
  print("This is a number guessing game")
  while True:
    guessed_number=int(input("Enter your guess: "))
    if guessed_number==random_number:
      print(f"You got it in {chance} tries")
      break
    elif guessed_number > random_number:
      print("Too high")
      chance +=1
    elif guessed_number < random_number:
      print("Too low")
      chance +=1


main(chance=0)
