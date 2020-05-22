import os
from django.conf import settings
def datasetloader(dataset):
	if dataset=="covtype":
		data = []
		with open("covtype.data","r") as inputFile:
			for line in inputFile:
				data.append([float(x) for x in line.strip().split(",")])
		return data
	elif dataset=="birch":
		data = []
		file=os.path.join(settings.BASE_DIR, 'static', 'datasets','birch.txt')
		print(file)
		with open(file,"r") as inputFile:
			for line in inputFile:
				l=[]
				l.append(line[4])
				l.append(line[8].replace("\n",""))
				data.append([float(x) for x in l])
		return data