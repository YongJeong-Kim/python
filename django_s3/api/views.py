import boto3
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from django_s3 import settings


class UploadView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(UploadView, self).dispatch(request, *args, **kwargs)

    s3_client = boto3.client(
        's3',
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY
    )

    def post(self, request, *args, **kwargs):
        files = request.FILES.getlist('file')
        for file in files:
            self.s3_client.upload_fileobj(
                file,
                settings.AWS_STORAGE_BUCKET_NAME,
                'media/' + file.name,
                ExtraArgs={
                    "ContentType": file.content_type
                }
            )

        file_urls = [
            f"{settings.AWS_S3_CUSTOM_DOMAIN}/media/{file.name}"
            for file in files
        ]

        return JsonResponse({'files': file_urls}, status=200)
