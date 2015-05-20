# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group_id', 'permission_id'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type_id', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user_id', 'group_id'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user_id', 'permission_id'),)


class Caja(models.Model):
    idcaja = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    responsable = models.IntegerField(blank=True, null=True)
    activo = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'caja'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    user = models.ForeignKey(AuthUser)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Entidad(models.Model):
    identidad = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    direccion = models.CharField(max_length=100, blank=True, null=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    nit = models.CharField(max_length=20, blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    activo = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'entidad'


class Estadoventa(models.Model):
    idestadoventa = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    activo = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'estadoventa'


class Impuesto(models.Model):
    idimpuesto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    valor = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    activo = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'impuesto'


class Inventariocaja(models.Model):
    idinventariocaja = models.AutoField(primary_key=True)
    idproducto = models.ForeignKey('Producto', db_column='idproducto', blank=True, null=True)
    idcaja = models.ForeignKey(Caja, db_column='idcaja', blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inventariocaja'


class Marca(models.Model):
    idmarca = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    activo = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'marca'


class Menu(models.Model):
    idmenu = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    activo = models.TextField(blank=True, null=True)  # This field type is a guess.
    url = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'menu'


class Parametro(models.Model):
    idparametro = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=5, blank=True, null=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    valor = models.CharField(max_length=45, blank=True, null=True)
    activo = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'parametro'


class Pedido(models.Model):
    idpedido = models.AutoField(primary_key=True)
    idventa = models.ForeignKey('Venta', db_column='idventa', blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    idinventariocaja = models.ForeignKey(Inventariocaja, db_column='idinventariocaja', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pedido'


class Producto(models.Model):
    idproducto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    idproveedor = models.ForeignKey('Proveedor', db_column='idproveedor', blank=True, null=True)
    idmarca = models.ForeignKey(Marca, db_column='idmarca', blank=True, null=True)
    valorunitario = models.IntegerField(blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)
    serie = models.CharField(max_length=15, blank=True, null=True)
    idtipoproducto = models.ForeignKey('Tipoproducto', db_column='idtipoproducto', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'producto'


class Proveedor(models.Model):
    idproveedor = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    activo = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'proveedor'


class Submenu(models.Model):
    idsubmenu = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    activo = models.TextField(blank=True, null=True)  # This field type is a guess.
    url = models.CharField(max_length=45, blank=True, null=True)
    idmenu = models.ForeignKey(Menu, db_column='idmenu', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'submenu'


class Tipodescuento(models.Model):
    idtipodescuento = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    descuento = models.CharField(max_length=10, blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    activo = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'tipodescuento'


class Tipopago(models.Model):
    idtipopago = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    activo = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'tipopago'


class Tipoproducto(models.Model):
    idtipoproducto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    activo = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'tipoproducto'


class Tipousuario(models.Model):
    idtipousuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    activo = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'tipousuario'


class Tipousuariomenu(models.Model):
    idtipousuariomenu = models.AutoField(primary_key=True)
    idmenu = models.ForeignKey(Menu, db_column='idmenu', blank=True, null=True)
    idtipousuario = models.ForeignKey(Tipousuario, db_column='idtipousuario', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipousuariomenu'


class Tipousuariosubmenu(models.Model):
    idtipousuariosubmenu = models.AutoField(primary_key=True)
    idsubmenu = models.ForeignKey(Submenu, db_column='idsubmenu', blank=True, null=True)
    idtipousuario = models.ForeignKey(Tipousuario, db_column='idtipousuario', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipousuariosubmenu'


class Usuario(models.Model):
    idusuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    direccion = models.CharField(max_length=100, blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    cupo = models.IntegerField(blank=True, null=True)
    usuario = models.CharField(max_length=100, blank=True, null=True)
    clave = models.TextField(blank=True, null=True)
    idtipousuario = models.ForeignKey(Tipousuario, db_column='idtipousuario', blank=True, null=True)
    idtipodescuento = models.ForeignKey(Tipodescuento, db_column='idtipodescuento', blank=True, null=True)
    activo = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'usuario'

    def __unicode__(self):
        return str(self.id) + self.name 

    def to_object(self):
        name = None
        description = None
        
        return {        
            'usuario' : {
                'id' : self.usuario.id,
                'nombre' : self.usuario.nombre,
                'usuario' : self.usuario.usuario,
            },
        }


class Venta(models.Model):
    idventa = models.AutoField(primary_key=True)
    idusuario = models.ForeignKey(Usuario, db_column='idusuario', blank=True, null=True)
    valortotal = models.IntegerField(blank=True, null=True)
    idestadoventa = models.ForeignKey(Estadoventa, db_column='idestadoventa', blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    idtipopago = models.ForeignKey(Tipopago, db_column='idtipopago', blank=True, null=True)
    idcaja = models.ForeignKey(Caja, db_column='idcaja', blank=True, null=True)
    factura = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'venta'
