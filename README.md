# API: File Metadata Microservice #

## Requirements
- Django==1.10
- djangorestframework==3.6.4

## Install
In the terminal
```

$ cd file_metadata_microservice
$ pip install -r requriements.txt
$ python manage.py migrate
$ python manage.py createsuperuser
$ python manage.py runserver

```


## User stories:

1. I can submit a FormData object that includes a file upload.
2. When I submit something, I will receive the file size in bytes within the JSON response.



## Example usage:
Run the server and upload a file.

Have fun... :)