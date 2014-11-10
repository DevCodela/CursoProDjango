from django.shortcuts import render, redirect, get_object_or_404

from .models import Event, Category
from apps.users.models import User
from .forms import EventoForm

from django.core.urlresolvers import reverse


def login(request):
    return render(request, "login.html", {})


def index(request):
    events = Event.objects.all().order_by('-created')[:6]
    categories = Category.objects.all()
    return render(request, 'events/index.html', {'events' : events, 'categories':categories})


def main_panel(request):
    #organizer = request.user.username
    events = Event.objects.filter(organizer__username='victorvillazon').order_by('is_free', '-created')
    cantidad_eventos = events.count()
    return render(request, 'events/panel/panel.html', {'events' : events, 'cantidad': cantidad_eventos})


def detalle_evento(request, evento_id):
    event = get_object_or_404(Event, pk=evento_id)
    return render(request, 'events/panel/detalle_evento.html', {'event': event})


def crear_evento(request):
    if request.method == "POST":
        modelform = EventoForm(request.POST, request.FILES)
        if modelform.is_valid():
            organizador = User.objects.get(pk=3)
            nuevo_evento = modelform.save()
            nuevo_evento.organizer = organizador
            nuevo_evento.save()
            return redirect(reverse('events_app:panel'))
    else:
        modelform = EventoForm()

    return render(request, "events/panel/crear_evento.html", {"form": modelform})


def editar_evento(request, evento_id):
    event = get_object_or_404(Event, pk=evento_id)
    
    if request.method == "POST":
        modelform = EventoForm(request.POST, request.FILES, instance=event)
        if modelform.is_valid():
            modelform.save()
            return redirect(reverse('events_app:panel'))
    else:
        modelform = EventoForm(instance=event)

    return render(request, "events/panel/editar_evento.html", {"form": modelform, 'event': event})


def eliminar_evento(request, evento_id):
    event = get_object_or_404(Event, pk=evento_id)
    
    if request.method == "POST":
        event.delete()
        return redirect(reverse('events_app:panel'))

    return render(request, "events/panel/eliminar_evento.html", {'event': event})