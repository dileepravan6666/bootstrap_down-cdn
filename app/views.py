from django.shortcuts import render

# Create your views here.
def download_bootstrap(request):
    return render(request,'bootstrap_download.html')

def cdn_bootstrap(request):
    return render(request,'bootstrap_cdn.html')
