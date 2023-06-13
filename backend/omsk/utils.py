from functools import wraps

from rest_framework.routers import DefaultRouter

class CustomRouter(DefaultRouter):
    def get_method_map(self, viewset, method_map):

        bound_methods = super().get_method_map(viewset, method_map)

        if 'patch' in bound_methods.keys():
            del bound_methods['patch']

        return bound_methods

def prevent_recursion(func):

    @wraps(func)
    def no_recursion(sender, instance=None, **kwargs):
        if not instance:
            return
        if hasattr(instance, '_dirty'):
            return

        func(sender, instance=instance, **kwargs)

        try:
            instance._dirty = True
            instance.save()
        finally:
            del instance._dirty

    return no_recursion