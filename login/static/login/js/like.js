
$(".like").click(function(){
    let pk = $(this).attr('name')
    let url = $(this).attr('href')
    alert(url)
    $.ajax(
        {
            type:"POST",
            url: url,
            data:{'pk':pk, 'csrfmiddlewaretoken':'{{ csrf_token }}'},
            dataType:"json",

            success: function(response){
                alert(response.message);
                $("#count-"+pk).html(response.like-count+"개");
                let users = $("#like-user-"+pk).text();
                if(users.indexOf(response.nickname)!=-1){
                    $("#like-user-"+pk).text(users.replace(response.nickname,""));
                }
                else{
                    $("#like-user-"+pk).text(response.nickname+users);
                }
            },
            error: function(request, status, error){
                alert("로그인이 필요합니다.")
                window.location.replace("/")
            },
        });
    })