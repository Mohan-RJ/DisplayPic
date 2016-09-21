register.controller('registerController', function($scope, $http, RegisterService){

	//Validate the registration form and submit data to backend
	$scope.registerclick = function(){
		var data = {
			method: 'POST',
			url: '/register/',
			data: {
				'username': $scope.username,
				'email': $scope.email,
				'password': $scope.password,
			}
		}
		$scope.postdata = RegisterService.RegisterPost(data);
		$scope.username="";
		$scope.email="";
		$scope.password="";
	}
});

propic.controller('ImageUpload', function($scope, $http, Upload){
	$scope.onFileSelect = function($files) {
    //$files: an array of files selected, each file has name, size, and type.
    // for (var i = 0; i < $files.length; i++) {
      uname = $scope.username;
      
      path = "static/users/+ '://' + uname"
      var $file = $files[0];
      Upload.upload({
        url: "path",
        file: $file,
        progress: function(e){}
      }).then(function(data, status, headers, config) {
        // file is uploaded successfully
        console.log(data);
      }); 
    // }
  }
});