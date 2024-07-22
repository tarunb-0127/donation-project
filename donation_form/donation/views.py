# donation/views.py
from django.shortcuts import render, redirect
from .models import Donation
from .forms import DonationForm

def donate(request):
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('donation_confirmation')
    else:
        form = DonationForm()
    return render(request, 'donate.html', {'form': form})

def donation_confirmation(request):
    return render(request, 'donation_confirmation.html')

def view_donations(request):
    donations = Donation.objects.all()
    return render(request, 'view_donations.html', {'donations': donations})
