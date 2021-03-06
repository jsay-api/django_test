# coding: utf-8

from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Post(models.Model):
	title = models.CharField('SpaceTitle', max_length = 100)
	text = models.TextField('SpaceText')
	create_date = models.DateTimeField('SpaceTime Sol#')

	def __unicode__(self):	#for Python 3.x this method is called __str__
		return '{0} {1}'.format(self.title, self.create_date)	