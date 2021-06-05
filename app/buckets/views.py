from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.db.models import Q
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Bucket


def index(request):
    """
    Index view for listing the search results
    """
    search_bucket = request.GET.get('search')

    if search_bucket:
        buckets = Bucket.objects.filter(
            (
                Q(title__icontains=search_bucket)
                | Q(description__icontains=search_bucket)
            )
            & Q(user=request.user)
        )
    else:
        buckets = Bucket.objects.filter(user=request.user).order_by("-title")
    
    context = {
        'buckets': buckets,
        'heading': f'Showing search results for : "{search_bucket}"'
    }

    return render(request, "buckets/bucket_list.html", context)


class BucketCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """
    Creating a new bucket
    """
    template_name = "buckets/bucket_form.html"
    model = Bucket
    fields = ('title', 'description', 'is_expirable', 'expiration_date',)
    success_message = 'Added new bucket!'

    login_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["heading"] = "Create new Bucket"
        return context
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class BucketUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """
    Updating an existing bucket
    """
    template_name = "buckets/bucket_form.html"
    model = Bucket
    fields = ('description', 'expiration_date',)
    success_message = 'Bucket updated!'

    login_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["heading"] = "Update Bucket"
        return context
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class BucketListView(LoginRequiredMixin, ListView):
    """
    Listing all the buckets present in database
    """
    template_name = "buckets/bucket_list.html"
    model = Bucket
    context_object_name = "buckets"

    login_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["heading"] = "Listing all bucket(s)"
        return context
    
    def get_queryset(self, **kwargs):
        return Bucket.objects.filter(user=self.request.user)


class BucketDetailView(LoginRequiredMixin, DetailView):
    """
    Printing details of a single bucket
    """
    template_name = "buckets/bucket_detail.html"
    model = Bucket
    context_object_name = "bucket"

    login_url = '/'


class BucketDeleteView(LoginRequiredMixin, DeleteView):
    """
    Deleting an existing bucket
    """
    template_name = "buckets/bucket_detail.html"
    model = Bucket
    context_object_name = "bucket"
    success_url = reverse_lazy("buckets:bucket-list")
    success_message = 'Bucket deleted!'

    login_url = '/'

    def delete(self, request, *args, **kwargs):
        messages.error(self.request, self.success_message)
        return super(BucketDeleteView, self).delete(request, *args, **kwargs)