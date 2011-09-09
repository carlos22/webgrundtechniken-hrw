	$(document).ready(function() {
	
		$('#calendar').fullCalendar({
		
			// Calenadar URL (XML)
			events: 'http://www.google.com/calendar/feeds/deqv6p7psqdabhbuhtgkh4ubfs%40group.calendar.google.com/private-4f8a8649699df7d8df65d22a678ea0f4/basic',
			//events: 'http://www.google.com/calendar/feeds/usa__en%40holiday.calendar.google.com/public/basic',

			eventClick: function(event) {
				// opens events in a popup window
				window.open(event.url, 'gcalevent', 'width=700,height=600');
				return false;
			},
			
			loading: function(bool) {
				if (bool) {
					$('#loading').show();
				}else{
					$('#loading').hide();
				}
			},
			firstDay: 1
			
		});
		
	});
