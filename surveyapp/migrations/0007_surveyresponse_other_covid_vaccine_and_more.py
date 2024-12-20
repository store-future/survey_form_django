# Generated by Django 5.1.4 on 2024-12-11 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveyapp', '0006_alter_surveyresponse_height'),
    ]

    operations = [
        migrations.AddField(
            model_name='surveyresponse',
            name='other_covid_vaccine',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='surveyresponse',
            name='autoimmune_condition',
            field=models.CharField(choices=[('None', 'None'), ("Crohn's disease", "Crohn's disease"), ('Ulcerative Colitis', 'Ulcerative Colitis'), ('Rheumatoid arthritis', 'Rheumatoid arthritis'), ('Lupus', 'Lupus'), ('Multiple Sclerosis', 'Multiple Sclerosis'), ('Type 1 Diabetes', 'Type 1 Diabetes'), ('Celiac disease', 'Celiac disease'), ('Psoriasis', 'Psoriasis'), ("Graves' disease", "Graves' disease"), ("Don't Know", "Don't Know")], max_length=50),
        ),
    ]
