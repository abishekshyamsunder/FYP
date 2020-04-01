import spacy
from spacy import displacy
nlp = spacy.load("en_core_web_sm")
var = 0
variable = ''
parameter = ''
equality_words = ['equals','greater','lesser','atleast','atmost','upward','downward','above','below','upwards','downwards']
def rec_call1(temp,variable,verb,subject,object1):
	if(temp == verb):# or temp == subject or temp == object1):
		return variable
	variable.append(str(temp.text))
	for child in temp.children:
		print(temp,child,child.dep_)
		variable = rec_call1(child,variable,verb,subject,object1)
	return variable

def main():
	doc = nlp("the value of y should be greater than 5 and the value of x should be lesser than y")
	#doc = nlp("the application must redirect to website after 10 seconds")
	#doc = nlp("the classifier must give an accuracy upward of 80 percent.")
	#doc = nlp("The interface must have 5 fields to be filled correctly")
	#doc = nlp("The browser should open within 5 seconds of clicking ")
	#doc = nlp("The CPU must clock atleast 10 cycles per minute")
	#doc = nlp("The function should not be called if one parameter is missing")
	#doc = nlp("The diplay should become 42 nits at sundown")
	##doc = nlp("battery saver should be switched on if battery falls below 5%")
	#doc = nlp('The name can\'t exceed 5 characters')
	about_interest_doc = doc
	#print('started main:')

	subject = ""
	object1 = ""
	verb = ""

	for token in doc:
		varii = 0
		if str(token.pos_) == "VERB" or str(token.pos_) == "AUX":
			for child in token.children:
				if(str(child.dep_).find('sub') != -1):
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
	if type(verb)==str:
		print('Can\'t find subject or object, sorry!')
		exit()
	variable = []
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

	print('\n\n\n\n\n')
	if(type(subject)==str):
		print('No subject')
	else:
		print('subject: ',subject.text)
	if(type(object1)==str or object1 == subject):
		print('No object')
	else:
		print('object: ',object1.text)
	print('verb: ',verb.text)

	constraint = ''
	variable.remove(parameter.text)
	for word in equality_words:
		if word in variable:
			constraint = word
			variable.remove(word)
			break

	variable2 = ''
	for token in doc:
		if token.text in variable:
			variable2 = variable2 + ' ' + token.text

	print('variable: ',variable2)
	#print('parameter: ',parameter.text)
	if constraint=='':
		print('No constraint')
	else:
		print('constraint: ',constraint)

	displacy.serve(about_interest_doc, style='dep')

if __name__== "__main__":
	main()

#to who:
#what should happen:
#when: 