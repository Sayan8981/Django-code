# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
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
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

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


class Employee(models.Model):
    employee_id = models.IntegerField(primary_key=True,verbose_name="Employee_ID")
    employee_name = models.CharField(max_length=1500, blank=True, null=True,verbose_name="Employee_Name")
    id = models.IntegerField(blank=True, null=True,verbose_name="ID")

    class Meta:
        managed = False
        db_table = 'employee'
        ordering=['id','employee_id','employee_name']


class EmployeeDetails(models.Model):
    employee_addr = models.CharField(max_length=1000, blank=True, null=True,verbose_name="Employee_Addr")
    employee_mobile_number = models.IntegerField(blank=True, null=True,verbose_name="Employee_contact_No")
    employee_designation = models.CharField(max_length=1000, blank=True, null=True,verbose_name="Post")
    employee_city = models.CharField(max_length=500, blank=True, null=True,verbose_name="City")
    employee_blood_grp = models.CharField(db_column='employee_Blood_grp', max_length=200, blank=True, null=True,
                         verbose_name="Blood_Group")  # Field name made lowercase.
    employee = models.ForeignKey(Employee, models.DO_NOTHING, blank=True, null=True,verbose_name="Employee_ID")
    id = models.IntegerField(primary_key=True,verbose_name="ID")
    doj = models.ForeignKey('EmployeeSalary', models.DO_NOTHING, db_column='DOJ', blank=True, null=True,
                         verbose_name="Date of Joining")  # Field name made lowercase

    # @property
    # def date_of_join(self):
    #     return self.doj

    class Meta:
        managed = False
        db_table = 'employee_details'
        ordering=['employee','employee_addr','employee_designation','employee_mobile_number','employee_city'
                 ,'employee_blood_grp'] 

class EmployeeSalary(models.Model):
    employee = models.ForeignKey(Employee, models.DO_NOTHING, blank=True, null=True,verbose_name="Employee_ID")
    employee_salary_monthly = models.CharField(db_column='employee_salary_Monthly', max_length=20000, blank=True,
                            verbose_name="Salary(per month)", null=True)  # Field name made lowercase.
    doj = models.CharField(db_column='DOJ', primary_key=True, max_length=200,verbose_name="Date of joining")# Field name made lowercase.
    id = models.IntegerField(blank=True, null=True,verbose_name="ID")

    class Meta:
        managed = False
        db_table = 'employee_salary'
        ordering=['id','employee','employee_salary_monthly','doj']
