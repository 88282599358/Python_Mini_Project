from django.db import models

# Create your models here.
class Organizer(models.Model):
    org_name = models.CharField(max_length=100,null=False)
    event_name = models.CharField(max_length=100,null=False)
    event_date = models.DateField(max_length=100,null=False)
    event_fee = models.IntegerField(default=0, null=False)
    sports_name = models.CharField(max_length=100,null=False)
    age = models.IntegerField(default=0, null=False)
    phone_number = models.IntegerField(default=0, null=False)
    event_location = models.CharField(max_length=100, null=False)

    def __str__(self):
        # return "%s %s %s %s %s %s %s %s " % (self.org_name, self.event_name, self.event_date, self.event_fee,self.sports_name,self.age,self.phone_number,self.event_location)
        return "%s | %s" % (
        self.org_name,self.event_name)


class Athlete(models.Model):
    name = models.CharField(max_length=100, null=False)
    contact_number = models.IntegerField(default=0, null=False)
    email = models.EmailField(max_length = 254)
    def __str__(self):
        # return "%s %s %s " % (self.name, self.contact_number, self.email)
        return "%s" % (self.name)

