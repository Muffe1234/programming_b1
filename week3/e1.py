while True:
    userinput = input("put in your score")
    try:
        score = int(userinput)
        break
    except ValueError:
        print("keine Zahl")
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D" 
else:
    score = "F"
print(f"{grade}")
