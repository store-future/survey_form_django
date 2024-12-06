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

    full_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    mobile_number = models.CharField(max_length=10)
    email = models.EmailField()
    date_of_birth = models.DateField()
    height_feet = models.CharField(max_length=10)
    height_inches = models.CharField(max_length=10)
    weight = models.CharField(max_length=10)
    description = models.CharField(max_length=100)
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES)
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
        ('None', 'None'),
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

    # Question 16: Medications for heart, blood pressure, or diabetes
    heart_blood_pressure_diabetes_medication_choices = [
        ('None', 'None'),
        ('Heart issues', 'Heart issues'),
        ('High BP', 'High BP'),
        ('Low BP', 'Low BP'),
        ('Diabetes', 'Diabetes'),
        ('Cholesterol', 'Cholesterol')
    ]
    heart_blood_pressure_diabetes_medication = models.CharField(max_length=15, choices=heart_blood_pressure_diabetes_medication_choices)

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
    most_recent_antibiotic_treatment = models.CharField(max_length=30)

    # Question 21: COVID-19 positive in the past month
    covid_tested_positive = models.BooleanField(default=False)  # Yes=True, No=False

# ----------------------------------------------------------------------Third Section---------------------------------------------------------------------------------------------------------

    # Question 1: Hair loss or balding
    hair_loss_choices = [
        ('No', 'No'),
        ('Yes', 'Yes')
    ]
    hair_loss = models.CharField(max_length=3, choices=hair_loss_choices)

    # Question 2: Vision problems
    vision_problems_choices = [
        ('No', 'No'),
        ('Yes', 'Yes')
    ]
    vision_problems = models.CharField(max_length=3, choices=vision_problems_choices)

    # Question 3: Ever donated blood
    blood_donation_choices = [
        ('No', 'No'),
        ('Yes', 'Yes')
    ]
    blood_donation = models.CharField(max_length=3, choices=blood_donation_choices)

    # Question 4: Body fat percentage
    body_fat_choices = [
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
    body_fat_percentage = models.CharField(max_length=15, choices=body_fat_choices)

    # Question 5: Birth type
    birth_choices = [
        ('Normal', 'Normal'),
        ('C-Section', 'C-Section'),
        ('Don\'t know', 'Don\'t know')
    ]
    birth_type = models.CharField(max_length=10, choices=birth_choices)

    # Question 6: Birth state
    birth_state_choices = [
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
    birth_state = models.CharField(max_length=30, choices=birth_state_choices)

    # Question 7: Pin code of current location
    pin_code = models.CharField(max_length=6)

    # Question 8: Current city
    current_city = models.CharField(max_length=100)

    # Question 9: Hours of exercise per day
    exercise_hours_choices = [
        ('0-1', '0-1'),
        ('1-2', '1-2'),
        ('2-3', '2-3'),
        ('3+', '3+')
    ]
    exercise_hours_per_day = models.CharField(max_length=3, choices=exercise_hours_choices)

    # Question 10: Days of exercise per week
    exercise_days_choices = [
        ('0-1', '0-1'),
        ('2-3', '2-3'),
        ('4-5', '4-5'),
        ('6-7', '6-7')
    ]
    exercise_days_per_week = models.CharField(max_length=3, choices=exercise_days_choices)

    # Question 11: Types of physical activities
    physical_activities_choices = [
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
    physical_activities = models.CharField(max_length=50, choices=physical_activities_choices)

    # Question 12: Sports or exercise proficiency
    proficiency_choices = [
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced')
    ]
    proficiency_level = models.CharField(max_length=15, choices=proficiency_choices)

    # Question 13: Upbringing (Rural, Urban, Suburban)
    upbringing_choices = [
        ('Rural', 'Rural'),
        ('Urban', 'Urban'),
        ('Suburban', 'Suburban')
    ]
    upbringing = models.CharField(max_length=10, choices=upbringing_choices)

    # Question 14: Blood group
    blood_group_choices = [
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
    blood_group = models.CharField(max_length=15, choices=blood_group_choices)

    # Question 15: Do you smoke
    smoking_choices = [
        ('No', 'No'),
        ('Occasionally', 'Occasionally'),
        ('Regularly', 'Regularly'),
        ('Former Smoker', 'Former Smoker')
    ]
    smoking = models.CharField(max_length=20, choices=smoking_choices)

    # Question 16: Alcohol consumption
    alcohol_choices = [
        ('No', 'No'),
        ('Occasionally', 'Occasionally'),
        ('Regularly', 'Regularly')
    ]
    alcohol_consumption = models.CharField(max_length=12, choices=alcohol_choices)

    # Question 17: Breastfeeding history
    breastfeeding_choices = [
        ('Not breastfed', 'Not breastfed'),
        ('0-3 months', '0-3 months'),
        ('3-6 months', '3-6 months'),
        ('6+ months', '6+ months'),
        ('Don\'t know', 'Don\'t know')
    ]
    breastfeeding = models.CharField(max_length=20, choices=breastfeeding_choices)

    # Question 18: Bowel movements
    bowel_movements_choices = [
        ('Regular', 'Regular'),
        ('Irregular', 'Irregular'),
        ('Varies', 'Varies')
    ]
    bowel_movements = models.CharField(max_length=15, choices=bowel_movements_choices)

    # Question 19: Frequency of bloating or acidity
    bloating_acidity_choices = [
        ('Rarely', 'Rarely'),
        ('Sometimes', 'Sometimes'),
        ('Often', 'Often')
    ]
    bloating_acidity = models.CharField(max_length=10, choices=bloating_acidity_choices)

    # Question 20: Constipation or diarrhea history
    digestive_issues_choices = [
        ('Constipation', 'Constipation'),
        ('Diarrhea', 'Diarrhea'),
        ('Neither', 'Neither')
    ]
    digestive_issues = models.CharField(max_length=12, choices=digestive_issues_choices)

    # Question 21: Food intolerances
    food_intolerances = models.BooleanField(default=False)  # Yes=True, No=False

    # Question 22: Meals per day
    meals_per_day_choices = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6+', '6+')
    ]
    meals_per_day = models.CharField(max_length=3, choices=meals_per_day_choices)

    # Question 23: Snacks per day
    snacks_per_day_choices = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6+', '6+')
    ]
    snacks_per_day = models.CharField(max_length=3, choices=snacks_per_day_choices)

    # Question 24: Home-cooked meals
    home_cooked_meals_choices = [
        ('None', 'None'),
        ('1', '1'),
        ('2', '2'),
        ('3+', '3+')
    ]
    home_cooked_meals = models.CharField(max_length=8, choices=home_cooked_meals_choices)

    # Question 25: Regular dairy consumption
    dairy_consumption_choices = [
        ('Yes', 'Yes'),
        ('No', 'No')
    ]
    dairy_consumption = models.CharField(max_length=3, choices=dairy_consumption_choices)

    # Question 26: Type of diet
    diet_choices = [
        ('Vegetarian', 'Vegetarian'),
        ('Non-vegetarian', 'Non-vegetarian'),
        ('Eggetarian', 'Eggetarian')
    ]
    diet_type = models.CharField(max_length=20, choices=diet_choices)

    # Question 27: Types of meat consumed
    meat_choices = [
        ('Chicken', 'Chicken'),
        ('Fish', 'Fish'),
        ('Beef', 'Beef'),
        ('Pork', 'Pork'),
        ('Lamb', 'Lamb'),
        ('Other', 'Other')
    ]
    meat_type = models.CharField(max_length=10, choices=meat_choices)

    # Question 28: Frequency of meat consumption
    meat_frequency_choices = [
        ('None', 'None'),
        ('1-2 times', '1-2 times'),
        ('3-4 times', '3-4 times'),
        ('5-6 times', '5-6 times'),
        ('Daily', 'Daily')
    ]
    meat_frequency = models.CharField(max_length=12, choices=meat_frequency_choices)

    # Question 29: Type of local cuisine consumed
    local_cuisine = models.TextField()

    # Question 30: Medications or supplements taken in the last week
    medications_taken = models.BooleanField(default=False)

    # Question 31: COVID-19 vaccination status
    covid_vaccinated_choices = [
        ('Yes', 'Yes'),
        ('No', 'No')
    ]
    covid_vaccination = models.CharField(max_length=3, choices=covid_vaccinated_choices)

    # Question 32: Which COVID-19 vaccine(s) received
    covid_vaccine_choices = [
        ('Covaxin', 'Covaxin'),
        ('Covishield', 'Covishield'),
        ('Pfizer', 'Pfizer'),
        ('Moderna', 'Moderna'),
        ('Other', 'Other')
    ]
    covid_vaccine = models.CharField(max_length=10, choices=covid_vaccine_choices)



    def __str__(self):
        return f"Name {self.full_name}"
