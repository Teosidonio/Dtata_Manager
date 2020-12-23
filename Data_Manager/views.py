from django.shortcuts import render

# Create your views here.
import csv
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.forms import widgets
from django.urls import reverse_lazy

from .models import Environment, EnvironmentBulkUpload
#from .models import 

@login_required
def Environment_list(request):
  Environments = Environment.objects.all()
  return render(request, 'Data_Manager/environment_list.html', {"Environments":Environments})


class EnvironmentDetailView(LoginRequiredMixin, DetailView):
    model = Environment
    template_name = "Data_Manager/environment_detail.html"

    def get_context_data(self, **kwargs):
        context = super(EnvironmentDetailView, self).get_context_data(**kwargs)
        #context['payments'] = Invoice.objects.filter(Environment=self.object)
        return context


class EnvironmentCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Environment
    fields = '__all__'
    success_message = "New Environment successfully added."

    def get_form(self):
        '''add date picker in forms'''
        form = super(EnvironmentCreateView, self).get_form()
        form.fields['creation_date'].widget = widgets.DateInput(
            attrs={'type': 'date'})
        #form.fields['address'].widget = widgets.Textarea(attrs={'rows': 2})
        #form.fields['others'].widget = widgets.Textarea(attrs={'rows': 2})
        return form


class EnvironmentUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Environment
    fields = '__all__'
    success_message = "Records successfully updated."

    def get_form(self):
        '''add date picker in forms'''
        form = super(EnvironmentUpdateView, self).get_form()
        form.fields['creation_date'].widget = widgets.DateInput(
            attrs={'type': 'date'})
        #form.fields['date_of_admission'].widget = widgets.DateInput(attrs={
        #                                                            'type': 'date'})
        #form.fields['address'].widget = widgets.Textarea(attrs={'rows': 2})
        #form.fields['others'].widget = widgets.Textarea(attrs={'rows': 2})
       # form.fields[''].widget = widgets.FileInput()
        return form


class EnvironmentDeleteView(LoginRequiredMixin, DeleteView):
    model = Environment
    success_url = reverse_lazy('environment-list')


class EnvironmentBulkUploadView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = EnvironmentBulkUpload
    template_name = 'Data_Manager/environments_upload.html'
    fields = ['csv_file']
    success_url = '/Data_Manager/list'
    success_message = 'Successfully uploaded Environments'

@login_required
def downloadcsv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="environment_template.csv"'

    writer = csv.writer(response)
    writer.writerow(['stage', 'platform', 'database', 'run_stack', 'web_server', 'ip_servername', 'hardware',
                     'product_app', 'provider', 'port', 'created_by', 'creation_date', 'brd'])

    return response