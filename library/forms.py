from django import forms
from .models import Book, Member, BookIssue

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        labels = {
            'title': 'Book Title',
            'author': 'Author Name',
            'cover': 'Cover Image',
            'pages': 'Number of Pages',
            'price': 'Price',
            'quantity': 'Quantity',
            'publication_date': 'Publication Date',
            'isbn': 'ISBN',
        }
        help_texts = {
            'cover': 'Upload an image for the book cover.',
        }
        widgets = {
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter book description',
                'rows': 4,
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter book title',
            }),
            'author': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter author name',
            }),
            'cover': forms.ClearableFileInput(attrs={
                'class': 'form-control',
            }),
            'pages': forms.NumberInput(attrs={
                'class':'form-control',
                'placeholder': 'Enter number of pages',
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter price',
            }),
            'quantity': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter quantity',
            }),
            'publication_date': forms.DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter publication date',
            }),
            'isbn': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter ISBN',
            }),
        }


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = '__all__'
        labels = {
            'memberID': 'Member ID',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email Address',
            'phone': 'Phone Number',
            'address': 'Address',
        }
        help_texts = {
            'email': 'Enter a valid email address.',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter first name',
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter last name',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter email address',
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter phone number',
            }),
            'address': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter full address',
                'rows': 4,
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control',
            }),
        }

class BorrowForm(forms.ModelForm):
    book = forms.ModelChoiceField(queryset=Book.objects.all(), empty_label='Select a book', widget=forms.Select(attrs={'class': 'form-control'}))
    member = forms.ModelChoiceField(queryset=Member.objects.all(), empty_label='Select a member', widget=forms.Select(attrs={'class': 'form-control'}))
    due_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Select due date'}))

    class Meta:
        model = BookIssue
        fields = ['book', 'member', 'due_date']
        labels = {
            'book': 'Book',
            'member': 'Member',
            'due_date': 'Due Date',
        }
        help_texts = {
            'due_date': 'Select the due date for the book issue.',
        }
