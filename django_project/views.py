import subprocess

from django.http import HttpResponse

__author__ = 'tfaris'


def add_view(request):
    addend = request.GET.get('a', 0)
    p = subprocess.Popen('mono lib/ConsoleApplication1.exe ' + str(addend), stdout=subprocess.PIPE)
    #p = subprocess.Popen('lib/ConsoleApplication1.exe ' + str(addend), stdout=subprocess.PIPE)
    p.wait()
    out = p.stdout.read().strip()
    return HttpResponse(out)

