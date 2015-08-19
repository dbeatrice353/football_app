

// create the module and name it "fanalyticalApp"
// include ngRoute to manage routing
app = angular.module('fanalyticalApp',['ngRoute']);

// configure the routes
fanalyticalApp.config(function($routeProvider) {
      $routeProvider
          .when('/test-route', {
              controller  : 'mainController'
          })
  });

app.controller('mainController', function(){
  alert("test!");
})
