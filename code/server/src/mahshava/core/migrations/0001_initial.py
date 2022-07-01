# Generated by Django 3.2.9 on 2022-05-15 11:13

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('contactName', models.CharField(default='', max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.CharField(default='', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='LeadershipAndOrganizationalCulture_Survey',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('awarenessOfTheSituation', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(7), django.core.validators.MinValueValidator(0)])),
                ('teamInvolvement', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(7), django.core.validators.MinValueValidator(0)])),
                ('teamCohesion', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(7), django.core.validators.MinValueValidator(0)])),
                ('innovationAndCreativity', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(7), django.core.validators.MinValueValidator(0)])),
                ('decisionMaking', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(7), django.core.validators.MinValueValidator(0)])),
            ],
        ),
        migrations.CreateModel(
            name='ProcessSteps',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('processName', models.CharField(default='', max_length=50)),
                ('isDone', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='RelationshipNetworks_Survey',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('effectivePartnerships', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(7), django.core.validators.MinValueValidator(0)])),
                ('multiProfessionalism', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(7), django.core.validators.MinValueValidator(0)])),
                ('leverageKnowledge', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(7), django.core.validators.MinValueValidator(0)])),
                ('internalCrises', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(7), django.core.validators.MinValueValidator(0)])),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('schoolName', models.CharField(default='', max_length=50)),
                ('city', models.CharField(default='', max_length=50)),
                ('district', models.CharField(default='', max_length=50)),
                ('pic', models.URLField(blank=True)),
                ('phoneNo', models.CharField(default='', max_length=13)),
                ('noOfTeachers', models.IntegerField(default=0)),
                ('noOfStudents', models.IntegerField(default=0)),
                ('consultant', models.CharField(default='', max_length=50)),
                ('psychologist', models.CharField(default='', max_length=50)),
                ('processStartDate', models.DateField(blank=True, null=True)),
                ('religiousAffiliation', models.CharField(default='', max_length=50)),
                ('lengthOfStudy', models.CharField(default='', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('taskName', models.CharField(default='', max_length=50)),
                ('isDone', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='WillingnessToChange_Survey',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('proactiveStance', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(7), django.core.validators.MinValueValidator(0)])),
                ('objectiveClarity', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(7), django.core.validators.MinValueValidator(0)])),
                ('checkPlans', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(7), django.core.validators.MinValueValidator(0)])),
                ('planningStrategy', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(7), django.core.validators.MinValueValidator(0)])),
            ],
        ),
        migrations.CreateModel(
            name='SurveysResults',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('noOfParticipants', models.IntegerField(default=0)),
                ('startDate', models.DateField(blank=True, null=True)),
                ('endDate', models.DateField(blank=True, null=True)),
                ('leadershipAndOrganizationalCultureSurvey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.leadershipandorganizationalculture_survey')),
                ('relationshipNetworksSurvey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.relationshipnetworks_survey')),
                ('willingnessToChangeSurvey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.willingnesstochange_survey')),
            ],
        ),
        migrations.CreateModel(
            name='SchoolProcess',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('lastActionDate', models.DateField(auto_now=True)),
                ('schedule', models.TextField(blank=True, default='none')),
                ('contactID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contact_name', to='core.contact')),
                ('processID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='processStep_name', to='core.processsteps')),
                ('schoolID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='school_name', to='core.school')),
            ],
        ),
        migrations.AddField(
            model_name='school',
            name='surveysRes',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.surveysresults'),
        ),
        migrations.AddField(
            model_name='processsteps',
            name='taskID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task_name', to='core.task'),
        ),
    ]
