from django.db import models

class Book(models.Model):
    cover = models.ImageField(upload_to='covers/', null=True, blank=True, default='covers/default_cover.jpg')
    title = models.CharField(max_length=200, null=False, blank=False)  
    author = models.CharField(max_length=150, null=False, blank=False)  
    publication_date = models.DateField(null=True, blank=True)
    isbn = models.CharField(max_length=13, unique=True, null=True, blank=True)  
    pages = models.PositiveIntegerField(null=True, blank=True) 
    price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)  
    quantity = models.PositiveIntegerField(default=0) 
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['title']
        db_table = 'books'
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

class Member(models.Model):
    image = models.ImageField(upload_to='image/', null=True, blank=True)
    memberID = models.CharField(max_length=12, null=False, blank=False, unique=True)
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=150, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    class Meta:
        ordering = ['first_name', 'last_name']
        db_table = 'members'
        verbose_name = 'Member'
        verbose_name_plural = 'Members'



    