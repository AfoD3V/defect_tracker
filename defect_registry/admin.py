from django.contrib import admin
from .models import Project, Domain, Defect, Comment, Attachment, UserProject

# Register your models here.
admin.site.register(Project)
admin.site.register(Domain)
admin.site.register(Defect)
admin.site.register(Comment)
admin.site.register(Attachment)
admin.site.register(UserProject)
