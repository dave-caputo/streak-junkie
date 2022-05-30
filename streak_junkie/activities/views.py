from activities.models import Activity
from activities.serializers import ActivitySerializer

from django.views.generic import CreateView
from rest_framework.viewsets import ModelViewSet


class ActivityCreateView(CreateView):
    template_name = "activities/create.html"
    model = Activity
    fields = ["name"]


class ActivityViewSet(ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
