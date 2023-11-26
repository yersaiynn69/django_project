from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
from django.utils import timezone

logged_events = {}


@receiver(user_logged_in)
def user_logged_in_handler(sender, request, user, **kwargs):
    if not hasattr(request, '_auth_logged_in'):
        log_event(user, 'Login')
        request._auth_logged_in = True

@receiver(user_logged_out)
def user_logged_out_handler(sender, request, user, **kwargs):
    if not hasattr(request, '_auth_logged_out'):
        log_event(user, 'Logout')
        request._auth_logged_out = True

def log_event(user, event_type):
    log_file_path = '/Users/ilassmagulov/PycharmProjects/myProject/text1.txt'

    with open(log_file_path, 'a') as log_file:
        timestamp = timezone.now().strftime('%Y-%m-%d %H:%M:%S')
        log_entry = f'{timestamp} - User: {user.username}, Event: {event_type}\n'
        log_file.write(log_entry)
        log_file.write('\n')
