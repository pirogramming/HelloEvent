from django.shortcuts import redirect,render,get_object_or_404
from .models import Comment
from .forms import CommentForm
from login.models import Creator, Member
from event.models import Event
from django.contrib.auth.decorators import login_required
from django.conf import settings

# @login_required
def comment_detail(request, pk):
    creator = Creator.objects.get(pk=pk)
    comments = creator.comments.all()
    if request.method =='POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.creator = creator
            comment.save()
            return redirect('event:comment_detail',pk=pk)
    else: 
        comment_form = CommentForm()

    ctx = {
        'creator':creator,
        'comments':comments,
        'comment_form':comment_form,
    }
    return render(request, 'comment/comment_detail.html', ctx)

@login_required
def comment_update():
    pass

@login_required
def comment_delete():
    pass

