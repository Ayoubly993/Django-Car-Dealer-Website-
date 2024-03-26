from django.db import models

# Create your models here.


class Car(models.Model):
    BRAND_CHOICES = (
        ('Acura', 'Acura'),
        ('Audi', 'Audi'),
        ('Bentley', 'Bentley'),
        ('BMW', 'BMW'),
        ('Bugatti', 'Bugatti'),
    )
    COLOR_CHOICES = (
        ('', 'Colors'),
        ('Red', 'Red'),
        ('Blue', 'Blue'),
        ('Black', 'Black'),
        ('Yellow', 'Yellow'),
    )
    MILEAGE_CHOICES = (
        ('27', '27'),
        ('20', '20'),
        ('15', '15'),
        ('10', '10'),
    )
    ENGINE_CHOICES = (
        ('BS3', 'BS3'),
        ('BS4', 'BS4'),
        ('BS5', 'BS5'),
        ('BS6', 'BS6'),
    )
    TRANSMISSION_CHOICES = (

        ('Bluetooth', 'Bluetooth'),
        ('WiFi', 'WiFi'),
        
    )
    BODY_STYLE_CHOICES = (
        ('', 'Body Style'),
        ('Sedan', 'Sedan'),
        ('SUV', 'SUV'),
        ('Coupe', 'Coupe'),
        ('Pickup Truck', 'Pickup Truck'),
        # Add more body style options here if needed
    )
    CONDITION_CHOICES = (
        ('First Hand', 'First Hand'),
        ('Second Hand', 'Second Hand'),
        
    )
    AVAILABILITY_CHOICES = (
        ('Rent', 'Rent'),
        ('Buy', 'Buy'),
    )
    brand = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    year = models.IntegerField()
    horsepower = models.IntegerField(null=True)
    year = models.IntegerField()
    condition = models.CharField(max_length=30,choices=CONDITION_CHOICES)
    transmission = models.CharField(max_length=30,choices=TRANSMISSION_CHOICES)
    mileage = models.DecimalField(max_digits=10, decimal_places=2)
    engine = models.CharField(max_length=30,choices=ENGINE_CHOICES)
    colors = models.CharField(max_length=100,choices=COLOR_CHOICES)
    body_style = models.CharField(max_length=30,choices=BODY_STYLE_CHOICES)
    price = models.IntegerField(null=True)
    availability = models.CharField(max_length=4,choices=AVAILABILITY_CHOICES)
    pic = models.ImageField(upload_to='images/',blank=True,null=True)
    main_car = models.BooleanField(default=False)
    def __str__(self):
        return self.brand + " " + self.model + str(self.year)

class CarImage(models.Model):
    car = models.ForeignKey(Car,related_name='car_images',on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    def __str__(self):
        return "gigi"
