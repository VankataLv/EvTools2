from django.db import models
from EvTools2.cars.validators import name_validator, nickname_validator, phone_number_validator, e_mail_validator
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime


def current_year():
    return datetime.now().year


class User(models.Model):
    first_name = models.CharField(
        max_length=50,
        validators=[name_validator]
    )
    last_name = models.CharField(
        max_length=50,
        validators=[name_validator]
    )
    nickname = models.CharField(
        max_length=30,
        validators=[nickname_validator],
        help_text='Enter a nickname between 3 and 30 characters. '
                  'Only letters, numbers, underscores, and hyphens are allowed.',
        unique=True,
    )
    phone_number = models.CharField(
        max_length=16,
        validators=[phone_number_validator],
        help_text='Enter a phone number. No dashes, slashes, or spaces are allowed. '
                  'Your number will be displayed only if you decide',
        unique=True,
    )
    email = models.EmailField(
        max_length=50,
        validators=[e_mail_validator],
        help_text='Enter a valid email address. '
                  'Your email will be displayed only if you decide',
        unique=True,
    )
    image_url = models.URLField(
        max_length=200,
        blank=True,
        null=True,
        default='staticfiles/images/icon_image.png'
    )
    created_on = models.DateField(auto_now_add=True)
    banned = models.BooleanField(default=False)

    def __str__(self):
        return self.nickname


class CarBrand(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class CarModel(models.Model):
    brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        unique_together = ('brand', 'name')

    def __str__(self):
        return self.name


class BaseEV(models.Model):
    class Meta:
        abstract = True

    LOCATION_CHOICES = [
        ('Sofia', 'Sofia'),
        ('Varna', 'Varna'),
        ('Burgas', 'Burgas'),
        ('Not in country', 'Not in country')
    ]
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cars')
    asking_price = models.IntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(1_000_000),
        ],
        help_text='Price in EUR. Only whole numbers',
    )
    battery_capacity = models.DecimalField(
        max_digits=5,
        decimal_places=2,
    )
    range = models.IntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(10_000),
        ],
        default=None,
        help_text='WLTP rating',
    )
    description = models.TextField(blank=True)
    location = models.CharField(
        max_length=30,
        choices=LOCATION_CHOICES,
    )

class EVCar(BaseEV):
    DRIVETRAIN_CHOICES = [
        ("FWD", "Front-wheel drive"),
        ("RWD", "Rear-wheel drive"),
        ("AWD", "All-wheel drive"),
    ]
    BODY_TYPE_CHOICES = [
        ("Sedan", "Sedan"),
        ("Hatch", "Hatchback"),
        ("Station wagon", "Station wagon"),
        ("Coupe", "Coupe"),
        ("SUV", "SUV"),
    ]
    COLOR_CHOICES = [
        ("White", "White"),
        ("Black", "Black"),
        ("Red", "Red"),
        ("Blue", "Blue"),
        ("Orange", "Orange"),
        ("Yellow", "Yellow"),
        ("Green", "Green"),
        ("Gray", "Gray"),
    ]
    DOORS_CHOICES = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
    ]

    brand = models.ForeignKey(CarBrand, on_delete=models.DO_NOTHING, related_name='cars')
    model = models.ForeignKey(CarModel, on_delete=models.DO_NOTHING, related_name='cars')
    trim_level = models.CharField(max_length=50, default='unknown')
    year = models.IntegerField(
        validators=[
            MinValueValidator(1900),
            MaxValueValidator(current_year),
        ],
        default=None,
    )
    mileage = models.IntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(1_000_000),
        ],
        default=0,
    )
    horsepower = models.IntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(1_000),
        ],
        default=0,
    )
    drivetrain = models.CharField(
        max_length=15,
        choices=DRIVETRAIN_CHOICES,
        default='unknown',
    )
    body_type = models.CharField(
        max_length=15,
        choices=BODY_TYPE_CHOICES,
        default='unknown',
    )
    color = models.CharField(
        max_length=15,
        choices=COLOR_CHOICES,
        default='unknown',
    )
    doors = models.IntegerField(
        choices=DOORS_CHOICES,
        default=4,
    )
    vin = models.CharField(
        max_length=17,
        help_text="Vehicle Identification Number",
        unique=True,
        null=True,
        blank=True,
    )

    def __str__(self):
        return f'{self.brand.name}: {self.model.name} - {self.year}'


class EVCarPhoto(models.Model):
    ev_car = models.ForeignKey(EVCar, on_delete=models.CASCADE, related_name='photos')
    photo = models.ImageField(
        upload_to='ev_photos/',  # Upload path for EV photos
        help_text='Upload a photo of the EV'
    )
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Photo of {self.ev_car}'

