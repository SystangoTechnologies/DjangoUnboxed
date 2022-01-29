from django.contrib import admin

from boilerplate_app.models import User, Projects


# Registering the models
admin.site.register(User)
admin.site.register(Projects)

