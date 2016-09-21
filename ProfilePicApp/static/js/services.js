register.service('RegisterService', function($http){

	this.RegisterPost = function(data){
		$http(data)
		.success(function(data){
			toastr["success"]("Registered Successfully.")
		})
		.error(function(data){
			toastr["error"]("Username or email id already exists.")
		})
	}
});