import uuid
from django.db import models
from extensions.models import AutoTimestampedModel, UserTrackingModel
from image_model_domain.enums import Hosted


class DLModels(AutoTimestampedModel, UserTrackingModel):
    """
    DLModels model.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    owner = models.CharField(max_length=255)
    hosted = models.TextField(choices=Hosted.choices(), default=Hosted.HUGGING_FACE)
    meta = models.JSONField(default=dict)
    description = models.TextField(null=True)

    class Meta:
        db_table = 'da_dlmodels'
        app_label = 'image_model_domain'
        unique_together = [('name', 'owner')]
        indexes = [
            models.Index(fields=['name']),
        ]

    @staticmethod
    def get_or_create(name, owner, hosted, meta, description):
        """
        Get or create a DLModels.
        """
        try:
            dlmodels = DLModels.objects.get(name=name, owner=owner)
        except DLModels.DoesNotExist:
            dlmodels = DLModels.objects.create(name=name, owner=owner, hosted=hosted, meta=meta, description=description)
            dlmodels.save()
        return dlmodels