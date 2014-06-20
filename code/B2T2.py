#translates grade 1 braille, given file named "braille.txt'
from collections import Counter as mset

import re

dict = {'100000' : 'a', '110000': 'b', '100100' : 'c', '100110' : 'd', '100010' : 'e', '110100':'f', '110110' : 'g', '110010' : 'h', '010100' : 'i', '010110' : 'j', '101000': 'k', '111000' : 'l', '100101': 'm', '101110': 'n', '101010': 'o', '111100': 'p', '111110' : 'q', '111010': 'r', '011100' : 's', '011110': 't', '101001' : 'u', '111001': 'v', '010111' : 'w', '101101': 'x', '101111' : 'y', '101011' : 'z', '000000' : ' '}

filename = 'braille3.txt'
filename0 = 'eng3.txt'

def execute():
	meaning(translate(file2array(filename)))

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



dictU={}
def translate(brl_array):
	t=[]
	count = 0
	for key in brl_array:
		if dict.get(key) == None:
			t.append(dict.get(key, str(count))) #Substitutes unknown pattern for integer to hold its place
			dictU[str(count)] = key #Appends substituted char and corresponding keyvalue, ex: '0':'010010' for future lookup
			count = count+1
		else:
			t.append(dict[key])
	return t
	

def meaning(t):	
	index_of_word = 0
	x = ''.join(t)
	x = [word.strip() for word in x.split(' ')] #a list of the partially translated words
	e = file2arrayE(filename0,'w') #a list of the english words
	#Note that the indexes of x and e show the relationship between the PT and eng words.
	counter=0
	for word in x:
		for m in re.finditer(r".\d\w?", word):
			if len(m.group()) == 3:
				p = (re.search('(?<=' + m.group()[0] + ')(\w*)' + m.group()[2], e[index_of_word])).group()
				dict[dictU[str(counter)]] = p[:-1]
			else:
				p = (re.search(m.group()[0] + '\w*', e[index_of_word])).group()
				dict[dictU[str(counter)]] = p[1:]
			counter = counter+1
		index_of_word = index_of_word +1
	print ''.join(translate(file2array(filename)))

	
execute()
    





