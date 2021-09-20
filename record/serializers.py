from rest_framework import serializers
from .models import Record

class RecordSerializer(serializers.ModelSerializer):
  class Meta:
    fields = ('id', 'title', 'artist', 'genre')
    model = Record