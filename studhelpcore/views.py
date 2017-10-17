from django.shortcuts import render
from django.urls import reverse
from django.conf import settings

from django.views.generic import TemplateView, CreateView, DetailView, ListView, DeleteView
from easy_pdf.views import PDFTemplateView

from .models import Discipline, Document, Chapter, DocumentChapter


class Index(TemplateView):

	def get_context_data(self, **kwargs):
		context = super(Index, self).get_context_data(**kwargs)
		context['top_disciplines'] = Discipline.objects.filter().order_by('views')[:5]
		context['recent_disciplines'] = Discipline.objects.filter().order_by('last_seen')[:5]
		context['recent_documents'] = Document.objects.filter().order_by('last_seen')[:5]
		context['total_disciplines'] = Discipline.objects.all().count()
		context['total_documents'] = Document.objects.all().count()
		return context


class CreateDocumentChapter(CreateView):

	def form_valid(self, form):
		chapter_obj = form.save()
		document_obj = Document.objects.get(pk=self.kwargs['pk'])

		DocumentChapter.objects.create(
			document_fk=document_obj,
			chapter_fk=chapter_obj)

		return super(CreateDocumentChapter, self).form_valid(form)


class AllDocumentByDiscipline(ListView):

	def get_queryset(self):
		discipline_obj = Discipline.objects.get(pk=self.kwargs['pk'])
		discipline_obj.add_view()
		return Document.objects.filter(discipline_fk=discipline_obj)

	def get_context_data(self, **kwargs):
		context = super(AllDocumentByDiscipline, self).get_context_data(**kwargs)
		context['discipline'] = Discipline.objects.get(pk=self.kwargs['pk'])
		return context


class DeleteChapter(DeleteView):

	def get_success_url(self):
		return reverse(
			'core:detail_document',
			args=[DocumentChapter.objects.get(
				pk=self.kwargs['pk']).document_fk.pk])


class GetDocument(DetailView):

	def get_object(self):
		doc_obj = Document.objects.get(pk=self.kwargs['pk'])
		doc_obj.add_view()
		return doc_obj


class ExportToPDF(PDFTemplateView):

	base_url = 'file://' + settings.STATIC_ROOT
	download_filename = 'pdf.pdf'

	def get_context_data(self, **kwargs):
		doc_obj = Document.objects.get(pk=self.kwargs['pk'])
		return super(ExportToPDF, self).get_context_data(
			pagesize='A4',
			title=doc_obj.title,
			description=doc_obj.description,
			content=doc_obj.get_chapters(),
			**kwargs
		)