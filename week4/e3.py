passwords = [ "Pass123",
"SecurePassword1", "weak",
"MyP@ssw0rd", "NOLOWER123"]

score = 0
score1 = 0
score2 = 0
zeichen = 0

for password in passwords:
    for char in password:
        if char.isupper():
            score = 1
        elif char.islower():
            score1 = 1
        elif char.isdigit():
            score2 = 1
    if len(password) >= 8:
        zeichen = 1
    print(f"Password {password} ist level: {score + score1 + score2 +zeichen}/4")
    
