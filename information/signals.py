from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import DevelopmentList, DevIteraction

@receiver(post_save, sender=DevIteraction)
def after_saving_session(sender, created, instance, *args, **kwargs):
  if instance.current == True:
    DevIteraction.objects.exclude(pk=instance.id).update(current=False)


@receiver(post_save, sender=DevelopmentList)
def after_saving_term(sender, created, instance, *args, **kwargs):
  if instance.current == True:
    DevelopmentList.objects.exclude(pk=instance.id).update(current=False)
