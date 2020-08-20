//대댓글작성
$('#recommentForm').submit(function(e){
    e.preventDefault()
    e.stopPropagation()
    $('input[name="is_ajax2"]').val("1");
    url = $(this).attr('action');
    var formData = new FormData(this);

    console.log(formData)
    for (var key of formData.keys()) {
        console.log(key); 
        }
        for (var value of formData.values()) {
        console.log(value); 
        }
    $.ajax({
        url:url,
        method:"POST",
        data:formData,
        processData: false,
        contentType: false,

    }).done(function(data) {
        $('#recomment_list').append(data.html);
        // is_ajax2 값 초기화
        $('input[name="is_ajax2"]').val("");
        $('#id_recomment_text').val("");
        $('#id_recomment_photo').val("");
    });
    return false;
});


