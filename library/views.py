from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Book, Member

# Home View
def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate 
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in.")
            return redirect('home')  # Replace 'home' with the name of the view you'd like to redirect to.
        else:
            messages.error(request, "There was an error logging in. Please try again.")
            return render(request, 'home.html', {})  # Render the form again with the error message.
    
    return render(request, 'home.html', {})

def logout_request(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect("home")

def Books(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'Books.html', context)

def members(request):
    members= Member.objects.all()
    context = {
        'members': members
    }
    return render(request, 'members.html', context)
    

def member(request, pk):
    member_ = Member.objects.get(pk = pk)
    return render(request, 'member.html', {'member' : member_})

