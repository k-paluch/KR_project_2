import os
from random import randint, seed
seed(1)
# This is an example puython programme which shows how to use the different stand-alone versions of OWL reasoners and forgetting programme

# Choose the ontology (in the OWL format) for which you want to explain the entailed subsumption relations.
inputOntology = "./mamo-xml.owl"

# Choose the set of subclass for which you want to find an explanation.
# this file can be generated using the second command (saveAllSubClasses)
inputSubclassStatements = "./subClasses.nt"

# Choose the ontology to which you want to apply forgetting. This can be the inputOntology, but in practise
# should be a smaller ontology, e.g. created as a justification for a subsumption
forgetOntology = "./result.owl"

# Decide on a method for the forgetter (check the papers of LETHE to understand the different options).
# The default is 1, I believe.
# 1 - ALCHTBoxForgetter
# 2 - SHQTBoxForgetter
# 3 - ALCOntologyForgetter
method = "2" #

# Choose the symbols which you want to forget.
signature = "./signature.txt"

# 1. PRINT ALL SUBCLASSES (inputOntology):
# print all subClass statements (explicit and inferred) in the inputOntology
# --> uncomment the following line to run this function
#os.system('java -jar kr_functions.jar ' + 'printAllSubClasses' + " " + inputOntology)

# 2. SAVE ALL SUBCLASSES (inputOntology):
# save all subClass statements (explicit and inferred) in the inputOntology to file datasets/subClasses.nt
# --> uncomment the following line to run this function
os.system('java -jar kr_functions.jar ' + 'saveAllSubClasses' + " " + inputOntology)

# 3. PRINT ALL EXPLANATIONS (inputOntology, inputSubclassStatements):
# print explanations for each subClass statement in the inputSubclassStatements
# --> uncomment the following line to run this function
#os.system('java -jar kr_functions.jar ' + 'printAllExplanations' + " " + inputOntology + " " + inputSubclassStatements)

# 4. SAVE ALL EXPLANATIONS (inputOntology, inputSubclassStatements):
# save explanations for each subClass statement in the inputSubclassStatements to file datasets/exp-#.owl
# --> uncomment the following line to run this function
# os.system('java -jar kr_functions.jar ' + 'saveAllExplanations' + " " + inputOntology + " " + inputSubclassStatements)

# For running LETHE forget command:
# --> uncomment the following line to run this function
# os.system('java -cp lethe-standalone.jar uk.ac.man.cs.lethe.internal.application.ForgettingConsoleApplication --owlFile ' + inputOntology + ' --method ' + method  + ' --signature ' + signature)

elements = []
with open("subClasses.nt", "r") as file:
	for line in file:
		words = line.split()
		if(words[0][1:-1] not in elements):
			elements.append(words[0][1:-1])
		if(words[2][1:-1] not in elements):
			elements.append(words[2][1:-1])

print(len(elements))

to_forget = []

for x in range(90):
	tmp = randint(0,len(elements)-1)
	to_forget.append(elements[tmp])
	elements.pop(tmp)

first = 0

for t in to_forget:
	with open("signature.txt", "w") as f:
		f.write(t)
	if(first == 0):
		os.system('java -cp lethe-standalone.jar uk.ac.man.cs.lethe.internal.application.ForgettingConsoleApplication --owlFile ' + inputOntology + ' --method ' + method  + ' --signature ' + signature)
		first+=1
	else:
		os.system('java -cp lethe-standalone.jar uk.ac.man.cs.lethe.internal.application.ForgettingConsoleApplication --owlFile ' + forgetOntology + ' --method ' + method  + ' --signature ' + signature)


# os.system('java -jar kr_functions.jar ' + 'saveAllSubClasses' + " " + forgetOntology)
os.system('java -jar kr_functions.jar ' + 'saveAllExplanations' + " " + forgetOntology + " " + inputSubclassStatements)


print(elements)