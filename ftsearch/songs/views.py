import logging

from django.conf import settings
from django.db import connection

from rest_framework import generics

from main.utils import QueryLogger
from songs.models import Song
from songs.serializers import SongSerializer
from songs.filters import SongFilter


file_logger = logging.getLogger("file_logger")
console_logger = logging.getLogger("console_logger")
query_logger = QueryLogger()


class SongListView(generics.ListAPIView):
    queryset = Song.objects.all().order_by("-views")
    serializer_class = SongSerializer
    filterset_class = SongFilter


    def list(self, request, *args, **kwargs):
        # Retrive query params and store them in a single string for logging/analysis purposes
        query_params = self.request.query_params.keys()
        unpacked_query_params = [*query_params]
        query_params_text = "-".join(unpacked_query_params)

        # Capture queries executed while calling the view list method
        with connection.execute_wrapper(query_logger):
            list_result = super().list(request, *args, **kwargs)

        # Log captured queries. The last is used to account for multiple requests
        file_logger.info(f'{query_params_text},{query_logger.queries[-1]["duration"]}')
        console_logger.info(query_logger.queries[-1])

        return list_result
