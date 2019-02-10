import hashlib
import time
import string

from django.utils.crypto import get_random_string


def generate_activation_code():
    allowed = string.ascii_uppercase + string.digits
    code = get_random_string(length=10, allowed_chars=allowed)
    return code


def generate_md5_hashcode(key_word):
    keyword = '{}-{}'.format(key_word, time.time())
    hashcode = hashlib.md5(keyword.encode('utf-8')).hexdigest()
    return hashcode
