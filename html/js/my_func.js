
function music_ctl(){
	$.ajax({
		type: 'POST',
		url: '/func/music_ctl',
		async: false,
		data: {},
		success: function(res){
			var data = $.parseJSON(res)
			//console.log(data)
			path = "..\\Musics\\" + data.music_num + ".wav";
			console.log(path)
    		$("#jquery_jplayer_1")
    			.jPlayer("stop")
				.jPlayer("setMedia", {wav:path})
    			.jPlayer("play");
		},
		dataType: "text"
	  });
}