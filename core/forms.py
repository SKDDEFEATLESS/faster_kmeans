from django import forms

class run_dataset_form(forms.Form):
    number_of_clusters = forms.CharField(label='Number of clusters', max_length=16)
    kmeans_threshold = forms.CharField(label='Kmeans Threshold', max_length=16)
    centroids_to_remember = forms.CharField(label='Centroids to remember', max_length=16)

    def __init__(self, *args, **kwargs):
        super(run_dataset_form, self).__init__(*args, **kwargs)
        self.fields['kmeans_threshold'].widget.attrs['placeholder'] = 'idk yet'
        self.fields['centroids_to_remember'].widget.attrs['placeholder'] = 'idl yet'

class run_random_form(forms.Form):
    number_of_points = forms.CharField(label='Number of points', max_length=16)
    dimension = forms.CharField(label='Number of dimensions', max_length=16)
    number_of_clusters = forms.CharField(label='Number of clusters', max_length=16)
    kmeans_threshold = forms.CharField(label='Kmeans Threshold', max_length=16)
    centroids_to_remember = forms.CharField(label='Centroids to remember', max_length=16)

    def __init__(self, *args, **kwargs):
        super(run_random_form, self).__init__(*args, **kwargs)
        self.fields['kmeans_threshold'].widget.attrs['placeholder'] = 'idk yet'
        self.fields['centroids_to_remember'].widget.attrs['placeholder'] = 'idl yet'
        self.fields['dimension'].widget.attrs['placeholder'] = '10'