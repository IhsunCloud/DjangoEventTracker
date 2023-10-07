from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Timestamped(models.Model):
	created_at = models.DateTimeField(_('Created at'), auto_now=False, auto_now_add=True)
	updated_at = models.DateTimeField(_('Updated at'), auto_now=True)

	class Meta:
		abstract = True
		ordering = ('-created_at',)


class TitleSlug(models.Model):
	title = models.CharField(_('Title'), max_length=128)
	slug  = models.SlugField(_('Unique Slug'), unique=True, primary_key=True, editable=False)

	class Meta:
		abstract = True

	def save(self, *args, **kwargs):
		while True:
			try:
				self.slug = slugify(self.title)
				super(TitleSlug, self).save(*args, **kwargs)
				break
			except Exception as e:
				raise e


class GeneralModel(Timestamped, TitleSlug):
    class Meta:
        abstract = True
        
        
