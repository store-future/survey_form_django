from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import Page1Form, Page2Form, Page3Form
from .models import SurveyResponse 

# def page1(request):
#     if request.method == "POST":
#         form = Page1Form(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             data['date_of_birth'] = data['date_of_birth'].strftime('%Y-%m-%d')  # Serialize date
#             request.session['page1'] = form.cleaned_data
#             print(f"sending to second page this data{request.session['page1']}")
#             return render(request, "message.html", {"message": "Congratulations! You are two steps ahead."})
#     else:
#         form = Page1Form()
#     return render(request, "page1.html", {"form": form})


# def page2(request):
#     # if 'page1' not in request.session:
#     #     return redirect('page1')


#     if request.method == "POST":
#         form = Page2Form(request.POST)
#         if form.is_valid():
#             request.session['page2'] = form.cleaned_data
#             print(f"sending to third page this data{request.session['page2']}")
#             return render(request, "message.html", {"message": "Great! Just one step to go."})
#     else:
#         form = Page2Form()
#     return render(request, "page2.html", {"form": form})


# def page3(request):
#     # if 'page1' not in request.session or 'page2' not in request.session:
#     #     return redirect('page1')

#     if request.method == "POST":
#         form = Page3Form(request.POST)
#         if form.is_valid():
#             data = {
#                 **request.session['page1'],
#                 **request.session['page2'],
#                 'page3_field1': form.cleaned_data['field1'],
#             }
#             print(f"Last page {data}")

#             # SurveyResponse.objects.create(**data)
#             return render(request, "message.html", {"message": "Survey completed. Thank you!"})
#     else:
#         form = Page3Form()
#     return render(request, "page3.html", {"form": form})

# survey/views.py
from django.shortcuts import render, redirect
from .forms import Page1Form, Page2Form, Page3Form
from .models import SurveyResponse

def page1(request):
    if request.method == "GET":
        request.session.flush()     # clearing session
    
    if request.method == "POST":
        form = Page1Form(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            data['date_of_birth'] = data['date_of_birth'].strftime('%Y-%m-%d')  # Serialize date
            request.session['page1'] = form.cleaned_data

            print(f"sending to second page this data{data}")
            return render(request, "message.html", {"message": "Congratulations! You are two steps away."})
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

  # Log session data for debugging
    if request.method == "POST":
        form = Page2Form(request.POST)
        if form.is_valid():
            request.session['page2'] = form.cleaned_data
            
            print(f"sending to third page this data{request.session['page2']}")
            return render(request, "message.html", {"message": "Congratulations! You are one step away."})
        else:
            # If form is invalid, re-render the form with error messages
            return render(request, 'page2.html', {'form': form})
    else:
        form = Page2Form()
    return render(request, "page2.html", {"form": form})

def page3(request):
    if 'page1' not in request.session or 'page2' not in request.session:
        return redirect('page1')  # Redirect to page 1 if session data doesn't exist

    if request.method == "POST":
        form = Page3Form(request.POST)
<<<<<<< HEAD
        print("Submitted POST data:", request.POST)

        # # Get the list of selected meat types
        # print(request.POST.getlist('meat_type'))  # List of meat types

        # # Convert the list into a comma-separated string
        # meat_types_str = ",".join(selected_meat_types)
        # print(f"-------------------------------{ request.session['page3']}----{meat_types_str} {type(meat_types_str)}")
        
        print("before valid")
        if form.is_valid():
            print("inside valid")

            request.session['page3'] = form.cleaned_data
            # print(f"page 3data \n :{request.session['page3']}")

=======
        if form.is_valid():
            request.session['page3'] = form.cleaned_data
>>>>>>> parent of 629f059 (add validations)

            # Combine data from all pages and save it to the database
            data = {**request.session['page1'], 
                    **request.session['page2'], 
                    **request.session['page3']
                }
            SurveyResponse.objects.create(**data)



             # Clear session after submission
            request.session.flush()     # clearing session

            return render(request, "message.html", {"message": "Survey completed. Thank you!"})
        else:
            print("outside form validation post")

            # If form is invalid, re-render the form with error messages
            return render(request, 'page3.html', {'form': form})
    else:
        form = Page3Form()
    return render(request, "page3.html", {"form": form})

# def page3(request):
#     if request.method == "POST":
#         form = Page3Form(request.POST)
#         if form.is_valid():
#             request.session['page3'] = form.cleaned_data

#             data = {
#                 **request.session['page1'],
#                 **request.session['page2'],
#                 **request.session['page3'],
#             }
#             print(f"Last page {data}")
#             SurveyResponse.objects.create(**data)
#             return render(request, "message.html", {"message": "Survey completed. Thank you!"})
#     else:
#         form = Page3Form()
#     return render(request, "page3.html", {"form": form})
