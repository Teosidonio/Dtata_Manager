
# Create your models here.
from django.db import models
from django.utils import timezone
from django.urls import reverse

from information.models import FeatureList
from django.core.validators import RegexValidator

class Environment(models.Model):
  STAGES = [
      ('d','DEVELOPMENT'),('s', 'SIT'), ('u','UAT'), ('st','STAGING/PRE-PROD') , ('p','PRODUCTION')
  ]
  DATABASES = [
      ('pst','POSTGRESQL'), ('md','MariaDB'), ('my','MySQL'), ('o','Oracle'),
      ('ms','MS SQL Server'),('sl', 'SQLite3'), ('cd','CosmosDB'), ('mg','MongoDB')
  ]

  PLATFORM = [
      ('m','MacOs'), ('l','LINUX'),
      ('w','WINDOWS')
  ]
  HARDWARE = [
      ('ps','PHISICAL_SERVER'), ('vm','VIRTUAL MACHINE')
  ]
  PROVIDER = [
      ('int','INTERNAL'), ('out','OUTSOURCED')
  ]



  stage = models.CharField(max_length=70, choices=STAGES)
  platform = models.CharField(max_length=50, choices=PLATFORM)
  database              = models.CharField(max_length=100, choices=DATABASES)
  run_stack             = models.CharField(max_length=100)
  web_server            = models.CharField(max_length=100)
  ip_servername         = models.IntegerField()
  hardware              = models.CharField(max_length=150, choices=HARDWARE)
  product_app           = models.CharField(max_length=300)
  provider              = models.CharField(max_length=100)
  port                  = models.IntegerField()

  created_by            = models.CharField(max_length=150, blank=True)
  creation_date         = models.DateTimeField(default=timezone.now)
  brd                   = models.ImageField(blank=True, upload_to='environment/brd/')  

  class Meta:
    ordering = ['stage', 'platform', 'database']

  def __str__(self):
    return f'{self.stage} {self.platform} {self.database} {self.run_stack} {self.web_server} {self.ip_servername} {self.hardware} {self.product_app} {self.provider} {self.port} {self.created_by} {self.creation_date} {self.brd}'

  def get_absolute_url(self):
    return reverse('environment_detail', kwargs={'pk': self.pk})


class EnvironmentBulkUpload(models.Model):
  date_uploaded       = models.DateTimeField(auto_now=True)
  csv_file            = models.FileField(upload_to='environment/bulkupload/')