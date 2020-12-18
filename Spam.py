import amino
import getpass
import os
os.system("clear")
print("\033[1;36m Amino :  \033[1;34mSirLez \n \n \033[1;36minsta : \033[1;34m SirLe0x \n \n \n")
client=amino.Client()
ss=0
sz=25
nuum=0
tst=False
while tst==False:
	try:
		email=input("\033[1;31m\n# ur Email : ")
		password=getpass.getpass("# ur Password : ")
		client.login(email=email,password=password)
		tst=True
	except:
		tst=False
		print("\n# Verify ur account! \n")
		exx=input("# continue? (y/n) : ")
		if exx=='N' or exx=='n' or exx=='no':
				os._exit(1)


os.system("clear")
infoos=input("\033[1;32m# Community url : ")
infoo=client.get_from_code(infoos)
comId=infoo.path[1:infoo.path.index("/")]
subclient = amino.SubClient(comId=comId,profile=client.profile)
os.system("clear")

chat=input("\033[1;32m\n\n# Chat url : ")
chatId=subclient.get_from_code(chat).objectId
os.system("clear")
b=input("\033[1;93m# 1 - Spam messages\n# 2 - Normal Ghost messages\n# 3 - Spam Ghost messages\033[1;32m\n# which one ? : ")
os.system('clear')
if b =='1':
	msg=input("# Type a message : ")
	k = True
	while k is True:
		try:
			subclient.send_message(message=msg,chatId=chatId)
		except:
			pass
			
				
elif b =='2':
				k = True
				while k is True:
					os.system("clear")
					msg=input("# Type a message : ")
					try:
						subclient.send_message(message=msg,messageType=110,chatId=chatId)	
					except:
						pass
						
elif b =='3':
	msg=input("# Type a message : ")
	k = True
	while k is True:
		try:
			subclient.send_message(message=msg,messageType=110,chatId=chatId)	
		except:
			pass