from django.db import models

class SurveyResponse(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other')
    ]

    CATEGORY_CHOICES = [
        ('Athletics', 'Athletics'),
        ('Badminton', 'Badminton'),
        ('Basketball', 'Basketball'),
        ('Boxing', 'Boxing'),
        ('Cricket', 'Cricket'),
        ('Football', 'Football'),
        ('Hockey', 'Hockey'),
        ('Kabaddi', 'Kabaddi'),
        ('Swimming', 'Swimming'),
        ('Tennis', 'Tennis'),
        ('Services Training', 'Services Training'),
        ('Other Sports', 'Other Sports'),

    ]
    
    DESCRIPTION_CHOICES = [
        ('sportsperson', 'Sportsperson/Athlete'),
        ('army_aspirant', 'Army Aspirant'),
        ('nutritionist', 'Nutritionist'),
        ('trainer', 'Trainer'),
        ('coach', 'Coach'),
        ('Other', 'Other'),
    ]

   
    full_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    mobile_number = models.CharField(max_length=10)
    email = models.EmailField()
    date_of_birth = models.DateField()
    height = models.CharField(max_length=10 , blank=True, null=True)
    # height_inches = models.CharField(max_length=10)
    weight = models.CharField(max_length=10)
    description = models.CharField(max_length=100 , choices=DESCRIPTION_CHOICES)
    # Other description
    other_description = models.CharField(max_length=100, blank=True, null=True)

    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES)
    # other category
    other_category = models.CharField(max_length=100, blank=True, null=True)

    coach_name = models.CharField(max_length=100)


# --------------------------------------------Second Section----------------------------------------------------------------------------------------------------------

    # Question 1: Diagnosed with serious infections
    infections_choices = [
        ('None', 'None'),
        ('HIV', 'HIV'),
        ('HBV', 'Hepatitis B virus'),
        ('HCV', 'Hepatitis C virus'),
        ('Syphilis', 'Syphilis'),
        ('Tuberculosis', 'Tuberculosis'),
        ('Cancer', 'Cancer')
    ]
    infections_diagnosed = models.CharField(max_length=20, choices=infections_choices)

    # Question 2: Autoimmune conditions
    autoimmune_choices = [
        ('None' , 'None'),
        ('Crohn\'s disease', 'Crohn\'s disease'),
        ('Ulcerative Colitis', 'Ulcerative Colitis'),
        ('Rheumatoid arthritis', 'Rheumatoid arthritis'),
        ('Lupus', 'Lupus'),
        ('Multiple Sclerosis', 'Multiple Sclerosis'),
        ('Type 1 Diabetes', 'Type 1 Diabetes'),
        ('Celiac disease', 'Celiac disease'),
        ('Psoriasis', 'Psoriasis'),
        ('Graves\' disease', 'Graves\' disease'),
        ('Don\'t Know', 'Don\'t Know')
    ]
    autoimmune_condition = models.CharField(max_length=50, choices=autoimmune_choices)

    # Question 3: Diseases of the reproductive or urinary system
    reproductive_urinary_conditions = models.BooleanField(default=False)  # No=False, Yes=True

    # Question 4: Cardiovascular conditions
    cardiovascular_conditions = models.BooleanField(default=False)  # No=False, Yes=True

    # Question 5: Nervous system, bones, or muscle diseases
    nervous_bone_muscle_conditions = models.BooleanField(default=False)  # No=False, Yes=True

    # Question 6: Sleep disorder medications
    sleep_disorder_medications = models.BooleanField(default=False)  # No=False, Yes=True

    # Question 7: Allergies or asthma
    allergies_asthma = models.BooleanField(default=False)  # No=False, Yes=True

    # Question 8: Skin conditions requiring medication
    skin_conditions = models.BooleanField(default=False)  # No=False, Yes=True

    # Question 9: Acne or history of acne
    acne_history = models.BooleanField(default=False)  # No=False, Yes=True

    # Question 10: Psychiatric or mental health conditions
    mental_health_conditions = models.BooleanField(default=False)  # No=False, Yes=True

    # Question 11: Blood transfusions or blood products
    blood_transfusion = models.BooleanField(default=False)  # No=False, Yes=True

    # Question 12: Travel to high-risk yellow fever countries
    high_risk_yellow_fever = models.BooleanField(default=False)  # No=False, Yes=True

    # Question 13: Hospitalization or surgery in the last 6 months
    hospitalization_surgery = models.BooleanField(default=False)  # No=False, Yes=True

    # Question 14: Contagious diseases in the last 2 weeks
    contagious_diseases = models.BooleanField(default=False)  # No=False, Yes=True

    # Question 15: Multi-drug resistant organisms
    multi_drug_resistant_organisms_choices = [
        ('None', 'None'),
        ('MRSA', 'MRSA'),
        ('VRE', 'VRE'),
        ('CRE', 'CRE'),
        ('Other', 'Other')
    ]
    multi_drug_resistant_organisms = models.CharField(max_length=5, choices=multi_drug_resistant_organisms_choices)

    # Other fields (Add these fields if necessary)
    other_multi_drug_resistant_organisms = models.CharField(max_length=100, blank=True, null=True)
    
    
    # Question 16: Medications for heart, blood pressure, or diabetes
    heart_blood_pressure_diabetes_medication_choices = [
        ('None', 'None'),
        ('Heart issues', 'Heart issues'),
        ('High BP', 'High BP'),
        ('Low BP', 'Low BP'),
        ('Diabetes', 'Diabetes'),
        ('Cholesterol', 'Cholesterol')
    ]
    heart_blood_pressure_diabetes_medication = models.CharField(max_length=100)

    # Question 17: Exposure to mold
    mold_exposure = models.BooleanField(default=False)  # No=False, Yes=True

    # Question 18: Congenital or genetic conditions
    genetic_conditions = models.BooleanField(default=False)  # No=False, Yes=True

    # Question 19: Number of times taken antibiotics
    antibiotics_taken_choices = [
        ('0', '0'),
        ('1-2', '1-2'),
        ('3-4', '3-4'),
        ('5+', '5+')
    ]
    antibiotics_taken = models.CharField(max_length=3, choices=antibiotics_taken_choices)

    # Question 20: Most recent antibiotic treatment
    most_recent_antibiotic_treatment = models.CharField(max_length=30,null=True, blank=True)

    # Question 21: COVID-19 positive in the past month
    covid_tested_positive = models.BooleanField(default=False)  # Yes=True, No=False

# ----------------------------------------------------------------------Third Section---------------------------------------------------------------------------------------------------------

    # Question 1: Hair loss or balding
    
    hair_loss = models.BooleanField(default=False)  # False for No, True for Yes
    # Question 2: Vision problems
    
    vision_problems = models.BooleanField(default=False)  # False for No, True for Yes

    # Question 3: Ever donated blood
    
    blood_donation = models.BooleanField(default=False)  # False for No, True for Yes

    # Question 4: Body fat percentage
    BODY_FAT_PERCENTAGE = [
        ('10-12%', '10-12%'),
        ('15-17%', '15-17%'),
        ('20-22%', '20-22%'),
        ('25%', '25%'),
        ('30%', '30%'),
        ('35%', '35%'),
        ('40%', '40%'),
        ('45%', '45%'),
        ('50%', '50%'),
        ('3-4%', '3-4%'),
        ('6-7%', '6-7%'),
        ('10-12%', '10-12%'),
        ('15%', '15%'),
        ('20%', '20%'),
        ('25%', '25%'),
        ('30%', '30%'),
        ('35%', '35%'),
        ('40%', '40%')
    ]
    body_fat_percentage = models.CharField(max_length=15, choices=BODY_FAT_PERCENTAGE)

    # Question 5: Birth type
    BIRTH_TYPE = [
        ('Normal', 'Normal'),
        ('C-Section', 'C-Section'),
        ('Don\'t know', 'Don\'t know')
    ]
    birth_type = models.CharField(max_length=10, choices=BIRTH_TYPE)

    # Question 6: Birth state
    BIRTH_STATE = [
        ('Andhra Pradesh', 'Andhra Pradesh'),
        ('Arunachal Pradesh', 'Arunachal Pradesh'),
        ('Assam', 'Assam'),
        ('Bihar', 'Bihar'),
        ('Chhattisgarh', 'Chhattisgarh'),
        ('Goa', 'Goa'),
        ('Gujarat', 'Gujarat'),
        ('Haryana', 'Haryana'),
        ('Himachal Pradesh', 'Himachal Pradesh'),
        ('Jharkhand', 'Jharkhand'),
        ('Karnataka', 'Karnataka'),
        ('Kerala', 'Kerala'),
        ('Madhya Pradesh', 'Madhya Pradesh'),
        ('Maharashtra', 'Maharashtra'),
        ('Manipur', 'Manipur'),
        ('Meghalaya', 'Meghalaya'),
        ('Mizoram', 'Mizoram'),
        ('Nagaland', 'Nagaland'),
        ('Odisha', 'Odisha'),
        ('Punjab', 'Punjab'),
        ('Rajasthan', 'Rajasthan'),
        ('Sikkim', 'Sikkim'),
        ('Tamil Nadu', 'Tamil Nadu'),
        ('Telangana', 'Telangana'),
        ('Tripura', 'Tripura'),
        ('Uttar Pradesh', 'Uttar Pradesh'),
        ('Uttarakhand', 'Uttarakhand'),
        ('West Bengal', 'West Bengal')
    ]
    birth_state = models.CharField(max_length=30, choices=BIRTH_STATE)

    # Question 7: Pin code of current location
    pin_code = models.CharField(max_length=6)

    # Question 8: Current city
    current_city = models.CharField(max_length=100)

    # Question 9: Hours of exercise per day
    EXERCISE_HOURS_PER_DAY = [
        ('0-1', '0-1'),
        ('1-2', '1-2'),
        ('2-3', '2-3'),
        ('3+', '3+')
    ]
    exercise_hours_per_day = models.CharField(max_length=3, choices=EXERCISE_HOURS_PER_DAY)

    # Question 10: Days of exercise per week
    EXERCISE_DAYS_PER_WEEK = [
        ('0-1', '0-1'),
        ('2-3', '2-3'),
        ('4-5', '4-5'),
        ('6-7', '6-7')
    ]
    exercise_days_per_week = models.CharField(max_length=3, choices=EXERCISE_DAYS_PER_WEEK)

    # Question 11: Types of physical activities
    PHYSICAL_ACTIVITIES = [
        ('Gym', 'Gym'),
        ('Running', 'Running'),
        ('Yoga', 'Yoga'),
        ('Sports', 'Sports'),
        ('Swimming', 'Swimming'),
        ('Cricket', 'Cricket'),
        ('Basketball', 'Basketball'),
        ('Badminton', 'Badminton'),
        ('Others', 'Others')
    ]
    physical_activities = models.CharField(max_length=50, choices=PHYSICAL_ACTIVITIES)
    other_physical_activities = models.CharField(max_length=70 , null=True , blank=True)
   
    # Question 12: Sports or exercise proficiency
    PROFICIENCY_LEVEL = [
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced')
    ]
    proficiency_level = models.CharField(max_length=15, choices=PROFICIENCY_LEVEL)

    # Question 13: Upbringing (Rural, Urban, Suburban)
    UPBRINGING = [
        ('Rural', 'Rural'),
        ('Urban', 'Urban'),
        ('Suburban', 'Suburban')
    ]
    upbringing = models.CharField(max_length=10, choices=UPBRINGING)

    # Question 14: Blood group
    BLOOD_GROUP = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
        ('Don\'t know', 'Don\'t know')
    ]
    blood_group = models.CharField(max_length=15, choices=BLOOD_GROUP)

    # Question 15: Do you smoke
    SMOKING = [
        ('No', 'No'),
        ('Occasionally', 'Occasionally'),
        ('Regularly', 'Regularly'),
        ('Former Smoker', 'Former Smoker')
    ]
    smoking = models.CharField(max_length=20, choices=SMOKING)

    # Question 16: Alcohol consumption
    ALCOHOL_CONSUMPTION = [
        ('No', 'No'),
        ('Occasionally', 'Occasionally'),
        ('Regularly', 'Regularly')
    ]
    alcohol_consumption = models.CharField(max_length=12, choices=ALCOHOL_CONSUMPTION)

    # Question 17: Breastfeeding history
    BREASTFEEDING = [
        ('Not breastfed', 'Not breastfed'),
        ('0-3 months', '0-3 months'),
        ('3-6 months', '3-6 months'),
        ('6+ months', '6+ months'),
        ('Don\'t know', 'Don\'t know')
    ]
    breastfeeding = models.CharField(max_length=20, choices=BREASTFEEDING)

    # Question 18: Bowel movements
    BOWEL_MOVEMENTS = [
        ('Regular', 'Regular'),
        ('Irregular', 'Irregular'),
        ('Varies', 'Varies')
    ]
    bowel_movements = models.CharField(max_length=15, choices=BOWEL_MOVEMENTS)

    # Question 19: Frequency of bloating or acidity
    BLOATING_ACIDITY = [
        ('Rarely', 'Rarely'),
        ('Sometimes', 'Sometimes'),
        ('Often', 'Often')
    ]
    bloating_acidity = models.CharField(max_length=10, choices=BLOATING_ACIDITY)

    # Question 20: Constipation or diarrhea history
    DIGESTIVE_ISSUES = [
        ('Constipation', 'Constipation'),
        ('Diarrhea', 'Diarrhea'),
        ('Neither', 'Neither')
    ]
    digestive_issues = models.CharField(max_length=12, choices=DIGESTIVE_ISSUES)

    # Question 21: Food intolerances
    food_intolerances = models.BooleanField(default=False)  # Yes=True, No=False

    # Question 22: Meals per day
    MEALS_PER_DAY = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6+', '6+')
    ]
    meals_per_day = models.CharField(max_length=3, choices=MEALS_PER_DAY)

    # Question 23: Snacks per day
    SNAKS_PER_DAY = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6+', '6+')
    ]
    snacks_per_day = models.CharField(max_length=3, choices=SNAKS_PER_DAY)

    # Question 24: Home-cooked meals
    HOME_COOCKED_MEALS = [
        ('None', 'None'),
        ('1', '1'),
        ('2', '2'),
        ('3+', '3+')
    ]
    home_cooked_meals = models.CharField(max_length=8, choices=HOME_COOCKED_MEALS)

    # Question 25: Regular dairy consumption
    
    dairy_consumption = models.BooleanField(default=False) 

    # Question 26: Type of diet
    DIET_TYPE = [
        ('Vegetarian', 'Vegetarian'),
        ('Non-vegetarian', 'Non-vegetarian'),
        ('Eggetarian', 'Eggetarian')
    ]
    diet_type = models.CharField(max_length=20, choices=DIET_TYPE)

    # Question 27: Types of meat consumed
    MEAT_TYPE = [
        ('Chicken', 'Chicken'),
        ('Fish', 'Fish'),
        ('Beef', 'Beef'),
        ('Pork', 'Pork'),
        ('Lamb', 'Lamb'),
        ('Other', 'Other')
    ]
    meat_type = models.CharField(max_length=255,null =True , blank = True )
    other_meat_type = models.CharField(max_length=100,null =True , blank = True )

    # Question 28: Frequency of meat consumption
    MEAT_FREQUENCY = [
        ('None', 'None'),
        ('1-2 times', '1-2 times'),
        ('3-4 times', '3-4 times'),
        ('5-6 times', '5-6 times'),
        ('Daily', 'Daily')
    ]
    meat_frequency = models.CharField(max_length=12, choices=MEAT_FREQUENCY , null =True , blank = True)

    # Question 29: Type of local cuisine consumed
    local_cuisine = models.CharField(max_length=100)
    # Question 30: Medications or supplements taken in the last week
    medications_taken = models.BooleanField(default=False)

    # Question 31: COVID-19 vaccination status
    COVID_VACCINNATION = [
        ('Yes', 'Yes'),
        ('No', 'No')
    ]
    covid_vaccination = models.CharField(max_length=3, choices=COVID_VACCINNATION)

    # Question 32: Which COVID-19 vaccine(s) received
    COVID_VACCINE = [
        ('Covaxin', 'Covaxin'),
        ('Covishield', 'Covishield'),
        ('Pfizer', 'Pfizer'),
        ('Moderna', 'Moderna'),
        ('Other', 'Other')
    ]
    covid_vaccine = models.CharField(max_length=10, choices=COVID_VACCINE , null = True , blank=True)
    other_covid_vaccine = models.CharField(max_length=20 , null = True , blank=True )
    created_at = models.DateTimeField(auto_now_add=True , null = True)  # Set only on creation


    def __str__(self):
        return f"{self.full_name}"