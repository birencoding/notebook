from django.urls import path
from .views import home, index, delete_note, update_note,save_note, create_note
app_name = 'notes'
urlpatterns = [
    path('', index, name='home'),
    path('notes/delete', delete_note, name='delete-note'),
    path('notes/update/<int:note_id>/', update_note, name='update-note'),
    path('notes/save/<int:note_id>/', save_note, name='update-save'),
    path('notes/create/', create_note, name='create-note'),

]
