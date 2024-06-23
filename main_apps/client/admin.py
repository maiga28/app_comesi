from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Client, ClientOrder

class ClientOrderInline(admin.TabularInline):
    model = ClientOrder
    extra = 1

class ClientAdmin(UserAdmin):
    inlines = (ClientOrderInline,)
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('photo', 'adresse', 'numero_telephone', 'bio', 'date_of_birth', 'phone_number', 'location', 'cover_picture')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('profile_picture', 'adresse', 'numero_telephone', 'bio', 'date_of_birth', 'phone_number', 'location', 'cover_picture')}),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'date_of_birth', 'numero_telephone')
    search_fields = ('username', 'email', 'first_name', 'last_name', 'numero_telephone')
    ordering = ('username',)

admin.site.register(Client, ClientAdmin)
admin.site.register(ClientOrder)

