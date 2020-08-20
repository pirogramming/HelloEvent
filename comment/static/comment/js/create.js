

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

// scroll 하단에 고정
$("#comment_list").scrollTop($("#comment_list")[0].scrollHeight);