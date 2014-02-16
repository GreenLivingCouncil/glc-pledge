'use strict';

/* Controllers */

function FormCtrl($scope, $http, $location, $routeParams) {
    $scope.eventCode = $routeParams.event;
    $scope.formMethod = 'POST';
    $scope.teamError = '';
    $scope.adminMode = ($routeParams.referrer == "admin");
    // Get event-specific information from the config
    $scope.eventData = _events[$routeParams.event];
    // Get user data through WebAuth.
    // The resulting user object should at least contain the fields "name", "email".
    $http.get(_paths.cgiBin + 'getWebAuthToken.py').
    success(function(data) {
        $scope.user = ($scope.adminMode) ? {} : data;
        $scope.user.private = false;
        $scope.user.comments = '';
        $scope.user.eventId = $scope.eventData.id;
        $scope.user.referrer = ($routeParams.referrer) ? 
            ($scope.adminMode ? data.sunetId : $routeParams.referrer) : '';
    });

    if (!$scope.adminMode) {
        $http.get(_paths.cgiBin + 'hasPledged.py?eventId=' + $scope.eventData.id).
        success(function(data) {
            $scope.hasPledged = data.hasPledged;
        });
    }

    // Form submission callback
    $scope.submit = function() {
        // Display warning and abort submission if no residence selected.
        if (!$scope.user.teamId) {
            $scope.teamError = "Please select a team.";
            return;
        }
        // POST form to the cgi script at the specific formURL
        $http({ 
            method: $scope.formMethod, 
            url: _paths.cgiBin + 'submitPledge.py',
            data: $scope.user 
        }). 
        success(function(data, status) { 
            $scope.status = status; 
            //$scope.formResponse = data; 
            //console.log(data);
            if (data.success) {
                location.reload();
            } else {
                alert("Form submission failed. Please refresh and try again.");
            }
        }). 
        error(function(data, status) { 
            $scope.formResponse = data || "Request failed"; 
            $scope.status = status; 
            alert("Form submission failed. Please refresh and try again.");
        }); 
    };
    // Function to get the team name TODO: this is copy-pasta!!
    $scope.getTeamName = function(teamId) {
        return this.eventData.teamList[parseInt(teamId)].name;
    };
}

function UpdatesCtrl($scope, $http) {
    // Get recent pledge list
    $http.get(_paths.cgiBin + 'getRecentPledges.py?limit=5&eventId=' + $scope.eventData.id).success(function(data) {
        $scope.recentPledges = data.pledges;
    });
}

function ThanksCtrl($scope, $routeParams, $http) {
    $http.get(_paths.cgiBin + 'getWebAuthToken.py').success(function(data) {
        $scope.sunetId = data.sunetId;
	$scope.refURL = encodeURIComponent("/group/glc/pledge/#/") + $scope.eventCode + encodeURIComponent("/form/") + $scope.sunetId;
    });
    $scope.eventCode = $routeParams.event;
    if (parseInt($routeParams.firstTime)) {
        $scope.message = "You are awesome.";
    } else {
        $scope.message = "It looks like you've already pledged&mdash;only one pledge per person counts.";
    }
}

function CountsCtrl($scope, $routeParams, $http) {
    $scope.eventCode = $routeParams.event;
    // Get event-specific information from the config
    $scope.eventData = _events[$scope.eventCode];
    $http.get(_paths.cgiBin + 'getPledgeCounts.py?eventId=' + $scope.eventData.id).success(function(data) {
        $scope.counts = data;
    });
    // Function to get the team name
    $scope.getTeamName = function(teamId) {
        return this.eventData.teamList[parseInt(teamId)].name;
    }
    // Function to get the team percentage pledged
    $scope.getTeamPercent = function(teamId, count) {
        var result = parseFloat(count) / parseFloat(this.eventData.teamList[parseInt(teamId)].size);
        return (Math.round(result*100)).toString();
    }
}

function RefCountsCtrl($scope, $routeParams, $http) {
    $scope.eventCode = $routeParams.event;
    $http.get(_paths.cgiBin + '/getWebAuthToken.py').success(function(data) {
        $scope.referrer = data.sunetId;
        $scope.person = "people";
	$scope.refURL = encodeURIComponent("/group/glc/pledge/#/") + $scope.eventCode + encodeURIComponent("/form/") + $scope.referrer;
        // Get count
        $http.get(_paths.cgiBin + '/getReferralCount.py').success(function(data) {
            $scope.count = parseInt(data.count);
            if ($scope.count == 1) {
                $scope.person = "person";
            }
        });
    });
}
// TODO: move this into main page?

function MenuCtrl($scope) {
    $scope.eventData = _events;
}
