from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from .forms import QuestionCreateormForm


def add_question(request, *args, **kwargs):
    if request.user.is_authenticated():
        print(str(request.user.username))

    if request.method == 'POST':
        print("I am here.......")
        form = QuestionCreateormForm(request.POST, request.FILES)
        if form.is_valid():
            question = form.cleaned_data['question']
            option1 = form.cleaned_data['option1']
            option2 = request.POST['option2']
            option3 = request.POST['option3']
            option4 = request.POST['option4']
            explanation = form.cleaned_data['explanation']

            print("I am here "+question+" "+option1+" "+option2+" "+option3+" "+option4 +" "+explanation+" "+str(request.user))

            if request.user.is_authenticated():
                # obj = form.save(commit=False)
        #         qs = Profile.objects.filter(user=request.user)
        #         print("edit-profile" + str(qs.exists()))
        #         print("edit-profile" + str(qs.count()))
        #         activation_key=""
        #         slug = ""
        #         if qs.exists() and qs.count() == 1:
        #             profile = qs.first()
        #             activation_key = profile.activation_key
        #             slug = profile.slug
        #
        #         print("edit-profile" + str(activation_key))



        #         obj.user = request.user
        #         obj.is_available = True
        #         if discount == "":
        #             obj.has_discount = False
        #         else:
        #             obj.has_discount = True

        #         obj.activation_key = activation_key
        #         obj.slug = slug
        #         obj.save()
        #         # profile_ = obj.user.profile
        #         # return render(request, "home.html", {"profile": obj})
                return HttpResponseRedirect('/home')
        #         # return HttpResponseRedirect('/')
        #     # form.save()
        #     return HttpResponseRedirect('/activation')

    form = QuestionCreateormForm()
    return render(request, "question/add_question.html", {"form": form})