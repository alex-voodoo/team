import base64

from team.settings import USE_BASIC_AUTH


def get_user(request):
    if USE_BASIC_AUTH:
        return base64.b64decode(request.META['HTTP_AUTHORIZATION'].split()[1]).decode('utf8').split(':')[0]
    return 'average_joe'
