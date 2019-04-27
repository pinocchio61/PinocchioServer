from django.http import HttpResponse

# /transcription/
def transcription(request):
    return HttpResponse("Your audio has been successfully transcribed.")

# /transcription/whee/
def whee(request):
    return HttpResponse("wheeeeeeeeeeeeeeeeee")