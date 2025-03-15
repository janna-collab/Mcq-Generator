from django.shortcuts import render
from django.http import JsonResponse
from ml_model.model import generate_mcqs

def home(request):
    return render(request, 'index.html')

def generate_mcq_view(request):
    if request.method == 'POST':
        text = request.POST.get('text', '')
        try:
            mcq_count = int(request.POST.get('mcqCount', '5'))
        except ValueError:
            mcq_count = 5
        if mcq_count > 20:
            mcq_count = 20
        if not text.strip():
            return JsonResponse({"error": "No text provided."}, status=400)
        
        mcqs = generate_mcqs(text, question_count=mcq_count)
        return JsonResponse({"mcqs": mcqs})
    else:
        return JsonResponse({"error": "Invalid request method."}, status=405)
