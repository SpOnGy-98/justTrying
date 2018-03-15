from django.db import models
from django.core.validators import MaxLengthValidator
# Create your models here.
class registerEntery(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    dateOfBirth = models.DateTimeField(null='false')
    emailId = models.EmailField()
    phoneNo = models.PositiveIntegerField(validators=[MaxLengthValidator(10)])

    def __str__(self):
        return '<Name: {} {}, ID: {}>'.format(self.firstName, self.lastName, self.id)