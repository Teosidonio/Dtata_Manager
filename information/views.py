from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import FeatureConfig, DevIteraction, DevelopmentList, Features, FeatureList
from .forms import FeatureConfigForm, DevIteractionForm, DevelopmentListForm, FeaturesForm, FeatureListForm

# Create your views here.
@login_required
def index_view(request):
  return render(request, 'index.html')

@login_required
def featureconfig_view(request):
  """ Feature Config View """
  if request.method == 'POST':
    form = FeatureConfigForm(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request, 'Configurations successfully updated')
      return HttpResponseRedirect('feature-config')
  else:
    form = FeatureConfigForm(queryset=FeatureConfig.objects.all())

  context = {"formset": form, "title": "Configuration"}
  return render(request, 'information/feature_config.html', context)


class FeatureListView(LoginRequiredMixin, SuccessMessageMixin, ListView):
  model = DevIteraction
  template_name = 'information/dev_cycle_iteration.html'

  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['form'] = DevIteractionForm()
      return context



class FeatureCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
  form_class = DevIteractionForm
  template_name = 'information/mgt_form.html'
  success_url = reverse_lazy('feature')
  success_message = 'New feature successfully added'

  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['title'] = 'Add new Feature'
      return context



class FeatureUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
  model = DevIteractionForm
  fields = ['name', 'main']
  success_url = reverse_lazy('feature')
  success_message = 'Feature successfully updated.'
  template_name = 'information/mgt_form.html'


  def form_valid(self, form):
    obj = self.object
    if obj.current == False:
      terms = DevIteraction.objects.filter(
          current=True).exclude(name=obj.name).exists()
      if not terms:
        messages.warning(self.request, 'You must set a feature to main.')
        return redirect('dev_cycle_iteration')
    return super().form_valid(form)


class FeatureDeleteView(LoginRequiredMixin, DeleteView):
  model = DevIteraction
  success_url = reverse_lazy('feature')
  template_name = 'infromation/confirm_feature_delete.html'
  success_message = "The feature {} has been deleted with all its attached content"


  def delete(self, request, *args, **kwargs):
      obj = self.get_object()
      if obj.main == True:
        messages.warning(request, 'This feature cannot be deleted because it is set to main')
        return redirect('feature')
      messages.success(self.request, self.success_message.format(obj.name))
      return super(FeatureDeleteView, self).delete(request, *args, **kwargs)

#Development List

class DevListView(LoginRequiredMixin, SuccessMessageMixin, ListView):
  model = DevelopmentList
  template_name = 'information/dev_list.html'

  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['form'] = DevelopmentListForm()
      return context



class DevCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
  form_class = DevelopmentListForm
  template_name = 'information/mgt_form.html'
  success_url = reverse_lazy('devfeature')
  success_message = 'New Developer successfully added'



class DevUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
  form_class = DevelopmentListForm
  success_url = reverse_lazy('devfeature')
  success_message = 'Dev_Feature successfully updated.'
  template_name = 'information/mgt_form.html'


  def form_valid(self, form):
    obj = self.object
    if obj.current == False:
      terms = DevelopmentList.objects.filter(current=True).exclude(name=obj.name).exists()
      if not devfeature:
        messages.warning(self.request, 'You must set a devfeature to main.')
        return redirect('devfeature')
    return super().form_valid(form)


class DevDeleteView(LoginRequiredMixin, DeleteView):
  model = DevelopmentList
  success_url = reverse_lazy('devfeature')
  template_name = 'information/confirm_feature_delete.html'
  success_message = "The devfeature {} has been deleted with all its attached content"


  def delete(self, request, *args, **kwargs):
      obj = self.get_object()
      if obj.current == True:
        messages.warning(request, 'This devfeature cannot be deleted because it is set to main!')
        return redirect('devfeature')
      messages.success(self.request, self.success_message.format(obj.name))
      return super(TermDeleteView, self).delete(request, *args, **kwargs)
#Team Management view


class TeamListView(LoginRequiredMixin, SuccessMessageMixin, ListView):
  model = Features
  template_name = 'information/feature_list.html'

  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['form'] = FeaturesForm()
      return context



class TeamCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
  form_class = FeaturesForm
  template_name = 'information/mgt_form.html'
  success_url = reverse_lazy('features')
  success_message = 'New features successfully added'



class TeamUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
  model = Features
  fields = ['name']
  success_url = reverse_lazy('features')
  success_message = 'Features successfully updated.'
  template_name = 'information/mgt_form.html'



class TeamDeleteView(LoginRequiredMixin, DeleteView):
  model = Features
  success_url = reverse_lazy('features')
  template_name = 'information/core_confirm_delete.html'
  success_message = "The features {} has been deleted with all its attached content"


  def delete(self, request, *args, **kwargs):
      obj = self.get_object()
      print(obj.name)
      messages.success(self.request, self.success_message.format(obj.name))
      return super(ClassDeleteView, self).delete(request, *args, **kwargs)

#Team members


class MainFListView(LoginRequiredMixin, SuccessMessageMixin, ListView):
  model = FeatureList
  template_name = 'information/team_list.html'

  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['form'] = FeatureListForm()
      return context



class MainFCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
  form_class = FeatureListForm
  template_name = 'information/mgt_form.html'
  success_url = reverse_lazy('team')
  success_message = 'New team successfully added'



class MainFUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
  model = FeatureList
  fields = ['name']
  success_url = reverse_lazy('team')
  success_message = 'Team successfully updated.'
  template_name = 'information/mgt_form.html'



class MainFDeleteView(LoginRequiredMixin, DeleteView):
  model = FeatureList
  success_url = reverse_lazy('team')
  template_name = 'information/core_confirm_delete.html'
  success_message = "The Team {} has been deleted with all its attached content"

  def delete(self, request, *args, **kwargs):
      obj = self.get_object()
      messages.success(self.request, self.success_message.format(obj.name))
      return super(SubjectDeleteView, self).delete(request, *args, **kwargs)


@login_required
def main_session_view(request):
  """ Main Session and Team """
  if request.method == 'POST':
    form = FeatureListForm(request.POST)
    if form.is_valid():
      session = form.cleaned_data['main_session']
      term = form.cleaned_data['development_list']
      DevIteraction.objects.filter(name=session).update(current=True)
      DevIteraction.objects.exclude(name=session).update(current=False)
      DevelopmentList.objects.filter(name=term).update(current=True)
      DevelopmentList.objects.exclude(name=term).update(current=False)

  else:
    form = FeatureListForm(initial={
      "main_session": DevIteraction.objects.get(current=True),
      "development_list": DevelopmentList.objects.get(current=True)
    })


  return render(request, 'information/main_session.html', {"form":form})
