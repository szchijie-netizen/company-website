from django.contrib import admin

# Register your models here.

from django.contrib import admin
from django.utils.html import format_html

from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ["name", "company", "email", "phone", "inquiry_type", "message_preview", "created_at"]
    list_filter = ["inquiry_type", "created_at"]
    search_fields = ["name", "company", "email", "phone", "message"]
    readonly_fields = ["created_at", "message_preview"]
    fieldsets = [
        ("联系信息", {"fields": ["name", "company", "email", "phone"]}),
        ("咨询内容", {"fields": ["inquiry_type", "message"]}),
        ("系统信息", {"fields": ["created_at"]}),
    ]

    @admin.display(description="留言内容")
    def message_preview(self, obj):
        text = obj.message or ""
        preview = text[:60] + ("..." if len(text) > 60 else "")
        return format_html(
            '<span title="{}">{}</span>',
            text.replace('"', "&quot;"),
            preview,
        )
