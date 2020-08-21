// scroll 하단에 고정
$("#comment_list").scrollTop($("#comment_list")[0].scrollHeight);
$(".recomment_list").scrollTop($(".recomment_list")[0].scrollHeight);  

// 댓글 작성
$('#comment_form').submit(function(e){
    
    e.preventDefault();
    $('input[name="is_ajax"]').val("1");
    url = $(this).attr('action');
    var formData = new FormData(this);
    var writer = $('input[name="comment_writer"]').val();
    formData.append("user",writer)

    $.ajax({
        url:url,
        method:"POST",
        data:formData,
        processData: false,
        contentType: false,
    }).done(function(data) {
        $('#comment_list').append(data.html); // tbody 시작 지점에 요소 끼워넣기
        // is_ajax 값 초기화
        $('input[name="is_ajax"]').val("");
        $('#id_comment_text').val("");
        $('#id_comment_photo').val("");
    });

    return false;
});

// 댓글 삭제
$('.btn_comment_delete').click(function(e) {
    e.preventDefault();
    var input = confirm('댓글을 삭제하시겠습니까?');
    if (input==true) {
        alert('댓글을 삭제하였습니다.');
        comment = $(this).parents('.single_comment');
        url = $(this).attr('href')+"?is_ajax=1"; // ajax 호출임을 구분할 수 있게 값 추가
        $.ajax({
            url:url
        }).done(function(data) {
            if (data.works) {
                comment.remove(); // 해당 객체 지우기
            }
        });
    }
});



$(function() {
    /* Rounded Dark */
    $("#comment_list").mCustomScrollbar({
      theme: "rounded-dark"
    });
  });