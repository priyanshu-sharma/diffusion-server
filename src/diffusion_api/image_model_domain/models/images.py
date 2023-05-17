import uuid
from django.db import models
from extensions.models import AutoTimestampedModel, UserTrackingModel
from image_model_domain.enums import ImageOwnerType


class Images(AutoTimestampedModel, UserTrackingModel):
    """
    Images model.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    owner = models.TextField(choices=ImageOwnerType.choices(), default=ImageOwnerType.LEONARDO_AI)
    path = models.TextField(null=False)
    meta = models.JSONField(default=dict)
    description = models.TextField(null=True)

    class Meta:
        db_table = 'da_images'
        app_label = 'image_model_domain'
        unique_together = [('name', 'owner')]
        indexes = [
            models.Index(fields=['path']),
        ]

    @staticmethod
    def get_or_create(name, owner, path, meta, description):
        """
        Get or create a Images.
        """
        try:
            images = Images.objects.get(name=name, owner=owner)
        except Images.DoesNotExist:
            images = Images.objects.create(name=name, owner=owner, path=path, meta=meta, description=description)
            images.save()
        return images