from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser
from .serializers import FileUploadSerializer
from filemetadata_app.models import FileUpload
from django.http import JsonResponse
from django.conf import settings
import os

# Create your views here.
class FileUploadView(APIView):
    parser_classes = (FileUploadParser,)
    serializer_class = FileUploadSerializer

    def post(self, request, filename, format=None):
        file_obj = request.data['file']

        file_to_save = FileUpload(datafile=file_obj)
        file_to_save.save()
        """
        # saving file chunk by chunk
        file_path = settings.MEDIA_ROOT
        full_filename = os.path.join(file_path, 'files/', file_obj.name)
        CHUNK = 16 * 1024
        with open(full_filename, 'wb') as f:
            while True:
                chunk = file_obj.read(CHUNK)
                if not chunk:
                    break
                f.write(chunk)
        """

        return JsonResponse({'file_size': str(file_obj.size)})
