from django import forms
from DragonLifts.models import AerobicExercise, AnaerobicExercise

class wOptions(forms.Form):
  choices = [('aerobic','Aerobic'), ('anaerobic', 'Anaerobic')]
  workoutOptions = forms.CharField(label="Add your own: Aerobic or Anaerobic?", widget = forms.Select(choices=choices))

class AnaerobicForm(forms.ModelForm):
  class Meta:
    model = AnaerobicExercise
    fields = [
      'name',
      'numSets',
      'numReps',
      'restTime'
    ]

class AerobicForm(forms.ModelForm):
  class Meta:
    model = AerobicExercise
    fields = [
      'name',
      'exerciseLength'
    ]
  