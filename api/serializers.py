from rest_framework import serializers
from filemetadata_app.models import FileUpload

class FileUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileUpload
        fields = ('datafile', 'created')
