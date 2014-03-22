from django.db import models
from authentication.models import UserProfile

class ApplianceClass(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __unicode__(self):
        return self.name

class ApplianceType(models.Model):
    appliance_class = models.ForeignKey(ApplianceClass)
    wattage = models.IntegerField()

    usage = models.ManyToManyField(UserProfile, through='ApplianceUsage')

    def __unicode__(self):
        return self.appliance_class.name + " " + str(self.wattage)

class ApplianceUsage(models.Model):
    appliance_type = models.ForeignKey(ApplianceType)
    user = models.ForeignKey(UserProfile)
    amount = models.IntegerField(default=1)
    def __unicode__(self):
        return self.user.__unicode__() + " " + self.appliance_type.appliance_class.name + " " + str(self.appliance_type.wattage) + " " + str(self.amount)