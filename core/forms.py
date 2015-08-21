from django.forms import ModelForm
from django.core.exceptions import ValidationError

from core import models


class TestForm(ModelForm):
    class Meta:
        model = models.Test
        fields = ['name', 'description', 'source']

    def __init__(self, *args, **kwargs):
        self.owner = kwargs.pop('owner', None)
        super().__init__(*args, **kwargs)

    def clean(self):
        if self.owner:
            self.instance.owner = self.owner

        return super().clean()

    def validate_unique(self):
        try:
            self.instance.validate_unique()
        except ValidationError as e:
            self._update_errors(e)
