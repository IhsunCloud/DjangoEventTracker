from django.db import models as dModels
from painless import models as iModels
from django.utils.translation import gettext_lazy as _


class Event(iModels.GeneralModel):
    """
    Model definition of Event.
    --------------------------

    Arguments:
    ----------
        - title       -> str:       Title of event.
        - slug        -> slug:      Title slugify of event.
        - created_at  -> datetime:  Created timestamp.
        - updated_at  -> datetime:  Updated timestamp.

        - description -> text:      Description of event.
        - event_date  -> datetime:  Event date.

    Methods:
    --------
        - __str__:  string representation of model.
        - __repr__: string representation of model.
    """

    description = dModels.TextField()
    event_date  = dModels.DateTimeField(_('Date'), auto_now_add=True)

    class Meta:
        ordering = ('-event_date',)

    def __str__(self) -> str:
        return f'{self.title} {self.created_at}'

    def __repr__(self) -> str:
        return self.__str__()