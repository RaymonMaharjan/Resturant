from django.db import models

# Create your models here.

class ItemList(models.Model):
    Category_name = models.CharField(max_length=50)


    def __str__(self):
        return self.Category_name
    

class Items(models.Model):
    Item_name = models.CharField(max_length=50)
    Description = models.TextField(blank=False)
    Price = models.IntegerField()
    Category = models.ForeignKey(ItemList,related_name='name',on_delete=models.CASCADE)
    Image = models.ImageField(upload_to='items/')

    def __str__(self):
        return self.Item_name
    
class Offer(models.Model):
    Item_name = models.CharField(max_length=50)
    offer_per = models.IntegerField()
    Image = models.ImageField(upload_to='offer/',blank=True)

    def __str__(self):
        return self.Item_name

class AboutUs(models.Model):
    Description = models.TextField(blank=False)

class Feedback(models.Model):
    User_name = models.TextField(blank=False)
    Description = models.TextField(blank=False)
    Rating = models.IntegerField()
    Image = models.ImageField(upload_to='feedback/', blank=True)

    def __str__(self):
        return self.User_name
    


class BookTable(models.Model):
    Name = models.CharField(max_length=15)
    Phone_number = models.IntegerField()
    Email = models.EmailField()
    Total_person = models.IntegerField()
    Booking_date = models.DateField()

    def __str__(self):
        return self.Name
    
