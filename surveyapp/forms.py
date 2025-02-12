from django import forms
from .models import SurveyResponse
from django.core.validators import RegexValidator


class Page1Form(forms.ModelForm):

    class Meta:
        model = SurveyResponse
        fields = ['full_name', 'gender', 'mobile_number', 'email', 'date_of_birth', 
                  'height', 'weight', 'description', 'category', 'coach_name','other_category','other_description']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            
        }
    full_name = forms.CharField(required=True, error_messages={'required': '* Full Name field cannot be empty.'})
    gender = forms.ChoiceField(choices=[('', 'Select Gender')] + SurveyResponse.GENDER_CHOICES, required=True, error_messages={'required': '* This field cannot be empty.'})
    mobile_number = forms.CharField(required=True, error_messages={'required': '* Mobile number is required.'})
    email = forms.EmailField(required=True, error_messages={'required': '* Email address is required.', 'invalid': '* Enter a valid email address.'})
    date_of_birth = forms.DateField(required=True, widget=forms.DateInput(attrs={'type': 'date'}), error_messages={'required': '* Date of birth is required.'})
    
    height_feet = forms.ChoiceField( required=True , choices=[('', 'Select Height')] + [(str(i), str(i)) for i in range(4, 8)], error_messages={'required': '* Feet is required.'})
    height_inches = forms.ChoiceField( required=True,choices =[('', 'Select Inch')] +  [(str(i) ,str(i)) for i in range(0,12)] , error_messages={'required': '* Inches is required.'})
    def clean(self):
        cleaned_data = super().clean()
        feet = cleaned_data.get('height_feet')
        inches = cleaned_data.get('height_inches')

        if feet is not None and inches is not None:

            # Validate feet and inches within the allowed range
            total_height = f"{feet}.{inches}"
            cleaned_data['height'] = total_height
            print(cleaned_data)

        return cleaned_data    
    
    weight = forms.CharField(required=True, error_messages={'required': '* Weight is required.'})
    description = forms.ChoiceField(required=True, choices=[('', 'Select description')] + SurveyResponse.DESCRIPTION_CHOICES, error_messages={'required': '* Description is required.'})
    other_description = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Specify your Describes '}))
    category = forms.ChoiceField(required=True, choices=[('', 'Select Category')] + SurveyResponse.CATEGORY_CHOICES, error_messages={'required': '* Category is required.'})
    other_category = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Specify sports Category'}))
    coach_name = forms.CharField(required=True, error_messages={'required': '* Coach name is required.'})



    def clean_mobile_number(self):
        mobile = self.cleaned_data.get('mobile_number')
        if not mobile.isdigit():  # Check if mobile number contains only digits
            raise forms.ValidationError('* Mobile number must contain only digits.')
        if len(mobile) != 10:  # Check if mobile number is exactly 10 digits
            raise forms.ValidationError('* Mobile number must be exactly 10 digits long.')
        return mobile
    
    def clean_weight(self):
        weight_data = self.cleaned_data.get('weight')

        # Check if the weight is a valid number
        try:
            weight_value = int(weight_data)
        except ValueError:
            raise forms.ValidationError('* Please enter a valid number for weight.')

        # Check if the weight is less than 100
        if weight_value > 120 or weight_value <40:
            raise forms.ValidationError('* Weight must be between 40 to 120.')
        
        return str(weight_value)    
    
class Page2Form(forms.ModelForm):


    class Meta:
        
        model = SurveyResponse
        fields = [
            'infections_diagnosed', 'autoimmune_condition', 'reproductive_urinary_conditions',
            'cardiovascular_conditions', 'nervous_bone_muscle_conditions', 'sleep_disorder_medications',
            'allergies_asthma', 'skin_conditions', 'acne_history', 'mental_health_conditions', 
            'blood_transfusion', 'high_risk_yellow_fever', 'hospitalization_surgery', 'contagious_diseases',
            'multi_drug_resistant_organisms', 'heart_blood_pressure_diabetes_medication', 'mold_exposure',
            'genetic_conditions', 'antibiotics_taken', 'most_recent_antibiotic_treatment', 'covid_tested_positive',
            'other_multi_drug_resistant_organisms'
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
   
    infections_diagnosed = forms.ChoiceField(choices=[('', 'Select Infection Diagnosed')] + SurveyResponse.infections_choices, required=True, error_messages={'required': '* This field is required.'})
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
    multi_drug_resistant_organisms = forms.ChoiceField(choices=[('', 'Select Resistant Organisms ')] + SurveyResponse.multi_drug_resistant_organisms_choices, required=True, error_messages={'required': '* This field is required.'})
    other_multi_drug_resistant_organisms = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Specify Your multi drug resistant organisms'}))

    # heart_blood_pressure_diabetes_medication = forms.ChoiceField(choices=[('', 'Select Medications Taken')] + SurveyResponse.heart_blood_pressure_diabetes_medication_choices, required=True, error_messages={'required': '* This field is required.'})
    heart_blood_pressure_diabetes_medication = forms.MultipleChoiceField(required=True,choices= SurveyResponse.heart_blood_pressure_diabetes_medication_choices,
                                            error_messages={'required': '* This field is required.'}, widget=forms.CheckboxSelectMultiple,
    )

    def clean_heart_blood_pressure_diabetes_medication(self):
        """Convert the list of selected values into a comma-separated string."""
        selected = self.cleaned_data.get('heart_blood_pressure_diabetes_medication', [])
        print(f"inside form{selected}")
        return ",".join(selected)  # Serialize to a string
        
    mold_exposure = forms.ChoiceField(choices=[(True, 'Yes'), (False, 'No')], required=True, error_messages={'required': '* This field is required.'})
    genetic_conditions = forms.ChoiceField(choices=[(True, 'Yes'), (False, 'No')], required=True, error_messages={'required': '* This field is required.'})
    
    antibiotics_taken = forms.ChoiceField(choices=[('', 'Select Options')] + SurveyResponse.antibiotics_taken_choices, required=True, error_messages={'required': '* Antibiotic taken field is required.'})
    most_recent_antibiotic_treatment = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Ex -  mm-yyyy or mm/yyyy'}), required=False)

    def clean(self):
        cleaned_data = super().clean()
        antibiotics_taken = cleaned_data.get("antibiotics_taken")
        most_recent_antibiotic_treatment = cleaned_data.get("most_recent_antibiotic_treatment")


        # If '0' is selected for antibiotics_taken, clear most_recent_antibiotic_treatment
        if antibiotics_taken == '0':
            cleaned_data['most_recent_antibiotic_treatment'] = ''
        
        # If antibiotics were taken and the field is empty, add error
        if antibiotics_taken != '0' and not most_recent_antibiotic_treatment:
            self.add_error('most_recent_antibiotic_treatment',"This field is required if you have taken antibiotics.")
        

         # If the field is not empty, validate its format
        if most_recent_antibiotic_treatment:
            regex_validator = RegexValidator(regex=r'^(0?[1-9]|1[0-2])[-/](\d{4})$',
                                            message='Enter a valid month and year in the format mm-yyyy or mm/yyyy.'
                                        )
            try:
                regex_validator(most_recent_antibiotic_treatment)
            except forms.ValidationError as e:
                self.add_error('most_recent_antibiotic_treatment', e.message)
        return cleaned_data
    
    covid_tested_positive = forms.ChoiceField(choices=[(True, 'Yes'), (False, 'No')], required=True, error_messages={'required': '* This field is required.'})
    


    
    # most_recent_antibiotic_treatment = forms.DateField(
    #     widget=forms.DateInput(attrs={'type': 'month' , }),
    #     input_formats=['%Y-%m'],  # Ensure the date is entered as YYYY-MM
    #     error_messages={'invalid': 'Enter a valid month and year.'}
    # )
    # def clean_most_recent_antibiotic_treatment(self):
    #     # Get the cleaned data
    #     date = self.cleaned_data['most_recent_antibiotic_treatment']
    #     month_year = f"{date.year}-{date.month:02d}"

    #     # Optionally, print or log the extracted month and year
    #     # print("Formatted Month/Year:", month_year)
        
    #     # Force the day to be the 1st of the month
    #     return month_year
    # most_recent_antibiotic_treatment = forms.CharField(
    #     widget=forms.TextInput(attrs={
    #         'placeholder': 'Select month and year',
    #         'class': 'flatpickr-month'  # Add a custom class
    #     }),
    #     error_messages={'invalid': 'Enter a valid month and year.'}
    # )






class Page3Form(forms.ModelForm):

    class Meta:
        model = SurveyResponse
        fields = [
            'hair_loss', 'vision_problems', 'blood_donation', 'body_fat_percentage', 'birth_type', 'birth_state',
            'pin_code', 'current_city', 'exercise_hours_per_day', 'exercise_days_per_week', 'physical_activities',
            'other_physical_activities','proficiency_level', 'upbringing', 'blood_group', 'smoking', 'alcohol_consumption', 'breastfeeding',
            'bowel_movements', 'bloating_acidity', 'digestive_issues', 'food_intolerances', 'meals_per_day',
            'snacks_per_day', 'home_cooked_meals', 'dairy_consumption', 'diet_type', 'meat_type', 'other_meat_type','meat_frequency',
            'local_cuisine', 'medications_taken', 'covid_vaccination', 'covid_vaccine','other_covid_vaccine',
        ]
        widgets = {
            'hair_loss' : forms.RadioSelect(choices=[(True, 'Yes'), (False, 'No')]),
            'vision_problems' : forms.RadioSelect(choices=[(True, 'Yes'), (False, 'No')]),
            'blood_donation' : forms.RadioSelect(choices=[(True, 'Yes'), (False, 'No')]),
            'food_intolerances' : forms.RadioSelect(choices=[(True, 'Yes'), (False, 'No')]),
            'dairy_consumption' : forms.RadioSelect(choices=[(True, 'Yes'), (False, 'No')]),
            'medications_taken' : forms.RadioSelect(choices=[(True, 'Yes'), (False, 'No')])
        }       

    def clean_pin_code(self):
        pin_code_data = self.cleaned_data.get('pin_code')
        if not pin_code_data.isdigit():  # Check if mobile number contains only digits
            raise forms.ValidationError('* Pin Code must contain only digits.')
        if len(pin_code_data) != 6:  # Check if mobile number is exactly 10 digits
            raise forms.ValidationError('* Pin Code must be exactly 6 digits long.')
        return pin_code_data
            
        
        
    hair_loss = forms.ChoiceField(choices=[(True, 'Yes'), (False, 'No')], required=True, error_messages={'required': '* Hair loss field is required.'})
    vision_problems = forms.ChoiceField(choices=[(True, 'Yes'), (False, 'No')], required=True, error_messages={'required': '* Vision problems field is required.'})
    blood_donation = forms.ChoiceField(choices=[(True, 'Yes'), (False, 'No')], required=True, error_messages={'required': '* Blood donation field is required.'})
    food_intolerances = forms.ChoiceField(choices=[(True, 'Yes'), (False, 'No')], required=True, error_messages={'required': '* Food intolerances field is required.'})
    dairy_consumption = forms.ChoiceField(choices=[(True, 'Yes'), (False, 'No')], required=True, error_messages={'required': '* Dairy consumption field is required.'})
    medications_taken = forms.ChoiceField(choices=[(True, 'Yes'), (False, 'No')], required=True, error_messages={'required': '* Medications taken field is required.'})

    # body_fat_percentage = forms.ChoiceField(required=True, choices=[('', 'Select body fat percentage')] + SurveyResponse.BODY_FAT_PERCENTAGE, error_messages={'required': '* Body fat percentage is required.'})
    body_fat_percentage = forms.ChoiceField(required=True, choices=[])

    def __init__(self, *args, **kwargs):
        gender = kwargs.pop('gender', None)  # Get gender
        super().__init__(*args, **kwargs)

        # Set dynamic choices based on gender
        if gender == "Male":
            self.fields['body_fat_percentage'].choices = [('', 'Select body fat percentage')] + SurveyResponse.BODY_FAT_MALE_CHOICES
        elif gender == "Female":
            self.fields['body_fat_percentage'].choices = [('', 'Select body fat percentage')] + SurveyResponse.BODY_FAT_FEMALE_CHOICES
        else:
            self.fields['body_fat_percentage'].choices = [('', 'Select body fat percentage')]  # default case

    def clean_body_fat_percentage(self):
        # Get the value from the form field
        value = self.cleaned_data.get('body_fat_percentage')
        # Check if the selected value is a valid choice
        valid_choices = dict(self.fields['body_fat_percentage'].choices).keys()
        if value not in valid_choices:
            raise forms.ValidationError('Invalid body fat percentage selected.')
        print(f"inside clean_body_fat_percetage {value} {type(value)}")
        return value
    

    birth_type = forms.ChoiceField(required=True, choices=[('', 'Select birth type')] + SurveyResponse.BIRTH_TYPE, error_messages={'required': '* Birth type is required.'})
    birth_state = forms.ChoiceField(required=True, choices=[('', 'Select birth state')] + SurveyResponse.BIRTH_STATE, error_messages={'required': '* Birth state is required.'})
    exercise_hours_per_day = forms.ChoiceField(required=True, choices=[('', 'Select hours of exercise per day')] + SurveyResponse.EXERCISE_HOURS_PER_DAY, error_messages={'required': '* Exercise hours per day is required.'})
    exercise_days_per_week = forms.ChoiceField(required=True, choices=[('', 'Select days of exercise per week')] + SurveyResponse.EXERCISE_DAYS_PER_WEEK, error_messages={'required': '* Exercise days per week is required.'})
    physical_activities = forms.ChoiceField(required=True, choices=[('', 'Select physical activities')] + SurveyResponse.PHYSICAL_ACTIVITIES, error_messages={'required': '* Physical activities are required.'})
    proficiency_level = forms.ChoiceField(required=True, choices=[('', 'Select proficiency level')] + SurveyResponse.PROFICIENCY_LEVEL, error_messages={'required': '* Proficiency level is required.'})
    upbringing = forms.ChoiceField(required=True, choices=[('', 'Select upbringing')] + SurveyResponse.UPBRINGING, error_messages={'required': '* Upbringing is required.'})
    blood_group = forms.ChoiceField(required=True, choices=[('', 'Select blood group')] + SurveyResponse.BLOOD_GROUP, error_messages={'required': '* Blood group is required.'})
    smoking = forms.ChoiceField(required=True, choices=[('', 'Select smoking habits')] + SurveyResponse.SMOKING, error_messages={'required': '* Smoking habits are required.'})
    alcohol_consumption = forms.ChoiceField(required=True, choices=[('', 'Select alcohol consumption')] + SurveyResponse.ALCOHOL_CONSUMPTION, error_messages={'required': '* Alcohol consumption is required.'})
    breastfeeding = forms.ChoiceField(required=True, choices=[('', 'Select breastfeeding history')] + SurveyResponse.BREASTFEEDING, error_messages={'required': '* Breastfeeding history is required.'})
    bowel_movements = forms.ChoiceField(required=True, choices=[('', 'Select bowel movements')] + SurveyResponse.BOWEL_MOVEMENTS, error_messages={'required': '* Bowel movements are required.'})
    bloating_acidity = forms.ChoiceField(required=True, choices=[('', 'Select bloating or acidity frequency')] + SurveyResponse.BLOATING_ACIDITY, error_messages={'required': '* Bloating or acidity frequency is required.'})
    digestive_issues = forms.ChoiceField(required=True, choices=[('', 'Select digestive issues')] + SurveyResponse.DIGESTIVE_ISSUES, error_messages={'required': '* Digestive issues are required.'})
    meals_per_day = forms.ChoiceField(required=True, choices=[('', 'Select meals per day')] + SurveyResponse.MEALS_PER_DAY, error_messages={'required': '* Meals per day are required.'})
    snacks_per_day = forms.ChoiceField(required=True, choices=[('', 'Select snacks per day')] + SurveyResponse.SNAKS_PER_DAY, error_messages={'required': '* Snacks per day are required.'})
    home_cooked_meals = forms.ChoiceField(required=True, choices=[('', 'Select home-cooked meals frequency')] + SurveyResponse.HOME_COOCKED_MEALS, error_messages={'required': '* Home cooked meals frequency is required.'})
    diet_type = forms.ChoiceField(required=True, choices=[('', 'Select diet type')] + SurveyResponse.DIET_TYPE, error_messages={'required': '* Diet type is required.'})
    meat_type = forms.MultipleChoiceField(required=False,choices=SurveyResponse.MEAT_TYPE,widget=forms.CheckboxSelectMultiple,)
    

    def clean_meat_type(self):
        """Convert the list of selected values into a comma-separated string."""
        selected = self.cleaned_data.get('meat_type', [])
        return ",".join(selected)  # Serialize to a string

    meat_frequency = forms.ChoiceField( required=False, choices=[('', 'Select meat consumption frequency')] + SurveyResponse.MEAT_FREQUENCY)
    

    def clean(self):
        cleaned_data = super().clean()
        diet_type = cleaned_data.get('diet_type')
        meat_type = cleaned_data.get('meat_type')
        meat_frequency = cleaned_data.get('meat_frequency')

        if diet_type == 'Vegetarian':
            cleaned_data['meat_type'] = ''
            cleaned_data['meat_frequency'] = ''

        # If diet type is Non-Vegetarian, both meat_type and meat_frequency must be filled
        if diet_type == 'Non-vegetarian':
            if not meat_type:
                self.add_error('meat_type', '* This field is required if diet type is Non-Vegetarian.')
            if not meat_frequency:
                self.add_error('meat_frequency', '* This field is required if diet type is Non-Vegetarian.')

        return cleaned_data
    local_cuisine = forms.CharField(max_length=100,required=True, error_messages={'required': '* Local cuisine is required.'})
    covid_vaccination = forms.ChoiceField(required=True, choices=[('', 'Select COVID-19 vaccination status')] + SurveyResponse.COVID_VACCINNATION, error_messages={'required': '* COVID-19 vaccination status is required.'})
    covid_vaccine = forms.ChoiceField(required=False, choices=[('', 'Select COVID-19 vaccine received')] + SurveyResponse.COVID_VACCINE, error_messages={'required': '* COVID-19 vaccine is required.'})
