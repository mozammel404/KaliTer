#!/usr/bin/python

import click

kaliterLoc = "/data/data/com.termux/files/usr/etc/KaliTer"
warnTxt = "\n# edit this file at your own risk and end up messing with your termux. :)"

@click.command()
@click.option("--username","-u")
@click.option("--password","-p")
def command(password: str, username: str):
	file = open(f"{kaliterLoc}/credentials.txt", "w+")
	kaliterCredentials = file.readlines()
	if username:
		hasUsr = len(kaliterCredentials) != 0
		if hasUsr:
			prevPass = kaliterCredentials[1][-1]
			file.write(f"{username}\n{password if password else ''}\n")
		else:
			file.write(f"{username}\n{password if password else ''}\n")
			with open('/data/data/com.termux/files/usr/etc/bash.bashrc', "a+") as f:
				f.write('export PS1="\\[\\e[1;32m\\]╭──(\\[\\e[1;37m\\]\\u\\[\\e[1;34m\\]㉿\\[\\e[1;37m\\]kaliter\\[\\e[1;32m\\]) \\[\\e[1;34m\\][\\w] \\[\\e[1;31m\\]\\$(if [[ \\$? != 0 ]]; then echo \\"✘ \\"; fi)\\[\\e[0;32m\\]\\n┗━\\[\\e[0m\\]$ "\npython /data/data/com.termux/files/usr/KaliTer/login.py\nclear')
	file.write(f"{warnTxt}\n")
	file.close()
if __name__=='__main__':
	command()
