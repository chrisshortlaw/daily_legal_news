from django.shortcuts import get_object_or_404, render
from .models import Profile
from .forms import ProfileForm
# Create your views here.


def profile(request):

    profile = get_object_or_404(Profile, user=request.user)

    form = ProfileForm()

    context = {
               "form": form,
               "profile": profile
              }

    return render(request, 'profile.html', context=context)
