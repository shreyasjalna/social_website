from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from home.models import *
from groups.models import *
from posts.models import *
from accounts.models import *

# Create your views here.
def index(request):
    return render(request,'index.html')
