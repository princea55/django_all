from django.db import models


# Create your models here.


class Musician(models.Model):
    # here "person's first name" is verbose name default is first parameter
    # like odoo but in relational field we have specify the
    # verbose_name = "the related poll" like this search the verbose_name keyword in this file
    first_name = models.CharField("person's first name", max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)

    class Meta:
        db_table = 'musician'
        unique_together = [['first_name', 'last_name']]

    def __str__(self):
        return self.first_name


class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE, verbose_name="the related poll")
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()

    class Meta:
        db_table = 'album'

    def __str__(self):
        return self.name


class PersonNormal(models.Model):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)


class Fruit(models.Model):
    name = models.CharField(max_length=100, primary_key=True)

    class Meta:
        # If you want to represent a model with the format app_label.object_name or
        # app_label.model_name you can use model._meta.label or model._meta.label_lower respectively.
        app_label = 'django_model'
        permissions = [('can_deliver_fruit', 'Can deliver fruits')]


# many to many relations through the third table
class Person(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through='Membership')

    def __str__(self):
        return self.name


class Membership(models.Model):
    name = models.CharField(max_length=128, null=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField(null=True, blank=True)
    invite_reason = models.CharField(max_length=64)

    class Meta:
        db_table = 'membership'
        # Latest by date_joined descending, name ascending.
        get_latest_by = ['name', '-date_joined']


class Employee(models.Model):
    name = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'employee'

    def __str__(self):
        return self.name


class Timesheet(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'timesheet'
        order_with_respect_to = 'employee'
        # this verbose_name and verbose_name_plural effect on admin panel
        verbose_name = "TimeSheet"
        # this verbose name remorev followed by s model name
        verbose_name_plural = "TimeSheet"

    def __str__(self):
        return self.employee.name


class Customer(models.Model):
    age = models.IntegerField()

    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(age__gte=18), name='age_gte_18'),
        ]
