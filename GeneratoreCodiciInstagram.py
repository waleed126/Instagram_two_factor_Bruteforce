import itertools
import operator
import numpy as np #Numpy è una libreria python scientifica

#Verifico che nella parola non ho più di 3 ripetizioni della lettera consecutiva
def check_word(word):
	count=0
	for i in range(1,len(word)):
		if word[i-1]==word[i]:
			count+=1
	#a tornare è il numero di ripetizioni non di lettere ovvero 222 equivale a 2 ripetizioni
	return count

wordlist = '0123456789'
strprd=[]
CodiciPossibili=0
CodiciTotaliGen=0

firstprd = itertools.product(wordlist,repeat=2)
#Ottengo una tupla, la trasformo in un array di valori
for x in firstprd:
	word=''.join(x)
	strprd.append(word)

#Permuto i valori dell'array
secondperm = list(itertools.permutations(strprd,3))
#Trasformo la lista di tuple in array
strperm=np.asarray(secondperm)

#Scrittura su file
f3=open('listGenInstagram.txt','w')
for each in strperm:
	#ottengo la parola intera
	word = ''.join(each)
	print(word)
	CodiciTotaliGen+=1
	#conto il numero di lettere ripetute num.ripetizioni+lettere ripetute
	contatore=check_word(word)+1
	#scrivo solo le parole con massimo due lettere consecutive
	if contatore<3:
		CodiciPossibili+=1
		f3.write(word+'\n')
f3.write('CodiciScremati: '+str(CodiciPossibili)+' '+'CodiciTotaliGenerati: '+str(CodiciTotaliGen))
f3.close()