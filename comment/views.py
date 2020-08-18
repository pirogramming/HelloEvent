from django.shortcuts import redirect,render,get_object_or_404
from .models import Comment, Recomment
from .forms import CommentForm, RecommentForm
from login.models import Creator, Member
from event.models import Event
from django.contrib.auth.decorators import login_required
from django.conf import settings

# @login_required
def comment_detail(request, pk): # 댓글 보여주기 + 생성하기
    creator = Creator.objects.get(pk=pk)
    comments = creator.comments.all
    # recomments = parent.recomments.all()
    if request.method =='POST':
        print('post시작')
        comment_form = CommentForm(request.POST, request.FILES)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.member = request.user
            comment.creator = creator
            comment.save()
            return redirect('event:comment_detail',pk=pk)

    else:
        print('get시작') 
        comment_form = CommentForm()
        recomment_form = RecommentForm()
        print('ctx반환직전')
        ctx = {
            'creator':creator,
            'comments':comments,
            'comment_form':comment_form,
            # 'recomments':recomments,
            'recomment_form':recomment_form,
        }
        return render(request, 'comment/comment_detail.html', ctx)


# 대댓글 달기
def recomment_create(request, comment_id):
    comment = Comment.objects.get(pk=comment_id)
    creator = comment.creator
    if request.method =='POST':
        print('re post시작')
        recomment_form = RecommentForm(request.POST, request.FILES)
        if recomment_form.is_valid():
            recomment = recomment_form.save(commit=False)
            recomment.parent = comment
            recomment.writer = request.user
            recomment.save()
            if recomment_form.is_valid():
                recomment = recomment_form.save(commit=False)
                return redirect('event:comment_detail',pk=creator.id)
    else:
        print('re get시작') 
        recomment_form = RecommentForm()
    print('re ctx반환직전')
    ctx = {
        'recomment_form':recomment_form,
    }
    return render(request, 'comment/comment_detail.html', ctx)

# @login_required
def comment_update(request, comment_id): # 댓글 수정하기
    comment = Comment.objects.get(pk=comment_id)
    creator = comment.creator

    if request.method =='POST':
        comment_form = CommentForm(request.POST, request.FILES, instance=comment)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.member = request.user
            comment.creator = creator
            comment.save()
            url = reverse('comment:comment_detail', kwargs={'pk':comment_id})
            return redirect(to=url)
    else:
        comment_form = CommentForm(instance=comment)

    return render(request, 'comment/comment_detail.html', {'comment_form':comment_form})



# @login_required
def comment_delete(request, comment_id):
    comment = Comment.objects.get(pk=comment_id)
    comment_creator = comment.creator
    comment.delete()
    return redirect('event:comment_detail',pk=comment_creator.id)

# ------------------------------------------------------------

