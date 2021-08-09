from django.urls import path
from .views import NoteView, DeleteView, BaseView

urlpatterns = [
    path('note/', NoteView.as_view(), name="note_view"),
    path('<int:id>/', DeleteView.as_view(), name="delete_note"),
    path('', BaseView.as_view(), name="base_view")
]