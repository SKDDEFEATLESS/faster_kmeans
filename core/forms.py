from django import forms

class run_dataset_form(forms.Form):
    number_of_clusters = forms.CharField(label='Number of clusters', max_length=16)
    kmeans_threshold = forms.CharField(label='Kmeans Threshold', max_length=16)
    centroids_to_remember = forms.CharField(label='Centroids to remember', max_length=16)

    def __init__(self, *args, **kwargs):
        super(run_dataset_form, self).__init__(*args, **kwargs)
        self.fields['kmeans_threshold'].widget.attrs['placeholder'] = 'idk yet'
        self.fields['centroids_to_remember'].widget.attrs['placeholder'] = 'idl yet'
