from rest_framework import viewsets, filters
from sample_app.models.memo import Memo
from sample_app.serializers.memo_serializer import MemoSerializer

class MemoViewSet(viewsets.ModelViewSet):
    queryset = Memo.objects.all()
    serializer_class = MemoSerializer