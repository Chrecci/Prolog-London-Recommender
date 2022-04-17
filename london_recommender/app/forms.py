from django import forms
from django.forms.widgets import NumberInput

class RangeInput(NumberInput):
    input_type = 'range'

# choices for dropdown menus
vibe_choices = [('chill', 'Chill'), ('active', 'Active'), ('food', 'Good Food'), ('energetic', 'Energetic')]
boolean_choices_work = [('yes', 'Yes :('), ('no', 'No :)')]
boolean_choices = [('yes', 'Yes'), ('no', 'No')]
meal_choices = [('breakfast', 'Breakfast'), ('lunch', 'Lunch'), ('dinner', 'Dinner'), ('snack', 'Snack')]
energy_choices = [('dance', "Let's Dance"), ('alcohol', 'Some Alcohol'), ('laughs', 'Good Laughs')]

class VibeForm(forms.Form):
    vibe = forms.CharField(label='What is your vibe? ', widget=forms.Select(choices=vibe_choices))

# Forms to take for chill vibes
class ChillForm(forms.Form):
    work = forms.CharField(label='Do you need to get work done? ', widget=forms.Select(choices=boolean_choices_work))

class WorkForm(forms.Form):
    env = forms.CharField(label='What work environment do you like today? ', widget=forms.Select(choices=[('library', 'Library'), ('cafe', 'Cafe')]))

class WalkForm(forms.Form):
    walk = forms.CharField(label='How do you feel about taking a walk? ', widget=forms.Select(choices=[('yes', 'love it!'), ('no', 'yuck!')]))
    mask = forms.CharField(label='Are you willing to wear mask? ', widget=forms.Select(choices=boolean_choices))
    travel_time = forms.IntegerField(label='How long are you willing to travel (mins) ? ', max_value=30, min_value=0)

# Forms to take for active vibes

class ActiveForm(forms.Form):
    bike = forms.CharField(label='Do you have a bike? ', widget=forms.Select(choices=boolean_choices))
    mask = forms.CharField(label='Are you willing to wear mask? ', widget=forms.Select(choices=boolean_choices))

# Forms to take for good food vibes

class GoodFoodForm(forms.Form):
    meal = forms.CharField(label='Which meal is it? ', widget=forms.Select(choices=meal_choices))

class BreakfastForm(forms.Form):
    english = forms.CharField(label='Wanna try a full English Breakfast? ', widget=forms.Select(choices=[('yes', 'Yes Please!'), ('no', 'Maybe another day')]))
    
class PriceForm(forms.Form):
    price = forms.IntegerField(label='How much are you willing to spend ($)? ', max_value=30, min_value=0)

# Forms to take for energetic vibes
class EnergeticForm(forms.Form):
    vulnerable = forms.CharField(label='Are you vulnerable for Covid? ', widget=forms.Select(choices=boolean_choices))
    energy = forms.CharField(label='What kind of energy are you feeling? ', widget=forms.Select(choices=energy_choices))
    travel_time = forms.IntegerField(label='How long are you willing to travel (mins) ? ', max_value=30, min_value=0)
