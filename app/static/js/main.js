

// create the module and name it "fanalyticalApp"
// include ngRoute to manage routing
app = angular.module('fanalyticalApp',['ngRoute']);

app.controller('mainController', function($scope){
  $scope.test_data = "test";
  $scope.change_data = function(){
    $scope.test_data = "Ha!";
  };
})
