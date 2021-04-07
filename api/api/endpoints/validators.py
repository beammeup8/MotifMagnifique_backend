import re


def no_validation(item):
    return True


def username_validate(username):
    return True


email_regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'


def email_validate(email):
    return re.search(email_regex, email)


def name_validate(name):
    return True

def pattern_name_validate(pattern_name):
    # Check for bad words
    return True


validation_mapping = {
    'authtoken': no_validation,
    'email': email_validate,
    'fName': name_validate,
    'lName': name_validate,
    'password': no_validation,
    'front_salt': no_validation,
    'username': username_validate,
    'pattern_name': pattern_name_validate
}


def validate_param(data, field_name):
    validation_func = validation_mapping.get(field_name)
    value = data.get(field_name)
    is_valid = value and validation_func(value)
    if not is_valid:
        value = (field_name, value)
    return is_valid, value

def validate_optional_param(data, field_name):
    validation_func = validation_mapping.get(field_name)
    value = data.get(field_name)
    if not validation_func(value):
        return False, (field_name, value)
    return True, value


def validate_params(data, field_names, optional_fields = []):
    field_values = []
    invalid = []

    for field_name in field_names:
        is_valid, value = validate_param(data, field_name)
        if is_valid:
            field_values.append(value)
        else:
            invalid.append(value)

    for field_name in optional_fields:
        is_valid, value = validate_param(data, field_name)
        if not is_valid:
            invalid.append(value)
        elif not value == None:
            field_values.append(value)
    
    if len(invalid) == 0:
        return True, field_values
    return False, invalid
