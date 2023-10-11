from django.core.validators import RegexValidator
from django.db import models as dModels
from django.utils.translation import gettext_lazy as _

from painless import models as iModels
from cities.models import Ostan, Shahr


class Organizer(iModels.GeneralModel):
    """ Model definition of Organizer. """
    phone_number = dModels.CharField(
        _(_('Phone number')),
        max_length = 16,
        validators = [RegexValidator(r"^(?:0|98|\+98|\+980|0098|098|00980)?(9\d{9})$")] # TODO: Add validator to separate file.
    )
    city         = dModels.ForeignKey(Shahr, on_delete=dModels.CASCADE, related_name='organizers')
    province     = dModels.ForeignKey(Ostan, on_delete=dModels.CASCADE, related_name='organizers')
    date_joined  = dModels.DateTimeField(_('Date Joined'), auto_now_add=True)
    description  = dModels.TextField(_('Organizer Description'))
    email        = dModels.EmailField(_('Email'), max_length=254)
    website      = dModels.URLField(_('Website URL'), max_length=200, help_text=_('https://www.alibaba.com/'))

    def __str__(self):
        return f'{self.title} {self.date_joined}'

    def __repr__(self):
        return self.__str__()