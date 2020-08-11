from django.shortcuts import redirect,render,get_object_or_404
from .models import Comment
from .forms import *
from login.models import Creator
from django.contrib.auth.decorators import login_required
from django.conf import settings


def comment_read(request,creator_id):
    comments = Comment.objects.all()
    creator = Creator.objects.get(id=creator_id)
    return render(request, 'comment_read.html', {'comments':comments, 'creator':creator})

# @login_required
# def comment_create(request, pk):
#     member = settings.AUTH_USER_MODEL
#     creator = member.creator
#     creator_detail = get_object_or_404(Creator, pk = creator_id)
#     comment_form = CommentForm(request.POST)
    
#     if comment_form.is_valid():
#         comment = comment_form.save(commit=False)
#         comment.writer = request.user
#         comment.creator = Creator.objects.get(pk=pk)
#         comment.save()
#         return redirect('comment_read.html',pk)
#     else: comment_form = CommentForm()

#     return render(request, 'comment_read.html', {'comment_form':comment_form})

@login_required
def comment_update():
    pass

@login_required
def comment_delete():
    pass
