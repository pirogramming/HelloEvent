$('#comment_form').submit(function(e){
    e.preventDefault();
    $('input[name="is_ajax"]').val("1");
    url = $(this).attr('action');
    params = $(this).serialize(); 
    $.ajax({
        url:url,
        method:"POST",
        data:params
    }).done(function(data) {
        $('#comment_list').prepend(data.html); // tbody 시작 지점에 요소 끼워넣기
        // is_ajax 값 초기화
        $('input[name="is_ajax"]').val("");
        $('#id_comment_text').val("");
    });
    return false;
});





