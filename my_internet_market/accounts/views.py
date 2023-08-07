from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from .forms import RegistrationForm
from .models import UserProfile


class RegistrationView(FormView):
    template_name = 'accounts/registration.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        user = form.save()
        UserProfile.objects.create(user=user, **form.cleaned_data)
        return super().form_valid(form)