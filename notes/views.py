from django.shortcuts import render
from notes.models import Notes
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def create_note(request):
    title = request.POST.get('title')
    note = request.POST.get('note')
    user = request.POST.get('user')
    if title and note and user:
        note = Notes(title=title,note=note,user=user)
        note.save()
        return JsonResponse({'status':'200'})
    else:
        return JsonResponse({'status':'500'})

@csrf_exempt
def update_note(request):
    id = request.POST.get('id')
    updated_note = request.POST.get('updated_note')
    if id:
        note = Notes.objects.get(id=id)
        note.note=updated_note
        note.save()
        return JsonResponse({'status':'200'})
    else:
        return JsonResponse({'status':'500'})
    
@csrf_exempt
def delete_note(request):
    id = request.POST.get('id')
   
    if id:
        note = Notes.objects.filter(id=id)
        note.delete()
        return JsonResponse({'status':'200'})
    else:
        return JsonResponse({'status':'500'})