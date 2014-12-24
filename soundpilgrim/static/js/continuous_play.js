function continuousPlayEval(){
	console.log("This is a test");
	var tracks = [];
	var widgets = $('iframe');
	var num_widgets = widgets.length;

	widgets.each(function(index, value){ 
		tracks.push(SC.Widget(value));
		if(index < num_widgets-1){
			tracks[index].bind(SC.Widget.Events.READY, function(){
				tracks[index].bind(SC.Widget.Events.FINISH, function(){
					setTimeout(function(){
						tracks[index+1].play();
					}, 1000);
				});
			});
			if(index == num_widgets-2){
			    //For the second to last widget, once play starts, load next page
			    tracks[index].bind(SC.Widget.Events.PLAY, function(){
				console.log("Load Next Page");
				$('.endless_more').click();
			    });
			}
		}
	 });
}
