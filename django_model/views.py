from django.http import HttpResponse
from django.shortcuts import render

from django_model.models import Person, Fruit, PersonNormal, Membership, Group, Employee, Timesheet


def django_model_choice(request):
    p = PersonNormal(name="Fred Flintstone", shirt_size="L")
    p.save()
    print("value that print that store in database", p.shirt_size)
    # here shirt_size is dynamically determined for getting display value
    # technically it's creates dynamic method to get display value
    print("by using this method we can access the display value ", p.get_shirt_size_display())
    return HttpResponse("Django model choice attribute")


def django_model_primary_key(request):
    # here name field is primary key
    fruit = Fruit.objects.create(name='Apple')
    # The primary key field is read-only. If you change the value of the primary key on an
    # existing object and then save it, a new object will be created alongside the old one. For example:
    fruit.name = 'Pear'
    fruit.save()
    name = Fruit.objects.values_list('name', flat=True)
    fruit_object = Fruit.objects.values_list('name', flat=True)
    # flat=True give list of fruit name
    print(name)
    # flat=False give list of fruit object
    print(fruit_object)
    return HttpResponse("Django model primary key")


def django_model_many_to_many(request):
    ringo = Person.objects.create(name="Ringo Starr")
    paul = Person.objects.create(name="Paul McCartney")
    john = Person.objects.create(name="john McCartney")
    beatles = Group.objects.create(name="The Beatles")
    m1 = Membership(person=ringo, group=beatles,
                    invite_reason="Needed a new drummer.")
    m1.save()
    print(beatles.members.all())

    print(ringo.group_set.all())

    m2 = Membership.objects.create(person=paul, group=beatles,
                                   invite_reason="Wanted to form a band.")
    print(beatles.members.all())
    print(ringo.membership_set)
    beatles.members.add(john, through_defaults={'invite_reason': 'Wanted to form a band.'})
    print(beatles.members.all())
    beatles.members.create(name="George Harrison", through_defaults={'invite_reason': 'Wanted to form a band.'})
    print(beatles.members.all())
    beatles.members.set([john, paul, ringo], through_defaults={'invite_reason': 'Wanted to form a band.'})
    print(beatles.members.all())
    beatles.members.remove(ringo)
    print(beatles.members.all())
    # beatles.members.clear()
    # print(beatles.members.all())
    print(Group.objects.filter(members__name__startswith='Paul'))
    Person.objects.filter(group__name='The Beatles')
    ringos_membership = Membership.objects.get(group=beatles, person=ringo)
    return HttpResponse("Django model many to many")


def order_with_respect_to(request):
    employee = Employee.objects.get(id=1)
    employee.get_timesheet_order()
    return HttpResponse("Django model many to many")