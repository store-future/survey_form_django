# Generated by Django 5.1.4 on 2024-12-09 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey_app', '0010_meattype_remove_surveyresponse_meat_type_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='surveyresponse',
            name='meat_type',
        ),
        migrations.DeleteModel(
            name='MeatType',
        ),
        migrations.AddField(
            model_name='surveyresponse',
            name='meat_type',
            field=models.CharField(blank=True, choices=[('Chicken', 'Chicken'), ('Fish', 'Fish'), ('Beef', 'Beef'), ('Pork', 'Pork'), ('Lamb', 'Lamb'), ('Other', 'Other')], max_length=100, null=True),
        ),
    ]
