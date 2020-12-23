from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.


class FeatureConfig(models.Model):
  """ Feature Configurations """
  key = models.SlugField()
  value = models.CharField(max_length=200)

  def __str__(self):
    return self.key


class DevIteraction(models.Model):
  """ Development Cycle/Iteration """
  name = models.CharField(max_length=200, unique=True)
  main = models.BooleanField(default=True)

  class Meta:
    ordering = ['-name']

  def __str__(self):
    return self.name


class DevelopmentList(models.Model):
  """ Ongoing Developments """
  name = models.CharField(max_length=20, unique=True)
  main = models.BooleanField(default=True)

  class Meta:
    ordering = ['name']

  def __str__(self):
    return self.name


class Features(models.Model):
  """ Feature """
  name = models.CharField(max_length=200, unique=True)

  class Meta:
    ordering = ['name']

  def __str__(self):
    return self.name


class FeatureList(models.Model):
  name = models.CharField(max_length=200, unique=True)

  class Meta:
    verbose_name = "Feature"
    verbose_name_plural = "Feature"
    ordering = ['name']

  def __str__(self):
    return self.name