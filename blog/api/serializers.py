from rest_framework import serializers
from ..models import Blog

class BlogSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="blog-api:detail", 
        lookup_field = "pk"
    )

    username = serializers.SerializerMethodField()

    def get_username(self, obj):
        return str(obj.user.username)

    class Meta:
        model = Blog
        fields = ["url", "username", "title", "description", "banner", "created_date", "is_deleted"]