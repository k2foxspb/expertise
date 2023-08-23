from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView

from data.models import Data


# Create your views here.
class DataView(PermissionRequiredMixin, ListView):
    model = Data

    template_name = 'data.html'
    permission_required = ("data.add_data",)
    permission_denied_message = 'неть'


def create(request):
    if request.method == "POST":
        data = Data()
        data.A = request.POST.get("A")
        data.B = request.POST.get("B")
        data.C = request.POST.get("C")
        data.D = request.POST.get("D")
        data.E = request.POST.get("E")
        data.F = request.POST.get("F")
        data.H = request.POST.get("H")
        data.I = request.POST.get("I")
        data.J = request.POST.get("J")
        data.K = request.POST.get("K")
        data.L = request.POST.get("L")

        data.save()
    return HttpResponseRedirect("/data")
