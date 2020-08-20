//대댓글작성
// var comment_pk = document.querySelector('#comment_pk_section').textContent

// document.querySelector('.recomment_submit_btn').addEventListener('click',function(e){
//     e.preventDefault
//     console.log(e)
// })

// $(`#recommentForm_${comment_pk}`).submit(setTimeout(function(e){
//     alert(comment_pk)
//     // let comment_pk = e.target.getAttribute('id').replace('recommentForm_','')
//     e.preventDefault()
//     e.stopPropagation()

//     $('input[name="is_ajax2"]').val("1");
//     url = $(this).attr('action');
//     var formData = new FormData(this);

//     console.log(formData)
//     for (var key of formData.keys()) {
//         console.log(key); 
//         }
//         for (var value of formData.values()) {
//         console.log(value); 
//         }
//     $.ajax({
//         url:url,
//         method:"POST",
//         data:formData,
//         processData: false,
//         contentType: false,
//     }).done(function(data) {
//         $('#recomment_list').append(data.html);
//         // is_ajax2 값 초기화
//         $('input[name="is_ajax2"]').val("");
//         $('#id_recomment_text').val("");
//         $('#id_recomment_photo').val("");

//     })
//     return false;
// },500));


