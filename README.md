# notes on the angular app

Kevin,

The SPA consists of a "frame" page, and some javascript to request data and activate/deactivate different portions of that page for the viewer. The "frame" page is app/templates/dashboard.html, and the javascript is in app/static/js/main.js.

The javascript consists of an angular app called "FanalyticalApp". FanalyticalApp does 2 things:

1) it binds buttons and links on the page to methods that acquire and display data.
2) it saves the state of the app (think of a FSM). In concrete terms, the state of the app is just a matter of what view/data is being displayed to the user in the SPA.

A quick note on the html: Each view/data state of the app has a corresponding div in dashboard.html. Each of the state divs are hidden by default. To enter a state, the javascript simply hides the div of the previous state (if applicable), and unhides the div of the new state. Look for a div of class "data-views" in dashboard.html. This parent div contains the different state/view divs.

Let's step through a use case:

1) The user clicks on the name of a player on the side bar of the SPA. 
2) That link causes the js app's method "show_player" to do the following:
  - request the particular player's data from the server
  - place the data in an instance variable
  - show the proper view 
  - register the state change by setting [the app's scope].current_view_id = [the view_id] (this happens in the show_view method)

Thats basically it: Request data, hold it in instance variables, swap out the views, and save the new state.

We can think of each user action that pertains to nfl data in those terms. Use the show_player method as a model.

When you want to start adding to the JS, I would recommend:
a) make a sandbox angular app somewhere else using a tutorial to get the gist of angular. 
b) create a new branch on this app.

That was not an exhaustive explanation, but I should get you started.

Dave


