'use strict';

/* Services */


// Demonstrate how to register services
// In this case it is a simple value service.
angular.module('PledgeApp.services', [], function($provide) {
    $provide.value('version', '1.0');
    /*
    $provide.factory('config', ['$http', function(http) { 
        http.get('config/events.json').success(function(eventsData) {
            http.get('config/paths.json').success(function(pathsData) {
                var result = { "events": eventsData, "paths": pathsData };
                alert("hello");
                return result;
            });
        });
    }]);
    */
});

