from rest_framework import serializers
from sample_app.models.memo import Memo

class MemoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Memo
        fields = '__all__'
