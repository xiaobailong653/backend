$(function() {
    particlesJS.load('particles-js', '/static/json/particles.json');
    $('#close').click(function() {
        $('#alert').hide();
    })
});


angular.module('app', []).controller('mainCtrl', function($scope, $http) {
    $scope.user = {username: '',password: '', role: "1"};
    $scope.enterEvent = function(e) {
        var keycode = window.event?e.keyCode:e.which;
        if(keycode==13){
            $scope.submit();
        }
    };
    $scope.submit = function() {
        $http.post('/login/', $scope.user).then(function(res){
            var query_params_string = window.location.search || ''; // ?next=/
            var next_params = '/';
            var split_once = query_params_string.split('&');
            if (split_once.length >= 1) {
                var split_two = split_once[0].split('=');
                if (split_two.length >= 2) {
                    next_params = split_two[1];
                }
            }
            next_params += window.location.hash || '';
            if(res.data.code == 1)  return window.location.href = next_params;
            $('#alert').show();
        })
    }
});
