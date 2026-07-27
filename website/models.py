from django.db import models

# Create your models here.

from django.db import models


class Contact(models.Model):
    """客户留言联系表"""

    INQUIRY_CHOICES = [
        ("sourcing", "商品采购"),
        ("oem", "OEM / ODM"),
        ("logistics", "物流与运输"),
        ("wholesale", "批发 / 分销"),
        ("other", "其他"),
    ]

    name = models.CharField(verbose_name="姓名", max_length=100)
    company = models.CharField(verbose_name="公司", max_length=200, blank=True, default="")
    email = models.EmailField(verbose_name="电子邮件", max_length=254)
    phone = models.CharField(verbose_name="电话 / WhatsApp", max_length=50, blank=True, default="")
    inquiry_type = models.CharField(
        verbose_name="查询类型", max_length=50, choices=INQUIRY_CHOICES, default="general"
    )
    message = models.TextField(verbose_name="留言")
    created_at = models.DateTimeField(verbose_name="提交时间", auto_now_add=True)

    class Meta:
        verbose_name = "客户留言"
        verbose_name_plural = verbose_name
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} — {self.get_inquiry_type_display()}"
