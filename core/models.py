from django.db import models

# Create your models here.


class Issue(models.Model):
	filename = models.CharField(max_length=200)
	text = models.TextField()

class IssueDetails(models.Model):
	issue = models.ForeignKey(Issue, unique=True, null=True)
	
	filename = models.CharField(max_length=200, unique=True)
	year = models.TextField(db_index=True)
	nyear = models.IntegerField(db_index=True)
	number = models.TextField(db_index=True)
	nnumber = models.IntegerField(db_index=True)
	mode = models.TextField(db_index=True)

	class Meta:
		ordering=['nyear','nnumber']
