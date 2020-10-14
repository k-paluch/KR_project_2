import argparse
import csv

parser = argparse.ArgumentParser(description='choose heuristic')


parser.add_argument('data', type=str, help='data')
argc = parser.parse_args()
ax = []
tmp = 0
with open('axioms.csv', mode='w', newline='') as axioms:
		axioms = csv.writer(axioms, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		with open(argc.data, "r") as file:
			for line in file:
				words = line.split()
				if(len(words)>3):
					if(words[3] == 'Axioms:' and words[0] == 'Result'):
						tmp += int(words[4])
				if(words==['Starting', 'Program...'] and tmp!=0):
					ax.append(tmp)
					tmp =0
		for x in ax:
			axioms.writerow([x])