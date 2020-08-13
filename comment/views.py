from django.shortcuts import redirect,render,get_object_or_404
from .models import Comment
from .forms import CommentForm
from login.models import Creator, Member
from event.models import Event
from django.contrib.auth.decorators import login_required
from django.conf import settings

# @login_required
def comment_detail(request, pk): # 댓글 보여주기 + 생성하기
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

# @login_required
# def comment_update(request, pk): # 댓글 수정하기
#     creator = Creator.objects.get(pk=pk)
#     comments = creator.comments.all()
#     comment_creator = Comment.creator
#     comment_creator = creator
#     if request.method =='POST':
#         comment_form = CommentForm(request.POST, instance=comment, pk=comment_creator)
#         if comment_form.is_valid():
#             comment = comment_form.save(commit=False)
#             comment.user = request.user
#             comment.creator = creator
#             comment.save()
#             return redirect('event:comment_detail',pk=pk)
#     else:
#         comment_form = CommentForm(instance=comment)
#         ctx = {
#             'comment_form':comment_form
#         }
#         return render(request, 'comment/comment_detail.html', ctx)

# @login_required
# def comment_delete(request, comment_id):
#     comment = creator.comments.get(pk=pk)
#     comment_creator = Comment.creator
#     # comment = Comment.objects.get(pk=..)
#     if request.method == 'POST':
#         comment.delete()
#         return redirect('event:comment_detail',pk=comment_creator)
#     return redirect('event:comment_detail',pk=comment_creator)
