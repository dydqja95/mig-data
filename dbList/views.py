from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Connection
from .forms import ConnectionForm

class ConnectionListView(View):
    def get(self, request):
        connections = Connection.objects.all()
        return render(request, 'connections/list.html', {'connections': connections})

class ConnectionCreateView(View):
    def get(self, request):
        form = ConnectionForm()
        return render(request, 'connections/form.html', {'form': form})

    def post(self, request):
        form = ConnectionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('connection_list')
        return render(request, 'connections/form.html', {'form': form})

class ConnectionUpdateView(View):
    def get(self, request, pk):
        connection = get_object_or_404(Connection, pk=pk)
        form = ConnectionForm(instance=connection)
        return render(request, 'connections/form.html', {'form': form})

    def post(self, request, pk):
        connection = get_object_or_404(Connection, pk=pk)
        form = ConnectionForm(request.POST, instance=connection)
        if form.is_valid():
            form.save()
            return redirect('connection_list')
        return render(request, 'connections/form.html', {'form': form})