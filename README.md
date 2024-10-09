# Password Cracker Script

This script attempts to crack a password entered by the user by generating random combinations of characters until the correct password is found.

## Description

The program simulates a brute force attack to guess a user's password. It works by randomly generating characters from a pre-defined list (`pwd`), which includes lowercase letters, numbers, and special characters (`@`, `#`). The guessed password is compared with the user-provided password until the correct match is found.

## How it works

1. The user inputs their password.
2. The script randomly selects characters from a predefined list (`pwd`).
3. The script compares the randomly generated password with the user’s password.
4. It repeats the guessing process until the generated password matches the user’s password.
5. Once the match is found, the correct password is printed.

## Code Snippet

```python
from random import randint

U_pwd = input("Enter a password: ")

pwd = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
    'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '@', '0', 
    '1', '2', '3', '4', '5', '6', '7', '8', '9', '#'
]

pw = " "
while pw != U_pwd:
    pw = ""
    for letter in range(len(U_pwd)):
        guess_pwd = pwd[randint(0, 17)]  # Randomly selects a character from 'pwd'
        pw = str(guess_pwd) + str(pw)
    print(pw)
    print("Cracking Password... Please wait")
    os.system("cls")

print("Your Password is: ", pw)
