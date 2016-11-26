#from __future__ import unicode_literals

from django.db import models

# Create your models here.

from shortener.models import VtuURL

class ClickEventManager(models.Manager):
	def create_event(self, vtuInstance):
		if isinstance(vtuInstance, VtuURL):
			obj, created = self.get_or_create(vtu_url=vtuInstance)
			obj.count += 1
			obj.save()
			return obj.count
		return None


class ClickEvent(models.Model):
	vtu_url = models.ForeignKey(VtuURL)
	count = models.IntegerField(default=0)
	updated	  = models.DateTimeField(auto_now=True) #every time model is saveed
	#timestamp = models.DateTimeField(auto_now_add=True)

	objects= ClickEventManager()

	def __str__(self):
		return "{i}".format(i=self.count)