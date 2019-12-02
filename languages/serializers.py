from rest_framework import serializers
from .models import Language, Paradigm, Programmers

# for urls use HyperlinkedModelSerializer
# else ModelSerializer is fine


class LanguageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Language
        # can use url with or without id
        fields = ('id', 'url', 'name', 'paradigm')


class ParadigmSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Paradigm
        # can use url with or without id
        fields = ('id', 'url', 'name')


class ProgrammerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Programmers
        # can use url with or without id
        fields = ('id', 'url', 'name', 'languages')
