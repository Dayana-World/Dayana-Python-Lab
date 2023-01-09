from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # CASECADE : If delete this field,all fields of this model deleted
    fathers_name = models.CharField(max_length=25)
    melicode = models.CharField(max_length=10)
    image = models.ImageField(upload_to='profiles/images', blank=True, null=True)

    def __str__(self):
        return self.user.username
        # verbose_name : name of model in admin
    class Meta:
        verbose_name = "حساب کاربری"
        verbose_name_plural = "حساب های کاربری"