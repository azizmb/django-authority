from django.contrib.auth.models import User
from authority import get_check

class AuthorityPermissionBackend(object):
    supports_object_permissions = True
    supports_anonymous_user = False

    def authenticate(self, username, password):
        return None

    def has_perm(self, user_obj, perm, obj=None):
        if user_obj.is_authenticated():
            params = []
            if obj:
                params.append(obj)
            check = get_check(user_obj, perm)
            granted = False
            if check is not None:
                if check(*params):
                    return True            
            return False
