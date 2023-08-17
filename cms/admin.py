from django.contrib import admin
from .models import  Item, Action
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

class DefaultUserAdmin(UserAdmin):
    list_display = ('id', 'username', 'email', 'is_staff')  # gradeとstatusを削除して、他のデフォルトフィールドを追加
    list_display_links = ('id', 'username')
    search_fields = ('username', 'email')  # statusを削除して、emailを追加
    # gradeとstatusのlist_filterを削除します。

admin.site.unregister(User)  # 既に登録されている場合のUserモデルをアンレジスタ
admin.site.register(User, DefaultUserAdmin)  # デフォルトのUserモデルを新しいAdmin定義で再登録
class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'item_name', 'status', 'category', 'mount')
    list_display_links = ('id', 'item_name')
    search_fields = ('item_name', 'category', 'mount')
    list_filter = ('status', 'category', 'mount')

admin.site.register(Item, ItemAdmin)

class ActionAdmin(admin.ModelAdmin):
    list_display = ('user', 'item', 'borrow_timestamp', 'return_timestamp')  # 両方のタイムスタンプを含めて更新
    # date_hierarchy に timestamp を使用していた場合、それも更新します
    date_hierarchy = 'borrow_timestamp'  # 必要に応じて 'return_timestamp' に変更

admin.site.register(Action, ActionAdmin)
