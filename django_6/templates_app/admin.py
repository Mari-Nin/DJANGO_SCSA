from django.contrib import admin

from .models import Post,Comment,Contact,Employee,Rates

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Contact)
admin.site.register(Employee)
admin.site.register(Rates)

