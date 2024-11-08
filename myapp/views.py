# myapp/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Note
from .serializers import NoteSerializer


# Create a new note
@api_view(["POST"])
def create_note(request):
    if request.method == "POST":
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Save the new note to the database
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Get all notes
@api_view(["GET"])
def get_all_notes(request):
    if request.method == "GET":
        notes = Note.objects.all()
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data)


# Get a single note by ID
@api_view(["GET"])
def get_note_by_id(request, pk):
    try:
        # Get the note by primary key (ID)
        note = Note.objects.get(pk=pk)
    except Note.DoesNotExist:
        # If the note does not exist, return a 404 error
        return Response({"error": "Note not found"}, status=status.HTTP_404_NOT_FOUND)

    # Serialize and return the single note
    serializer = NoteSerializer(note)
    return Response(serializer.data)


# Update an existing note
@api_view(["PUT"])
def update_note(request, pk):
    try:
        note = Note.objects.get(pk=pk)
    except Note.DoesNotExist:
        return Response({"error": "Note not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = NoteSerializer(note, data=request.data)
    if serializer.is_valid():
        serializer.save()  # Update the note with new data
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Delete a note
@api_view(["DELETE"])
def delete_note(request, pk):
    try:
        note = Note.objects.get(pk=pk)
    except Note.DoesNotExist:
        return Response({"error": "Note not found"}, status=status.HTTP_404_NOT_FOUND)

    note.delete()  # Delete the note from the database
    return Response(status=status.HTTP_204_NO_CONTENT)
