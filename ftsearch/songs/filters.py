from django.db.models import Q

from django_filters import rest_framework as filters

from django.contrib.postgres.search import SearchQuery

from songs.models import Song


class SongFilter(filters.FilterSet):
    # Filters using icontains

    ititle = filters.CharFilter(field_name="title", lookup_expr="icontains")
    iartist = filters.CharFilter(field_name="artist", lookup_expr="icontains")
    ilyrics = filters.CharFilter(field_name="title", lookup_expr="icontains")

    # Multifield filters

    search = filters.CharFilter(method="song_search_filter")
    ftsearch = filters.CharFilter(method="song_ftsearch_filter")

    class Meta:
        model = Song
        fields = (
            "title",
            "artist",
            "lyrics",
        )

    def song_search_filter(self, queryset, name, value):
        words = value.split() # Default separator is a whitespace " "

        search_filter = Q()

        # First approach to manual search
        for word in words:
            search_filter &= Q(
                title__icontains=word
            ) | Q(
                artist__icontains=word
            ) | Q(
                lyrics__icontains=word
            )
        
        return queryset.filter(search_filter)


    def song_ftsearch_filter(self, queryset, name, value):
        # Full text search using SearchVector
        config = self.request.query_params.get("language", "english")
        return queryset.filter(search_vector=SearchQuery(value, config=config, search_type="websearch"))
