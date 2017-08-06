# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class File_Hashes(models.Model):
	file_name = models.TextField()
	file = models.BinaryField(default=None)
	user = models.ForeignKey(User, editable=False, default=None)
	hash = models.TextField(db_index=True)

	def save(self, *args, **kwargs):
		super(File_Hashes, self).save(*args, **kwargs)