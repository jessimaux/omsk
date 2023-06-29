from django.db import transaction

from .models import *


class LogService:
    @transaction.atomic
    def create(self, obj_type: str, obj_id: int, action: str, created_by_id: int) -> Log:
        return Log.objects.create(object_type=obj_type,
                                  object_id=obj_id,
                                  action=action,
                                  created_by_id=created_by_id)
