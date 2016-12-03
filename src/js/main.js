var myApp = angular.module('learningApp', []);
myApp.controller('IndexController', function($scope, $http, $location) {
    $scope.courses = [];
    $scope.notes = [];
    $scope.quizLoaded = false;
    $scope.i = 0;
    $scope.answered = 0;
    $scope.input = {userAnswer: ''};
    $scope.savedAnswer = '';

    $scope.initRound = function() {
        $scope.input.userAnswer = '';
        $scope.answered = 0;
    };

    $scope.quizAnswer = function () {
        $scope.savedAnswer = $scope.input.userAnswer;
        $scope.answered = 1;
    };

    $scope.quizCorrect = function () {
        $scope.i++;
        if($scope.i < $scope.notes.length)
            $scope.initRound();
    };

    $scope.quizWrong = function () {
        $scope.i++;
        if($scope.i < $scope.notes.length)
            $scope.initRound();
    };

    $http({
        method: 'GET',
        url: '/api/courses'
    }).then(function successCallback(response) {
        $scope.courses = response.data;
    }, function errorCallback(response) {
        console.log(response);
    });

    $scope.coursePicked = function(id) {
        console.log(id);
        $http({
            method: 'GET',
            url: '/api/notes/' + id
        }).then(function successCallback(response) {
            $scope.notes = response.data;
            $scope.initRound();
            $scope.quizLoaded = true;
        }, function errorCallback(response) {
            console.log(response);
        });
    }
});
