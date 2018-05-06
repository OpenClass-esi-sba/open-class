# Generated by Django 2.0.4 on 2018-05-04 17:52

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Badge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('img', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submission_date', models.DateTimeField()),
                ('comment', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Have_badge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('priority', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='MCQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Preference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('confidentiality', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), (' ', '')], default=' ', max_length=1)),
                ('score', models.PositiveIntegerField()),
                ('phone_number', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(regex='^(\\+[\\d ]{3})?[\\d ]+$')])),
                ('birthday', models.DateField(null=True)),
                ('verification_token', models.CharField(max_length=64)),
                ('verified', models.BooleanField(default=False)),
                ('photo', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='asked', to='openclass.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('P', 'Pending'), ('A', 'Accepted'), ('R', 'Refused'), ('C', 'Canceled')], default='P', max_length=1)),
                ('date_registration', models.DateTimeField()),
                ('date_cancel', models.DateTimeField(null=True)),
                ('present', models.BooleanField(default=False)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='openclass.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Workshop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('required_materials', models.TextField()),
                ('objectives', models.TextField()),
                ('requirements', models.TextField()),
                ('seats_number', models.PositiveIntegerField()),
                ('submission_date', models.DateTimeField()),
                ('decision_date', models.DateTimeField(null=True)),
                ('start_date', models.DateTimeField()),
                ('duration', models.DurationField()),
                ('registration_politic', models.CharField(choices=[('F', 'FIFO'), ('M', 'Manual')], default='F', max_length=1)),
                ('location', models.CharField(max_length=20)),
                ('cover_img', models.ImageField(upload_to='')),
                ('status', models.CharField(choices=[('P', 'Pending'), ('A', 'Accepted'), ('R', 'Refused'), ('D', 'Done'), ('C', 'Canceled')], db_index=True, default='P', max_length=1)),
                ('animator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='animated', to='openclass.Profile')),
                ('mc_questions', models.ManyToManyField(to='openclass.MCQuestion')),
                ('registred', models.ManyToManyField(related_name='registred_to', through='openclass.Registration', to='openclass.Profile')),
                ('topics', models.ManyToManyField(to='openclass.Tag')),
            ],
        ),
        migrations.CreateModel(
            name='BadgeAttendance',
            fields=[
                ('badge_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='openclass.Badge')),
                ('nb_attendance', models.PositiveIntegerField()),
            ],
            bases=('openclass.badge',),
        ),
        migrations.AddField(
            model_name='registration',
            name='workshop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='openclass.Workshop'),
        ),
        migrations.AddField(
            model_name='question',
            name='workshop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='openclass.Workshop'),
        ),
        migrations.AddField(
            model_name='profile',
            name='badges',
            field=models.ManyToManyField(through='openclass.Have_badge', to='openclass.Badge'),
        ),
        migrations.AddField(
            model_name='profile',
            name='interests',
            field=models.ManyToManyField(to='openclass.Tag'),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='preference',
            name='profile',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='openclass.Profile'),
        ),
        migrations.AddField(
            model_name='have_badge',
            name='badge',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='openclass.Badge'),
        ),
        migrations.AddField(
            model_name='have_badge',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='openclass.Profile'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='openclass.Profile'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='choices',
            field=models.ManyToManyField(to='openclass.Choice'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='workshop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='openclass.Workshop'),
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='openclass.MCQuestion'),
        ),
        migrations.AlterUniqueTogether(
            name='registration',
            unique_together={('workshop', 'profile')},
        ),
        migrations.AlterUniqueTogether(
            name='feedback',
            unique_together={('workshop', 'author')},
        ),
    ]