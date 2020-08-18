from django.shortcuts import redirect,render,get_object_or_404
from .models import Comment, Recomment
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
        print('post시작')
        comment_form = CommentForm(request.POST, request.FILES)
        print(1)
        if comment_form.is_valid():
            print(2)
            comment = comment_form.save(commit=False)
            print(comment.comment_text)
            print(comment.comment_photo)
            comment.member = request.user
            print(4)
            comment.creator = creator
            print(5)
            comment.save()
            print(6)
            return redirect('event:comment_detail',pk=pk)
            print(7)
    else:
        print('get시작') 
        comment_form = CommentForm()
        print('ctx반환직전')
        ctx = {
            'creator':creator,
            'comments':comments,
            'comment_form':comment_form,
        }
        return render(request, 'comment/comment_detail.html', ctx)

# @login_required
def comment_update(request, comment_id): # 댓글 수정하기
    comment = Comment.objects.get(pk=comment_id)
    creator = comment.creator

    if request.method =='POST':
        comment_form = CommentForm(request.POST, instance=comment)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.member = request.user
            comment.creator = creator
            comment.save()
            return redirect('event:comment_detail',pk=creator.id)
    else:
        comment_form = CommentForm(instance=comment)
        ctx = {
            'comment_form':comment_form
        }
        return render(request, 'comment/comment_detail.html', ctx)

# @login_required
def comment_delete(request, comment_id):
    comment = Comment.objects.get(pk=comment_id)
    comment_creator = comment.creator
    comment.delete()
    return redirect('event:comment_detail',pk=comment_creator.id)

# ------------------------------------------------------------
# 대댓글 보여주기
# def recomment_detail(request, comment_id):
#     comment = Comment.objects.get(pk=comment_id)
#     comments = creator.comments.all()
#     if request.method =='POST':
#         print('post시작')
#         comment_form = CommentForm(request.POST)
#         recomment_form = CommentForm(request.POST)
#         if comment_form.is_valid():
#             comment = comment_form.save(commit=False)
#             comment.member = request.user
#             comment.creator = creator
#             comment.save()
#             if recomment_form.is_valid():
#                 recomment = recomment_form.save(commit=False)
#                 recomment.parent = parent
#                 recomment.member = request.user
#                 # 
#             return redirect('event:comment_detail',pk=pk)
#     else:
#         print('get시작') 
#         comment_form = CommentForm()
#     print('ctx반환직전')
#     ctx = {
#         'creator':creator,
#         'comments':comments,
#         'comment_form':comment_form,
#     }
#     return render(request, 'comment/comment_detail.html', ctx)
#         recomments = comments.recomment_set.all()
