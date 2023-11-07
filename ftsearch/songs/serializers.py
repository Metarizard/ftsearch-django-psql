from rest_framework import serializers

from songs.models import Song


class SongSerializer(serializers.ModelSerializer):

    class Meta:
        model = Song
        fields = (
            "id",
            "title",
            "tag",
            "artist",
            "year",
            "views",
            "features",
            "lyrics",
            "language",
        )
        read_only_fields = (
            "title",
            "tag",
            "artist",
            "year",
            "views",
            "features",
            "lyrics",
            "language",
        )
