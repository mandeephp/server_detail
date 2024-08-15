import json
from time import strftime

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.db.models import Count
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.utils import timezone
import re
from core.models import *
from django.core.serializers.json import DjangoJSONEncoder
from datetime import datetime, timedelta


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


@login_required(login_url='login')
def setup_dashboard(request):
    SetupModel = Setup
    current_date = datetime.now()
    previous_date = current_date - timedelta(days=1)
    previous_date = previous_date.strftime('%Y%m%d')
    today_date = current_date.strftime('%Y%m%d')
    SetupModel._meta.db_table = today_date
    if not SetupModel.objects.exists():
        SetupModel._meta.db_table = previous_date
    setup_aggregates = Setup.objects.values('mosl').annotate(count=Count('id'))

    setup_data = []
    setups = SetupModel.objects.all()

    for setup in setups:
        expiry_color = '#bbebbb'
        if setup.expiry_date:
            days_until_expiry = (setup.expiry_date.date() - setup.start_time.date()).days
            if days_until_expiry <= 10:
                expiry_color = '#e39195'

        trades_color = '#bbebbb' if setup.trades == setup.dc_trades else '#e39195'
        stream_color = '#bbebbb' if setup.contract_file_date == setup.stream_id_file_date else '#e39195'

        setup_data.append({
            'setup': {
                'id': setup.id,
                'mosl': setup.mosl,
                'server': setup.server,
                'start_time': setup.start_time if setup.start_time else None,
                'expiry_date': setup.expiry_date if setup.expiry_date else None,
                'ats': setup.ats,
                'expiry_color': expiry_color,
                'trades': setup.trades,
                'dc_trades': setup.dc_trades,
                'scripts_loaded': setup.scripts_loaded,
                'contract_file_date': setup.contract_file_date.isoformat() if setup.contract_file_date else None,
                'stream_id_file_date': setup.stream_id_file_date.isoformat() if setup.stream_id_file_date else None,
                'trades_color': trades_color,
                'stream_color': stream_color,
                'fcast': setup.fcast,
                'highest_temperature': setup.highest_temperature,
                'recovery': setup.recovery,
                'stream_id1_lastsequence': setup.stream_id1_lastsequence,
                'stream_id1_livesequence': setup.stream_id1_livesequence,
                'stream_id2_lastsequence': setup.stream_id2_lastsequence,
                'stream_id2_livesequence': setup.stream_id2_livesequence,
                'stream_id3_lastsequence': setup.stream_id3_lastsequence,
                'stream_id3_livesequence': setup.stream_id3_livesequence,
                'stream_id4_lastsequence': setup.stream_id4_lastsequence,
                'stream_id4_livesequence': setup.stream_id4_livesequence,
                'stream_id5_lastsequence': setup.stream_id5_lastsequence,
                'stream_id5_livesequence': setup.stream_id5_livesequence,
                'stream_id6_lastsequence': setup.stream_id6_lastsequence,
                'stream_id6_livesequence': setup.stream_id6_livesequence,
                'stream_id7_lastsequence': setup.stream_id7_lastsequence,
                'stream_id7_livesequence': setup.stream_id7_livesequence,
                'stream_id8_lastsequence': setup.stream_id8_lastsequence,
                'stream_id8_livesequence': setup.stream_id8_livesequence,
            }
        })

    setup_data_json = json.dumps(setup_data, cls=DjangoJSONEncoder)

    return render(request, 'core/setup_dashboard.html', {
        'setup_aggregates': setup_aggregates,
        'setup_data': setup_data,
        'setup_data_json': setup_data_json,
    })
