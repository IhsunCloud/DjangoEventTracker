from django.db import models as dModels
from django.utils.translation import gettext_lazy as _

from painless import models as iModels
from event.models import Event


class Organizer(iModels.GeneralModel):
    """ Model definition of Organizer. """
    city         = dModels.CharField(_('City'), max_length=32)
    date_joined  = dModels.DateTimeField(_('Date Joined'), auto_now_add=True)
    description  = dModels.TextField(_('Organizer Description'))
    email        = dModels.EmailField(_('Email'), max_length=254)
    events       = dModels.ForeignKey(Event, on_delete=dModels.CASCADE, related_name='event')
    phone_number = dModels.CharField(_(_('Phone number')), max_length=16)
    website      = dModels.URLField(_('Website URL'), help_text=_('https://www.alibaba.com/'), max_length=200)

    def __str__(self):
        return f'{self.title} {self.date_joined}'

    def __repr__(self):
        return self.__str__()