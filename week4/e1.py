login_attempts = [
("alice", "success"),
("bob", "failed"),
("bob", "failed"),
("charlie", "success"),
("bob", "failed"),
("alice", "failed")]

fails = {}

for username, status in login_attempts:
    if status == "failed":
        if username not in fails:
            fails[username] = 0
        fails[username]+= 1
        if fails[username] >= 3:
            print(f"{username} hat über 3 Fehlversuche!")