from django.shortcuts import render,redirect,redirect,render_to_response
from django.http import Http404,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.urlresolvers import reverse_lazy
from apps.comment.forms import FormComment
from apps.comment.models import Comment
import simplejson as json
# Create your views here.

def view_comment(request):
    comment = Comment.objects.all()
    form = FormComment()
    return render(request,'comments/form_comment.html', {'form':form, 'comments':comment})

@csrf_exempt
def new_comment(request):
    if request.method == "POST":
        form = FormComment(request.POST)
        if form.is_valid():
            comment = form.save()
        return HttpResponse(json.dumps({'id':comment.id,'author':comment.author,'comment':comment.comment}))
    else:
        raise Http404
