from django.views.generic import ListView, DetailView, TemplateView	
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView
from django.views.generic.dates import DayArchiveView, TodayArchiveView

from blog.models import Post
from tagging.models import Tag, TaggedItem
from tagging.views import TaggedObjectList

from django.views.generic.edit import FormView		
from blog.forms import PostSearchForm			
from django.db.models import Q				
from django.shortcuts import render			

from django.views.generic.edit import CreateView, UpdateView, DeleteView	# 추가
from django.urls import reverse_lazy				# 추가
from web.views import LoginRequiredMixin					# 추가

#--- TemplateView
class TagTV(TemplateView) :
    template_name = 'tagging/tagging_cloud.html'

#--- ListView
class PostLV(ListView) :
    model = Post
    template_name = 'blog/post_all.html'
    context_object_name = 'posts'
    paginate_by = 2

class PostTOL(TaggedObjectList) :
    model = Post
    template_name = 'tagging/tagging_post_list.html'

#--- DetailView
class PostDV(DetailView) : 
    model = Post

#--- ArchiveView
class PostAV(ArchiveIndexView) :
    model = Post                                                    
    date_field = 'modify_date'

class PostYAV(YearArchiveView) :
    model = Post
    date_field = 'modify_date'
    make_object_list = True

class PostMAV(MonthArchiveView) :
    model = Post
    date_field = 'modify_date'

class PostDAV(DayArchiveView) :
    model = Post
    date_field = 'modify_date'

class PostTAV(TodayArchiveView) :
    model = Post
    date_field = 'modify_date'

# FormView					
class SearchFormView(FormView):			
    form_class = PostSearchForm			
    template_name = 'blog/post_search.html'	

    def form_valid(self, form):			
        schWord = '%s' % self.request.POST['search_word'] 		
        post_list = Post.objects.filter(Q(title__icontains=schWord) | Q(description__icontains=schWord) | Q(content__icontains=schWord)).distinct()	

        context = {}								
        context['form'] = form						
        context['search_term'] = schWord				
        context['object_list'] = post_list					

        return render(self.request, self.template_name, context)	# No Redirection

class PostCreateView(LoginRequiredMixin, CreateView):			# 추가
    model = Post							# 추가
    fileds = ['title', 'slug', 'description', 'content', 'tag']		# 추가
    initial = {'slug': 'auto-filling-do-not-input'}			# 추가
    fields = ['title', 'description', 'content', 'tag']		# 추가
    success_url = reverse_lazy('blog:index')				# 추가

    def form_vaild(self, form):						# 추가
        form.instance.owner = self.request.user				# 추가
        return super(PostCreateView, self).form_vaild(form)		# 추가

class PostChangeLV(LoginRequiredMixin, ListView):			# 추가
    template_name = 'blog/post_change_list.html'			# 추가

    def get_queryset(self):						# 추가
        return Post.objects.filter(owner=self.request.user)		# 추가

class PostUpdateView(LoginRequiredMixin, UpdateView):			# 추가
    model = Post							# 추가
    fields = ['title', 'slug', 'description', 'content', 'tag']		# 추가
    succes_url = reverse_lazy('blog:index')				# 추가

class PostDeleteView(LoginRequiredMixin, DeleteView) :			# 추가
    model = Post							# 추가
    success_url = reverse_lazy('blog:index')				# 추가
