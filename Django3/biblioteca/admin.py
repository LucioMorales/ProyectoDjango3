from django.contrib import admin
from .models import *

# Register your models here.

class MaterialAdmin(admin.ModelAdmin):
    list_display = ['tipoMaterial','codigo','autor','titulo','año','status',]
    list_display_links = ['tipoMaterial','codigo','autor','titulo','año','status',]
    search_fields = ['tipoMaterial','codigo','autor','titulo','año','status',]

class MaterialInline(admin.StackedInline):
    model = Material
    extra = 0
    fields = ['tipoMaterial','autor','titulo','año','status',]

class PersonaAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Descripcion', {
          'fields': ('tipoPersona','nombre','apellido')  
        }),
        ('Datos', {
            'fields': ('correo','telefono',)
        }),
        ('Extra', {
          'fields': ('numLibros','adeudo',)  
        }),
    )
    list_display = ['tipoPersona','nombre','apellido','correo','telefono','numLibros','adeudo',]
    list_display_links = ['tipoPersona','nombre','apellido','correo','telefono','numLibros','adeudo',]
    search_fields = ['tipoPersona','nombre','apellido','correo','telefono','numLibros','adeudo',]

class PersonaInline(admin.StackedInline):
    model = Material
    extra = 0
    fields = ['tipoPersona','nombre','apellido','correo','telefono','numLibros','adeudo',]

class PrestamoAdmin(admin.ModelAdmin):

    inlines = [MaterialInline]

class ProfesorAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Descripcion', {
          'fields': ('tipoPersona','nombre','apellido')  
        }),
        ('Datos', {
            'fields': ('correo','telefono',)
        }),
        ('Extra', {
          'fields': ('numLibros','adeudo','numEmpleado')  
        }),
    )
    list_display = ['numEmpleado',]
    list_display_links = ['numEmpleado',]
    search_fields = ['numEmpleado',]

class AlumnoAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Descripcion', {
          'fields': ('tipoPersona','nombre','apellido')  
        }),
        ('Datos', {
            'fields': ('correo','telefono',)
        }),
        ('Extra', {
          'fields': ('numLibros','adeudo','matricula')  
        }),
    )
    list_display = ['matricula',]
    list_display_links = ['matricula',]
    search_fields = ['matricula',]

class LibroAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Descripcion', {
          'fields': ('tipoMaterial','autor','titulo','portada',)  
        }),
        ('Extra', {
            'fields': ('año','status','editorial')
        }),
    )
    list_display = ['tipoMaterial','codigo','autor','titulo','año','status','editorial',]
    list_display_links = ['tipoMaterial','codigo','autor','titulo','año','status','editorial',]
    search_fields = ['tipoMaterial','codigo','autor','titulo','año','status','editorial',]

class RevistaAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Descripcion', {
          'fields': ('tipoMaterial','autor','titulo',)  
        }),
        ('Extra', {
            'fields': ('año','status',)
        }),
    )
    list_display = ['tipoMaterial','autor','titulo','año','status',]
    list_display_links = ['tipoMaterial','autor','titulo','año','status',]
    search_fields = ['tipoMaterial','autor','titulo','año','status',]

admin.site.register(Prestamo, PrestamoAdmin)
admin.site.register(Persona, PersonaAdmin)
admin.site.register(Profesor, ProfesorAdmin)
admin.site.register(Alumno, AlumnoAdmin)
admin.site.register(Material, MaterialAdmin)
admin.site.register(Libro, LibroAdmin)
admin.site.register(Revista, RevistaAdmin)
