from django.contrib import admin
# for password field read - only
from django.contrib.auth.admin import UserAdmin
from . models import Account

# Register your models here.

class AccountAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'username', 'last_login', 'date_joined', 'is_active')
    list_display_links = ('email','first_name', 'last_name')
    readonly_fields = ('last_login', 'date_joined')
    ordering = ('-date_joined',)

    # Solution to error - <class 'accounts.admin.AccountAdmin'>: (admin.E116) The value of 'list_filter[3]' refers to 'groups', which does not refer to a Field.
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Account, AccountAdmin)
