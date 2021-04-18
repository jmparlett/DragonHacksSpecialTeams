from django.db import models 
from DragonLifts.utils import *

class AnaerobicExercise(models.Model):
  name = models.CharField(max_length = 25, default = "name")
  numSets = models.IntegerField(default=3)
  numReps = models.IntegerField(default=10)
  currentSet = models.IntegerField(default=1)
  restTime = models.IntegerField(default=90)
  restTimer = Timer()

  def incrementSet(self):
    self.currentSet+=1
    if self.restTimer.getStatus():
      self.restTimer.stop()
    self.restTimer.start()
    

class AerobicExercise(models.Model):
  name = models.CharField(max_length = 10, default='Run')
  exerciseLength = models.IntegerField(default=5)


class user(models.Model):
  name= models.CharField(max_length = 10)
  age = models.IntegerField()
  height = models.IntegerField()
  weight = models.IntegerField()
  BMI = models.IntegerField()

  def calculateBMI(self):
    kg = self.weight / 0.453592 
    meters = self.height / 0.0254

    #BMI = mass
    self.BMI = round(kg / meters)
      


  