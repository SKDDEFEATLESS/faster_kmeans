from .kmeans import *
from .faster_kmeans import *
from .enhanced_kmeans import *
from .faster_enhanced_kmeans import *
from .triangle_inequality import *
from .faster_triangle_inequality import *
from .datasetloader import datasetloader

def start_clustering(numClusters,kmeans_threshold,centroids_to_remember):
	pointList=datasetloader("birch")
	print("here")
	# numClusters=10 #take input
	numClusters=int(numClusters)
	kmeans_threshold=int(kmeans_threshold)
	centroids_to_remember=int(centroids_to_remember)
	Time=[]

	net_start=time.time()

	start = time.time()
	config1= Kmeans(numClusters,pointList,kmeans_threshold)
	Time.append("Kmeans Time taken:"+str(time.time() - start))

	start = time.time()
	config2= Faster_Kmeans(numClusters,pointList,kmeans_threshold,centroids_to_remember)
	Time.append("Faster Kmeans Time taken:"+str(time.time() - start))

	start = time.time()
	config3= Enhanced_Kmeans(numClusters,pointList,kmeans_threshold)
	Time.append("Enhanced Kmeans Time taken:"+str(time.time() - start))

	start = time.time()
	config4= Faster_Enhanced_Kmeans(numClusters,pointList,kmeans_threshold,centroids_to_remember)
	Time.append("Faster Enhanced Kmeans Time taken:"+str(time.time() - start))

	start = time.time()
	config5= Triangle_Inequality(numClusters,pointList,kmeans_threshold)
	Time.append("Triangle_Inequality Time taken:"+str(time.time() - start))
	cList=[]
	for centroid in config5.centroidList:
		point = centroid.centerPos[0]
		cList.append(point)
	start = time.time()
	config6= Triangle_Inequality(numClusters,pointList,kmeans_threshold,cList)
	Time.append("Triangle_Inequality Part 2 Time taken:"+str(time.time() - start))

	start = time.time()
	config7= Faster_Triangle_Inequality(numClusters,pointList,kmeans_threshold,centroids_to_remember)
	Time.append("Faster_Triangle_Inequality Time taken:"+str(time.time() - start))
	cList=[]
	for centroid in config5.centroidList:
		point = centroid.centerPos[0]
		cList.append(point)
	start = time.time()
	config8= Faster_Triangle_Inequality(numClusters,pointList,kmeans_threshold,centroids_to_remember,cList)
	Time.append("Faster_Triangle_Inequality Part 2 Time taken:"+str(time.time() - start))
	return Time




	# print(time1)
	# print(time2)
	# print(time3)
	# print(time4)
	# print(time5)
	# print(time6)
	# print(time7)
	# print(time8)
