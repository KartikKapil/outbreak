from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .APIs import chronic

@login_required
def search(request):
    if request.POST:
        return redirect('list_hospitals', {'data': request.POST['data']})
    else:
        return render(request, 'list_hospitals/search.html', {})


@login_required
def list_hospitals(request, data):
    if not data:
        # Generate all nearby facilities
        hospitals = chronic(28.6358749, 77.3738937)
    else:
        # Generate Customised facilities
        hospitals = chronic(28.6358749, 77.3738937)
    return render(request, 'list_hospitals/index.html', {'hospitals': hospitals })
