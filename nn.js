function read(){
	jQuery.get('nnn.txt',function(txt){
		$('#content').text(txt);
		});
	}
	