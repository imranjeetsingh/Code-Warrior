import datetime
import os


# AWS credentials
try:
    AWS_GROUP_NAME = os.environ.get('AWS_GROUP_NAME')
    AWS_USER_NAME = os.environ.get('AWS_USER_NAME')
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
except:
    from judge import credentials

    AWS_GROUP_NAME = credentials.AWS_GROUP_NAME
    AWS_USER_NAME = credentials.AWS_USER_NAME
    AWS_ACCESS_KEY_ID = credentials.AWS_ACCESS_KEY_ID
    AWS_SECRET_ACCESS_KEY = credentials.AWS_SECRET_ACCESS_KEY
    AWS_STORAGE_BUCKET_NAME = credentials.AWS_STORAGE_BUCKET_NAME


AWS_FILE_EXPIRE = 200
AWS_PRELOAD_METADATA = True
AWS_QUERYSTRING_AUTH = False

DEFAULT_FILE_STORAGE = 'judge.aws.utils.MediaRootS3BotoStorage'
STATICFILES_STORAGE = 'judge.aws.utils.StaticRootS3BotoStorage'
S3DIRECT_REGION = 'ap-southeast-1'
S3_URL = '//%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
MEDIA_URL = '//%s.s3.amazonaws.com/media/' % AWS_STORAGE_BUCKET_NAME
MEDIA_ROOT = MEDIA_URL
STATIC_URL = S3_URL + 'static/'
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

two_months = datetime.timedelta(days=61)
date_two_months_later = datetime.date.today() + two_months
expires = date_two_months_later.strftime("%A, %d %B %Y 20:00:00 GMT")

AWS_HEADERS = { 
    'Expires': expires,
    'Cache-Control': 'max-age=%d' % (int(two_months.total_seconds()), ),
}
