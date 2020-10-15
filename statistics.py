import subprocess
import csv

types = ["-M1","-M2","-M3"]
heurs = ["-S2","-S3","-S4","-S5"]
to_reads = [
['http://bioportal.bioontology.org/ontologies/FISHO#FISHO_0000125\nhttp://bioportal.bioontology.org/ontologies/FISHO#FISHO_0000253','./FishOntology.owl'],
['http://bioportal.bioontology.org/ontologies/FISHO#FISHO_0000446\nhttp://bioportal.bioontology.org/ontologies/FISHO#FISHO_0000127','./FishOntology.owl'],
['http://bioportal.bioontology.org/ontologies/FISHO#FISHO_0000443\nhttp://bioportal.bioontology.org/ontologies/FISHO#FISHO_0000346','./FishOntology.owl'],
['http://bioportal.bioontology.org/ontologies/FISHO#FISHO_0000447\nhttp://bioportal.bioontology.org/ontologies/FISHO#FISHO_0000328','./FishOntology.owl'],
['http://purl.obolibrary.org/obo/ERO_0000490\nhttp://purl.obolibrary.org/obo/ERO_0001707','./ero.owl'],
['http://purl.obolibrary.org/obo/OBI_0000341\nhttp://purl.obolibrary.org/obo/OBI_0000073','./ero.owl'],
['http://purl.obolibrary.org/obo/ERO_0001762\nhttp://purl.obolibrary.org/obo/ERO_0001523','./ero.owl']
]

with open(f'statistics.csv', mode='w', newline='') as statistics:
		 	statistics = csv.writer(statistics, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		 	statistics.writerow(['type', 'heuristic', 'data', 'axioms', 'runtime'])

for r in to_reads:
	with open('to_explain.txt', mode='w') as to_read:
		to_read.write(r[0])
	for t in types:
		for h in heurs:
			c= subprocess.call(["python3", "myProgram.py", h, t, r[1]])