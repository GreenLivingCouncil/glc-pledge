'use strict';


// Declare app level module which depends on filters, and services
angular.module('PledgeApp', ['PledgeApp.filters', 'PledgeApp.services', 'PledgeApp.directives']).
  config(['$routeProvider', function($routeProvider) {
    $routeProvider.when('/:event/form', {templateUrl: 'partials/form.html', controller: FormCtrl});
    $routeProvider.when('/:event/form/:referrer', {templateUrl: 'partials/form.html', controller: FormCtrl});
    $routeProvider.when('/:event/thanks/:firstTime', {templateUrl: 'partials/thanks.html', controller: ThanksCtrl});
    $routeProvider.when('/:event/counts', {templateUrl: 'partials/counts.html', controller: CountsCtrl});
    $routeProvider.when('/:event/referrals', {templateUrl: 'partials/refcounts.html', controller: RefCountsCtrl});
    $routeProvider.when('/menu', {templateUrl: 'partials/menu.html', controller: MenuCtrl});
    $routeProvider.when('/:event', {redirectTo: '/:event/form'});
    $routeProvider.otherwise({redirectTo: '/menu'});
  }]);
