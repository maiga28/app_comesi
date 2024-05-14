from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.shortcuts import redirect

@receiver(user_logged_in)
def user_logged_in_callback(sender, request, user, **kwargs):
    if user.groups.filter(name='client').exists():
        return redirect('client:client')
    elif user.groups.filter(name='admin').exists():
        return redirect('gestion:gestion')
    elif user.groups.filter(name='camionnaire').exists():
        return redirect('camionnaire:camionnaire')
    else:
        # Redirection par défaut pour les utilisateurs sans groupe spécifié
        return redirect('client:client')  # Vous devez définir cette vue

##############################################################################
import six
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import user_passes_test

def group_required(group, login_url=None, raise_exception=False):
    def check_perms(user):
        if isinstance(group, six.string_types):
            groups = (group, )
        else:
            groups = group
        # First check if the user has the permission (even anon users)

        if user.groups.filter(name__in=groups).exists():
            return True
        # In case the 403 handler should be called raise the exception
        if raise_exception:
            raise PermissionDenied
        # As the last resort, show the login form
        return False
    return user_passes_test(check_perms, login_url=login_url)
# ############################################################################