
// create the module and name it "fanalyticalApp"
// include ngRoute to manage routing
app = angular.module('fanalyticalApp',['ngRoute']);

app.controller('mainController', function($scope,$http){
  // keep track of which view is visible
  $scope.current_view_id = null;

  // these variables connect to the content tags in the views
  $scope.position_value = null;
  $scope.team_value = null;

  $scope.player = {
                    name: null,
                    team: null,
                    college: null,
                    age: null,
                    height: null,
                    weight: null,
                    DOB: null
                  };
  //$scope.player = {
  //  name: null,
  //  team: null,
  //  college: null,
  //  age: null,
  //  height: null,
  //  weight: null,
  //  DOB: null;
  //};

  $scope.close_current_view = function(){
    hide_element($scope.current_view_id);
    $scope.current_view_id = null;
  }

  $scope.show_position = function(value){
    var view_id = 'positions_view';
    show_view(view_id);
    $scope.position_value = value;
  };

  $scope.show_team = function(value){
    var view_id = 'teams_view';
    show_view(view_id);
    $scope.team_value = value;
  };

  $scope.show_player = function(player_id){
    // specify the type of view we want
    var view_id = 'players_view';
    // define the request
    $http.get("/player_profile/" + String(player_id))
    // on success, do the following:
    .success(function(response) {
      // update the page with the new data
      set_player_data(response)
      // make the updated portion of the page visible
      show_view(view_id);
      });
  };

  set_player_data = function(player){
    $scope.player.name = player.name;
    $scope.player.team = player.team;
    $scope.player.college = player.college;
    $scope.player.age = player.age;
    $scope.player.height = player.height;
    $scope.player.weight = player.weight;
    $scope.player.DOB = player.DOB;
  };

  // Show the proper view
  show_view = function(view_id){
    if($scope.current_view_id != view_id){
      if($scope.current_view_id){
        hide_element($scope.current_view_id);
      }
      $scope.current_view_id = view_id
      show_element(view_id);
    }
  }

  // hide an element via it's id
  hide_element = function(element_id){
    var element = $('#' + element_id);
    element.slideUp();
    //element.css("display","none")
  };

  // show an element via it's id
  show_element = function(element_id){
    var element = $('#' + element_id);
    element.slideDown();
    //$('#' + element_id).css("display","inline")
  };

})

// hide all views
// show a progress bar
// request data from server
// on timeout or failure
//      close progress bar
//      show previous view if there was one
//      show "failure" popup
// on sucess
//      turn off the progress bar
//      load the received data into the proper view
//      turn on the proper view
