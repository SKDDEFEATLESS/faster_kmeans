from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import run_dataset_form
from .start_clustering import start_clustering
from django.http import HttpResponse

def run_dataset(request):
	if request.method =='POST':
		algorithm=request.POST.get('algorithm')
		form= run_dataset_form(request.POST)
		if form.is_valid():
			number_of_clusters=form.cleaned_data['number_of_clusters']
			kmeans_threshold=form.cleaned_data['kmeans_threshold']
			centroids_to_remember=form.cleaned_data['centroids_to_remember']
			print(algorithm)
			Time=start_clustering(number_of_clusters,kmeans_threshold,centroids_to_remember,algorithm)
			print(Time)
			if Time is None:
				messages.success(request, f' Time exceeded, please enter reasonable parameters!')
			else:
				messages.success(request, f' %s seconds' %Time)
	else:
		form= run_dataset_form()
	return render(request,'core/run_dataset.html',{'form':form})
