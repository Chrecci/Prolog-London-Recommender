from django import forms
from django.forms.widgets import NumberInput

class RangeInput(NumberInput):
    input_type = 'range'

vibe_choices = [('chill', 'Chill'), ('active', 'Active'), ('good_food', 'Good Food'), ('energetic', 'Energetic')]
boolean_choices_work = [('yes', 'Yes :('), ('no', 'No :)')]
boolean_chocies = [('yes', 'Yes'), ('no', 'No')]
class VibeForm(forms.Form):
    vibe = forms.CharField(label='What is your vibe? ', widget=forms.Select(choices=vibe_choices))
    new_field =forms.CharField(label='Success')

class ChillForm(forms.Form):
    work = forms.CharField(label='Do you need to get work done? ', widget=forms.Select(choices=boolean_choices_work))

class WorkForm(forms.Form):
    env = forms.CharField(label='What work environment do you like today? ', widget=forms.Select(choices=[('library', 'Library'), ('cafe', 'Cafe')]))

class WalkForm(forms.Form):
    walk = forms.CharField(label='How do you feel about taking a walk? ', widget=forms.Select(choices=[('yes', 'love it!'), ('no', 'yuck!')]))
    mask = forms.CharField(label='Are you willing to wear mask? ', widget=forms.Select(choices=boolean_chocies))
    travel_time = forms.IntegerField(label='How long are you willing to travel? ', max_value=30, min_value=0)