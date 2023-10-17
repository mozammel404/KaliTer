import colorama
Colors = colorama.Fore
from getpass import getpass
import os

kaliterLoc = "/data/data/com.termux/files/usr/etc/KaliTer"

file = open(f"{kaliterLoc}/credentials.txt", "r")
credentials = file.readlines()
usrname = str(credentials[0])[:-1]
passwrd = str(credentials[1])[:-1]

os.system("clear")
while True:
        try:
                print(Colors.BLUE+ "user: "+Colors.GREEN+usrname+Colors.WHITE)
                input_pass = getpass(Colors.BLUE+"password: "+Colors.WHITE)
                if input_pass == passwrd:
                        print(Colors.GREEN+ "[+] Login Successful!"+Colors.WHITE)
                        break
                else:
                        print("Sorry, try again.")
        except KeyboardInterrupt as e:
                print("\nEnter the password to log in")

        except Exception as e:
                print(Colors.RED+f"\n{e} occured while logging in."+ Colors.WHITE)

file.close()
