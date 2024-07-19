from django.shortcuts import render
from django.views.generic import ListView, DetailView
from bookmark.models import Bookmark

from django.views.generic.edit import CreateView, UpdateView, DeleteView 	# 추가
from django.urls import reverse_lazy				# 추가
from web.views import LoginRequiredMixin					# 추가

# Create your views here.

# -- ListView
class BookmarkLV(ListView) :
    model = Bookmark

# -- DetailView
class BookmarkDV(DetailView) :
    model = Bookmark

class BookmarkCreateView(LoginRequiredMixin, CreateView):			# 추가
    model = Bookmark								# 추가
    fields = ['title', 'url']							# 추가
    success_url = reverse_lazy('bookmark:index')				# 추가
    def form_valid(self, form):							# 추가
        form.instance.owner = self.request.user					# 추가
        return super(BookmarkCreateView, self).form_valid(form)			# 추가

class BookmarkChangeLV(LoginRequiredMixin, ListView):				# 추가
    template_name = 'bookmark/bookmark_change_list.html'			# 추가

    def get_queryset(self):							# 추가
        return Bookmark.objects. filter(owner=self.request.user)		# 추가

class BookmarkUpdateView(LoginRequiredMixin, UpdateView) :			# 추가
    model = Bookmark								# 추가
    fields = ['title', 'url']							# 추가
    success_url = reverse_lazy('bookmark:index')				# 추가

class BookmarkDeleteView(LoginRequiredMixin, DeleteView) :			# 추가
    model = Bookmark								# 추가
    success_url = reverse_lazy('bookmark:index')				# 추가

