$(document).ready(function(){
  $("#eventCreateForm").submit(function(e){
    e.preventDefault();
    var name = $("#name").val();
    var category = $("#category").val();
    var place = $("#place").val();
    var address = $("#address").val();
    var start_date = $("#datetimepicker1").find("input").val();
    var end_date = $("#datetimepicker2").find("input").val();
    var type = $("#eventType").val();
    var data ={'name':name,'category':category,'place':place, 'address':address, 'start_date':start_date, 'finish_date':end_date, 'type':type};
    console.log(data);
    var url= BASE_URL + "crear/";
    var request= $.post(url,data);
    request.done(function(data){
        console.log(data);
        if(data=="Exito"){
            window.location.replace(BASE_URL+"index/");
        }else{
            alert("No se pudo crear el evento, Intente nuevamente.")
        }
    });
  });
});
