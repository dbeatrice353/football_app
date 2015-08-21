

// create the module and name it "fanalyticalApp"
// include ngRoute to manage routing
app = angular.module('fanalyticalApp',['ngRoute']);

app.controller('mainController', function($scope){
  // keep track of which view is visible
  $scope.current_view_id = null;

  // these variables connect to the content tags in the views
  $scope.position_value = null;
  $scope.team_value = null;
  $scope.position_value =  null;

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

  $scope.show_player= function(value){
    var view_id = 'players_view';
    show_view(view_id);
    $scope.position_value = value;
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
