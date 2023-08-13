from django.contrib import admin
from .models import User, Item, Action

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'grade', 'status')
    list_display_links = ('id', 'username')
    search_fields = ('username', 'status')
    list_filter = ('grade', 'status')

admin.site.register(User, UserAdmin)

class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'item_name', 'status', 'category', 'mount')
    list_display_links = ('id', 'item_name')
    search_fields = ('item_name', 'category', 'mount')
    list_filter = ('status', 'category', 'mount')

admin.site.register(Item, ItemAdmin)

class ActionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'item', 'action_type', 'timestamp')
    list_display_links = ('id', 'user', 'item')
    search_fields = ('user__username', 'item__item_name', 'action_type')
    list_filter = ('action_type',)
    date_hierarchy = 'timestamp'

admin.site.register(Action, ActionAdmin)
