password = input("Enter password: ")

common = ["password", "123456", "qwerty", "admin", "letmein", "password123", "iloveyou"]

if password.lower() in common:
    print("Very common password! Don't use this.")
    exit()

score = 0
tips = []

if len(password) >= 8:
    score += 1
else:
    tips.append("Use at least 8 characters")

if any(c.isupper() for c in password):
    score += 1
else:
    tips.append("Add an uppercase letter")

if any(c.islower() for c in password):
    score += 1
else:
    tips.append("Add a lowercase letter")

if any(c.isdigit() for c in password):
    score += 1
else:
    tips.append("Add a number")

if any(not c.isalnum() for c in password):
    score += 1
else:
    tips.append("Add a symbol like @ or #")

if score <= 2:
    print("Weak password")
elif score <= 4:
    print("Medium password")
else:
    print("Strong password")

for tip in tips:
    print("-", tip)