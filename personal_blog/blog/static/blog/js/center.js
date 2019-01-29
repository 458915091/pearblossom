var index=0
$(function(){
	$('.center .menu li').click(function(){
		index=$('.center .menu li').index($(this));
		$(this).addClass('activate').siblings().removeClass('activate');
		if(index==0){
			$('.center .select').addClass('one').removeClass('two').removeClass('three').removeClass('four');
		}else if(index==1){
			$('.center .select').addClass('two').removeClass('one').removeClass('three').removeClass('four');
		}else if(index==2){
			$('.center .select').addClass('three').removeClass('one').removeClass('two').removeClass('four');
		}else if(index==3){
			$('.center .select').addClass('four').removeClass('one').removeClass('two').removeClass('three');
		}
	})
});

$(function(){
	$('#file_input').click(function(){
		$('.center .content input.imgfile').click();
	})
});

$(function(){
	$('.center .content input.imgfile').on('change', function(){
		var choose_file = $(this)[0].files[0];
		var reader = new FileReader();
		reader.readAsDataURL(choose_file);
		reader.onload = function(){
			$('.body .center .content p img.face').attr('src', reader.result);
		};
		$('.body .center .informations #file_input span.before').css('display','none');
		$('.body .center .informations #file_input span.after').css('display','block');
	});
})