from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import Page1Form, Page2Form, Page3Form
from .models import SurveyResponse
import openpyxl
from django.http import HttpResponse
import json
import requests













def dashboard_view(request):
    data = SurveyResponse.objects.all().values()

    for response in data:
        print(f"newline \n{response}\n")
    return render(request,'dashboard.html',{'data_key' :data})

    
def export_to_excel(request):
    # Create an Excel workbook and sheet
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = 'Survey Data'

    # Write header row
    headers = [
        'ID','Full Name', 'Gender', 'Mobile Number', 'Email', 'Date of Birth', 'Height', 'Weight', 
        'Description', 'Category', 'Coach Name', 'Other Category', 'Other Description',
        'Infections Diagnosed', 'Autoimmune Condition', 'Reproductive Urinary Conditions',
        'Cardiovascular Conditions', 'Nervous Bone Muscle Conditions', 'Sleep Disorder Medications',
        'Allergies Asthma', 'Skin Conditions', 'Acne History', 'Mental Health Conditions', 
        'Blood Transfusion', 'High Risk Yellow Fever', 'Hospitalization Surgery', 'Contagious Diseases',
        'Multi Drug Resistant Organisms', 'Heart Blood Pressure Diabetes Medication', 'Mold Exposure',
        'Genetic Conditions', 'Antibiotics Taken', 'Most Recent Antibiotic Treatment', 'Covid Tested Positive',
        'Other Multi Drug Resistant Organisms', 'Hair Loss', 'Vision Problems', 'Blood Donation',
        'Body Fat Percentage', 'Birth Type', 'Birth State', 'Pin Code', 'Current City', 'Exercise Hours Per Day',
        'Exercise Days Per Week', 'Physical Activities', 'Other Physical Activities', 'Proficiency Level', 
        'Upbringing', 'Blood Group', 'Smoking', 'Alcohol Consumption', 'Breastfeeding', 'Bowel Movements', 
        'Bloating Acidity', 'Digestive Issues', 'Food Intolerances', 'Meals Per Day', 'Snacks Per Day',
        'Home Cooked Meals', 'Dairy Consumption', 'Diet Type', 'Meat Type', 'Other Meat Type', 'Meat Frequency',
        'Local Cuisine', 'Medications Taken', 'Covid Vaccination', 'Covid Vaccine', 'Other Covid Vaccine'
    ]
    
    sheet.append(headers)

    # Write data rows
    for response in SurveyResponse.objects.all().values():
        row = [
            response['id'], response['full_name'], response['gender'], response['mobile_number'], response['email'], response['date_of_birth'],
            response['height'], response['weight'], response['description'], response['other_description'], response['category'], response['other_category'],
            response['coach_name'], response['infections_diagnosed'], response['autoimmune_condition'], response['reproductive_urinary_conditions'],
            response['cardiovascular_conditions'], response['nervous_bone_muscle_conditions'], response['sleep_disorder_medications'], response['allergies_asthma'],
            response['skin_conditions'], response['acne_history'], response['mental_health_conditions'], response['blood_transfusion'], response['high_risk_yellow_fever'],
            response['hospitalization_surgery'], response['contagious_diseases'], response['multi_drug_resistant_organisms'], response['other_multi_drug_resistant_organisms'],
            response['heart_blood_pressure_diabetes_medication'], response['mold_exposure'], response['genetic_conditions'], response['antibiotics_taken'],
            response['most_recent_antibiotic_treatment'], response['covid_tested_positive'], response['hair_loss'], response['vision_problems'], response['blood_donation'],
            response['body_fat_percentage'], response['birth_type'], response['birth_state'], response['pin_code'], response['current_city'], response['exercise_hours_per_day'],
            response['exercise_days_per_week'], response['physical_activities'], response['other_physical_activities'], response['proficiency_level'], response['upbringing'],
            response['blood_group'], response['smoking'], response['alcohol_consumption'], response['breastfeeding'], response['bowel_movements'], response['bloating_acidity'],
            response['digestive_issues'], response['food_intolerances'], response['meals_per_day'], response['snacks_per_day'], response['home_cooked_meals'], response['dairy_consumption'],
            response['diet_type'], response['meat_type'], response['other_meat_type'], response['meat_frequency'], response['local_cuisine'], response['medications_taken'],
            response['covid_vaccination'], response['covid_vaccine'], response['other_covid_vaccine']
        ]
        
        
        sheet.append(row)

    # Prepare HTTP response with Excel file
    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename=survey_data.xlsx'
    workbook.save(response)
    return response




def consent(request):
    if request.method == "GET":
        request.session.flush() 
    return render(request, 'consent.html')


def page1(request):
    if request.method == "GET":
        request.session.flush()     # clearing session
    
    if request.method == "POST":
        form = Page1Form(request.POST)

        if form.is_valid():

            # cleaning data
            cleaned_data = form.cleaned_data
            cleaned_data.pop('height_feet', None)  # Remove height_feet
            cleaned_data.pop('height_inches', None)  # Remove height_inches
            cleaned_data['date_of_birth'] = cleaned_data['date_of_birth'].strftime('%Y-%m-%d')  # Serialize date
            
            # saving data into session 
            request.session['page1'] = cleaned_data

            print(f"sending to second page this data{request.session['page1']}")
            return render(request, "message.html", {"message": "Great! You are two steps away."})
        else:
            # If form is invalid, re-render the form with error messages
            return render(request, 'page1.html', {'form': form})
    else:
        form = Page1Form()
    return render(request, "page1.html", {"form": form})

def page2(request):

    # Redirect to Page 1 if it hasn't been completed
    # if 'page1' not in request.session:
    #     return redirect('page1')  # Redirect to page 1 if session data doesn't exist

    if request.method == "POST":
        form = Page2Form(request.POST)

        if form.is_valid():
            # saving data into session 
            data = form.cleaned_data
            request.session['page2'] = form.cleaned_data

            print(f"sending to third page this data{request.session['page2']}")
            return render(request, "message.html", {"message": "Great! You are one step away."})
        else:
            # If form is invalid, re-render the form with error messages
            return render(request, 'page2.html', {'form': form})
    else:
        form = Page2Form()
    return render(request, "page2.html", {"form": form})

    






def page3(request):
   # if 'page1' not in request.session or 'page2' not in request.session:
    #    return redirect('page1')  # Redirect to page 1 if session data doesn't exist

    if request.method == "POST":
        form = Page3Form(request.POST)

        if form.is_valid():
            
            # saving data into session 
            request.session['page3'] = form.cleaned_data

            # Combine data from all pages and save it to the database
            
            data = {**request.session['page1'], 
                    **request.session['page2'], 
                    **request.session['page3']    
                  }
            
            #print(f"last view of whole data before submitting\n:{data}")
          
          
            #captche verification for google-reCaptche
            clientkey = request.POST['g-recaptcha-response']
            secretkey = '6Lervm8oAAAAAAQ9K0mO-MRd6y-wdfSiV_xFiCLX'
            CaptcheData = {
                'secret' : secretkey,
                'response' : clientkey
                }
            r = requests.post('https://www.google.com/recaptcha/api/siteverify' , data=CaptcheData)
            
            response = json.loads(r.text)
            verify = response['success']
            #print(f"capcthe verification{verify}")
      
      
            #saving obj into database only if captche verification success
            if verify:
                # saving obj into database
                SurveyResponse.objects.create(**data)
                
                #  Clear session after submission
                request.session.flush()     # clearing session

                return render(request, "success.html")
   
        else:
            # If form is invalid, re-render the form with error messages
            return render(request, 'page3.html', {'form': form})
    else:
        form = Page3Form()
    return render(request, "page3.html", {"form": form})





















# def page3(request):
#    # if 'page1' not in request.session or 'page2' not in request.session:
#     #    return redirect('page1')  # Redirect to page 1 if session data doesn't exist

#     if request.method == "POST":
#         form = Page3Form(request.POST)

#         if form.is_valid():
            
#             # saving data into session 
#             request.session['page3'] = form.cleaned_data

#             # Combine data from all pages and save it to the database
#             '''
#             data = {**request.session['page1'], 
#                     **request.session['page2'], 
#                     **request.session['page3']    
#                   }
#             '''
#             data = request.session['page3']
#             #print(f"last view of whole data before submitting\n:{data}")
          
          
#             #captche verification for google-reCaptche
#             clientkey = request.POST['g-recaptcha-response']
#             secretkey = '6Lervm8oAAAAAAQ9K0mO-MRd6y-wdfSiV_xFiCLX'
#             CaptcheData = {
#                 'secret' : secretkey,
#                 'response' : clientkey
#                 }
#             r = requests.post('https://www.google.com/recaptcha/api/siteverify' , data=CaptcheData)
            
#             response = json.loads(r.text)
#             verify = response['success']
#             #print(f"capcthe verification{verify}")
      
      
#             #saving obj into database only if captche verification success
#             if verify:
#                 # saving obj into database
#                 #SurveyResponse.objects.create(**data)
                
#                 #  Clear session after submission
#                 #request.session.flush()     # clearing session

#                 return render(request, "success.html")
   
#         else:
#             # If form is invalid, re-render the form with error messages
#             return render(request, 'page3.html', {'form': form})
#     else:
#         form = Page3Form()
#     return render(request, "page3.html", {"form": form})




