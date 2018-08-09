from django.shortcuts import render
from django.contrib.auth.models import Group
from allauth.account.views import SignupView
from allauth.account.forms import SignupForm
from .models import BrandManagerProfile


class BrandManagerSignupView(SignupView):
    template_name = 'account/managers_signup.html'
    form_class = SignupForm
    group = Group.objects.get(id=1)

    def form_valid(self, form):
        response = super(BrandManagerSignupView, self).form_valid(form)
        user = self.user
        self.group.user_set.add(user)
        BrandManagerProfile.objects.create(user=user)
        return response
