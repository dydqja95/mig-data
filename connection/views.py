from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from .models import Connection
from .forms import ConnectionForm  # ConnectionForm을 정의해야 합니다.

# Create
@csrf_exempt
def connection_create(request):
    if request.method == 'POST':
        form = ConnectionForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
    else:
        form = ConnectionForm()
    # return render(request, 'connection_list.html', {'form': form})
    return redirect('connection:connection_list')

# Read
def connection_list(request):
    connections = Connection.objects.all()
    connection_type_choices = Connection.CONNECTION_TYPE_CHOICES
    print(connections)
    return render(request, 
                 'connection_list.html', 
                 {'connections': connections,
                  'connection_type_choices': connection_type_choices,
                 })

# Update
def connection_update(request, pk):
    connection = get_object_or_404(Connection, pk=pk)
    if request.method == 'POST':
        form = ConnectionForm(request.POST, instance=connection)
        if form.is_valid():
            form.save()
            return redirect('connection_list')
    else:
        form = ConnectionForm(instance=connection)
    return render(request, 'connection_update.html', {'form': form})

# Delete
def connection_delete(request, pk):
    connection = get_object_or_404(Connection, pk=pk)
    if request.method == 'POST':
        connection.delete(commit=True)
    return redirect('connection:connection_list')
    # return render(request, 'connection_delete.html', {'connection': connection})


if __name__ == '__main__':
    connection_list()