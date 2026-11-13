def caesar(text, shift):
    result = ""
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result += chr((ord(ch) - base + shift) % 26 + base)
        else:
            result += ch
    return result

print("1. Encrypt")
print("2. Decrypt")
print("3. Brute force (key theriyaadhu)")
choice = input("Choose 1, 2 or 3: ")
text = input("Enter text: ")

if choice == "1":
    shift = int(input("Enter shift (1-25): "))
    print("Result:", caesar(text, shift))
elif choice == "2":
    shift = int(input("Enter shift (1-25): "))
    print("Result:", caesar(text, -shift))
elif choice == "3":
    for s in range(1, 26):
        print(f"Shift {s:2}: {caesar(text, -s)}")
else:
    print("Invalid choice")