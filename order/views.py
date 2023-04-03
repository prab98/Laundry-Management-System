from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.contrib import messages
from .models import LaundryItem
from .forms import LaundryItemForm

def orderrequest(request):
	order_details=LaundryItemForm()
    
	if request.method == "POST":
		order_details=LaundryItemForm(request.POST)
		if order_details.is_valid():
			order_details.save()
			#return redirect('/studentattendance/viewattendance')
		else:				print(order_details.errors)
			
	return render(request,'order.html',context={"order_details":order_details})
