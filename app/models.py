from django.db import models


class Category(models.Model):
    cat_name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.id)


class SubCategory(models.Model):
    subcat_name = models.CharField(max_length=200)
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)  
    def __str__(self):
        return str(self.id)      
    
class Product(models.Model):
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcat = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    discription = models.TextField(default='')
    image = models.ImageField( upload_to='productimg')
    def __str__(self):
        return str(self.id)
