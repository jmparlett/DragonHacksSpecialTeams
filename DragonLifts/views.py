from django.shortcuts import render
from DragonLifts.models import AerobicExercise, AnaerobicExercise
from DragonLifts.forms import wOptions, AnaerobicForm, AerobicForm
from django.http import JsonResponse

def workoutBuilder(request):
  mainContext = {
    'anaero' : [[i.name,i.numSets, i.numReps, i.currentSet, i.restTime] for i in AnaerobicExercise.objects.all()],
    'aero' : [[i.name, i.exerciseLength] for i in AerobicExercise.objects.all()],
    'exerciseType' : wOptions(),
    # 'addAna' : AnaerobicForm(),
    # 'addAero' : AerobicForm(),
    # 'addExercise' : False
  }

  return render(request, 'DragonLifts/index.html', mainContext)

def aboutPage(request):
  return render(request, 'DragonLifts/about.html')

def addAnaExcercise(request):
  form = AnaerobicForm(request.POST or None)
  form2 = AerobicForm(request.POST or None)
  if form.is_valid():
    form.save()
  if form2.is_valid():
    form2.save()
  context = {'anaform' : form, 'aeroform': form2}
  print(form, form2, "KASKFDKAFKASFASF")
  return render(request, 'DragonLifts/addAna.html', context)


# def addExercise(request):
#   form1 = AnaerobicForm(request.POST or None)
#   form2 = AerobicForm(request.POST or None)

#   if form1.is_valid() and form2.is_valid():
#     form1.save()
#     form2.save()
#   else:
#     form1 = AnaerobicForm()
#     form2 = AerobicForm()
#   context = {
#     'anaform' : form1,
#     'aeroform': form2
#     }
#   return render(request, 'DragonLifts/addAna.html', context)
