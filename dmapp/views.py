from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Dm

# Create your views here.
def home(request):
    dms = Dm.objects.filter(receiver_id=request.user.id)
    return render(request, 'home.html', {'count': dms.count()})

def dm_list(request):
    dms = Dm.objects.filter(receiver_id=request.user.id)
    return render(request, 'list.html', {'dms': dms})

def create(request):
    if request.method == 'POST':
        dm = Dm()
        dm.sender_id = request.user.id
        dm.receiver_id = request.POST['user_id']
        dm.content = request.POST['content']
        dm.send_time = timezone.datetime.now()
        dm.save()
        return redirect('/detail/', str(dm.id))
    else:
        user_id = request.GET['sender_id']
        return render(request, 'create.html', {'user_id': user_id})

def detail(request, id):
    dm = get_object_or_404(Dm, pk = id)
    return render(request, 'detail.html', {'dm': dm})