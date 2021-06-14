from django.shortcuts import render
from django.views.generic.base import TemplateView

from buckets.models import Bucket


class DashboardView(TemplateView):
    """
    Presenting all the user's progress
    """
    template_name = 'dashboard/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['planned_count'] = Bucket.objects.filter(is_open=True,start_date=None).count()
        context['inprogress_count'] = Bucket.objects.filter(is_open=True).exclude(start_date=None).count()
        context['completed_count'] = Bucket.objects.filter(is_open=False).count()
        context['last_active_buckets'] = Bucket.objects.all()[:3]
        return context
