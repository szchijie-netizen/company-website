from rest_framework import serializers

from .models import Contact


class ContactSerializer(serializers.ModelSerializer):
    inquiry_type_display = serializers.CharField(source="get_inquiry_type_display", read_only=True)

    class Meta:
        model = Contact
        fields = [
            "id",
            "name",
            "company",
            "email",
            "phone",
            "inquiry_type",
            "inquiry_type_display",
            "message",
            "created_at",
        ]
        read_only_fields = ["id", "created_at"]

    def validate_phone(self, value):
        """phone 或 email 至少提供一个联系方式"""
        return value  # 联合校验放在全局 validate 中更灵活

    def validate(self, attrs):
        if not attrs.get("email") and not attrs.get("phone"):
            raise serializers.ValidationError("电子邮件和电话至少填写一项")
        return attrs
