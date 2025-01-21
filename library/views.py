from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Book, Member, BookIssue
from .forms import BookForm , MemberForm ,BorrowForm

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
    for book in books:
        if not book.cover:
            book.cover = 'default_cover.jpg'  # Replace with the path to your default cover image
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

def delete(request, pk):
    member_ = Member.objects.get(pk = pk)
    member_.delete()
    return redirect('members')

def add_book(request):
    form = BookForm()
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)  # Renamed to `book`
            if not book.cover:  # Adjust to your model's field name
                book.cover = 'default_image.jpg'  # Default image path
            book.save()
            return redirect('Books')
        
    return render(request, 'add_book.html', {'form': form})


def add_member(request):
    form = MemberForm()
    if request.method == 'POST':
        form = MemberForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('members')
    return render(request, 'add_member.html', {'form':form})

def edit(request, pk):
    member_ = Member.objects.get(pk = pk)
    form = MemberForm(instance=member_)
    if request.method == 'POST':
        form = MemberForm(request.POST, request.FILES, instance=member_)
        if form.is_valid():
            form.save()
            return redirect('member', pk=pk)
    return render(request, 'edit.html', {'form':form, 'member':member_})

def aboutbook(request, pk):
    aboutbook_ = Book.objects.get(pk = pk)
    return render(request, 'aboutbook.html', {'aboutbook':aboutbook_})

def edit_book(request, pk):
    book = Book.objects.get(pk=pk)
    form = BookForm(instance=book)  # Initialize with the book instance
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()  # Add parentheses to call the method
            return redirect('aboutbook', pk=pk)  # Redirect with the correct view name
        
    return render(request, 'edit_book.html', {'form': form, 'book': book})  # Correct template name


def delete_book(request, pk):
    book = Book.objects.get(pk = pk)
    book.delete()
    return redirect('Books')

# for showing detail of book
def borrowed_books(request):
    borrowed_books = BookIssue.objects.all()
    return render(request, 'borrowed_books.html', {'borrowed_books': borrowed_books})

def return_book(request, pk):
    book_issue = BookIssue.objects.get(pk=pk)
    book_issue.returned = True
    book_issue.save()
    book = book_issue.book
    book.No_of_copies_issued -= 1
    book.save()
    return redirect('borrowed_books')


from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from .forms import BorrowForm
from .models import Book

def add_borrow(request): 
    form = BorrowForm()
    if request.method == 'POST':
        form = BorrowForm(request.POST)
        if form.is_valid():
            # Get the book instance using its ID (from the form)
            book = form.cleaned_data['book']
            if book.quantity > book.No_of_copies_issued:
                book.No_of_copies_issued += 1
                book.save()
                form.save()
                return redirect('borrowed_books')
            else:
                messages.error(request, 'Not enough copies available to borrow.')
        else:
            messages.error(request, 'Invalid form submission.')

    return render(request, 'add_borrow.html', {'form': form})




    



        
