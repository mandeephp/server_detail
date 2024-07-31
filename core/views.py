import json
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from core.models import ServerMetric, ORMS


# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        redirect_to = request.POST.get('redirect')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            if redirect_to == 'custom':
                custom_page = request.POST.get('custom-page')
                return HttpResponseRedirect(custom_page)
            elif redirect_to:
                return redirect(redirect_to)
        else:
            return render(request, 'core/login.html', {'error': 'Invalid credentials'})

    # If it's a GET request, just render the login page
    return render(request, 'core/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def orm_dashboard(request):
    orms = ORMS.objects.all()
    server_details = list(ServerMetric.objects.all().values(
        'id', 'server', 'start_time', 'orms','orms__name', 'm2m', 'realised', 'cepos',
        'pepos', 'fut_pos', 'total_pos', 'delta', 'scripts', 'streams', 'stream_number'
    ))

    context = {
        'orms_data':orms,
        'server_details': server_details,
        'server_details_json': json.dumps(server_details, default=str)  # Serialize to JSON
    }
    return render(request, 'core/dashboard.html', context)

@login_required(login_url='login')
def strategy_dashboard(request):
    return render(request, 'core/strategy_dashboard.html')