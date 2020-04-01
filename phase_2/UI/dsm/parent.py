import os
import requests
import django
from UI.models import Post, Requirements

# x = Post.objects.all()
# mess =[]
# for y in x:
# 	mess.append(y.description)

def insert(originalfile,string):
    with open(originalfile,'r') as f:
        with open('newfile.txt','w') as f2: 
            f2.write(string)
            f2.write(f.read())
    #os.remove('go1.py')
    os.rename('newfile.txt',originalfile)
    f.close()
    f2.close()

def check(userinput):
	#file1 = open('userinput.temp','r')
	path = os.getcwd()
	path2 = os.getcwd()
	os.chdir(path+'/UI/dsm')
	cnt = 0
	while 1:
		messages = 'messages = ['
		print('run: ',cnt)
		with open('go.py') as f:
			with open('go1.py','w') as f1:
				for line0 in f:
					#line0 = line0.replace('\n','').replace('\r','')
					f1.write(line0)
		f.close()
		f1.close()
		line = userinput
		line = line.replace("\n", "")
		messages = messages + "\""+line+"\",\n"
		x = Post.objects.all()
		for y in x:
			line2 = y.description.replace("\n", "")
			messages = messages + "\""+line2+"\",\n"
		messages = messages + ']\n'

		insert('go1.py',messages)
		#os.system('python3 go1.py')

		from UI.dsm.go1 import go_function
		ltemp = go_function()


		messages = 'messages = ['
		print('run: ',cnt)
		with open('go.py') as f:
			with open('go2.py','w') as f1:
				for line0 in f:
					f1.write(line0)
		f.close()
		f1.close()
		line = userinput
		line = line.replace("\n", "")
		messages = messages + "\""+line+"\",\n"
		# for x in range(97,110):
		# 	info = Requirements(id_number=x-96,description=chr(x))
		# 	info.save()
		x = Requirements.objects.all()
		for y in x:
			line2 = y.description.replace("\n", "")
			messages = messages + "\""+line2+"\",\n"
		messages = messages + ']\n'

		insert('go2.py',messages)
		#os.system('python3 go1.py')

		from UI.dsm.go2 import go_function
		ltemp = ltemp +' '+go_function().replace('SIMILAR ISSUE FOUND','REQUIREMENT IDENTIFIED')

		cnt = cnt + 1
		if cnt == 1:
			break
	os.chdir(path2)

	message = userinput
	r = requests.post('http://localhost:5002/webhooks/rest/webhook', json={"message": message})
	print("After req")
	for i in r.json():
		bot_message = i['text']
	ltemp = ltemp +' '+bot_message
	print(ltemp)
	return ltemp

#check('The Browser is slow to respond')