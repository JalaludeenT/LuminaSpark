from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateAccountForm
from .models import District, Gender, Account_type, Materials, CreateAccount, Branch
from django.contrib.auth.decorators import login_required
from django.core.files.base import ContentFile
from .decorator import validate_account


# Create your views here.


def logo(request):
    return render(request, 'logo.html')


def home(request):
    return render(request, 'home.html')


def locations(request):
    return render(request, 'locations.html')


def register(request):
    if request.method == 'POST':
        username = request.POST.get('Username')
        password = request.POST.get('Password')
        password_confirmation = request.POST.get('Confirm_password')

        if password == password_confirmation:
            if User.objects.filter(username=username).exists():
                messages.error(request, f'Error: That {username} is already registered')
                return redirect('BANK:register')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                messages.success(request, f'Successfully created an account {username}!')
                return redirect('BANK:login')
        else:
            messages.error(request, 'Error: passwords do not match')
            return redirect('BANK:register')

    return render(request, 'register.html')


def user_login(request):
    login_success_flag = False

    if request.method == 'POST':
        username = request.POST.get('Username')
        password = request.POST.get('Password')

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Login successful')
            login_success_flag = True
            # return redirect('BANK:success')
            if not login_success_flag:
                # If login was not successful, raise a 404 error
                # or handle it as per your requirement
                get_object_or_404(User, pk=request.user.pk)
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('BANK:login')

    return render(request, 'login.html', {'login_success_flag': login_success_flag})


@login_required
def get_branches(request):
    district_id = request.GET.get('district')
    branches = Branch.objects.filter(district_id=district_id).values('id', 'name')
    return JsonResponse({'branches': list(branches)})


@login_required
def create_account_view(request):
    districts = District.objects.all()
    genders = Gender.objects.all()
    account_types = Account_type.objects.all()
    materials_provided = Materials.objects.all()
    account_success_flag = False
    account_id = None
    image_missing_flag = False
    if request.method == 'POST':
        form = CreateAccountForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            name = data['name']
            date_of_birth = data['date_of_birth']
            age = data['age']
            gender = data['gender']
            phone_number = data['phone_number']
            mail_id = data['mail_id']
            address = data['address']
            district = data['district']
            branch = data['branch']
            account_type = data['account_type']
            profile_image = request.FILES.get('profile_image')
            materials_provide_ids = [int(material_id) for material_id in request.POST.getlist('materials_provide')]
            materials_provide = Materials.objects.filter(pk__in=materials_provide_ids)
            account = CreateAccount(
                name=name,
                date_of_birth=date_of_birth,
                age=age,
                gender=gender,
                phone_number=phone_number,
                mail_id=mail_id,
                address=address,
                district=district,
                branch=branch,
                account_type=account_type,
                profile_image=profile_image,
            )
            if profile_image:
                # Save the image data
                account.profile_image.save(profile_image.name, ContentFile(profile_image.read()))
                account.save()
                account.materials_provide.set(materials_provide)
                account_success_flag = True
                account_id = account.pk
                # request.session['account_id'] = account_id
            else:
                image_missing_flag = True
        else:
            # messages.error(request, "You created a wrong form create again.")
            pass
    else:
        form = CreateAccountForm()
    context = {
        'form': form,
        'districts': districts,
        'genders': genders,
        'account_types': account_types,
        'materials_provided': materials_provided,
        'account_success_flag': account_success_flag,
        'account_id': account_id,
        'image_missing_flag': image_missing_flag,
    }
    return render(request, 'account.html', context)


@login_required
def account_login(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        email_id = request.POST.get('email_id')
        existing_account = CreateAccount.objects.filter(
            phone_number=phone_number,
            mail_id=email_id,
        ).first()
        if existing_account:
            request.session['account_id'] = existing_account.pk
            return redirect('BANK:profile', account_id=existing_account.pk)
        else:
            messages.error(request, 'Account does not exist.')
            return redirect('BANK:account_login')
    return render(request, 'exist_account.html')


@login_required
@validate_account
def profile(request, account_id):
    account = get_object_or_404(CreateAccount, pk=account_id)
    context = {
        'account': account,
    }
    return render(request, 'profile.html', context)


@login_required
@validate_account
def account_details_view(request, account_id):
    account = get_object_or_404(CreateAccount, pk=account_id)
    context = {
        'account': account,
    }
    return render(request, 'account_details.html', context)


@login_required
def logout(request):
    auth.logout(request)
    return redirect('BANK:home')
