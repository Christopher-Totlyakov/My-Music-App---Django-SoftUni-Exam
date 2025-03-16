from django.views.generic import DetailView
from profiles.models import Profile
from musicApp.utils import get_user_obj

class ProfileDetailView(DetailView):
    template_name = 'profiles/profile-details.html'

    def get_object(self, queryset=None):
        return get_user_obj()