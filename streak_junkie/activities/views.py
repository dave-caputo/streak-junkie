from activities.models import Activity

from django.views.generic import CreateView


class ActivityCreateView(CreateView):
    template_name = "activities/create.html"
    model = Activity
    fields = ["name"]
