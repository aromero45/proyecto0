$(document).ready(function(){

  $("#formularioRegistro").submit(function(e){
    e.preventDefault();
    var email = $("#email").val();
    var password = $("#password").val();
    var data ={'email':email,'password':password};
    var url= BASE_URL + "registrar/";
    var request= $.post(url,data);
    request.done(function(data){
        console.log(data);
        if(data=="Exito"){
            window.location.replace(BASE_URL+"index/");
        }else{
            alert("No se pudo crear el usuario, Intente nuevamente.")
        }
    });

  });

});