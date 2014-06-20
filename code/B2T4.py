#translates grade 1 braille, given file named "braille.txt'
from collections import Counter as mset

import re

#dictionary of known Grade 1 patterns
dict = {'100000' : 'a', '110000': 'b', '100100' : 'c', '100110' : 'd', '100010' : 'e', '110100':'f', '110110' : 'g', '110010' : 'h', '010100' : 'i', '010110' : 'j', '101000': 'k', '111000' : 'l', '100101': 'm', '101110': 'n', '101010': 'o', '111100': 'p', '111110' : 'q', '111010': 'r', '011100' : 's', '011110': 't', '101001' : 'u', '111001': 'v', '010111' : 'w', '101101': 'x', '101111' : 'y', '101011' : 'z', '000000' : ' '}

trial = '5'

filename = 'braille' + trial + '.txt' #filename of G2 Braille
filename0 = 'eng' + trial + '.txt' #filename of equivalent English

def execute():
	meaning(translate(file2array(filename))) #Finds meaning of braille2

def file2array(filename):
	with open(filename, 'r') as f:
		array = [word.strip() for word in f] #extracts strings from file
		array = [word.strip() for word in str(array[0]).split(' ')] 
	return array

def file2arrayE(file_name,char_word):
	with open(file_name, 'r') as f:
		array = [word.strip() for word in f] #extracts strings from file
		if char_word == 'c': array = list(array[0]) #breaks words into characters for comparison
		elif char_word == 'w': array = [word.strip() for word in str(array[0]).split(' ')] #breaks string into words clears whitespace from strings
	return array



dictU={}
U={}
def translate(brl_array):
	t=[]
	count = 0
	for key in brl_array:
		if dict.get(key) == None and U.get(key) == None:
			t.append(dict.get(key, str(count))) #Substitutes unknown pattern for integer to hold its place
			dictU[str(count)] = key #Appends substituted char and corresponding keyvalue, ex: '0':'010010' for future lookup
			U[key] = str(count) #Appends substituted char and corresponding keyvalue, ex: '010010':'0' for future lookup, and to negate marking a symbol as unknown twice
			count = count+1
		elif U.get(key) != None:
			t.append(dict.get(key, U[key])) #Substitutes unknown pattern for integer to hold its place
		else:
			t.append(dict[key])
	return t
	

def meaning(t):	
	index_of_word = 0
	x = ''.join(t)
	x = [word.strip() for word in x.split(' ')] #a list of the partially translated words
	e = file2arrayE(filename0,'w') #a list of the english words
	#Note that the indexes of x and e show the relationship between the PT and eng words.
	print x #partially translated text
	counter=0 #Used to determine which cell is being evaluated within word, if word contains multiple unknown cells
	for word in x:
		for m in re.finditer("\w*?(?=\d)\w*?", word):
			p = (re.search('(?<=' + m.group() + ')\w*', e[index_of_word])).group()
			print m.group()
		
			counter = counter+1
			index_of_word = index_of_word +1
	print ''.join(translate(file2array(filename))) 

#print final translation, using inferred cells
			
"""
			if re.search('[a-zA-Z]\d[a-zA-z]', m.group()) != None:
				p = (re.search(m.group()[0] + '(\w*)' + m.group()[2], e[index_of_word])).group()
				dict[dictU[str(counter)]] = p[:-1]

			elif re.search('\b\d', m.group()) != None:
				x = re.search('\w(?=\d)', m.group())
				print x.group()
				#p = (re.search('\w(?=\d)', e[index_of_word])).group()
				#dict[dictU[str(counter)]] = p
				#FIXME: find way to limit string in cases
			elif re.search('\d[a-zA-Z]', m.group()) != None:
				p = (re.search('\w*' + m.group()[1], e[index_of_word])).group()
				dict[dictU[str(counter)]] = p[:-1]
				
			else: 
				p = (re.search('\w*', e[index_of_word])).group()
				dict[dictU[str(counter)]] = p
				x = re.search('\w(?=\d)', m.group())
				print x.group()
"""
		
	
execute()
    





