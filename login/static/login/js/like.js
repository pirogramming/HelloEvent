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
                $("#count-"+pk).text(response.like_count+"개");
            },
            error: function(request, status, error){
                alert("로그인이 필요합니다.")
                window.location.replace("/")
            },
        });
    })