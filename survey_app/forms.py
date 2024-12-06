from django import forms
from .models import SurveyResponse


class Page1Form(forms.ModelForm):
    class Meta:
        model = SurveyResponse
        fields = ['full_name', 'gender', 'mobile_number', 'email', 'date_of_birth', 
                  'height_feet', 'height_inches', 'weight', 'description', 'category', 'coach_name']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }


class Page2Form(forms.ModelForm):
    class Meta:
        model = SurveyResponse
        fields = [
            'infections_diagnosed', 'autoimmune_condition', 'reproductive_urinary_conditions',
            'cardiovascular_conditions', 'nervous_bone_muscle_conditions', 'sleep_disorder_medications',
            'allergies_asthma', 'skin_conditions', 'acne_history', 'mental_health_conditions', 
            'blood_transfusion', 'high_risk_yellow_fever', 'hospitalization_surgery', 'contagious_diseases',
            'multi_drug_resistant_organisms', 'heart_blood_pressure_diabetes_medication', 'mold_exposure',
            'genetic_conditions', 'antibiotics_taken', 'most_recent_antibiotic_treatment', 'covid_tested_positive'
        ]


class Page3Form(forms.ModelForm):
    # hair_loss = forms.ChoiceField(
    #     choices=[('yes', 'Yes'), ('no', 'No')],
    #     widget=forms.RadioSelect,
    #     initial='no'
    # )
    class Meta:
        model = SurveyResponse
        fields = [
            'hair_loss', 'vision_problems', 'blood_donation', 'body_fat_percentage', 'birth_type', 'birth_state',
            'pin_code', 'current_city', 'exercise_hours_per_day', 'exercise_days_per_week', 'physical_activities',
            'proficiency_level', 'upbringing', 'blood_group', 'smoking', 'alcohol_consumption', 'breastfeeding',
            'bowel_movements', 'bloating_acidity', 'digestive_issues', 'food_intolerances', 'meals_per_day',
            'snacks_per_day', 'home_cooked_meals', 'dairy_consumption', 'diet_type', 'meat_type', 'meat_frequency',
            'local_cuisine', 'medications_taken', 'covid_vaccination', 'covid_vaccine'
        ]
        
