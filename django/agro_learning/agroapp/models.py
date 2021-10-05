# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Cultivos(models.Model):
    idcultivos = models.AutoField(db_column='idCultivos', primary_key=True)  # Field name made lowercase.
    nombrecultivo = models.CharField(db_column='NombreCultivo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    alturamaxima = models.FloatField(db_column='AlturaMaxima', blank=True, null=True)  # Field name made lowercase.
    semanamax = models.IntegerField(db_column='SemanaMax', blank=True, null=True)  # Field name made lowercase.
    tasacresi = models.FloatField(db_column='TasaCresi', blank=True, null=True)  # Field name made lowercase.
    cantidad = models.IntegerField(db_column='Cantidad', blank=True, null=True)  # Field name made lowercase.
    precioinicial = models.FloatField(db_column='PrecioInicial', blank=True, null=True)  # Field name made lowercase.
    estadocultivo_idestadocultivo = models.ForeignKey('Estadocultivo', models.DO_NOTHING, db_column='EstadoCultivo_idEstadoCultivo')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cultivos'


class Cultivosvsprocesos(models.Model):
    idcultivovsproce = models.AutoField(db_column='idCultivoVsProce', primary_key=True)  # Field name made lowercase.
    cultivos_idcultivos = models.ForeignKey(Cultivos, models.DO_NOTHING, db_column='Cultivos_idCultivos')  # Field name made lowercase.
    procesoscultivos_codigo_cultivo = models.ForeignKey('Procesoscultivos', models.DO_NOTHING, db_column='ProcesosCultivos_CODIGO_Cultivo')  # Field name made lowercase.
    cultivoscosechados = models.CharField(db_column='CultivosCosechados', max_length=120, blank=True, null=True)  # Field name made lowercase.
    precio = models.FloatField(db_column='Precio', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cultivosvsprocesos'


class Estadocultivo(models.Model):
    idestadocultivo = models.AutoField(db_column='idEstadoCultivo', primary_key=True)  # Field name made lowercase.
    nombredeestado = models.CharField(db_column='NombreDeEstado', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'estadocultivo'


class Ofertademandaregistros(models.Model):
    idofertademandaregistros = models.AutoField(db_column='idOfertaDemandaRegistros', primary_key=True)  # Field name made lowercase.
    partidasusuarios_idpartidasusuarios = models.ForeignKey('Partidasusuarios', models.DO_NOTHING, db_column='PartidasUsuarios_idPartidasUsuarios')  # Field name made lowercase.
    cantidad = models.IntegerField(db_column='Cantidad', blank=True, null=True)  # Field name made lowercase.
    preciototal = models.FloatField(db_column='PrecioTotal', blank=True, null=True)  # Field name made lowercase.
    producacum = models.FloatField(db_column='ProducAcum', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ofertademandaregistros'


class Partidasusuarios(models.Model):
    idpartidasusuarios = models.AutoField(db_column='idPartidasUsuarios', primary_key=True)  # Field name made lowercase.
    usuarios_idusuario = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='usuarios_IDUsuario')  # Field name made lowercase.
    nombre_finca = models.CharField(db_column='Nombre_finca', max_length=45, blank=True, null=True)  # Field name made lowercase.
    semanas = models.IntegerField(db_column='Semanas', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'partidasusuarios'


class Procesoscultivos(models.Model):
    codigo_cultivo = models.AutoField(db_column='CODIGO_Cultivo', primary_key=True)  # Field name made lowercase.
    agua = models.FloatField(db_column='Agua', blank=True, null=True)  # Field name made lowercase.
    semana = models.IntegerField(db_column='Semana', blank=True, null=True)  # Field name made lowercase.
    alturacultivo = models.FloatField(db_column='AlturaCultivo', blank=True, null=True)  # Field name made lowercase.
    partidasusuarios_idpartidasusuarios = models.ForeignKey(Partidasusuarios, models.DO_NOTHING, db_column='PartidasUsuarios_idPartidasUsuarios')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'procesoscultivos'


class Registrosdeentradassalidas(models.Model):
    codigo_registro = models.AutoField(db_column='CODIGO_Registro', primary_key=True)  # Field name made lowercase.
    entrada = models.DateTimeField(db_column='Entrada', blank=True, null=True)  # Field name made lowercase.
    salida = models.DateTimeField(db_column='Salida', blank=True, null=True)  # Field name made lowercase.
    usuarios_idusuario = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='usuarios_IDUsuario')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'registrosdeentradassalidas'


class TipoUsuario(models.Model):
    nombre_usuario = models.CharField(db_column='Nombre_usuario', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tipo_usuario'


class Usuarios(models.Model):
    idusuario = models.AutoField(db_column='IDUsuario', primary_key=True)  # Field name made lowercase.
    nombres = models.CharField(db_column='Nombres', max_length=45)  # Field name made lowercase.
    apellidos = models.CharField(db_column='Apellidos', max_length=45)  # Field name made lowercase.
    numero_celular = models.CharField(db_column='Numero_celular', max_length=15)  # Field name made lowercase.
    correo = models.CharField(max_length=50, blank=True, null=True)
    nombre_usuario = models.CharField(max_length=20)
    contraseña = models.CharField(max_length=50)
    dataderegistro = models.DateTimeField(db_column='DataDeRegistro', blank=True, null=True)  # Field name made lowercase.
    tipo_usuario = models.ForeignKey(TipoUsuario, models.DO_NOTHING)
    estadocultivo_idestadocultivo = models.ForeignKey(Estadocultivo, models.DO_NOTHING, db_column='EstadoCultivo_idEstadoCultivo')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'usuarios'