from django.db import models
from django.urls import reverse
from django.dispatch import receiver

from ckeditor_uploader.fields import RichTextUploadingField
import datetime


class Discipline(models.Model):

	created_date = models.DateTimeField(auto_now_add=True)

	update_date = models.DateTimeField(null=True)

	name = models.CharField(
		max_length=50,
		verbose_name='Nom')

	description = models.CharField(
		max_length=254,
		blank=True,
		verbose_name='Description')

	views = models.IntegerField(default=0)

	last_seen = models.DateTimeField()

	def get_absolute_url(self):
		return reverse('core:all_document_by_discipline', args=[self.pk])

	def get_nb_documents(self):
		return Document.objects.filter(discipline_fk=self).count()

	def add_view(self):
		self.views += 1
		self.save(update_date=False)

	def save(self, update_date=True, *args, **kwargs):
		self.last_seen = datetime.datetime.now()
		if self.id and update_date:
			self.update_date = datetime.datetime.now()
		super(Discipline, self).save(*args, **kwargs)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['update_date', 'created_date']


class Document(models.Model):

	created_date = models.DateTimeField(auto_now_add=True)

	update_date = models.DateTimeField(null=True)

	discipline_fk = models.ForeignKey(
		Discipline,
		verbose_name='Discipline')

	title = models.CharField(
		max_length=50,
		verbose_name='Titre')

	description = models.CharField(
		max_length=254,
		blank=True,
		verbose_name='Description')

	views = models.IntegerField(default=0)

	last_seen = models.DateTimeField()

	def get_absolute_url(self):
		return reverse('core:detail_document', args=[self.pk])

	def get_chapters(self):
		chapter_list = []
		for documentChapter_list_obj in DocumentChapter.objects.filter(
			document_fk=self):
			chapter_list.append(documentChapter_list_obj.chapter_fk)
		return chapter_list

	def get_nb_chapters(self):
		return DocumentChapter.objects.filter(document_fk=self).count()

	def add_view(self):
		self.views += 1
		self.save(update_date=False)

	def save(self, update_date=True, *args, **kwargs):
		self.last_seen = datetime.datetime.now()
		if self.id and update_date:
			self.update_date = datetime.datetime.now()
		super(Document, self).save(*args, **kwargs)

	def __str__(self):
		return self.title

	class Meta:
		ordering = ['update_date', 'created_date']


class Chapter(models.Model):

	title = models.CharField(
		max_length=50,
		verbose_name='Titre')

	content = RichTextUploadingField(
		verbose_name='Contenu')

	example = RichTextUploadingField(
		blank=True,
		verbose_name='Exemple',
		help_text='(Facultatif) Vous pouvez ici saisir des exemples.')

	note = RichTextUploadingField(
		blank=True,
		verbose_name='Note',
		help_text='(Facultatif) Vous pouvez ici saisir des notes complémentaires.')

	def get_absolute_url(self):
		return reverse(
			'core:detail_document',
			args=[DocumentChapter.objects.get(chapter_fk=self).document_fk.pk])

	def __str__(self):
		return self.title

	class Meta:
		ordering = ['-id']


class DocumentChapter(models.Model):

	document_fk = models.ForeignKey(Document)

	chapter_fk = models.ForeignKey(Chapter)


@receiver(models.signals.post_delete, sender=DocumentChapter)
def delete_chapter(sender, instance, *args, **kwargs):
	Chapter.objects.get(pk=instance.chapter_fk.pk).delete()


@receiver(models.signals.post_save, sender=Chapter)
def update_or_create_chapter(sender, instance, created, *args, **kwargs):
	if not created:
		doc_chap_obj = DocumentChapter.objects.get(chapter_fk=instance)
		doc_chap_obj.document_fk.save()