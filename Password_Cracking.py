from random import*
import as 
U_pwd= input(" Enter a password : ")
pwd=[ 'a', 'b',  'c',  'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
     'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '@', '0', '1',
     '2', '3','4', '5', '6', '7', '8', '9', '#' ]
pw=" "
while(pw !=u_pwd):
  pw =""
  for letter in range(len(u_pwd)):
    guess_pwd=pwd[randint(0,17)]
    pw=str(guess_pwd)+str(pw)
    print(pw)
    print(" Cracking Password .... Please wait")
    os.system("cls")
print(" Your Password is : ",pw)








