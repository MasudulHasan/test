from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
from django.db.models.signals import pre_save
from django.urls import reverse

from .utils import unique_slug_generator

User = get_user_model()
class Question(models.Model):
    # associations
    # user = models.ForeignKey(User,related_name='owner')

    # item stuff
    title               = models.TextField()
    option1             = models.TextField()
    option2             = models.TextField()
    option3             = models.TextField()
    option4             = models.TextField()
    explanation         = models.TextField()
    category            = models.CharField(max_length=1000)
    slug                = models.SlugField(null=True, blank=True)
    timestamp           = models.DateTimeField(auto_now_add=True)
    updated             = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    # def get_absolute_url(self): #get_absolute_url
    #     #return f"/restaurants/{self.slug}"
    #     return reverse('menus:detail', kwargs={'title': self.title})

    class Meta:
        ordering = ['-updated', '-timestamp']

def rl_pre_save_receiver(sender, instance, *args, **kwargs):
    # instance.category = instance.category.capitalize()
    # print("In rl_pre _save"+ str(instance.slug) + str(instance.activation_key) + str(instance.activated))

    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(rl_pre_save_receiver, sender=Question)

