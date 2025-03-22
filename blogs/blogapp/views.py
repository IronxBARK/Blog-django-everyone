from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import BlogEntry
from django.urls import reverse_lazy
from .forms import EntryForm 
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .mixins import LoginRequired
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied

# Create your views here.
class MainPage(LoginRequiredMixin, ListView):
    model = BlogEntry
    template_name = 'home.html'
    
    context_object_name = 'blogs'
    
    slug_field = 'slug'
    slug_url_kwargs = 'slug'
    
    login_url = 'login' # login_url is required in LoginRequiredMixin
    
class Detail(LoginRequired, DetailView):
    model = BlogEntry
    template_name = 'one.html'
    
    context_object_name = 'one'
    
class Create(LoginRequired, CreateView):
    form_class = EntryForm
    template_name = 'create.html'
    
    success_url = reverse_lazy('main')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, "Blog entry created successfully!")  
        return super().form_valid(form)
    
class Update(LoginRequired, UpdateView):
    form_class = EntryForm
    template_name = 'create.html'
    
    success_url = reverse_lazy('main')
    
    
    def get_queryset(self):
        entry = get_object_or_404(BlogEntry, slug=self.kwargs['slug'])
        if entry.author != self.request.user:
            raise PermissionDenied
        return BlogEntry.blog.filter(slug=self.kwargs['slug'])
    
    def form_valid(self, form):
        messages.success(self.request, "Blog entry updated successfully!")  
        return super().form_valid(form)


class Delete(LoginRequired, DeleteView):
    model = BlogEntry
    template_name = 'one.html'

    success_url = reverse_lazy('main')
    
    def get_queryset(self):
        entry = get_object_or_404(BlogEntry, slug=self.kwargs['slug'])
        if entry.author != self.request.user:
            raise PermissionDenied
        return BlogEntry.blog.filter(slug=self.kwargs['slug'])