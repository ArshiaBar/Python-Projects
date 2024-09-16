ans = "Jim Duggan"
g = ""
gc = 0
gl = 3
oog = False
while g != ans and not oog:
   if gc < gl:
       g = input("Who won the first ever royal rumble?: ")
       gc += 1
   else:
        oog = True
if oog:
    print("Your defeat is my sweetest pleasure.")
else:
    print("winninggggggggggggg")

