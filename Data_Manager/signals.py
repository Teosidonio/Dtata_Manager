import os
import csv
from io import StringIO
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from Data_Manager.models import EnvironmentClass
from .models import Environment, EnvironmentBulkUpload

@receiver(post_save, sender=EnvironmentBulkUpload)
def create_bulk_student(sender, created, instance, *args, **kwargs):
  if created:
    opened = StringIO(instance.csv_file.read().decode())
    reading = csv.DictReader(opened, delimiter=',')
    environment = []
    for row in reading:
      if 'stage' in row and row['stage']:
        stage = row['stage']
        platform = row['platform'] if 'platform' in row and row['platform'] else ''
        database = row['database'] if 'database' in row and row['database'] else ''
        run_stack = row['run_stack'] if 'run_stack' in row and row['run_stack'] else ''
        web_server = row['web_server'] if 'web_server' in row and row['web_server'] else ''
        ip_servername = row['ip_servername'] if 'ip_servername' in row and row['ip_servername'] else ''
        hardware = row['hardware'] if 'hardware' in row and row['hardware'] else ''
        product_app = row['product_app'] if 'product_app' in row and row['product_app'] else ''
        provider = row['provider'] if 'provider' in row and row['provider'] else ''
        port = row['port'] if 'port' in row and row['port'] else ''
        created_by = row['created_by'] if 'created_by' in row and row['created_by'] else ''
        creation_date = row['creation_date'] if 'creation_date' in row and row['creation_date'] else ''
        brd = row['brd'] if 'brd' in row and row['brd'] else ''
        if Environment:
          EnvironmentClass, kind = EnvironmentClass.objects.get_or_create(name=Environment)

        check = Environment.objects.filter(stage=stage).exists()
        if not check:
          environment.append(
            Student(
                stage=stage,
                platform=platform,
                database=database,
                run_stack=run_stack,
                web_server=web_server,
                ip_servername=ip_servername,
                hardware=hardware,
                product_app=product_app,
                provider = provider,
                port=port,
                created_by=created_by,
                creation_date=creation_date,
                brd=brd
            )
          )

    environment.objects.bulk_create(environment)
    instance.csv_file.close()
    instance.delete()


def _delete_file(path):
   """ Deletes file from filesystem. """
   if os.path.isfile(path):
       os.remove(path)

@receiver(post_delete, sender=EnvironmentBulkUpload)
def delete_csv_file(sender, instance, *args, **kwargs):
  if instance.csv_file:
    _delete_file(instance.csv_file.path)


@receiver(post_delete, sender=Environment)
def delete_passport_on_delete(sender, instance, *args, **kwargs):
  if instance.brd:
    _delete_file(instance.brd.path)
