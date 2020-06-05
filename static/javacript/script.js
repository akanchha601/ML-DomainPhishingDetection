/*This action method calls on submit button to response the user input request and shows the result on screen*/
('#idform').on('submit', function (){
	$.getJSON('/application_process', {
	    domain: $('input[name="domain"]').val(),
		}, function(inputData) {
		$("#result").text(inputData.result);
		});
		return false;
		});

