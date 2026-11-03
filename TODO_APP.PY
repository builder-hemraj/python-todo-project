#TODO_APP.PY

LEARNING = input("what did you learn today ? ")

try:

 with open("notes__.txt" , "a") as file:
    file.write(LEARNING + "\n")

except :
   print("couldn't do")
else:
   print("saved BOSS !")

reseen = input(" DO YOU WANNA SEE THE PREVIOUS NOTES  SAY Y/N ? ")

if reseen == "Y".casefold():
  with open("notes__.txt") as file:
    print(file.read())
elif reseen == "N".casefold():
  pass




