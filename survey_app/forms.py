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

    full_name = forms.CharField(required=True, error_messages={'required': '* Full Name field cannot be empty.'})
    gender = forms.ChoiceField(choices=[('', 'Select Gender')] + SurveyResponse.GENDER_CHOICES, required=True, error_messages={'required': '* This field cannot be empty.'})
    mobile_number = forms.CharField(required=True, error_messages={'required': '* Mobile number is required.'})
    email = forms.EmailField(required=True, error_messages={'required': 'Email address is required.', 'invalid': '* Enter a valid email address.'})
    date_of_birth = forms.DateField(required=True, widget=forms.DateInput(attrs={'type': 'date'}), error_messages={'required': '* Date of birth is required.'})
    height_feet = forms.CharField(required=True, error_messages={'required': '* Height in feet is required.'})
    height_inches = forms.CharField(required=True, error_messages={'required': '* Height in inches is required.'})
    weight = forms.CharField(required=True, error_messages={'required': '* Weight is required.'})
    description = forms.CharField(required=True,  error_messages={'required': '* Description is required.'})
    category = forms.ChoiceField(required=True, choices=[('', 'Select Category')] + SurveyResponse.CATEGORY_CHOICES, error_messages={'required': '* Category is required.'})
    coach_name = forms.CharField(required=True, error_messages={'required': '* Coach name is required.'})

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
        widgets = {
            'reproductive_urinary_conditions': forms.RadioSelect(choices=[(True, 'Yes'), (False, 'No')]),
            'cardiovascular_conditions': forms.RadioSelect( choices=[(True, 'Yes'), (False, 'No')]),
            'nervous_bone_muscle_conditions': forms.RadioSelect( choices=[(True, 'Yes'), (False, 'No')]),
            'sleep_disorder_medications': forms.RadioSelect( choices=[(True, 'Yes'), (False, 'No')]),
            'allergies_asthma': forms.RadioSelect(choices=[(True, 'Yes'), (False, 'No')]),
            'skin_conditions': forms.RadioSelect(choices=[(True, 'Yes'), (False, 'No')]),
            'acne_history': forms.RadioSelect( choices=[(True, 'Yes'), (False, 'No')]),
            'mental_health_conditions': forms.RadioSelect( choices=[(True, 'Yes'), (False, 'No')]),
            'blood_transfusion': forms.RadioSelect( choices=[(True, 'Yes'), (False, 'No')]),
            'high_risk_yellow_fever': forms.RadioSelect( choices=[(True, 'Yes'), (False, 'No')]),
            'hospitalization_surgery': forms.RadioSelect(choices=[(True, 'Yes'), (False, 'No')]),
            'contagious_diseases': forms.RadioSelect( choices=[(True, 'Yes'), (False, 'No')]),
            'mold_exposure': forms.RadioSelect( choices=[(True, 'Yes'), (False, 'No')]),
            'genetic_conditions': forms.RadioSelect( choices=[(True, 'Yes'), (False, 'No')]),
            'covid_tested_positive': forms.RadioSelect( choices=[(True, 'Yes'), (False, 'No')]),
        }
    # infections_diagnosed = forms.ChoiceField(choices=[('', 'Select Infection Diagnosed')] + SurveyResponse.infections_choices, required=True, error_messages={'required': '* This field is required.'})
    # autoimmune_condition = forms.ChoiceField(choices=[('', 'Select Autoimmune Condition')] + SurveyResponse.autoimmune_choices, required=True, error_messages={'required': '* This field is required.'})
    # reproductive_urinary_conditions = forms.BooleanField(required=True, error_messages={'required': '* This field is required.'})
    # cardiovascular_conditions = forms.BooleanField(required=True, error_messages={'required': '* This field is required.'})
    # nervous_bone_muscle_conditions = forms.BooleanField(required=True, error_messages={'required': '* This field is required.'})
    # sleep_disorder_medications = forms.BooleanField(required=True, error_messages={'required': '* This field is required.'})
    # allergies_asthma = forms.BooleanField(required=True, error_messages={'required': '* This field is required.'})
    # skin_conditions = forms.BooleanField(required=True, error_messages={'required': '* This field is required.'})
    # acne_history = forms.BooleanField(required=True, error_messages={'required': '* This field is required.'})
    # mental_health_conditions = forms.BooleanField(required=True, error_messages={'required': '* This field is required.'})
    # blood_transfusion = forms.BooleanField(required=True, error_messages={'required': '* This field is required.'})
    # high_risk_yellow_fever = forms.BooleanField(required=True, error_messages={'required': '* This field is required.'})
    # hospitalization_surgery = forms.BooleanField(required=True, error_messages={'required': '* This field is required.'})
    # contagious_diseases = forms.BooleanField(required=True, error_messages={'required': '* This field is required.'})
    # multi_drug_resistant_organisms = forms.ChoiceField(choices=[('', 'Select Resistant Organisms ')] + SurveyResponse.multi_drug_resistant_organisms_choices, required=True, error_messages={'required': 'This field is required.'})
    # heart_blood_pressure_diabetes_medication = forms.ChoiceField(choices=[('', 'Select Medications Taken')] + SurveyResponse.heart_blood_pressure_diabetes_medication_choices, required=True, error_messages={'required': 'This field is required.'})
    # mold_exposure = forms.BooleanField(required=True, error_messages={'required': '* This field is required.'})
    # genetic_conditions = forms.BooleanField(required=True, error_messages={'required': '* This field is required.'})
    # antibiotics_taken = forms.ChoiceField(choices=[('', 'Select Options')] + SurveyResponse.antibiotics_taken_choices, required=True, error_messages={'required': '* This field is required.'})
    # most_recent_antibiotic_treatment = forms.CharField(max_length=30, required=True, error_messages={'required': '* This field is required.'})
    # covid_tested_positive = forms.BooleanField(required=True, error_messages={'required': '* This field is required.'})


    autoimmune_condition = forms.ChoiceField(choices=[('', 'Select Autoimmune Condition')] + SurveyResponse.autoimmune_choices, required=True, error_messages={'required': '* This field is required.'})
    reproductive_urinary_conditions = forms.ChoiceField(choices=[(True, 'Yes'), (False, 'No')], required=True, error_messages={'required': '* This field is required.'})
    cardiovascular_conditions = forms.ChoiceField(choices=[(True, 'Yes'), (False, 'No')], required=True, error_messages={'required': '* This field is required.'})
    nervous_bone_muscle_conditions = forms.ChoiceField(choices=[(True, 'Yes'), (False, 'No')], required=True, error_messages={'required': '* This field is required.'})
    sleep_disorder_medications = forms.ChoiceField(choices=[(True, 'Yes'), (False, 'No')], required=True, error_messages={'required': '* This field is required.'})
    allergies_asthma = forms.ChoiceField(choices=[(True, 'Yes'), (False, 'No')], required=True, error_messages={'required': '* This field is required.'})
    skin_conditions = forms.ChoiceField(choices=[(True, 'Yes'), (False, 'No')], required=True, error_messages={'required': '* This field is required.'})
    acne_history = forms.ChoiceField(choices=[(True, 'Yes'), (False, 'No')], required=True, error_messages={'required': '* This field is required.'})
    mental_health_conditions = forms.ChoiceField(choices=[(True, 'Yes'), (False, 'No')], required=True, error_messages={'required': '* This field is required.'})
    blood_transfusion = forms.ChoiceField(choices=[(True, 'Yes'), (False, 'No')], required=True, error_messages={'required': '* This field is required.'})
    high_risk_yellow_fever = forms.ChoiceField(choices=[(True, 'Yes'), (False, 'No')], required=True, error_messages={'required': '* This field is required.'})
    hospitalization_surgery = forms.ChoiceField(choices=[(True, 'Yes'), (False, 'No')], required=True, error_messages={'required': '* This field is required.'})
    contagious_diseases = forms.ChoiceField(choices=[(True, 'Yes'), (False, 'No')], required=True, error_messages={'required': '* This field is required.'})
    multi_drug_resistant_organisms = forms.ChoiceField(choices=[('', 'Select Resistant Organisms ')] + SurveyResponse.multi_drug_resistant_organisms_choices, required=True, error_messages={'required': 'This field is required.'})
    heart_blood_pressure_diabetes_medication = forms.ChoiceField(choices=[('', 'Select Medications Taken')] + SurveyResponse.heart_blood_pressure_diabetes_medication_choices, required=True, error_messages={'required': 'This field is required.'})
    mold_exposure = forms.ChoiceField(choices=[(True, 'Yes'), (False, 'No')], required=True, error_messages={'required': '* This field is required.'})
    genetic_conditions = forms.ChoiceField(choices=[(True, 'Yes'), (False, 'No')], required=True, error_messages={'required': '* This field is required.'})
    antibiotics_taken = forms.ChoiceField(choices=[('', 'Select Options')] + SurveyResponse.antibiotics_taken_choices, required=True, error_messages={'required': '* This field is required.'})
    covid_tested_positive = forms.ChoiceField(choices=[(True, 'Yes'), (False, 'No')], required=True, error_messages={'required': '* This field is required.'})








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
        widgets = {
            'hair_loss' : forms.RadioSelect(choices=[(True, 'Yes'), (False, 'No')]),
            'vision_problems' : forms.RadioSelect(choices=[(True, 'Yes'), (False, 'No')]),
            'blood_donation' : forms.RadioSelect(choices=[(True, 'Yes'), (False, 'No')]),
            'food_intolerances' : forms.RadioSelect(choices=[(True, 'Yes'), (False, 'No')]),
            'dairy_consumption' : forms.RadioSelect(choices=[(True, 'Yes'), (False, 'No')]),
            'medications_taken' : forms.RadioSelect(choices=[(True, 'Yes'), (False, 'No')])
        }       
<<<<<<< HEAD

    # body_fat_percentage = forms.ChoiceField(required=True, choices=[('', 'Select body fat percentage')] + SurveyResponse.BODY_FAT_PERCENTAGE, error_messages={'required': '* Body fat percentage is required.'})
    # birth_type = forms.ChoiceField(required=True, choices=[('', 'Select birth type')] + SurveyResponse.BIRTH_TYPE, error_messages={'required': '* Birth type is required.'})
    # birth_state = forms.ChoiceField(required=True, choices=[('', 'Select birth state')] + SurveyResponse.BIRTH_STATE, error_messages={'required': '* Birth state is required.'})
    # exercise_hours_per_day = forms.ChoiceField(required=True, choices=[('', 'Select hours of exercise per day')] + SurveyResponse.EXERCISE_HOURS_PER_DAY, error_messages={'required': '* Exercise hours per day is required.'})
    # exercise_days_per_week = forms.ChoiceField(required=True, choices=[('', 'Select days of exercise per week')] + SurveyResponse.EXERCISE_DAYS_PER_WEEK, error_messages={'required': '* Exercise days per week is required.'})
    # physical_activities = forms.ChoiceField(required=True, choices=[('', 'Select physical activities')] + SurveyResponse.PHYSICAL_ACTIVITIES, error_messages={'required': '* Physical activities are required.'})
    # proficiency_level = forms.ChoiceField(required=True, choices=[('', 'Select proficiency level')] + SurveyResponse.PROFICIENCY_LEVEL, error_messages={'required': '* Proficiency level is required.'})
    # upbringing = forms.ChoiceField(required=True, choices=[('', 'Select upbringing')] + SurveyResponse.UPBRINGING, error_messages={'required': '* Upbringing is required.'})
    # blood_group = forms.ChoiceField(required=True, choices=[('', 'Select blood group')] + SurveyResponse.BLOOD_GROUP, error_messages={'required': '* Blood group is required.'})
    # smoking = forms.ChoiceField(required=True, choices=[('', 'Select smoking habits')] + SurveyResponse.SMOKING, error_messages={'required': '* Smoking habits are required.'})
    # alcohol_consumption = forms.ChoiceField(required=True, choices=[('', 'Select alcohol consumption')] + SurveyResponse.ALCOHOL_CONSUMPTION, error_messages={'required': '* Alcohol consumption is required.'})
    # breastfeeding = forms.ChoiceField(required=True, choices=[('', 'Select breastfeeding history')] + SurveyResponse.BREASTFEEDING, error_messages={'required': '* Breastfeeding history is required.'})
    # bowel_movements = forms.ChoiceField(required=True, choices=[('', 'Select bowel movements')] + SurveyResponse.BOWEL_MOVEMENTS, error_messages={'required': '* Bowel movements are required.'})
    # bloating_acidity = forms.ChoiceField(required=True, choices=[('', 'Select bloating or acidity frequency')] + SurveyResponse.BLOATING_ACIDITY, error_messages={'required': '* Bloating or acidity frequency is required.'})
    # digestive_issues = forms.ChoiceField(required=True, choices=[('', 'Select digestive issues')] + SurveyResponse.DIGESTIVE_ISSUES, error_messages={'required': '* Digestive issues are required.'})
    # meals_per_day = forms.ChoiceField(required=True, choices=[('', 'Select meals per day')] + SurveyResponse.MEALS_PER_DAY, error_messages={'required': '* Meals per day are required.'})
    # snacks_per_day = forms.ChoiceField(required=True, choices=[('', 'Select snacks per day')] + SurveyResponse.SNAKS_PER_DAY, error_messages={'required': '* Snacks per day are required.'})
    # home_cooked_meals = forms.ChoiceField(required=True, choices=[('', 'Select home-cooked meals frequency')] + SurveyResponse.HOME_COOCKED_MEALS, error_messages={'required': '* Home-cooked meals frequency is required.'})
    # diet_type = forms.ChoiceField(required=True, choices=[('', 'Select diet type')] + SurveyResponse.DIET_TYPE, error_messages={'required': '* Diet type is required.'})
    # meat_type = forms.ChoiceField( required=False, choices=[('', 'Select meat type')] + SurveyResponse.MEAT_TYPE, error_messages={'required': '* Meat type is required.'})    
    meat_type = forms.MultipleChoiceField(
        required=False,
        choices=SurveyResponse.MEAT_TYPE,
        widget=forms.CheckboxSelectMultiple,
        error_messages={'required': '* Please select at least one meat type.'}
    )

    
    # meat_frequency = forms.ChoiceField( required=False, choices=[('', 'Select meat consumption frequency')] + SurveyResponse.MEAT_FREQUENCY, error_messages={'required': '* Meat consumption frequency is required.'})
    # covid_vaccination = forms.ChoiceField(required=True, choices=[('', 'Select COVID-19 vaccination status')] + SurveyResponse.COVID_VACCINNATION, error_messages={'required': '* COVID-19 vaccination status is required.'})
    # covid_vaccine = forms.ChoiceField(required=False, choices=[('', 'Select COVID-19 vaccine received')] + SurveyResponse.COVID_VACCINE, error_messages={'required': '* COVID-19 vaccine is required.'})
    
=======
        
 
>>>>>>> parent of 629f059 (add validations)
