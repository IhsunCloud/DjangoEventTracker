from django.db import models as dModels
from django.utils.translation import gettext_lazy as _

from painless import models as iModels


class Event(iModels.GeneralModel):
    """
    Model definition of Event.
    --------------------------

    Arguments:
    ----------
        - title        -> str:       Title of event.
        - slug         -> slug:      Title slugify of event.
        - description  -> text:      Description of event.
        - event_date   -> datetime:  Event date.
        - event_price  -> datetime:  Event price.
        - created_at   -> datetime:  Created timestamp.
        - updated_at   -> datetime:  Updated timestamp.

    Methods:
    --------
        - __str__:  string representation of model.
        - __repr__: string representation of model.
    """

    description = dModels.TextField()
    event_date  = dModels.DateTimeField(_('Date'), auto_now_add=True)
    event_price = dModels.DecimalField(_('Price'), max_digits=5, decimal_places=2)

    class Meta:
        ordering = ('-event_date',)

    def __str__(self) -> str:
        return f'{self.title} {self.created_at}'

    def __repr__(self) -> str:
        return self.__str__()