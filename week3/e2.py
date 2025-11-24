pin = "8888"
maxtry = 3
i = 0
loginsuccess = False

while i < maxtry: 
    while True:
        userinput = input("deine pin")
        try:
         userpin = int(userinput)
         break
        except ValueError:
          print("gib zahl")
    if userpin == pin:
        print("pin korrekt")
        loginsuccess = True
        break
    else:
        i += 1
        print(f"pin nicht korrekt, noch {maxtry-i} versuche")
if not loginsuccess:
    print("acc locked")


