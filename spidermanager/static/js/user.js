/**
 * Created by taoyang on 2017/3/23.
 */



$(function(){
    reload();
});

function reload(){
  loadUser();
}

$('#user-modal').on('hidden.bs.modal', function (e) {
    $('#username').val("").attr("disabled",false);
    $('#description').val("");
    $('#password').val("");
    $('#type').val("basic");
    $('#webuiport').val("");
    $('#schedulerport').val("");
    $('#projectdb').val("");
    $('#taskdb').val("");
    $('#resultdb').val("");
});

$('#save-btn').on('click', function (e) {
    if($('#username').prop("disabled")){
        url="user/edit";
    }else{
        url="user/add";
    }
    var settings = {
      "async": true,
      "dataType" : "json",
      "url": url,
      "method": "POST",
      "data": {
          "username":$('#username').val(),
          "description":$('#description').val(),
          "password":$('#password').val(),
          "type":$('#type').val(),
          "webuiport":$('#webuiport').val(),
          "schedulerport":$('#schedulerport').val(),
          "projectdb":$('#projectdb').val(),
          "taskdb":$('#taskdb').val(),
          "resultdb":$('#resultdb').val()
      }
    };

    $.ajax(settings).done(function (response) {
        if(response.status=="ok"){
            $('#user-modal').modal('hide');
            reload();
        }else if(response.status=="error"){
            alert(response.detail);
        }
    });
});

function loadUser(){

    var settings = {
      "async": true,
      "dataType" : "json",
      "url": "user/load",
      "method": "GET"
    };

    $.ajax(settings).done(function (response) {
        $("#user-tbody").children().remove();
        inHtml = "";
        for (var i=0; i<response.length; i++){
            inHtml +=
            '<tr data-id="'+ response[i].username +'">' +
            '<th scope="row">'+ (i+1) +'</th>' +
            '<td>'+ response[i].username +'</td>' +
            '<td>'+ response[i].description +'</td>' +
            getTypeHtml(response[i].type) +
            getStatusHtml(response[i].status) +
            getOperationHtml(response[i].status) +
            '</tr>' +
            '';
        }
        $("#user-tbody").append(inHtml)
    });
}

$('#user-tbody').on('click','.btn-delete', function (e) {
    if(confirm("确认删除吗")){
        //alert($(this).parent().parent().data('id'));
        deleteUser($(this).parent().parent().data('id'))
    } else {
        return;
    }
});

function deleteUser(username){

    var settings = {
      "async": true,
      "dataType" : "json",
      "url": "user/delete",
      "method": "POST",
      "data": {
          "username":username
      }
    };

    $.ajax(settings).done(function (response) {
        if(response.status=="ok"){
            reload();
        }else if(response.status=="error"){
            alert(response.detail);
        }
    });
}

function getUserType_to_start(username,hint,action){
	    var settings = {
	      "async": true,
	      "dataType" : "json",
	      "url": "user/get",
	      "method": "POST",
	      "data": {
	          "username":username
	      }
	    };

	    $.ajax(settings).done(function (response) {
	    		var user_type = response.type;
	    		alert("gets:"+user_type);
	    		if(confirm(hint)){
	    	        executeCommand(username,user_type,action);
	    	    } else {
	    	        return;
	    	    }
	    });
}

$('#user-tbody').on('click','.btn-start', function (e) {
    var username = $(this).parent().parent().data('id');
    getUserType_to_start(username,"确认启动吗","start");
});

$('#user-tbody').on('click','.btn-stop', function (e) {
    var username = $(this).parent().parent().data('id');
    getUserType_to_start(username,"确认停止吗","stop");
});

$('#user-tbody').on('click','.btn-restart', function (e) {
    var username = $(this).parent().parent().data('id');
    getUserType_to_start(username,"确认重启吗","restart");
});

function executeCommand(username,user_type,action){
	alert(username+user_type);
    var settings = {
      "async": true,
      "dataType" : "json",
      "url": "user/"+action,
      "method": "POST",
      "data": {
          "username":username,
          "user_type":user_type
      }
    };

    $.ajax(settings).done(function (response) {
        if(response.status=="ok"){
            reload();
        }else if(response.status=="error"){
            alert(response.detail);
        }
    });
}


$('#user-tbody').on('click','.btn-detail', function (e) {

    var settings = {
      "async": true,
      "dataType" : "json",
      "url": "user/getlink",
      "method": "POST",
      "data": {
          "username":$(this).parent().parent().data('id')
      }
    };

    $.ajax(settings).done(function (response) {
        //alert(response.link);
        window.open(response.link);
    });

});

$('#user-tbody').on('click','.btn-edit', function (e) {

    editUser($(this).parent().parent().data('id'))

});

function editUser(username){
    $('#username').attr("disabled",true);
    var settings = {
      "async": true,
      "dataType" : "json",
      "url": "user/get",
      "method": "POST",
      "data": {
          "username":username
      }
    };

    $.ajax(settings).done(function (response) {
        $('#username').val(response.username);
        $('#description').val(response.description);
        $('#password').val(response.password);
        $('#type').val(response.type);
        $('#webuiport').val(response.webuiport);
        $('#schedulerport').val(response.schedulerport);
        $('#projectdb').val(response.projectdb);
        $('#taskdb').val(response.taskdb);
        $('#resultdb').val(response.resultdb);
        $('#user-modal').modal('show');
    });
}

function getStatusHtml(status){
    if(status=="running"){
        text="运行中";
        color="green";
    }else if(status=="stop"){
        text="已停止";
        color="red";
    }else{
        text="异常";
        color="orange";
    }
    return '<td style="color: '+ color +'">'+ text +'</td>';
}

function getTypeHtml(type){
    if(type=="basic"){
        text="基本套餐";
    }else if(type=="premium"){
        text="高级套餐";
    }else if(type=="ultimate"){
        text="旗舰套餐";
    }else{
        text="未知套餐";
    }
    return '<td>'+ text +'</td>';
}

function getOperationHtml(status){
    if(status=="running"){
        disabledStart='disabled="disabled"';
        disabledStop='';
        disabledRestart='';
        disabledEdit='disabled="disabled"';
        disabledDelete='disabled="disabled"';
        disabledLink='';
    }else if(status=="stop"){
        disabledStart='';
        disabledStop='';
        disabledRestart='';
        disabledEdit='';
        disabledDelete='';
        disabledLink='disabled="disabled"';
    }else{
        disabledStart='';
        disabledStop='';
        disabledRestart='';
        disabledEdit='';
        disabledDelete='';
        disabledLink='';
    }



    return '<td>' +
            '<button type="button" class="btn btn-sm btn-success btn-start" '+disabledStart+'>启动</button>' +
            '<button type="button" class="btn btn-sm btn-danger btn-stop" '+disabledStop+'>停止</button>' +
            '<button type="button" class="btn btn-sm btn-warning btn-restart" '+disabledRestart+'>重启</button>' +
            '<button type="button" class="btn btn-sm btn-primary btn-edit"  '+disabledEdit+'>编辑</button>' +
            '<button type="button" class="btn btn-sm btn-danger btn-delete"  '+disabledDelete+'>删除</button>' +
            '<button type="button" class="btn btn-sm btn-default btn-detail" '+disabledLink+'>查看详情</button>' +
            '</td>';
}