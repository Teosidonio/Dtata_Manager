from .models import DevelopmentList, DevIteraction, FeatureConfig

def site_defaults(request):
  main_session = DevIteraction.objects.get(current=True)
  development_list = DevelopmentList.objects.get(current=True)
  vals = SiteConfig.objects.all()
  contexts = {
      "main_session": main_session.name,
      "development_list": development_list.name
  }
  for val in vals:
    contexts[val.key] = val.value

  return contexts
