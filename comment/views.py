from django.shortcuts import redirect,render,get_object_or_404
from django.urls import reverse
from .models import Comment, Recomment
from .forms import CommentForm, RecommentForm
from login.models import Creator, Member
from event.models import Event
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# @login_required
@csrf_exempt
def comment_detail(request, pk): # 댓글 보여주기
    # ajax
    # receive_comment = request.POST.get('comment',None)

    creator = Creator.objects.get(pk=pk)
    comments = creator.comments.all()

    print('get시작') 
    comment_form = CommentForm()
    recomment_form = RecommentForm()
    print('ctx반환직전')
    ctx = {
        'creator':creator,
        'comments':comments,
        'comment_form':comment_form,
        'recomment_form':recomment_form,
    }
    return render(request, 'comment/comment_detail.html', ctx)

@login_required
@csrf_exempt
def comment_create_ajax(request, pk): # 댓글 생성하기
    # is_ajax : ajax 기능에 의해 호출된 것인지 구분하기 위한 값
    is_ajax = request.POST.get('is_ajax')

    creator = Creator.objects.get(pk=pk)
    comment_form = CommentForm(request.POST, request.FILES)
    recomment_form = RecommentForm(request.POST, request.FILES)
    recomment = recomment_form.save(commit=False)

    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.member = request.user
        comment.creator = creator
        comment.save()
            
    if is_ajax:
        # 데이터 만들어서 던져주기
        html = render_to_string('comment/comment_create.html',{'comment':comment, 'username':request.user, 'recomment_form':recomment_form, 'recomment':recomment})
        return JsonResponse({'html':html})
    return redirect(reverse('event:comment_detail', args=[pk]))

        # if self.request.is_ajax():
        #     print('ajax request')   #ajax요청일때는 jsonresponse로 응답!
        #     return JsonResponse({
        #         'id': comment.id,
        #         #  'message': comment.message,
        #         #  'updated_at': comment.updated_at,
        #         #  'edit_url': resolve_url('blog:comment_edit', comment.post.pk, comment.pk),
        #         #  'delete_url': resolve_url('blog:comment_delete', comment.post.pk, comment.pk),
        #         }) 
        # return response


def recomment_detail(request, comment_id): # 대댓글 보여주기
    comment = Comment.objects.get(pk=comment_id)
    creator = comment.creator
    recomment_form = RecommentForm()
    ctx = {
        'comment':comment,
        'creator':creator,
        'recomment_form':recomment_form,
    }
    return render(request, 'comment/comment_detail.html', ctx)

@login_required
@csrf_exempt
def recomment_create_ajax(request, comment_id): # 대댓글 생성하기
    # is_ajax : ajax 기능에 의해 호출된 것인지 구분하기 위한 값
    is_ajax2 = request.POST.get('is_ajax2')
    print(is_ajax2)
    comment = Comment.objects.get(pk=comment_id)
    creator = comment.creator
    recomment_form = RecommentForm(request.POST, request.FILES)
    if recomment_form.is_valid():
        recomment = recomment_form.save(commit=False)
        recomment.parent = comment
        recomment.writer = request.user
        recomment.save()
        
    if is_ajax2:
        print("ajax성공")
        html = render_to_string('comment/recomment_create.html',{'recomment':recomment, 'username':request.user})
        return JsonResponse({'html':html})
    else:
        print("ajax실패")
    return redirect(reverse('comment:recomment_detail', args=[comment_id]))


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


def comment_delete(request, comment_id):
    is_ajax = request.GET.get('is_ajax') if 'is_ajax' in request.GET else request.POST.get('is_ajax',False)
    comment = get_object_or_404(Comment, pk=comment_id)
    creator = comment.creator

    if is_ajax:
        print("ajax 성공")
        comment.delete()
        return JsonResponse({"works":True})

    if request.method == "POST":
        print('post 시작')
        comment.delete()
        return redirect(creator)
    else:
        print('get')
        return render(request, 'comment/comment_detail.html', {'object': comment})


def recomment_delete(request, recomment_id):
    is_ajax = request.GET.get('is_ajax') if 'is_ajax' in request.GET else request.POST.get('is_ajax',False)

    recomment = get_object_or_404(Recomment, pk=recomment_id)
    comment = get_object_or_404(Comment, pk=recomment.parent.pk)
    creator = comment.creator

    if is_ajax:
        print("ajax 성공")
        recomment.delete()
        print('삭제')
        return JsonResponse({"works":True})

    if request.method == "POST":
        print('post 시작')
        recomment.delete()
        return redirect(creator)
    else:
        print('get')
        return render(request, 'comment/comment_detail.html', {'object': recomment} )