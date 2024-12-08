from textblob import TextBlob

word= input("Enter the word: ")

a= TextBlob(word)

corrected= str(a.correct())

print(f"corrected word is:  {corrected}")