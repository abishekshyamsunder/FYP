import os
import time
import operator
def check(userinput):
	path = os.getcwd()
	path2 = os.getcwd()
	os.chdir(path+'/UI/dsm')
	f1 = open('datastore.txt','r')
	f3 = open('validation.txt0','w')
	if os.path.exists('eval_output.txt'):
		os.remove('eval_output.txt')
	while(True):
		line = f1.readline()
		if not line:
			break
		outputline = "0\t"+userinput+"\t"+line
		f3.write(outputline)
	f3.close()
	print('Shifting Control to eval.py')
	f1.close()
	os.system('python eval.py --model model.ckpt-861000')
	print('Shifting Control back to parent.py')
	while not os.path.exists('eval_output.txt'):
	    time.sleep(1)
	if os.path.isfile('eval_output.txt'):
		#print('works')
		d = {}
		with open("eval_output.txt") as f:
		    for line in f:
		       (key, val) = line.split()
		       d[int(key)] = float(val)
		sorted_d = sorted(d.items(), key=operator.itemgetter(1))
		#print(sorted_d)
		value = sorted_d[0][0]
		f1 = f1 = open('datastore.txt','r')
		i = 1
		while(True):
			line = f1.readline()
			if not line:
				break
			if(i == int(value)):
				print(line)
				f1.close()
				os.chdir(path2)
				return('|<---->|SIMILAR ISSUE FOUND: '+line)
			i = i + 1
		os.chdir(path2)
		return('nothing matched')
		

		

