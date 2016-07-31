from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from openfonacide.models import *

@admin.register(NotificacionesReportes)
class NotificacionesReportesAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Notificaciones", {
            'fields': ('email',),
            'description': "A este correo se enviar&aacute;n notificaciones por cada <strong>Reporte</strong> de la "
                           "ciudadan&iacute;a sobre las prioridades."
        }),
    )

# AUN NO IMPLEMENTADO
# @admin.register(NotificacionesCambioDeEstado)
# class NotificacionesCambioDeEstadoAdmin(admin.ModelAdmin):
#     fieldsets = (
#         ("Notificaciones", {
#             'fields': ('email',),
#             'description': "A este correo se enviar&aacute;n notificaciones por cada <strong>Cambio de Estado</strong> "
#                            "en las obras."
#         }),
#     )
#
#
# @admin.register(NotificacionesVerificacion)
# class NotificacionesVerificacionAdmin(admin.ModelAdmin):
#     fieldsets = (
#         ("Notificaciones", {
#             'fields': ('email',),
#             'description': "A este correo se enviar&aacute;n notificaciones por cada "
#                            "<strong>Verificaci&oacute;n</strong> hecha sobre el Estado de una obra."
#         }),
#     )


####### IMPORTACION ####################
class ImportacionResource(resources.ModelResource):
    class Meta:
        model = Importacion


@admin.register(Importacion)
class ImportacionAdmin(ImportExportModelAdmin):
    resource_class = ImportacionResource
    pass


####### ADJUDICACION ####################
class AdjudicacionResource(resources.ModelResource):
    class Meta:
        model = Adjudicacion


@admin.register(Adjudicacion)
class AdjudicacionAdmin(ImportExportModelAdmin):
    resource_class = AdjudicacionResource
    pass


class PlanificacionResource(resources.ModelResource):
    class Meta:
        model = Planificacion
        # exclude = ('id',)


@admin.register(Planificacion)
class PlanificacionAdmin(ImportExportModelAdmin):
    resource_class = PlanificacionResource
    pass

####### ESTABLECIMIENTO ####################

class EstablecimientoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'nombre_distrito','nombre_departamento')
    search_fields = ['nombre', 'nombre_distrito','nombre_departamento' , 'codigo_establecimiento']


class EstablecimientoResource(resources.ModelResource):
    class Meta:
        model = Establecimiento
        # exclude = ('id',)

admin.site.register(Establecimiento,EstablecimientoAdmin )
#@admin.register(Establecimiento)
class EstablecimientoAdmin(ImportExportModelAdmin):
    resource_class = EstablecimientoResource
    pass

####### INSTITUCIONES ####################
class InstitucionAdmin(admin.ModelAdmin):
    list_display = ('nombre_institucion', 'nombre_distrito','nombre_departamento')
    search_fields = ['nombre_institucion', 'nombre_distrito','nombre_departamento' , 'codigo_institucion']


class InstitucionResource(resources.ModelResource):
    class Meta:
        model = Institucion
        # exclude = ('id',)

admin.site.register(Institucion,InstitucionAdmin )

class InstitucionAdmin(ImportExportModelAdmin):
    resource_class = InstitucionResource
    pass

####### SANITARIO ####################
class SanitariosResource(resources.ModelResource):
    class Meta:
        model = Sanitario
        # exclude = ('id',)


@admin.register(Sanitario)
class SanitariosAdmin(ImportExportModelAdmin):
    search_fields = ['periodo','codigo_institucion','codigo_establecimiento', 'nombre_institucion', 'nombre_distrito','nombre_departamento']
    list_display = ('periodo','codigo_institucion','codigo_establecimiento', 'nombre_institucion', 'nombre_distrito','nombre_departamento' )
    resource_class = SanitariosResource
    pass

####### ESPACIOS ####################
class EspaciosResource(resources.ModelResource):
    
    class Meta:
        model = Espacio

        # exclude = ('id',)


@admin.register(Espacio)
class EspaciosAdmin(ImportExportModelAdmin):
    search_fields = ['periodo','codigo_institucion','codigo_establecimiento', 'nombre_institucion', 'nombre_distrito','nombre_departamento']
    list_display = ('periodo','codigo_institucion','codigo_establecimiento', 'nombre_institucion', 'nombre_distrito','nombre_departamento' )
    resource_class = EspaciosResource
    pass


####### MOBILIARIO ####################
class MobiliariosResource(resources.ModelResource):
   
    class Meta:
        model = Mobiliario
        # exclude = ('id',)


@admin.register(Mobiliario)
class MobiliariosAdmin(ImportExportModelAdmin):
    search_fields = ['periodo','codigo_institucion','codigo_establecimiento', 'nombre_institucion', 'nombre_distrito','nombre_departamento']
    list_display = ('periodo','codigo_institucion','codigo_establecimiento', 'nombre_institucion', 'nombre_distrito','nombre_departamento' )
    resource_class = MobiliariosResource
    pass


class EstadosResource(resources.ModelResource):
    class Meta:
        model = ServicioBasico
        # exclude = ('id',)


@admin.register(ServicioBasico)
class EstadosAdmin(ImportExportModelAdmin):
    resource_class = EstadosResource
    pass
