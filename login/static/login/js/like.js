let like_btn = document.querySelector('.like').children[0]
$(".like").click(function(e){
    e.preventDefault()
    let pk = $(this).attr('name')
    let url = $(this).attr('href')
    $.ajax(
        {
            type:"POST",
            url: url,
            data:{'pk':pk, 'csrfmiddlewaretoken':'{{ csrf_token }}'},
            dataType:"json",

            success: function(response){
                if(response.message=="좋아요"){
                    if(like_btn.classList.contains('far')){
                        like_btn.classList.remove('far')
                        like_btn.classList.add('fas')
                    }
                }
                else {
                    if(like_btn.classList.contains('fas')){
                        like_btn.classList.remove('fas')
                        like_btn.classList.add('far')
                    }
                }
                $("#count-"+pk).text(response.like_count+"개");
            },
            error: function(request, status, error){
                alert("로그인이 필요합니다.")
                window.location.replace("/")
            },
        });
    })