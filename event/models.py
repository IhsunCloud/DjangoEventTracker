from django.db import models as dModels
from django.utils.translation import gettext_lazy as _

from painless import models as iModels
from organizer.models import Organizer
from cities.models import Ostan, Shahr


class Event(iModels.GeneralModel):
    """
    Model definition of Event.
    --------------------------

    Arguments:
    ----------
        - title        -> str:       Title of event.
        - slug         -> slug:      Title slugify of event.
        - category     -> fk:        Category of event.
        - description  -> text:      Description of event.
        - event_date   -> datetime:  Event date.
        - event_price  -> datetime:  Event price.
        - organizer    -> fk:        Organization associated with event.
        - tags         -> fk:        Tag of event.
        - created_at   -> datetime:  Created timestamp.
        - updated_at   -> datetime:  Updated timestamp.

    Methods:
    --------
        - __str__:  string representation of model.
        - __repr__: string representation of model.
    """
    description = dModels.TextField(_('Description'))
    city        = dModels.ForeignKey(Shahr, on_delete=dModels.CASCADE, related_name='events')
    event_date  = dModels.DateTimeField(_('Date'), auto_now_add=False)
    event_price = dModels.DecimalField(_('Price'), max_digits=5, decimal_places=2)
    organizer   = dModels.ForeignKey(Organizer, on_delete=dModels.CASCADE, related_name='events')
    province    = dModels.ForeignKey(Ostan, on_delete=dModels.CASCADE, related_name='events')

    class Meta:
        ordering = ('-event_date',)

    def __str__(self) -> str:
        return f'Title: {self.title} | Date: {self.event_date}'

    def __repr__(self) -> str:
        return self.__str__()


class Category(iModels.TitleSlug):
    """ Model definition of Category. """
    title = dModels.CharField(_('Title'), max_length=64)
    event = dModels.ForeignKey('Event', on_delete=dModels.CASCADE, verbose_name=_('Category'),)


class Tag(iModels.TitleSlug):
    """ Model definition of Category. """
    title = dModels.CharField(_('Title'), max_length=64)
    event = dModels.ForeignKey('Event', on_delete=dModels.CASCADE, verbose_name=_('Event'))


class Ticket(dModels.Model):
    """ Model definition of Ticket. """
    event = dModels.ForeignKey(Event, on_delete=dModels.CASCADE, related_name='tickets')
    # TODO: Add guest attribute here.