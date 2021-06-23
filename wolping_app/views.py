import os

from django.shortcuts import redirect, render
from .models import Data

from wakeonlan import send_magic_packet

def index(request):
    if request.user.is_authenticated:
        response = ""
        if 'ping' in request.GET:
            if request.GET['ping']:
                response = "Host is up"
            else:
                response = "Host is down"
        if 'wol' in request.GET:
            response = "WoL package sent"
        obj = Data.objects.get(pk=1)
        ip = obj.ip_address
        mac = obj.mac_address
        context = {'ip': ip, 'mac': mac, 'response': response}
        return render(request, 'wolping_app/index.html', context)
    else:
        return redirect('/admin')


def update(request):
    if request.user.is_authenticated:
        obj = Data.objects.get(pk=1)
        if request.POST.get('update'):
            ip = request.META['REMOTE_ADDR']
        if request.POST.get('save'):
            ip = request.POST['ip-address']
        mac = request.POST['mac-address']
        obj.ip = ip
        obj.mac = mac
        obj.save()
    else:
        return redirect('/admin')


def ping(request):
    if request.user.is_authenticated:
        obj = Data.objects.get(pk=1)
        ip = obj.ip_address
        host_up = True if os.system("ping -n 1 " + ip) == 0 else False
        print(host_up)
        return redirect(f"/wolping_app?ping={host_up}")
    else:
        return redirect('/admin')

def wake_on_lan(request):
    if request.user.is_authenticated:
        obj = Data.objects.get(pk=1)
        mac = obj.mac_address
        send_magic_packet(mac)
        return redirect(f"/wolping_app?wol")
    else:
        return redirect('/admin')
