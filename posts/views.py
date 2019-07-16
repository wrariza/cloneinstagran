"""Posts views."""

# Django
from django.http import HttpResponse

# Utilities
from datetime import datetime
from random import randint


posts = [
    {
        'name': 'All post magic',
        'user': 'william',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H-%M hrs'),
        'picture': 'https://picsum.photos/id/{pid}/200/300'.format(pid=randint(1, 100))

    },
    {
        'name': 'All post magic',
        'user': 'william',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H-%M hrs'),
        'picture': 'https://picsum.photos/id/{pid}/200/300'.format(pid=randint(1, 100))

    },
    {
        'name': 'All post magic',
        'user': 'william',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H-%M hrs'),
        'picture': 'https://picsum.photos/id/{pid}/200/300'.format(pid=randint(1, 100))

    },

]


def list_posts(request):
    content = []
    for post in posts:
        content.append("""
                    <p><strong>{name}</strong></p>
                    <p><small>{user} - <i>{timestamp}</i></small></p>
                    <figure><img src="{picture}"/></figure>
                """.format(**post))
    return HttpResponse('<br>'.join(content))
