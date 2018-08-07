from django.db import models

# Create your models here.

class City(models.Model):
    name = models.CharField(max_length=20)
    area = models.PositiveIntegerField()

    def __str__(self):
        return "{} {} {}".format(self.id, self.name, self.area)


class Citizen(models.Model):
    name = models.CharField(max_length=20)
    age = models.PositiveIntegerField()
    related_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='ccc')

    def __str__(self):
        return "id={} {}".format(self.id, self.name)


class Crop(models.Model):
    name = models.CharField(max_length=20)
#    related_crop = models.ForeignKey("Crop", on_delete=models.CASCADE, null=True)
    related_crop = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return "{} {} [{}]".format(self.id, self.name, self.related_crop)



class Month(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Survey(models.Model):
    name = models.CharField(max_length=20)
    related_month = models.ManyToManyField(Month)

    def __str__(self):
        return "{} {} [{}]".format(self.id, self.name, self.related_month.all().values_list('name', flat=True))


class Player(models.Model):
    pid = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return "{} {}".format(self.id, self.pid)


class Profile(models.Model):
    name = models.CharField(max_length=20)
    age = models.PositiveIntegerField()
    related_player = models.OneToOneField(Player, on_delete=models.CASCADE)

    def __str__(self):
        return "{} {} {} [{}]".format(self.id, self.name, self.age, self.related_player)


class Item(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class ItemDetail(models.Model):
    atk = models.IntegerField()
    defend = models.IntegerField()
    description = models.CharField(max_length=255)
    related_item = models.ForeignKey(Item, on_delete=models.CASCADE, unique=True)

    def __str__(self):
        return self.related_item.name
