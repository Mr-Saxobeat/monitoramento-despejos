from django import forms
from despejos.models import Despejo
from django.contrib.gis.geos import Point


class DespejoForm(forms.ModelForm):

    latitude = forms.DecimalField(
        min_value=-90,
        max_value=90,
        required=True,
    )
    longitude = forms.DecimalField(
        min_value=-180,
        max_value=180,
        required=True,
    )

    class Meta(object):
        model = Despejo
        exclude = []
        widgets = {'geom': forms.HiddenInput()}

    def clean(self):
        super().clean()
        if any(x for x in ['latitude', 'longitude'] if x in self.changed_data):
            latitude = float(self.cleaned_data['latitude'])
            longitude = float(self.cleaned_data['longitude'])
            self.cleaned_data['geom'] = Point(longitude, latitude)

    def __init__(self, *args, **kwargs):
        try:    
            coordinates = kwargs['instance'].geom.tuple    #If PointField exists 
            initial = kwargs.get('initial', {})    
            initial['longitude'] = coordinates[0]    #Set longitude from coordinates
            initial['latitude'] = coordinates[1]    #Set Latitude from coordinates
            kwargs['initial'] = initial
        except (KeyError, AttributeError):
            pass
        super().__init__(*args, **kwargs)