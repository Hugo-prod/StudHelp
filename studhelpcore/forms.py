from django import forms

from .models import Discipline, Document, Chapter


class DisciplineForm(forms.ModelForm):

	def get_title(self):
		if self.instance.id :
			return 'Modification de la discipline "{}"'.format(self.instance.name)
		else:
			return 'Création d\'une discipline'

	class Meta:
		model = Discipline
		fields = ['name', 'description']
		widgets = {
			'description': forms.Textarea,
		}

class DocumentForm(forms.ModelForm):

	def get_title(self):
		if self.instance.id :
			return 'Modification du document "{}"'.format(self.instance.title)
		else:
			return 'Création d\'un document'

	class Meta:
		model = Document
		fields = ['discipline_fk', 'title', 'description']
		widgets = {
			'description': forms.Textarea,
		}


class ChapterForm(forms.ModelForm):

	def get_title(self):
		if self.instance.id :
			return 'Modification du chapitre "{}"'.format(self.instance.title)
		else:
			return 'Création d\'un chapitre'

	class Meta:
		model = Chapter
		fields = ['title', 'content', 'example', 'note']