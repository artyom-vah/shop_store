from django.contrib import admin
from users.models import User  # импортируем нашу модель
from products.admin import BasketAdminInLine


#admin.site.register(User)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    inlines = (BasketAdminInLine,)

