# from django.contrib import admin
# from apps.telegrambot import models
#
#
# @admin.register(models.TelegramUser)
# class TelegramUserAdmin(admin.ModelAdmin):
#     list_display = ("id", "telegram_id", "user")
#     search_fields = ("telegram_id", "user__first_name")
#
#     def has_add_permission(self, request) -> bool:
#         return False
#
#     def has_change_permission(self, request, obj=None) -> bool:
#         return False
#
#     def has_delete_permission(self, request, obj=None) -> bool:
#         return False
