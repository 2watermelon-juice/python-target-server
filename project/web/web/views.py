from django.views.generic.base import TemplateView

from django.views.generic.edit import CreateView		
from django.contrib.auth.forms import UserCreationForm	
from django.urls import reverse_lazy			

from django.contrib.auth.decorators import login_required	# 추가

# create your views here.

#--- Homepage View
class HomeView(TemplateView) :
    template_name = 'home.html'

#-- User Creation						
class UserCreateView(CreateView):			
    template_name = 'registration/register.html'	
    form_class = UserCreationForm				
    success_url = reverse_lazy('register_done')			
class UserCreateDoneTV(TemplateView):				
    template_name = 'registration/register_done.html'		

class LoginRequiredMixin(object):					# 추가
    @classmethod							# 추가
    def as_view(cls, **initkwargs):					# 추가
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)	# 추가
        return login_required(view)					# 추가
