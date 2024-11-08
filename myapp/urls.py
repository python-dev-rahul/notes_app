from django.urls import path
from . import views

urlpatterns = [
    # Create a new note
    path('note/', views.create_note, name='create-note'),
    
    # Get all notes
    path('notes/', views.get_all_notes, name='get-all-notes'),
    
    # Get a single note by ID
    path('note/<int:pk>/', views.get_note_by_id, name='get-note-by-id'),
    
    # Update an existing note
    path('note/update/<int:pk>/', views.update_note, name='update-note'),
    
    # Delete a note
    path('note/delete/<int:pk>/', views.delete_note, name='delete-note'),
]
