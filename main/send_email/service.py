from django.core.mail import send_mail



def send(user_email):
    send_mail(
        'Hello!',
        'Subscribed to the newsletter',
        'myemail@gmail.com'
    [user_email],
    fail_silently=False,
    )

