from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',
                              upload_to='profile_pics', blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    # change image resolution size to fit (300, 300)
    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs) #these extra parameters are added due to extra default profile creation during creating user
        img = Image.open(self.image.path)
        if img.height > 300 or img.width >300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

def create_user(sender, **kwargs):
    if kwargs['created']:
        user_profile = Profile.objects.create(user = kwargs['instance'])
post_save.connect(create_user, sender=User)
