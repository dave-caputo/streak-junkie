from activities.views import ActivityCreateView

from django.urls import path

urlpatterns = [
    path("create/", ActivityCreateView.as_view()),
]
