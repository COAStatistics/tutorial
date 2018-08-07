# Documentation https://docs.djangoproject.com/en/2.0/topics/db/models/

from django.db import models

#from django.db.models import Model

# Create your models here.

# Introduction some Fields

    # CharField
    # TextField
    # EmailField

    # IntegerField
    # BigIntegerField
    # PositiveIntegerField
    # PositiveSmallIntegerField

    # FloatField
    # DecimalField

    # DateField
    # DateTimeField

    # BooleanField
    # NullBooleanField

class ExampleText(models.Model):
    # CharField must define a 'max_length' attribute
    # TextField is a textarea. You can specify a max_length attribute, it will be reflected in the Textarea widget of the auto-generated form field. However it is not enforced at the model or database level. Use a CharField for that.
    # EmailField is a CharField that checks that the value is valid email address. default max_length=254
    name = models.CharField(max_length=20, null=False, blank=False)
    subscription = models.TextField()
    email = models.EmailField()

    # Return a string representation display in the admin.
    # __str__ for python3
    # __unicode__ for python2
    def __str__(self):
        return self.name


class ExampleNumber(models.Model):
    # IntegerField values from -2147483648 to 2147483647
    # BigIntegerField is a 64-bit integer, numbers from -9223372036854775808 to 9223372036854775807
    num1 = models.IntegerField()
    num2 = models.BigIntegerField()
    # PositiveIntegerField values from 0 to 2147483647
    # PositiveSmallIntegerField values from 0 to 32767
    num3 = models.PositiveIntegerField()
    num4 = models.PositiveSmallIntegerField()

    # DecimalField has two required arguments, max_digits, decimal_places
    # 12345.678 has 8 digits, max_digits=8, decimal_places=3
    # 123.45678 has 8 digits, max_digits=8, decimal_places=5
    # What different between FloatField and DecimalField ?
    # https://docs.djangoproject.com/en/2.0/ref/models/fields/#floatfield-vs-decimalfield
    # https://stackoverflow.com/questions/2569015/django-floatfield-or-decimalfield-for-currency
    price = models.FloatField()
    money = models.DecimalField(max_digits=10, decimal_places=3)

    def __str__(self):
        return "[%d] [%d] [%d] [%d] [%f] [%f]" % (self.num1, self.num2, self.num3, self.num4, self.price, self.money)

import datetime
from django.utils import timezone
class ExampleDate(models.Model):
    # DateField is represented in Python by a datetime.date instance.
    # DateTimeField is represented in Python by a datetime.datetime instance.
    # auto_now=False and auto_now_add=False are default options to DateField and DateTimeFIeld.
    # If auto_now=True, the date or datetime automatically set when Object created, only changed when calling Object.save() everytime, useful for "last-modified"
    # If auto_now_add=True, the date or datetime automatically set whe Object created, useful for "creation for timestamps". You can override it after the Object created, but set value will be ignore when creating Object.
    date1 = models.DateField(auto_now=True)
    date2 = models.DateField(auto_now_add=True)
    date3 = models.DateField()
    time1 = models.DateTimeField(auto_now=datetime.datetime.now(timezone.utc))
    time2 = models.DateTimeField(auto_now_add=True)
    time3 = models.DateTimeField()

    def __str__(self):
        return "date1=[{}] date2=[{}] date3=[{}] time1=[{}] time2=[{}] time3=[{}]".format(self.date1, self.date2, self.date3, self.time1, self.time2, self.time3)

class ExampleBoolean(models.Model):
    # BooleanField is a True/False CheckBoxInput, default is False. If you need to accept null values(null=True) then use NullBooleanField instead.
    # NullBooleanField is a like BooleanField but accept null. Select with options "UnKnown", "Yes", "No", default is Unknown.
    check1 = models.BooleanField()
    check2 = models.NullBooleanField()

    # def __str__(self):
    #     return self.name


# Their are some optional arguments avaliable to all field types.

    # null option
    # blank option
    # choices option
    # default option
    # help_text option
    # primary_key option
    # unique option
    # verbose_name option

class ExampleOption(models.Model):
    # primary_key option
    # Django will automatically add an id colum as primarykey, so you don't need to set it.
    # primary_key=True implies null=False and unique=True. Only one primary key is allowed on an object.
    # primary key is read-only.
#    id = models.PositiveIntegerField(primary_key=True)

    # null option
    # blank option
    # For all Field null=False and blank=False are default, if not set
    # https://stackoverflow.com/questions/8609192/differentiate-null-true-blank-true-in-django
    name = models.CharField(max_length=20, null=False, blank=True)

    # unique option
    # This option invalid on ManyToManyField and OneToOneField
    code = models.PositiveIntegerField(unique=True)

    # verbose_name option
    # A human-readable name for the field. If the verbose name isn’t given, Django will automatically create it using the field’s attribute name, converting underscores to spaces.
    nick = models.CharField(max_length=5, verbose_name="NICK NAME")

    def __str__(self):
        return self.code

class ExampleChoices(models.Model):

    # choices option
    FRESHMAN = 'FR'
    SOPHOMORE = 'SO'
    JUNIOR = 'JR'
    SENIOR = 'SR'
    YEAR_IN_SCHOOL_CHOICES = (
        (FRESHMAN, 'Freshman'),
        (SOPHOMORE, 'Sophomore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
    )
    year_in_school = models.CharField(
        max_length=2,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default=FRESHMAN,
    )

    ONE = '1'
    TWO = '2'
    THREE = '3'
    GRADE_IN_SCHOOL_CHOICES = (
        (ONE, 'One1'),
        (TWO, 'Two2'),
        (THREE, 'Three3'),
    )

    grade_in_school = models.CharField(
        max_length=1,
        choices=GRADE_IN_SCHOOL_CHOICES,
    )

    def __str__(self):
        return self.year_in_school


class ExampleHelp(models.Model):
    uid = models.CharField(max_length=10, primary_key=True, help_text='primary key')

    def __str__(self):
        return self.uid


# Introduction ForeignKey
# Many-to-One relationship. Requires two arguments: the class to which the model is related and the on_delete option.
# bar = models.ForeignKey(to_whitch_model, on_delete=models.CASCADE)
# on_delete options
# models.CASCADE, models.PROTECT, models.SET_NULL, models.SET_DEFAULT, models.SET(), models.DO_NOTHING()
# What different between ForeignKey with unique and OneToOneField ?
# https://stackoverflow.com/questions/5870537/whats-the-difference-between-django-onetoonefield-and-foreignkey
class ExampleForeignKeyOneCity(models.Model):
    name = models.CharField(max_length=5)

    def __str__(self):
        return "{} {}".format(self.id, self.name)

class ExampleForeignKeyManyCitizen(models.Model):
    related_city = models.ForeignKey(ExampleForeignKeyOneCity, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    age = models.PositiveIntegerField()
    MAN = "M"
    FEMALE = "F"
    SEX_CHOICES = (
        (MAN, "Man"),
        (FEMALE, "Female"),
    )
    sex = models.CharField(max_length=5, choices=SEX_CHOICES)

    def __str__(self):
        return "{} {} {}".format(self.id, self.related_city.name, self.name)


class CitizenItem(models.Model):
    related_citizen = models.ForeignKey(ExampleForeignKeyManyCitizen, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    amount = models.PositiveIntegerField()

    def __str__(self):
        return "{} {} {}".format(self.id, self.name, self.amount)


# Introduction OneToOneField


# Introduction ManyToManyField
