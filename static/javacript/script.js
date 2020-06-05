/*This action method calls on submit button to response the user input request and shows the result on screen */
('#idform').on('submit', function () {
	$.getJSON('/background_process', {
	    domain: $('input[name="domain"]').val(),
		}, function(data) {
		$("#result").text(data.result);
		});
		return false;
		});
