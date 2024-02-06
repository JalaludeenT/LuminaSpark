from functools import wraps
from django.shortcuts import redirect
from .models import CreateAccount


def validate_account(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        account_id = kwargs.get('account_id')  # Retrieve account_id from kwargs
        # Retrieve CreateAccount instance based on account_id
        create_account_instance = CreateAccount.objects.filter(pk=account_id).first()
        # Check if the user's phone_number and email are valid
        if create_account_instance and validate_phone_and_email(create_account_instance):
            return func(request, *args, **kwargs)
        else:
            # Redirect to the login page or handle the invalid account scenario as needed
            return redirect(
                'BANK:create_account')  # Replace 'login' with the actual URL name or path for your login page

    return wrapper


def validate_phone_and_email(create_account_instance):
    """Validate that the phone number and email are valid."""
    # Add your validation logic here
    phone_number = create_account_instance.phone_number
    email = create_account_instance.mail_id
    # Example validation: Check if both phone number and email are not empty
    if phone_number and email:
        return True
    else:
        return False
