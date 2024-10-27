from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DeleteView, UpdateView
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Connection, srcTableBas, srcTableDtl
from .forms import ConnectionForm  # ConnectionForm을 정의해야 합니다.

# Create
@csrf_exempt
def connection_create(request):
    if request.method == 'POST':
        form = ConnectionForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
        else:
            if Connection.objects.filter(conn_name=request.POST['conn_name']).exists():
                messages.error(request, '커넥션명이 중복됩니다.')
    else:
        form = ConnectionForm()

    return redirect('connection:connection_list')

# Read
def connection_list(request):
    connections = Connection.objects.all()
    connection_type_choices = Connection.CONNECTION_TYPE_CHOICES
    
    tables = srcTableBas.objects.all()
    return render(request, 
                 'connection_list.html', 
                 {'connections': connections,
                  'connection_type_choices': connection_type_choices,
                  'tables' : tables,
                 }) 

# Update
class ConnectionUpdateView(UpdateView):
    model = Connection
    fields = [
        'conn_name',
        'conn_type',
        'owner',
        'ip',
        'port',
        'user',
        'pwd',
        'extra',
    ]

# Delete
class ConnectionDeleteView(DeleteView):
    model = Connection
    # template_name = "connection_delete_confirm.html"
    success_url   = reverse_lazy('connection:connection_list')



# def connection_update(request, pk):
#     connection = get_object_or_404(Connection, pk=pk)
#     if request.method == 'POST':
#         form = ConnectionForm(request.POST, instance=connection)
#         if form.is_valid():
#             form.save()
#             return redirect('connection_list')
#     else:
#         form = ConnectionForm(instance=connection)
#     return render(request, 'connection_update.html', {'form': form})