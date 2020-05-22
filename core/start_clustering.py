from .kmeans import *
from .faster_kmeans import *
from .enhanced_kmeans import *
from .faster_enhanced_kmeans import *
from .triangle_inequality import *
from .faster_triangle_inequality import *
from .datasetloader import datasetloader

def start_clustering(numClusters,kmeans_threshold,centroids_to_remember,algorithm,is_random,number_of_points,dim):
	numClusters=int(numClusters)
	if is_random==False:
		pointList=datasetloader("birch")
		print("here")
	else:
		number_of_points=int(number_of_points)
		dim=int(number_of_points)
		pointList=get_random_points(number_of_points,numClusters,dim)
	# numClusters=10 #take input
	kmeans_threshold=int(kmeans_threshold)
	centroids_to_remember=int(centroids_to_remember)
	# Time=[]

	# net_start=time.time()
	if algorithm=="kmeans":
		start = time.time()
		config1= Kmeans(numClusters,pointList,kmeans_threshold)
		return("Time taken for Kmeans: "+str(time.time() - start))

	elif algorithm=="faster_kmeans":
		start = time.time()
		config2= Faster_Kmeans(numClusters,pointList,kmeans_threshold,centroids_to_remember)
		return("Time taken for Faster Kmeans: "+str(time.time() - start))

	elif algorithm=="enhanced_kmeans":
		start = time.time()
		config3= Enhanced_Kmeans(numClusters,pointList,kmeans_threshold)
		return("Time taken for Enhanced Kmeans: "+str(time.time() - start))

	elif algorithm=="faster_enhanced_kmeans":
		start = time.time()
		config4= Faster_Enhanced_Kmeans(numClusters,pointList,kmeans_threshold,centroids_to_remember)
		return("Time taken for Faster Enhanced Kmeans: "+str(time.time() - start))

	
	elif algorithm=="triangle_inequality":
		start = time.time()
		config5= Triangle_Inequality(numClusters,pointList,kmeans_threshold)
		Time="Time taken for Triangle Inequality: "+str(time.time() - start)
		cList=[]
		for centroid in config5.centroidList:
			point = centroid.centerPos[0]
			cList.append(point)
		start = time.time()
		config6= Triangle_Inequality(numClusters,pointList,kmeans_threshold,cList)
		Time+=" seconds, Time taken for Triangle Inequality with initial centorids: "+str(time.time() - start)
		return Time

	elif algorithm=="faster_triangle_inequality":
		start = time.time()
		config7= Faster_Triangle_Inequality(numClusters,pointList,kmeans_threshold,centroids_to_remember)
		Time="Time taken for Faster Triangle Inequality: "+str(time.time() - start)
		cList=[]
		for centroid in config7.centroidList:
			point = centroid.centerPos[0]
			cList.append(point)
		start = time.time()
		config8= Faster_Triangle_Inequality(numClusters,pointList,kmeans_threshold,centroids_to_remember,cList)
		Time+=" seconds, Time taken for Faster Triangle Inequality with initial centorids: "+str(time.time() - start)
		return Time

def get_random_points(number_of_points,numClusters,dim):
	pointList = []
	x = []
	y = []
	c = []
	k = 0
	for i in range(0,numClusters):
		num = int(number_of_points/numClusters)
		p = makeRandomPoint(dim,num,k)
		k += 0
		pointList += p.tolist()
	return pointList

def makeRandomPoint(n, lower, upper):
	return numpy.random.normal(loc=upper, size=[lower, n])