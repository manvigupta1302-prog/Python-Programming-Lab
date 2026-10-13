import random

digits = int(input("Enter number of digits for OTP (4 or 6): "))

if digits == 4 or digits == 6:
    otp = ""
    for i in range(digits):
        otp = otp + str(random.randint(0, 9))
    print("Your OTP is:", otp)
else:
    print("Invalid choice. Please enter 4 or 6.")