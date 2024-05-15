#./signals.py

from allauth.account.signals import user_signed_up
from django.dispatch import receiver
from django.contrib.auth.models import Group

@receiver(user_signed_up)
def add_user_to_group(sender, request, user, **kwargs):
    # Replace 'default_group' with the name of the group you want to add users to
    default_group, created = Group.objects.get_or_create(name='client')
    user.groups.add(default_group)
