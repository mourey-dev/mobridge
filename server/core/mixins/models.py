from django.db import models


class TimestampMixin(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class DeleteMixin(models.Model):
    is_delete = models.BooleanField(default=False)

    def soft_delete(self):
        self.is_delete = True
        self.save()

    def restore(self):
        self.is_delete = False
        self.save()

    class Meta:
        abstract = True
