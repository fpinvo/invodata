from django.contrib.auth.models import Permission
from django.db import models


# Permission.objects.filter()
# Permission.objects.all()[12].content_type.permission_set.all()
# Permission.objects.all().exclude(content_type__model__in=['session','logentry','group','permission','contenttype']).values('content_type__model')

