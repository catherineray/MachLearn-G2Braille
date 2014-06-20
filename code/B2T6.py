#translates grade 1 braille, given file named "braille.txt'
from collections import Counter as mset

import re

all_powerful_counter = 1
#dictionary of known Grade 1 patterns
dict = {'100000' : 'a', '110000': 'b', '100100' : 'c', '100110' : 'd', '100010' : 'e', '110100':'f', '110110' : 'g', '110010' : 'h', '010100' : 'i', '010110' : 'j', '101000': 'k', '111000' : 'l', '100101': 'm', '101110': 'n', '101010': 'o', '111100': 'p', '111110' : 'q', '111010': 'r', '011100' : 's', '011110': 't', '101001' : 'u', '111001': 'v', '010111' : 'w', '101101': 'x', '101111' : 'y', '101011' : 'z', '000000' : ' '}

filename = 'braille5.txt' #filename of G2 Braille
filename0 = 'eng5.txt' #filename of equivalent English

def execute():
	testing(matching(translate(file2array(filename)))) #Finds meaning of braille2

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
def translate(brl_array, count=0):
	t=[]
	duplicates = []
	count = count
	for key in brl_array:
		if dict.get(key) == None and duplicates.count(key) == 0:
			duplicates.append(key)
			t.append(dict.get(key, str(count))) #Substitutes unknown pattern for integer to hold its place
			dictU[str(count)] = key #Appends substituted char and corresponding keyvalue, ex: '0':'010010' for future lookup
			
			count = count+1
		elif dict.get(key) == None and duplicates.count(key) != 0:
			t.append(dict.get(key, str(duplicates.index(key))))
		else:
			t.append(dict[key])
	x = ''.join(t)
	x = [word.strip() for word in x.split(' ')] #a list of the partially translated words
	#Note that the indexes of x and e show the relationship between the PT and eng words.
	return x #partially translated text
	
e = file2arrayE(filename0,'w') #a list of the english words

def testing(new):
	#print new
	new_translation = [word.strip() for word in new.split(' ')] 
	print matching(new_translation)


def matching(partially_translated_text):
	duplicates1 = []; index_of_word = 0
	z = partially_translated_text
	counter = 0 #Used to determine which cell is being evaluated within word, if word contains multiple unknown cells
	for word in z:
		for m in re.finditer("[a-zA-Z\s]*?\d\w*", word):
			if re.search('[a-z]*', m.group()) != None:
				unknown = (re.search('\d+', m.group())).group() #find unknowns in word
				for n in re.finditer('\d{1}', m.group()):
					if len(unknown) != 1: break
					else: 	
						#\w*?(?=\d) ==> abc1nn ===> abc
						tag = (re.search('\w*(?=\d)', m.group())).group() #find unknowns in word
						h = e[index_of_word].replace(tag, '') #look at corresponding english word, remove tagged char from word
						l = m.group().replace(tag, '')
						if re.search('[a-z]+', l) != None: #If there are translated letters after the unknown, clear the translated letters.
							next=(re.search('[a-z]+', l)).group()
							print l.replace(next, '')
							dict[dictU[n.group()]] = h.replace(next, '')
						else: dict[dictU[n.group()]] = h #set unknown equal to english match

									
			counter = counter+1
		index_of_word = index_of_word +1
	version = all_powerful_counter + 1
	return ' '.join(translate(file2array(filename),version))



	
execute()
    





