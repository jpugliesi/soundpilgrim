var tracks = [];
var widgets = $('iframe');
var num_widgets = widgets.length;

widgets.each(function(index, value){ 
	tracks.push(SC.Widget(value));
	if(index < num_widgets-1){
		tracks[index].bind(SC.Widget.Events.FINISH, function(){
			tracks[index+1].play();
		});
	}
 });
