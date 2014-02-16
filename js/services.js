'use strict';

/* Services */


// Demonstrate how to register services
// In this case it is a simple value service.
angular.module('PledgeApp.services', [], function($provide) {
    $provide.value('version', '1.1');
});

