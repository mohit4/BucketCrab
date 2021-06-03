from django.urls import path

from .views import BucketCreateView, BucketUpdateView, BucketListView, BucketDetailView, BucketDeleteView
from .views import index

app_name = 'buckets'

urlpatterns = [
    path('bucket/all/', BucketListView.as_view(), name='bucket-list' ),
    path('bucket/<int:pk>/', BucketDetailView.as_view(), name='bucket-detail' ),
    path('bucket/create/', BucketCreateView.as_view(), name='bucket-create' ),
    path('bucket/<int:pk>/update/', BucketUpdateView.as_view(), name='bucket-update' ),
    path('bucket/<int:pk>/delete/', BucketDeleteView.as_view(), name='bucket-delete' ),
    path('bucket', index, name='bucket-search' ),
]