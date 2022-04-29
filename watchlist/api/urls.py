from django.urls import path
from .views import ShowListView, ShowDetailView, StreamPlatformListView, StreamPlatformDetailView, ReviewListView, ReviewDetailView, ReviewCreateView

urlpatterns = [
    # ------------------STREAMING PLATFORMS----------#
    path('platform', StreamPlatformListView.as_view(), name="streamingplatform-list"),
    path('platform/<slug:slug>', StreamPlatformDetailView.as_view(), name="streamingplatform-details"),

    # ------------------Watch------------------------#
    path('show', ShowListView.as_view(), name="show-list"),
    path('show/<slug:slug>', ShowDetailView.as_view(), name="show-details"),

    # ------------------Review------------------------#
    path('show/<slug:slug>/review-list', ReviewListView.as_view(), name="review-list"),
    path('show/<slug:slug>/review-create', ReviewCreateView.as_view(), name="review-create"),
    path('review/<int:pk>', ReviewDetailView.as_view(), name="review-details"),
]
