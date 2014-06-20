#translates grade 1 braille, given file named "braille.txt'
from collections import Counter as mset

dict = {'100000' : 'a', '110000': 'b', '100100' : 'c', '100110' : 'd', '100010' : 'e', '110100':'f', '110110' : 'g', '110010' : 'h', '010100' : 'i', '010110' : 'j', '101000': 'k', '111000' : 'l', '100101': 'm', '101110': 'n', '101010': 'o', '111100': 'p', '111110' : 'q', '111010': 'r', '011100' : 's', '011110': 't', '101001' : 'u', '111001': 'v', '010111' : 'w', '101101': 'x', '101111' : 'y', '101011' : 'z', '000000' : ' '}

filename = 'braille3.txt'
filename0 = 'eng3.txt'

def execute():
	translate(file2array(filename))

def file2array(filename):
	with open(filename, 'r') as f:
		array = [word.strip() for word in f] #extracts strings from file
		array = [word.strip() for word in str(array[0]).split(' ')] #clears whitespace from string
	return array

def file2arrayE(file_name,char_word):
	with open(file_name, 'r') as f:
		array = [word.strip() for word in f] #extracts strings from file
		if char_word == 'c': array = list(array[0]) #breaks words into characters for comparison
		elif char_word == 'w': array = [word.strip() for word in str(array[0]).split(' ')]
	return array


t=[]

def translate(brl_array):
	count = 0
	for key in brl_array:
		if dict.get(key) == None:
			#t.append(dict.get(key, "(" + str(count) + "*" + ")"))
			#count = count+1
			t.append("(" + key + ")")
		else:
			t.append(dict[key])
	x = ''.join(t)
	x = [word.strip() for word in x.split(' ')]
	w1 = match(file2arrayE(filename0,'w'),x)[0]
	w2 = match(x,file2arrayE(filename0,'w'))[0]
	print w1 + ' = ' + w2
	print ''.join(match(w1,w2)) + ' = ' + ''.join(match(w2,w1))

def match(a, b):
	return [aa for aa in a if aa not in b] 

execute()
    



