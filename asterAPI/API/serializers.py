from rest_framework import serializers
from .models import Cdr


class CdrSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cdr
        fields = [
            'calldate', 'clid', 'src', 'dst', 'duration', 'disposition', 'cnum', 'cnam'
        ]