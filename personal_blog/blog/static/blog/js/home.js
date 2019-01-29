// var index=0;
// var time=setInterval(function(){
// 	index++;
// 	if (index>3){
// 		index=0;
// 	}
// 	$('.carousel .carousel_content li').eq(index).fadeIn().siblings().fadeOut();
// },5000);

var time=0;
var position=0;
var index=0;
var runtime=setInterval(function(){
	if(time==0){
		position=position-440;
		index++;
		if (position<-1320){
			position=0;
		}
		if (index>3){
			index=0;
		}
		$('.carousel .carousel_content').css('left',position);
		$('.carousel .carousel_title li').eq(index).addClass('on').siblings().removeClass('on');
		$('.carousel .carousel_point span').eq(index).addClass('on').siblings().removeClass('on');
	}
},5000);

var timeflash=setInterval(function(){
	if (time==1){
		time--;
	}
},2000);


$(function(){
	$('.carousel .carousel_point span').click(function(){
		index=$('.carousel .carousel_point span').index(this);
		position=index* -440;
		time=1;
		$(this).addClass('on').siblings().removeClass('on');
		$('.carousel .carousel_title li').eq(index).addClass('on').siblings().removeClass('on');
		$('.carousel .carousel_content').css('left',position);
	});
});


var actionsone=0;
var actionstwo=340;
var actionstime=setInterval(function(){
	actionsone--;
	actionstwo--;
	if ( actionsone == -340 ){
		actionsone=340;
	}
	if ( actionstwo == -340 ){
		actionstwo=340;
	}
	$('.head .blog_user .default-body img.one').css('left',actionsone);
	$('.head .blog_user .default-body img.two').css('left',actionstwo);
},20);

var span_index=-1;
var span_end=0;
var span_time=setInterval(function(){
	span_index=span_index+1;
	span_end=span_index % 2;
	if ( span_end == 0 ){
		span_color='#4682B4';
	}else{
		span_color='#f25d8e';
	}
	$('.body div.body-item li').eq(span_index).children('span').css('background', span_color);
},1);