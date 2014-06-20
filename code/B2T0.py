#translates grade 1 braille, given file named "braille.txt'

dict = {'100000' : 'a', '110000': 'b', '100100' : 'c', '100110' : 'd', '100010' : 'e', '110100':'f', '110110' : 'g', '110010' : 'h', '010100' : 'i', '010110' : 'j', '101000': 'k', '111000' : 'l', '100101': 'm', '101110': 'n', '101010': 'o', '111100': 'p', '111110' : 'q', '111010': 'r', '011100' : 's', '011110': 't', '101001' : 'u', '111001': 'v', '010111' : 'w', '101101': 'x', '101111' : 'y', '101011' : 'z', '000000' : ' '}


def execute():
	translate(file2array())

def file2array():
	with open('braille2.txt', 'r') as f:
		brl_array = [word.strip() for word in f] #extracts strings from file
		brl_array = [word.strip() for word in str(brl_array[0]).split(' ')] #clears whitespace from string
	return brl_array

t=[]
def translate(brl_array):
	for key in brl_array:
		if dict.get(key) == None:
			t.append(dict.get(key, "*"))
		else:
			t.append(dict[key])
	print ''.join(t)


execute()
    



