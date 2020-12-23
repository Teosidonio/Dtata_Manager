from .models import DevelopmentList, DevIteraction

class SiteWideConfigs:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
      main_session = DevIteraction.objects.get(main=True)
      development_list = DevelopmentList.objects.get(main=True)

      request.main_session = main_session
      request.development_list = development_list

      response = self.get_response(request)

      return response