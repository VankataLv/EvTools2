from django.db import models
from EvTools2.cars.validators import name_validator, nickname_validator, phone_number_validator, e_mail_validator
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime

# Create your models here.


class User(models.Model):
    first_name = models.CharField(
        max_length=50,
        validators=[name_validator, ]
    )
    last_name = models.CharField(
        max_length=50,
        validators=[name_validator, ]
    )
    nickname = models.CharField(
        max_length=30,
        validators=[nickname_validator, ],
        help_text='Enter a nickname between 3 and 30 characters.'
                  'Only letters, numbers, underscores, and hyphens are allowed.',
        unique=True,
    )
    phone_number = models.CharField(
        max_length=16,
        validators=[phone_number_validator, ],
        help_text='Enter a phone number. No dashes, slashes or spaces are allowed. '
                  'Your number will be displayed only of you decide',
        unique=True,
    )
    email = models.EmailField(
        max_length=50,
        validators=[e_mail_validator, ],
        help_text='Enter a valid email address. '
                  'Your email will be displayed only of you decide',
        unique=True,
    )

    image_url = models.URLField(
        # For now the image of the user will be stored only as URL to local HD
        max_length=200,
        blank=True, null=True
    )

    created_on = models.DateField(auto_now_add=True, )
    banned = models.BooleanField(default=False, )

    # In the future add roles FK

    def __str__(self):
        return self.nickname


class CarBrand(models.Model):
    name = models.CharField(max_length=50,)

    def __str__(self):
        return self.name


class CarModel(models.Model):
    brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE,)
    name = models.CharField(max_length=50,)

    def __str__(self):
        return self.name


class EVCar(models.Model):
    # for now, it will be a normal class, later will be converted to base class
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

    # @classmethod
    # def filter_choices(cls):
    #     return [(model_obj.id, model_obj.name) for model_obj in CarModel.objects.filter('brand')]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE)
    model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    year = models.IntegerField(
        validators=[
            MinValueValidator(1900),
            MaxValueValidator(int(datetime.now().year)),
        ],
        default=None,
    )
    asking_price = models.IntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(1_000_000),
        ],
        help_text='Price in EUR. Only whole numbers',
    )
    mileage = models.IntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(1_000_000),
        ],
        default=0,
    )
    battery_capacity = models.DecimalField(
        max_digits=5,
        decimal_places=2,
    )
    horsepower = models.IntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(1_000),
        ],
        default=0,
    )

    range = models.IntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(10_000),
        ],
        default=None,
        help_text='WLTP rating',
    )

    drivetrain = models.CharField(
        max_length=15,
        choices=DRIVETRAIN_CHOICES,
        default='unknown'
    )

    body_type = models.CharField(
        max_length=15,
        choices=BODY_TYPE_CHOICES,
        default='unknown'
    )

    color = models.CharField(
        max_length=15,
        choices=COLOR_CHOICES,
        default='unknown'
    )

    description = models.TextField()

    doors = models.IntegerField(
        choices=DOORS_CHOICES,
        default=4
    )
    vin = models.CharField(
        max_length=50,
        default='unknown'
    )

    def __str__(self):
        return f'{self.brand.name}: {self.model.name} - {self.year}'
