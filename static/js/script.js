$(document).ready(function () {
    console.log("script linked");
    $('#stanceform').submit(function(e){
        e.preventDefault();
        console.log("clicked")
        var formdata = $('#stanceform').serializeArray();
        // console.log(formdata);
        $.post('http://127.0.0.1:8787/detect', formdata, function (data, status) {
            console.log(data);
            $("#resultmodal").show();
            $("#resultpara").html("The headline has a <span style='color:blue;'>" + data.stance + "</span>"+ "stance with the article");
            // $("#resultpara").html("The obtained mark is:- <span style='color:blue;'>" + "50" + "</span>");
            
        })
    perform = function(){
        document.getElementById('resultmodal').style.display='none';
        $('textarea').val("");
    }
    })
})