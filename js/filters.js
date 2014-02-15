'use strict';

/* Filters */

angular.module('PledgeApp.filters', []).
  filter('interpolate', ['version', function(version) {
    return function(text) {
      return String(text).replace(/\%VERSION\%/mg, version);
    }
  }]).
  filter('fromNow', function() {
    return function(dateString) {
        var date = new Date(dateString);
        return moment(date).fromNow();
    }
  });
