from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Upload
import ftplib

@receiver(post_save, sender=Upload)
def print_gif(sender, instance, **kwargs):
    session = ftplib.FTP('10.200.200.49', 'anonymous', 'password')
    #session.login()
    gif_path = 'media/'+str(instance.gif)
    gif_file = open(gif_path,'rb')
    cmd = 'STOR pub/'+str(instance.gif).split('/')[-1]
    session.storbinary(cmd, gif_file)
    gif_file.close()
    session.quit()
