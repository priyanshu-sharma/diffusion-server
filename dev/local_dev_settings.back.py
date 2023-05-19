DEBUG = True

ALLOWED_HOSTS = ["*"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': 'localhost',
        'PORT': 5432,
        'NAME': 'diffusion_api',
        'USER': 'priyanshu',
        'PASSWORD': 'anshU11528997',
    }
}

# CELERY_BROKER_URL = "amqp://rabbitmq:pwd@localhost:5672//"

REDIS_HOST = 'redis://redis_test:6379'

# CELERY_TASK_ALWAYS_EAGER = True

# CELERY_TASK_EAGER_PROPAGATES = True
