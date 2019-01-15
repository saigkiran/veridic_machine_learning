user=input("enter username: ")
pasw=input("enter password: ")
if (user[:3]!="VER") or (len(user)<8):
    print("Re-enter username starting with VER and with minimum of 8 characters")
else:
    print("username ok")

if any(c.isdigit() for c in pasw) and any(c.isupper() for c in pasw) and any(c.islower() for c in pasw):
    print("Password is OK")
else:
    print("Re-enter password")
