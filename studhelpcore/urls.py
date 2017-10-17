from django.conf.urls import url

from django.views.generic import CreateView, DetailView,\
	 UpdateView, DeleteView, ListView

from .forms import DisciplineForm, DocumentForm, ChapterForm
from .models import Discipline, Document, Chapter, DocumentChapter
from .views import *

urlpatterns = [

    url(r'^$', Index.as_view(template_name='index.html', content_type='text/html'), name='home'),

	################
	## DISCIPLINE ##
	################

	url(r'^discipline/create$', 
		CreateView.as_view(
			model=Discipline,
			form_class=DisciplineForm,
			template_name='form.html'),
				name='create_discipline'),

	url(r'^discipline/(?P<pk>\d+)/update$', 
		UpdateView.as_view(
			model=Discipline,
			form_class=DisciplineForm,
			template_name='form.html'),
				name='update_discipline'),

	url(r'^discipline/(?P<pk>\d+)/delete$', 
		DeleteView.as_view(
			model=Discipline,
			template_name='studhelpcore/discipline/confirm_delete_discipline.html'),
				name='delete_discipline'),

	url(r'^discipline/all$',
		ListView.as_view(
			model=Discipline,
			template_name='studhelpcore/discipline/all_discipline.html',
			paginate_by=10),
				name='all_discipline'),

	# Add all document by discipline

	##############
	## DOCUMENT ##
	##############
	
	url(r'^document/create$', 
		CreateView.as_view(
			model=Document,
			form_class=DocumentForm,
			template_name='form.html'),
				name='create_document'),

	url(r'^document/(?P<pk>\d+)/update$', 
		UpdateView.as_view(
			model=Document,
			form_class=DocumentForm,
			template_name='form.html'),
				name='update_document'),

	url(r'^document/(?P<pk>\d+)/detail$', 
		GetDocument.as_view(
			model=Document,
			template_name='studhelpcore/document/detail_document.html'),
				name='detail_document'),

	url(r'^document/(?P<pk>\d+)/pdf$', ExportToPDF.as_view(
		template_name='studhelpcore/document/export_pdf.html'),
			name='document_to_pdf'),

	url(r'^document/(?P<pk>\d+)/delete$', 
		DeleteView.as_view(
			model=Document,
			template_name='studhelpcore/document/confirm_delete_document.html'),
				name='delete_document'),

	url(r'^document/all$',
		ListView.as_view(
			model=Document,
			template_name='studhelpcore/document/all_document.html',
			paginate_by='20'),
				name='all_document'),

	url(r'^document/recent$',
		ListView.as_view(
			queryset=Document.objects.all().order_by('last_seen'),
			template_name='studhelpcore/document/recent_documents.html',
			paginate_by='20'),
				name='all_recent_documents'),

	url(r'^document/discipline/(?P<pk>\d+)$',
		AllDocumentByDiscipline.as_view(
			template_name='studhelpcore/document/all_document_by_discipline.html',
			paginate_by='20'),
				name='all_document_by_discipline'),

	#############
	## CHAPTER ##
	#############
	
	url(r'^document/(?P<pk>\d+)/chapter/create$', 
		CreateDocumentChapter.as_view(
			model=Chapter,
			form_class=ChapterForm,
			template_name='studhelpcore/document/add_upd_chapter.html'),
				name='create_chapter'),

	url(r'^document/(?P<pk>\d+)/chapter/update$', 
		UpdateView.as_view(
			model=Chapter,
			form_class=ChapterForm,
			template_name='studhelpcore/document/add_upd_chapter.html'),
				name='update_chapter'),

	url(r'^document/(?P<pk>\d+)/chapter/delete$',
		DeleteChapter.as_view(
			model=DocumentChapter,
			template_name='studhelpcore/document/confirm_delete_chapter.html'),
				name='delete_chapter'),
]
