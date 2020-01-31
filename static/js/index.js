$(document).ready(function(){
  $("#login").submit(function(e){
    e.preventDefault();
    var email = $("#email").val();
    var password = $("#password").val();
    var data ={'email':email, 'password':password};
    var url= BASE_URL + "loggear/";
    var request= $.post(url,data);
    request.done(function(data){
        console.log(data);
        if(data=="Exito"){
            window.location.replace(BASE_URL+"index/");
        }else{
            alert("No se pudo loggear, Intente nuevamente.")
        }
    });
  });
  $(".delete").click(function(e){
    var id=$(this).attr("todelete");
    var url= BASE_URL + "eliminar/";
    var data={'id':id};
    var request= $.post(url,data);
    request.done(function(data){
        if(data=="Exito"){
            window.location.replace(BASE_URL+"index/");
        }else{
            alert("No se pudo eliminar el evento, Intente nuevamente.")
        }
    });
  });
  $("#logoutLink").click(function(e){
    e.preventDefault();
    var data ={};
    var url= BASE_URL + "logout/";
    var request= $.post(url,data);
    request.done(function(data){
        console.log(data);
        if(data=="Exito"){
            window.location.replace(BASE_URL+"index/");
        }else{
            alert("No se pudo finalizar sesion, Intente nuevamente.")
        }
    });
  });
});
