// Generated by CoffeeScript 1.9.3
(function() {
  var app;

  app = angular.module("app", ['ui.router', "ngResource", "ui.bootstrap", "isteven-multi-select", 'ui.sortable', "angularjs-dropdown-multiselect", "lr.upload"]);

  app.run(function($rootScope) {
    return $rootScope.bos_export = function() {
      return $rootScope.$broadcast('do_export_now');
    };
  });

  app.config(function($stateProvider, $urlRouterProvider, $interpolateProvider, $httpProvider) {
      $interpolateProvider.startSymbol('{(');
      $interpolateProvider.endSymbol(')}');
      $urlRouterProvider.otherwise('');
      return $stateProvider.state('userList', {
          url: '/user/list/',
          templateUrl: '/backend/view/user/list/',
          controller: 'userListCtrl'
      }).state('permissionList', {
          url: '/permission/list/',
          templateUrl: '/backend/view/permission/list/',
          controller: 'permissionListCtrl'
      }).state('productType', {
          url: '/product/type/',
          templateUrl: '/backend/view/product/type/',
          controller: 'productTypeCtrl'
      }).state('productList', {
          url: '/product/list/',
          templateUrl: '/backend/view/product/list/',
          controller: 'productListCtrl'
      }).state('orderList', {
          url: '/order/list/',
          templateUrl: '/backend/view/order/list/',
          controller: 'orderListCtrl'
      }).state('orderTotal', {
          url: '/order/total/',
          templateUrl: '/backend/view/order/total/',
          controller: 'orderTotalCtrl'
      }).state('orderAbnormal', {
          url: '/order/abnormal/',
          templateUrl: '/backend/view/order/abnormal/',
          controller: 'orderAbnormalCtrl'
      });
  });

}).call(this);

// 怎么对url加上参数？
// https://github.com/angular-ui/ui-router/wiki/URL-Routing
