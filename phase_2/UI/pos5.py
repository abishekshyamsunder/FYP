import spacy
import os
import random
import subprocess
from spacy import displacy
from word2number import w2n
nlp = spacy.load("en_core_web_sm")
var = 0
variable = ''
parameter = True
summa_object = ''
equality_words = ['equals','equal to','equal','greater','lesser','atleast','atmost','upward','downward','above','below','upwards','downwards']

def rec_call1(temp,variable,verb,subject,object1):
	if(temp == verb):# or temp == subject or temp == object1):
		return variable
	variable.append(str(temp.text))
	for child in temp.children:
		print(temp,child,child.dep_)
		variable = rec_call1(child,variable,verb,subject,object1)
	return variable

def object_finder(child):
	if(str(child.dep_).find('obj') != -1 and str(child)!="defaultss"):
		return child
	else:
		for kozhandha in child.children:
			x = object_finder(kozhandha)
			if x != None:
				return x
	return None


def returns_testcase(req_string):
	strings = []
	strings.append(req_string)
	for string in strings:
		variable = ''
		parameter = True
		cardinality = 0
		flag = 0
		i = 0
		for x in string:
			i = i + 1
			if(x.isdigit() and i >= len(string)-3): # Assuming the last word is greater than 2 characters
				flag = 2
				for y in string[i:]:
					if y.isalpha():
						flag = 1
						break
			if flag == 2:
				string = string + ' defaultss'
				break
		flag = 0
		print("\n\n\n")
		print(string)
		doc = nlp(string)
		about_interest_doc = doc
		# print('started main:')
		# displacy.serve(about_interest_doc, style='dep')
		subject = ""
		object1 = ""
		verb = ""
		prn = ''
		negation = False
		for token in doc:
			varii = 0
			if str(token.pos_) == "VERB" or str(token.pos_) == "AUX":
				summa_object = object_finder(token)
				for child in token.children:
					if(str(child.dep_).find('sub') != -1):
						for x in child.children:
							if((x.dep_).find('poss')!=-1):
								prn = x
								print(str(prn))
						subject = child
						verb = token
						if varii == 1:
							break
						else:
							varii = 1
					if(str(child.dep_).find('obj') != -1):
						object1 = child
						if varii == 1:
							break
						else:
							varii = 1
					if(str(child.dep_).find('neg') != -1):
						negation = True
		if type(verb)==str:
			print('Can\'t find subject or object, sorry!')
			#exit()
		variable = []

		cardinal = ''
		for token in doc.ents:
			if str(token.label_)== "CARDINAL":
				cardinal = cardinal + str(token)

		for token in doc:
			temp = token
			for child in token.children:
				if str(child.dep_) == 'nummod':
					parameter = child
					temp = token
					var = 1
					if(type(object1)==str):
						object1 = subject
					variable = rec_call1(temp,variable,verb,subject,object1)
					break
		if len(cardinal)!=0:
			cardinality = 1
			parameter = cardinal

		print('\n')
		
		if(type(subject)==str):
			print('No subject')
		else:
			print('subject: ',str(prn) +' '+ subject.text)
		if(type(object1)==str or object1 == subject):
			print('No object')
		else:
			print('object: ',object1.text)
		object2 = ''
		if(summa_object != None):
			for x in summa_object.children:
				if(x.dep_=='compound'):
					object2 = object2 + str(x)
		print("Summa_object " + str(object2) + str(summa_object))
		print('verb: ',verb.text)
		constraint = ''
		if(type(parameter)==bool):
			print("This is not a requirement that test cases can be generated for")
			return("This is not a requirement that test cases can be generated for")
		if(cardinality==1):
			res = parameter.split()
			variable = [x for x in variable if x not in res]
		else:
			# if(type(parameter)==bool):
			# 	print("This is not a requirement that test cases can be generated for")
			# 	return("This is not a requirement that test cases can be generated for")
			variable.remove(parameter.text)

		for word in equality_words:
			if word in variable:
				constraint = word
				variable.remove(word)
				break

		for token in doc:
			if str(token.pos_) == "AUX":
				for child in token.children:
					if(str(child.dep_).find('acomp') != -1):
						constraint += str(child)

		if(negation == True):
			if(constraint=='greater'):
				constraint = 'lesser'
			elif(constraint=='lesser'):
				constraint = 'greater'
			elif(constraint=='equal to' or constraint==''):
				constraint = 'lesser'

		if(str(variable).find('defaultss')!=-1):
			variable.remove('defaultss')		
		variable2 = ''
		for token in doc:
			if token.text in variable:
				variable2 = variable2 + ' ' + token.text

		if(len(variable2)==0):
			variable2=str(prn) +' '+ subject.text
			if (object2!=None and summa_object!=None):
				variable2 = str(object2)+str(summa_object) + variable2
		print('variable:',variable2)
		#if(type(parameter)==str):
			#print("This is not a requirement that test cases can be generated for")
			#return("This is not a requirement that test cases can be generated for")
		print('parameter: ',parameter)
		if constraint=='':
			print('No constraint')
		else:
			print('constraint:',constraint)
		v = []
		c = []
		p = []
		p.append(w2n.word_to_num(str(parameter)))		
		if constraint=='':
			c.append("equal to")
		else:
			c.append(constraint)
		v.append(variable2)
		# output = subprocess.check_output("python p4.py {0} True".format(c+v+p), shell=True,encoding='utf-8')
		# output = output + "\n" + subprocess.check_output("python p4.py {0} False".format(c+v+p), shell=True,encoding='utf-8')
		print(c[0])
		#os.system("python3 p4.py {0} True".format(c+v+p))
		#finished = []
		for i in range(min(2,int(p[0]))):
			#print('inside')
			# if(c[0].find("equal")!=-1 or c[0].find("great")!=-1):
			# 	x = int(p[0])
			# 	p[0] = str((random.randint(x,100)))
			# 	os.system("python3 p4.py {0} True".format(c+v+p))
			# 	p[0] = x
			# 	p[0] = str((random.randint(0,x-1)))
			# 	print(p[0])
			# 	os.system("python3 p4.py {0} True".format(c+v+p))


			if(c[0].find("equal")!=-1 or c[0].find("less")!=-1 or c[0].find("greater")!=-1):
				c[0]="greater"
				x = int(p[0])
				print(x)
				p[0] = str((random.randint(0,x-1)))
				print(p[0])
				os.system("python3 UI/p4.py {0} temp.temp".format(c+v+p))
				p[0] = str((random.randint(x,100)))
				print(p[0])
				os.system("python3 UI/p4.py {0} temp1.temp".format(c+v+p))
				p[0] = x
				c[0] = "lesser"
		# for i in range(min(5,int(p[0]))):
		# 	if(c[0].find("equal")!=-1 or c[0].find("great")!=-1):
		# 		x = int(p[0])
		# 		p[0] = str((random.randint(x,100)))
		# 		os.system("python3 p4.py {0} False".format(c+v+p))
		# 		p[0] = x

		# 	if(c[0].find("equal")!=-1 or c[0].find("less")!=-1):
		# 		c[0]="greater"
		# 		x = int(p[0])
		# 		print(x)
		# 		p[0] = str((random.randint(0,x-1)))
		# 		print(p[0])
		# 		os.system("python3 p4.py {0} False".format(c+v+p))
		# 		p[0] = x
		# 		c[0] = "lesser"

		#os.system("python UI/p42.py {0} False".format(c+v+p))
		output = "<u><b>Test cases generated:</b></u> \n\n Check with: \n\n"

		f = open("temp.temp","r")
		while 1:
			line = f.readline()
			if not line:
				break
			output = output +'&nbsp &nbsp &nbsp'+"<i>"+line.replace('[','').replace(']','')+"</i>"+"\n"
		f.close()
		output = output + "<hr>"
		f = open("temp1.temp","r")
		while 1:
			line = f.readline()
			if not line:
				break
			output = output +'&nbsp &nbsp &nbsp'+"<i>"+line.replace('[','').replace(']','')+"</i>"+"\n"
		f.close()
		# os.system("rm temp.temp")
		# print(output)
	os.system("rm temp.temp")
	os.system("rm temp1.temp")

	print( output)
	return(output)

# def main():
# 	returns_testcase("the accuracy should be lesser than 30 percent")
# if __name__== "__main__":
#  	main()

#to who:
#what should happen:
#when: 