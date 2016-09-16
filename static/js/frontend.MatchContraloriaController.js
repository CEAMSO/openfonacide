(function () {
    /**
     * Controlador de Match Difuso
     */
    angular.module('frontEnd')
        .controller('MatchContraloriaController', ['$scope', 'backEnd', '$timeout', function ($scope, backEnd, $timeout) {

            var controller = this;
            controller.guardar = function () {
                var data_list = new Array();
                $('.checkbox input:checked').each(function (idx, el) {
                    var tmp_obj = {
                        'id_llamado': $(el).data('llamado'),
                        'codigo_institucion': $(el).data('institucion'),
                        'periodo': $(el).data('periodo'),
                        'indice': $(el).data('indice'),
                        'id': $(el).data('databaseid')
                    };
                    data_list.push(tmp_obj);
                });
                $('#each_match_controller').addClass('active');
                $('#each_match_controller').show();
                backEnd.temporal.save(JSON.stringify(data_list), function (data) {
                    var respuesta_list = data['resultado'];
                    var resultados = $scope.resultados;
                    for (var respuesta in respuesta_list) {
                        resultados.splice(respuesta_list[respuesta], 1);
                    }

                }).$promise.finally(function () {
                        $('#each_match_controller').removeClass('active');
                        $('#each_match_controller').hide();
                    });

            };
            
          
       
         
        
        }]);

})();
