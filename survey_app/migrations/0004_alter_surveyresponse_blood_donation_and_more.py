# Generated by Django 5.1.4 on 2024-12-07 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey_app', '0003_alter_surveyresponse_most_recent_antibiotic_treatment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='surveyresponse',
            name='blood_donation',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='surveyresponse',
            name='dairy_consumption',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='surveyresponse',
            name='hair_loss',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='surveyresponse',
            name='local_cuisine',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='surveyresponse',
            name='vision_problems',
            field=models.BooleanField(default=False),
        ),
    ]
