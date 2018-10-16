# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TableDesErreurs(models.Model):
    f1 = models.FloatField(db_column='F1', blank=True, null=True)  # Field name made lowercase.
    f2 = models.FloatField(db_column='F2', blank=True, null=True)  # Field name made lowercase.
    f3 = models.FloatField(db_column='F3', blank=True, null=True)  # Field name made lowercase.
    f4 = models.DateTimeField(db_column='F4', blank=True, null=True)  # Field name made lowercase.
    f5 = models.FloatField(db_column='F5', blank=True, null=True)  # Field name made lowercase.
    f6 = models.FloatField(db_column='F6', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        app_label = 'groupamasi'
        managed = True
        db_table = 'Table des erreurs'


class Alternative(models.Model):
    id_alternative = models.AutoField(primary_key=True)
    id_functionnality = models.ForeignKey('Functionnality', models.DO_NOTHING, db_column='id_functionnality', blank=True, null=True)
    name_alternative = models.CharField(max_length=255, blank=True, null=True)
    usage_alternative = models.CharField(max_length=255, blank=True, null=True)
    flag_alternative = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        app_label = 'groupamasi'
        managed = True
        db_table = 'alternative'


class Component(models.Model):
    id_component = models.AutoField(primary_key=True)
    name_component = models.CharField(max_length=255, blank=True, null=True)
    owner_component = models.ForeignKey('Engineer', models.DO_NOTHING, db_column='owner_component', blank=True, null=True)
    id_subsystem = models.ForeignKey('Subsystem', models.DO_NOTHING, db_column='id_subsystem', blank=True, null=True)

    class Meta:
        app_label = 'groupamasi'
        managed = True
        db_table = 'component'


class Defect(models.Model):
    id_defect = models.AutoField(primary_key=True)
    rel_name = models.CharField(db_column='REL_NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    date_defect_start = models.DateTimeField(blank=True, null=True)
    date_defect_end = models.DateTimeField(blank=True, null=True)
    id_recyc = models.IntegerField(blank=True, null=True)
    id_recyc_parent = models.IntegerField(blank=True, null=True)
    name_recyc = models.CharField(max_length=255, blank=True, null=True)
    date_recyc_start = models.DateTimeField(blank=True, null=True)
    date_recyc_end = models.DateTimeField(blank=True, null=True)
    id_bug_bg = models.CharField(max_length=255, blank=True, null=True)
    statut_bg = models.CharField(max_length=255, blank=True, null=True)
    responsible_bg = models.CharField(max_length=255, blank=True, null=True)
    subject_bg = models.CharField(max_length=255, blank=True, null=True)
    summary_bg = models.CharField(max_length=255, blank=True, null=True)
    description_bg = models.TextField(blank=True, null=True)
    comments_dev_bg = models.TextField(blank=True, null=True)
    reproductible_bg = models.CharField(max_length=255, blank=True, null=True)
    severity_bg = models.CharField(max_length=255, blank=True, null=True)
    priority_bg = models.CharField(max_length=255, blank=True, null=True)
    detected_bg = models.CharField(max_length=255, blank=True, null=True)
    date_bg_detection = models.DateTimeField(blank=True, null=True)
    version_bg_detection = models.CharField(max_length=255, blank=True, null=True)
    actual_bg_fix_time = models.CharField(max_length=255, blank=True, null=True)
    date_closing_bg = models.DateTimeField(blank=True, null=True)
    ver_bug_bg_stamp = models.CharField(max_length=255, blank=True, null=True)
    bg_vts = models.CharField(db_column='BG_VTS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    bg_detected_in_rel = models.CharField(db_column='BG_DETECTED_IN_REL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    bg_detected_in_recyc = models.CharField(max_length=255, blank=True, null=True)
    id_report = models.ForeignKey('Report', models.DO_NOTHING, db_column='id_report', blank=True, null=True)

    class Meta:
        app_label = 'groupamasi'
        managed = True
        db_table = 'defect'


class Engineer(models.Model):
    id_eng = models.AutoField(primary_key=True)
    eng_fn = models.CharField(max_length=255, blank=True, null=True)
    eng_ln = models.CharField(max_length=255, blank=True, null=True)
    date_arrival = models.DateTimeField(blank=True, null=True)
    date_departure = models.DateTimeField(blank=True, null=True)
    id_scientific = models.CharField(max_length=255, blank=True, null=True)
    company = models.CharField(max_length=255, blank=True, null=True)
    departement = models.CharField(max_length=255, blank=True, null=True)
    section = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    function = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.eng_fn + ' ' + self.eng_ln

    class Meta:
        app_label = 'groupamasi'
        managed = True
        db_table = 'engineer'


class Functionnality(models.Model):
    id_functionnality = models.AutoField(primary_key=True)
    id_component = models.ForeignKey(Component, models.DO_NOTHING, db_column='id_component', blank=True, null=True)
    name_functionnality = models.CharField(max_length=255, blank=True, null=True)
    class_field = models.CharField(db_column='class', max_length=255, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    type_functionnality = models.CharField(max_length=255, blank=True, null=True)
    unit = models.CharField(max_length=255, blank=True, null=True)
    dimension = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        app_label = 'groupamasi'
        managed = True
        db_table = 'functionnality'


class Incident(models.Model):
    id_incident = models.AutoField(primary_key=True)
    id_systemofsystem = models.ForeignKey('Systemofsystem', models.DO_NOTHING, db_column='id_systemofsystem', blank=True, null=True)
    type_application = models.CharField(max_length=255, blank=True, null=True)
    classification_incident = models.CharField(max_length=255, blank=True, null=True)
    analyse_incident = models.CharField(max_length=255, blank=True, null=True)
    date_incident = models.DateTimeField(blank=True, null=True)
    owner_incident = models.IntegerField(blank=True, null=True)
    commentaire_incident = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        app_label = 'groupamasi'
        managed = True
        db_table = 'incident'


class RelDataVcomponent(models.Model):
    rel_data_vcomponent = models.AutoField(primary_key=True)
    id_data = models.IntegerField(blank=True, null=True)
    id_vcomponent = models.ForeignKey('Vcomponent', models.DO_NOTHING, db_column='id_vcomponent', blank=True, null=True)
    comment_data_vcomponent = models.CharField(max_length=255, blank=True, null=True)
    owner_data_vcomponent = models.IntegerField(blank=True, null=True)
    date_data_vcomponent = models.DateTimeField(blank=True, null=True)

    class Meta:
        app_label = 'groupamasi'
        managed = True
        db_table = 'rel_data_vcomponent'


class RelResultValternative(models.Model):
    id_rel_result_valternative = models.AutoField(primary_key=True)
    id_result = models.ForeignKey('TechnicalResult', models.DO_NOTHING, db_column='id_result', blank=True, null=True)
    id_valternative = models.ForeignKey('Valternative', models.DO_NOTHING, db_column='id_valternative', blank=True, null=True)
    comment_result_valternative = models.BooleanField(blank=True, null=True)
    date_result_valternative = models.DateTimeField(blank=True, null=True)
    owner_result_valternative = models.IntegerField(blank=True, null=True)

    class Meta:
        app_label = 'groupamasi'
        managed = True
        db_table = 'rel_result_valternative'


class RelValternativeVdata(models.Model):
    rel_valternative_vdata = models.AutoField(primary_key=True)
    id_valternative = models.ForeignKey('Valternative', models.DO_NOTHING, db_column='id_valternative', blank=True, null=True)
    id_vdata = models.ForeignKey('Vdata', models.DO_NOTHING, db_column='id_vdata', blank=True, null=True)
    comment_valternative_vdata = models.CharField(max_length=255, blank=True, null=True)
    date_valternative_vdata = models.DateTimeField(blank=True, null=True)
    owner_valternative_vdata = models.IntegerField(blank=True, null=True)

    class Meta:
        app_label = 'groupamasi'
        managed = True
        db_table = 'rel_valternative_vdata'


class RelVcomponentVfunctionnality(models.Model):
    rel_vcomponent_vfunctionnality = models.AutoField(primary_key=True)
    id_vcomponent = models.ForeignKey('Vcomponent', models.DO_NOTHING, db_column='id_vcomponent', blank=True, null=True)
    id_vfunctionnality = models.ForeignKey('Vfunctionnality', models.DO_NOTHING, db_column='id_vfunctionnality', blank=True, null=True)
    comment_vcomponent_vfunctionnality = models.CharField(max_length=255, blank=True, null=True)
    owner_vcomponent_vfunctionnality = models.IntegerField(blank=True, null=True)
    date_vcomponent_vfunctionnality = models.DateTimeField(blank=True, null=True)

    class Meta:
        app_label = 'groupamasi'
        managed = True
        db_table = 'rel_vcomponent_vfunctionnality'


class RelVfunctionnalityDefect(models.Model):
    rel_vfunctionnality_defect = models.AutoField(primary_key=True)
    id_vfunctionnality = models.ForeignKey('Vfunctionnality', models.DO_NOTHING, db_column='id_vfunctionnality', blank=True, null=True)
    id_defect = models.ForeignKey(Defect, models.DO_NOTHING, db_column='id_defect', blank=True, null=True)
    comment_vfunctionnality_defect = models.CharField(max_length=255, blank=True, null=True)
    owner_vfunctionnality_defect = models.IntegerField(blank=True, null=True)
    date_vfunctionnality_defect = models.DateTimeField(blank=True, null=True)

    class Meta:
        app_label = 'groupamasi'
        managed = True
        db_table = 'rel_vfunctionnality_defect'


class RelVfunctionnalityValternative(models.Model):
    rel_vfunctionnality_valternative = models.AutoField(primary_key=True)
    id_vfunctionnality = models.ForeignKey('Vfunctionnality', models.DO_NOTHING, db_column='id_vfunctionnality', blank=True, null=True)
    id_valternative = models.ForeignKey('Valternative', models.DO_NOTHING, db_column='id_valternative', blank=True, null=True)
    comment_vfunctionnality_valternative = models.CharField(max_length=255, blank=True, null=True)
    owner_vfunctionnality_valternative = models.IntegerField(blank=True, null=True)
    date_vfunctionnality_valternative = models.DateTimeField(blank=True, null=True)

    class Meta:
        app_label = 'groupamasi'
        managed = True
        db_table = 'rel_vfunctionnality_valternative'


class RelVsubsystemVcomponent(models.Model):
    rel_subsystem_vcomponent = models.AutoField(primary_key=True)
    id_vsubsystem = models.ForeignKey('Vsubsystem', models.DO_NOTHING, db_column='id_vsubsystem', blank=True, null=True)
    id_vcomponent = models.ForeignKey('Vcomponent', models.DO_NOTHING, db_column='id_vcomponent', blank=True, null=True)
    owner_subsystem_vcomponent = models.IntegerField(blank=True, null=True)
    comment_subsystem_vcomponent = models.CharField(max_length=255, blank=True, null=True)
    date_subsystem_vcomponent = models.DateTimeField(blank=True, null=True)

    class Meta:
        app_label = 'groupamasi'
        managed = True
        db_table = 'rel_vsubsystem_vcomponent'


class RelVsystemVincident(models.Model):
    rel_vsystem_incidents = models.AutoField(primary_key=True)
    id_vsystem = models.ForeignKey('Vsystem', models.DO_NOTHING, db_column='id_vsystem', blank=True, null=True)
    id_incidents = models.ForeignKey('Vincident', models.DO_NOTHING, db_column='id_incidents', blank=True, null=True)
    comment_vsystem_incidents = models.CharField(max_length=255, blank=True, null=True)
    date_vsystem_incidents = models.DateTimeField(blank=True, null=True)
    owner_vsystem_incidents = models.IntegerField(blank=True, null=True)

    class Meta:
        app_label = 'groupamasi'
        managed = True
        db_table = 'rel_vsystem_vincident'


class RelVsystemVsubsystem(models.Model):
    rel_vsystem_vsubsystem = models.AutoField(primary_key=True)
    id_vsystem = models.ForeignKey('Vsystem', models.DO_NOTHING, db_column='id_vsystem', blank=True, null=True)
    id_vsubsystem = models.ForeignKey('Vsubsystem', models.DO_NOTHING, db_column='id_vsubsystem', blank=True, null=True)
    comment_vsystem_vsubsystem = models.CharField(max_length=255, blank=True, null=True)
    owner_vsystem_vsubsystem = models.IntegerField(blank=True, null=True)
    date_vsystem_vsubsystem = models.DateTimeField(blank=True, null=True)

    class Meta:
        app_label = 'groupamasi'
        managed = True
        db_table = 'rel_vsystem_vsubsystem'


class RelVsystemofsystemVsystem(models.Model):
    id_rel_vsystemofsystem_vsystem = models.AutoField(primary_key=True)
    id_vsystem = models.ForeignKey('Vsystem', models.DO_NOTHING, db_column='id_vsystem', blank=True, null=True)
    id_vsystemofsystem = models.ForeignKey('Vsystemofsystem', models.DO_NOTHING, db_column='id_vsystemofsystem', blank=True, null=True)
    owner_rel_vsystemofsystem_vsystem = models.IntegerField(blank=True, null=True)
    date_rel_vsystemofsystem_vsystem = models.DateTimeField(blank=True, null=True)

    class Meta:
        app_label = 'groupamasi'
        managed = True
        db_table = 'rel_vsystemofsystem_vsystem'


class Report(models.Model):
    id_report = models.AutoField(primary_key=True)
    id_eng = models.IntegerField(blank=True, null=True)
    id_eng_report_review = models.IntegerField(blank=True, null=True)
    id_eng_report_approval = models.IntegerField(blank=True, null=True)
    detail_report = models.CharField(max_length=50, blank=True, null=True)
    report_cath = models.IntegerField(blank=True, null=True)
    name_report = models.CharField(max_length=255, blank=True, null=True)
    date_report = models.DateTimeField(blank=True, null=True)

    class Meta:
        app_label = 'groupamasi'
        managed = True
        db_table = 'report'


class Subsystem(models.Model):
    id_subsystem = models.AutoField(primary_key=True)
    name_subsystem = models.CharField(max_length=255, blank=True, null=True)
    owner_subsystem = models.IntegerField(blank=True, null=True)
    id_system = models.ForeignKey('System', models.DO_NOTHING, db_column='id_system', blank=True, null=True)

    def __str__(self):
        return self.name_subsystem

    class Meta:
        app_label = 'groupamasi'
        managed = True
        db_table = 'subsystem'


class System(models.Model):
    id_system = models.AutoField(primary_key=True)
    id_systemofsystem = models.ForeignKey('Systemofsystem', models.DO_NOTHING, db_column='id_systemofsystem', blank=True, null=True)
    name_system = models.CharField(max_length=255, blank=True, null=True)
    owner_system = models.ForeignKey(Engineer, models.DO_NOTHING, db_column='owner_system', blank=True, null=True)
    type_system = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name_system

    class Meta:
        app_label = 'groupamasi'
        managed = True
        db_table = 'system'


class Systemofsystem(models.Model):
    id_systemofsystem = models.AutoField(primary_key=True)
    name_systemofsystem = models.CharField(max_length=255, blank=True, null=True)
    owner_systemofsystem = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name_systemofsystem

    class Meta:
        app_label = 'groupamasi'
        managed = True
        db_table = 'systemofsystem'


class TechnicalResult(models.Model):
    id_technical_result = models.AutoField(primary_key=True)
    titre_result = models.CharField(max_length=255, blank=True, null=True)
    owner_result = models.CharField(max_length=255, blank=True, null=True)
    date_result = models.DateTimeField(blank=True, null=True)
    comment_result = models.CharField(max_length=255, blank=True, null=True)
    report_result = models.ForeignKey(Report, models.DO_NOTHING, db_column='report_result', blank=True, null=True)

    class Meta:
        app_label = 'groupamasi'
        managed = True
        db_table = 'technical_result'


class Valternative(models.Model):
    id_valternative = models.AutoField(primary_key=True)
    id_alternative = models.ForeignKey(Alternative, models.DO_NOTHING, db_column='id_alternative', blank=True, null=True)
    version_valternative = models.IntegerField(blank=True, null=True)
    owner_valternative = models.ForeignKey(Engineer, models.DO_NOTHING, db_column='owner_valternative', blank=True, null=True)
    date_valternative = models.DateTimeField(blank=True, null=True)
    comment_valternative = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        app_label = 'groupamasi'
        managed = True
        db_table = 'valternative'


class Vcomponent(models.Model):
    id_vcomponent = models.AutoField(primary_key=True)
    version_vcomponent = models.CharField(max_length=255, blank=True, null=True)
    owner_vcomponent = models.ForeignKey(Engineer, models.DO_NOTHING, db_column='owner_vcomponent', blank=True, null=True)
    date_vcomponent = models.DateTimeField(blank=True, null=True)
    id_component = models.ForeignKey(Component, models.DO_NOTHING, db_column='id_component', blank=True, null=True)
    comment_vcomponent = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        app_label = 'groupamasi'
        managed = True
        db_table = 'vcomponent'


class Vdata(models.Model):
    id_vdata = models.AutoField(primary_key=True)
    id_alternative = models.ForeignKey(Alternative, models.DO_NOTHING, db_column='id_alternative', blank=True, null=True)
    value_vdata = models.IntegerField(blank=True, null=True)
    date_vdata = models.DateTimeField(blank=True, null=True)
    owner_vdata = models.ForeignKey(Engineer, models.DO_NOTHING, db_column='owner_vdata', blank=True, null=True)
    report_vdata = models.ForeignKey(Report, models.DO_NOTHING, db_column='report_vdata', blank=True, null=True)
    comment_vdata = models.CharField(max_length=255, blank=True, null=True)
    show_vdata = models.CharField(max_length=255, blank=True, null=True)
    value_vdata_link = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        app_label = 'groupamasi'
        managed = True
        db_table = 'vdata'


class Vfunctionnality(models.Model):
    id_vfunctionnality = models.AutoField(primary_key=True)
    id_functionnality = models.ForeignKey(Functionnality, models.DO_NOTHING, db_column='id_functionnality', blank=True, null=True)
    version_vfunctionnality = models.CharField(max_length=255, blank=True, null=True)
    date_vfunctionnality = models.DateTimeField(blank=True, null=True)
    comment_vfunctionnality = models.CharField(max_length=255, blank=True, null=True)
    owner_vfunctionnality = models.ForeignKey(Engineer, models.DO_NOTHING, db_column='owner_vfunctionnality', blank=True, null=True)

    class Meta:
        app_label = 'groupamasi'
        managed = True
        db_table = 'vfunctionnality'


class Vincident(models.Model):
    id_vincident = models.AutoField(primary_key=True)
    postprod = models.CharField(max_length=255, blank=True, null=True)
    vincident_number = models.CharField(max_length=255, blank=True, null=True)
    availability_level = models.CharField(max_length=255, blank=True, null=True)
    date_vincident_creation = models.DateTimeField(blank=True, null=True)
    configuration_element = models.CharField(max_length=255, blank=True, null=True)
    brief_description = models.CharField(max_length=255, blank=True, null=True)
    statut = models.CharField(db_column='Statut', max_length=255, blank=True, null=True)  # Field name made lowercase.
    date_vincident_update = models.DateTimeField(blank=True, null=True)
    priority_vincident = models.CharField(max_length=255, blank=True, null=True)
    entity_vincident = models.CharField(max_length=255, blank=True, null=True)
    description_vincident = models.TextField(blank=True, null=True)
    assigination_vincident_group = models.CharField(max_length=255, blank=True, null=True)
    date_vincident_cloture = models.DateTimeField(blank=True, null=True)
    version_vincident_number = models.CharField(max_length=255, blank=True, null=True)
    id_incident = models.ForeignKey(Incident, models.DO_NOTHING, db_column='id_incident', blank=True, null=True)
    tags_vincident = models.CharField(max_length=255, blank=True, null=True)
    code_vincident_resolution = models.CharField(max_length=255, blank=True, null=True)
    comment_vincident_resolution_visible_pour_les_clients_field = models.CharField(db_column='comment_vincident_resolution (Visible pour les clients)', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    date_vincident_resolution = models.DateTimeField(blank=True, null=True)
    comment_vincident_note_work = models.TextField(blank=True, null=True)
    owner_vincident = models.CharField(max_length=255, blank=True, null=True)
    state_vincident = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        app_label = 'groupamasi'
        managed = True
        db_table = 'vincident'


class Vsubsystem(models.Model):
    id_vsubsystem = models.AutoField(primary_key=True)
    version_vsubsystem = models.IntegerField(blank=True, null=True)
    owner_vsubsystem = models.ForeignKey(Engineer, models.DO_NOTHING, db_column='owner_vsubsystem', blank=True, null=True)
    date_vsubsystem = models.DateTimeField(blank=True, null=True)
    id_subsystem = models.ForeignKey(Subsystem, models.DO_NOTHING, db_column='id_subsystem', blank=True, null=True)
    comment_vsubsystem = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        app_label = 'groupamasi'
        managed = True
        db_table = 'vsubsystem'


class Vsystem(models.Model):
    id_vsystem = models.AutoField(primary_key=True)
    version_vsystem = models.IntegerField(blank=True, null=True)
    owner_vsystem = models.ForeignKey(Engineer, models.DO_NOTHING, db_column='owner_vsystem', blank=True, null=True)
    date_vsystem = models.DateTimeField(blank=True, null=True)
    id_system = models.ForeignKey(System, models.DO_NOTHING, db_column='id_system', blank=True, null=True)
    comment_vsystem = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        app_label = 'groupamasi'
        managed = True
        db_table = 'vsystem'


class Vsystemofsystem(models.Model):
    id_vsystemofsystem = models.AutoField(primary_key=True)
    id_systemofsystem = models.ForeignKey(Systemofsystem, models.DO_NOTHING, db_column='id_systemofsystem', blank=True, null=True)
    name_vsystemofsystem = models.CharField(max_length=255, blank=True, null=True)
    owner_vsystemofsystem = models.ForeignKey(Engineer, models.DO_NOTHING, db_column='owner_vsystemofsystem', blank=True, null=True)
    date_vsystemofsystem = models.DateTimeField(blank=True, null=True)
    comment_vsystemofsystem = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        app_label = 'groupamasi'
        managed = True
        db_table = 'vsystemofsystem'