$(function() {
    $('#comment_form').submit(function(e){
        e.preventDefault();
        $('input[name='is_ajax']').val("1");
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
});

// let input_comment = document.querySelector('#id_comment_text')
// let input_comment_value = input_comment.value
// let send_comment_btn = document.querySelector('#sendComment_btn')

// // input_comment.addEventListener('change',function(e){
// //     // e.value = input_comment_value
// //     alert(e.target.value)
// // })
// send_comment_btn.addEventListener('click',function(e){
//     e.preventDefault()
//     // console.log(input_comment.value)
// })


// $("#sendComment_btn").click(function(e){
//     $('input[name="is_ajax"]').val("1");
//     params = $(this).serialize();

//     $.ajax({
//         type:"POST",
//         url: "",
//         data :{'comment_form':input_comment.value ,'csrfmiddlewaretoken': '{{csrf_token}}'},
//         dataType:"json",
//         success: function(response){
//             alert(response.data)
//         }
//     })        
// })



