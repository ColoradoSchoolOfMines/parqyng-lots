$(function(){
    var socket = io.connect('/pingpong', {'resource':'socketio'});
    socket.on('pong',function(data){
        $('#result').append(data.sound + '<br/>');
    });
    socket.on('error',function(error, info) {
        if (error == 'method_access_denied') { alert(info); }
        else { console.log(info); alert(error); }
    });
    $('.ping').click(function(event){
        event.preventDefault();
        socket.emit('ping',{'type':$(this).data('attack')});
    });
});
