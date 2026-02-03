passwords = [ "Pass123",
"SecurePassword1", "weak",
"MyP@ssw0rd", "NOLOWER123"]

for password in passwords:
    score = 0      # Großbuchstaben
    score1 = 0     # Kleinbuchstaben
    score2 = 0     # Zahlen
    zeichen = 0    # Länge >= 8
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
    
