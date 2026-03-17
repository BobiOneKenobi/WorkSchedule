from django.views.generic import TemplateView
from django.shortcuts import render
class HomeView(TemplateView):
    template_name = 'common/home.html'
def custom_404(request, exception):
    return render(request, '404.html', status=404)