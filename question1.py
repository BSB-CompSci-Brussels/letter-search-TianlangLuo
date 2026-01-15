def countLetters(anyText:str,anyLetter:str)->int:
  counter = 0
  # Write code that counts the number of anyLetter in anyText
  
  for i in range(len(anyText)):
    if anyLetter == anyText[i]:
        counter = counter + 1

  return counter

text = input("Which word?")
letter = input("Which letter?")

print(countLetters(text,letter))
