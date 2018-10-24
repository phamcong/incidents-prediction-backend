from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
# Many values can be set to a parameter
TYPE_CHOICES = (
    ("number", "Number"),
    ("string", "String"),
)
class Value(models.Model):
    type_value = models.CharField(max_length=10, choices=TYPE_CHOICES, default="STRING")
    value = models.CharField(max_length=100, blank=False, default='')

    class Meta:
        app_label = 'predictionmodel'
        managed = True
    
    def __str__(self):
        return self.type_value + ':' + self.value

    def save(self, *args, **kwargs):
        print('entered type of value: ', type(self.value))
        if (self.type_value == 'number') and (not str.isdigit(self.value)):
            raise ValidationError({'Entered value is not a number!!!'})
        else:
            super(Value, self).save(*args, **kwargs)




# Each model contains many parameters
class Parameter(models.Model):
    name = models.CharField(max_length=100, blank=False, default='')
    label =  models.CharField(max_length=100, blank=False, default='')
    values = models.ManyToManyField(Value)

    def __str__(self):
        return self.name
        
    class Meta:
        app_label = 'predictionmodel'


# Predict Model
class PredictModel(models.Model):
    name = models.CharField(max_length=100, blank=False, default='')
    label = models.CharField(max_length=100, blank=False, default='')
    function_name = models.CharField(max_length= 100, blank=True, default='')
    parameters = models.ManyToManyField(Parameter)

    def __str__(self):
        return self.name
    
    class Meta:
        app_label = 'predictionmodel'