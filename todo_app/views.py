from django.shortcuts import render, redirect
from django.views import View
from .forms import NoteForm
from .models import Note
from django.contrib.auth.mixins import LoginRequiredMixin

number = 123
number % 3


class BaseView(View):
    def get(self, request):
        return render(request, 'main_page.html', context={})


class NoteView(LoginRequiredMixin, View):
    def get(self, request):
        user_login = request.user
        notes = Note.objects.filter(user=user_login)
        return render(request, 'form_page.html', context={'form': NoteForm(),
                                                          'last_notes': notes})

    def post(self, request):
        form = NoteForm(request.POST)
        user_login = request.user
        if form.is_valid():
            new_note = Note(title=form.cleaned_data['title'], text=form.cleaned_data['text'], user=user_login)
            new_note.save()
        return redirect('note_view')


class DeleteView(LoginRequiredMixin, View):
    def post(self, request, id):
        delete_object = Note.objects.get(pk=id)
        delete_object.delete()
        return redirect('note_view')
