import os
from random import randint, seed,shuffle
import time
from timeit import default_timer
import argparse
import csv

parser = argparse.ArgumentParser(description='choose heuristic')

parser.add_argument('-S1', '--heur1', help='no_heur', action = "store_true")
parser.add_argument('-S2', '--heur2', help='heur1', action = "store_true")
parser.add_argument('-S3', '--heur3', help='heur3', action = "store_true")
parser.add_argument('-S4', '--heur4', help='heur3', action = "store_true")
parser.add_argument('-S5', '--heur5', help='heur4', action = "store_true")
parser.add_argument('-M1', '--method1', help='method1', action = "store_true")
parser.add_argument('-M2', '--method2', help='method2', action = "store_true")
parser.add_argument('-M3', '--method3', help='method3', action = "store_true")
parser.add_argument('data', type=str, help='data')
argc = parser.parse_args()

seed(1)

def no_heur(file):
	symbols = []
	with open(file, "r") as file:
		for line in file:
			words = line.split()
			if(words[0][1:-1] not in symbols):
				symbols.append(words[0][1:-1])
			if(words[2][1:-1] not in symbols):
				symbols.append(words[2][1:-1])
	return symbols

def heur1(file):
	tmp = {}
	symbols = []
	with open(file, "r") as file:
		for line in file:
			words = line.split()
			if(words[0][1:-1] not in symbols):
				tmp.update({words[0][1:-1]: 1})
				symbols.append(words[0][1:-1])
			else:
				tmp.update({words[0][1:-1]: tmp[words[0][1:-1]]+1})
			if(words[2][1:-1] not in symbols):
				tmp.update({words[2][1:-1]: 1})
				symbols.append(words[2][1:-1])
			else:
				tmp.update({words[2][1:-1]: tmp[words[2][1:-1]]+1})

	tmp = sorted(tmp.items(), key=lambda kv: kv[1])
	heur1 = []
	for x in tmp:
		heur1.append(x[0])

	return heur1

def heur2(file):
	return shuffle(no_heur(file))

def heur3(file):
	return heur1(file)[::-1]

def heur4(file):
	# adjust this function
	# 
	# 
	# 
	# 
	# 
	# 
	return heur1(file)[::-1]

inputOntology = argc.data
inputSubclassStatements = "./subClasses.nt"
forgetOntology = "./result.owl"
signature = "./signature.txt"
# 1 - ALCHTBoxForgetter
# 2 - SHQTBoxForgetter
# 3 - ALCOntologyForgetter
if(argc.method1):
	method = "1" #
elif(argc.method2):
	method = "2" #
else:
	method = "3"

os.system('java -jar kr_functions.jar ' + 'saveAllSubClasses' + " " + inputOntology)

if(argc.heur1):
	symbols = no_heur('subClasses.nt')
elif(argc.heur2):
	symbols = heur1('subClasses.nt')
elif(argc.heur3):
	symbols = heur2('subClasses.nt')
elif(argc.heur4):
	symbols = heur3('subClasses.nt')
else:
	symbols = heur4('subClasses.nt')

to_explain = []
with open('to_explain.txt', "r") as f:
	to_explain = f.read().splitlines() 

for x in to_explain:
	symbols.pop(symbols.index(x))

first = 0
n = 0

start = default_timer()

for t in symbols:
	with open("signature.txt", "w") as f:
		f.write(t)
	if(first == 0):
		os.system('java -cp lethe-standalone.jar uk.ac.man.cs.lethe.internal.application.ForgettingConsoleApplication --owlFile ' + inputOntology + ' --method ' + method  + ' --signature ' + signature)
		first+=1
	else:
		os.system('java -cp lethe-standalone.jar uk.ac.man.cs.lethe.internal.application.ForgettingConsoleApplication --owlFile ' + forgetOntology + ' --method ' + method  + ' --signature ' + signature)
	n+=1

os.system('java -jar kr_functions.jar ' + 'saveAllSubClasses' + " " + forgetOntology)
os.system('java -jar kr_functions.jar ' + 'saveAllExplanations' + " " + forgetOntology + " " + inputSubclassStatements)
runtime = default_timer() - start

with open(f'statistics.csv', mode='a', newline='') as statistics:
		statistics = csv.writer(statistics, delimiter=',')
		if(argc.heur1):
			heuristic = '0'
		elif(argc.heur2):
			heuristic = '1'
		elif(argc.heur3):
			heuristic = '2'
		elif(argc.heur4):
			heuristic = '3'
		else:
			heuristic = '4'

		if(argc.method1):
			type = 'ALCHTBoxForgetter'
		elif(argc.method2):
			type = 'SHQTBoxForgetter'
		elif(argc.method3):
			type = 'ALCOntologyForgetter'
		statistics.writerow([type, heuristic, argc.data, 'x', runtime])