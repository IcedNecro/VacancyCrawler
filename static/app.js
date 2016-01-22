var app = angular.module('indexApp', [])

app.controller('indexController', ['$scope', '$http', function($scope, $http) {
	$scope.current_page = 1
	$scope.filter = {}

	$scope.getList = function(i, limit) {
		if(i && limit) {
			$scope.filter.page = i
			$scope.filter.limit = limit
		}
		if($scope.filter.source == 'any')
			delete $scope.filter.source
		if($scope.filter.like == '')
			delete $scope.filter.like

		$http({
			method: 'GET',
			url: '/api/list',
			params: $scope.filter
		}).success(function(data) {
			$scope.list = data.data;
			$scope.first_page = data.first_page
			$scope.last_page = data.last_page
			$scope.current_page = data.current_page
		})
	}
	$scope.range = function(min, max, step) {
	    step = step || 1;
	    var input = [];
	    for (var i = min; i <= max; i += step) {
	        input.push(i);
	    }
	    return input;
	};
	$scope.getList()
}])