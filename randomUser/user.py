import requests
import sys

class RandomUserError(Exception):
    def __init__(self, message):
        super(RandomUserError, self).__init__(message)

class resultsError(RandomUserError):
    """When there's an error with results value"""

class genderError(RandomUserError):
    """When there's an error with gender value"""

class passwordCharsetError(RandomUserError):
    """When there's an error with the pass_charset value"""

class passwordLengthError(RandomUserError):
    """When there's an error with the pass_length value"""
    def __init__(self):
        super(passwordLengthError, self).__init__(message="Incorrect pass_length format. Should be either a single number or range of numbers from 1-64.")

class formatError(RandomUserError):
    """When there's an error with the format value"""
    def __init__(self):
        super(formatError, self).__init__(message='Invalid format. Format must be from the following list: json, pretty, csv, yaml, xml')

class natError(RandomUserError):
    """When there's an error with the nat value"""
    def __init__(self):
        super(natError, self).__init__(message='Invalid nat format. nat must be a single value or comma separated list of values from the following list of countries: AU, BR, CA, CH, DE, DK, ES, FI, FR, GB, IE, IR, NL, NZ, TR, US')

class incError(RandomUserError):
    """When there's an error with the nat value"""
    def __init__(self):
        super(incError, self).__init__(message='Invalid inc format. inc must be a single value or comma separated list of values from the following list of parameters: gender, name, location, email, login, registered, dob, phone, cell, id, picture, nat')

class excError(RandomUserError):
    """When there's an error with the nat value"""
    def __init__(self):
        super(excError, self).__init__(message='Invalid inc format. inc must be a single value or comma separated list of values from the following list of parameters: gender, name, location, email, login, registered, dob, phone, cell, id, picture, nat')


def get_user(results=1, gender="", pass_charset="", pass_length="", seed="", format="", nat="", inc="", exc=""):
    url = 'https://randomuser.me/api/?'

    # Validate results value
    ########################
    if results <= 0 or results >= 5000:
        raise resultsError('results must be between 1 and 5000.')
    else: 
        user_url = url + "results={}".format(results)

    # Validate gender value
    #######################
    if gender:
        try:
            if gender in ["male", "female"]:
                user_url = user_url + "&gender={}".format(gender)
            else:
                raise genderError('gender must be male or female')
        except:
            raise genderError('gender must be male or female')

    # Validate password values
    #########################
    if (pass_charset and not pass_length) or (not pass_charset and pass_length):
        raise RandomUserError('Both pass_length and pass_charset must be provided when defining the password.')
    if pass_charset and pass_length:
        for item in pass_charset.split(','):
            if not item.strip(' ') in ["special", "upper", "lower", "number"]:
                raise passwordCharsetError('pass_charset should be one or more comma separated of the following: special, upper, lower, number')
        if "-" in str(pass_length):
            a = str(pass_length).split('-')
            try:
                if len(a) != 2 or int(a[0]) == 0 or int(a[0])>int(a[1]) or int(a[1])>64:
                    raise passwordLengthError()
            except:
                raise passwordLengthError()
        else:
            try:
                if int(pass_length) == 0 or int(pass_length)>64:
                    raise passwordLengthError()
            except:
                raise passwordLengthError()
        user_url = user_url + "&password={},{}".format(pass_charset.replace(' ',''), pass_length)

    # Validate seed value
    #####################
    if seed:
        user_url = user_url + "&seed={}".format(seed)

    # Validate format values
    ########################
    if format:
        try:
            if format in ['json', 'pretty', 'csv', 'yaml', 'xml']:
                user_url = user_url +"&format={}".format(format)
            else:
                raise formatError()
        except:
            raise formatError()

    # Validate nat values
    ####################
    if nat:
        try:
            nat_list = nat.lower().replace(' ','').split(',')
            for item in nat_list:
                if not item in ['au', 'br', 'ca', 'ch', 'de', 'dk', 'es', 'fi', 'fr', 'gb', 'ie', 'ir', 'nl', 'nz', 'tr', 'us']:
                    raise natError()
            user_url = user_url + "&nat={}".format(','.join(nat_list))
        except:
            raise natError()

    # Validate inc
    ##############
    if inc:
        try:
            inc_list = inc.lower().replace(' ','').split(',')
            for item in inc_list:
                if not item in ['gender', 'name', 'location', 'email', 'login', 'registered', 'dob', 'phone', 'cell', 'id', 'picture', 'nat']:
                    raise incError()
            user_url = user_url + "&inc={}".format(','.join(inc_list))
        except:
            raise incError()

    # Validate exc
    ##############
    if exc:
        try:
            exc_list = exc.lower().replace(' ','').split(',')
            for item in exc_list:
                if not item in ['gender', 'name', 'location', 'email', 'login', 'registered', 'dob', 'phone', 'cell', 'id', 'picture', 'nat']:
                    raise excError()
            user_url = user_url + "&exc={}".format(','.join(exc_list))
        except:
            raise excError()


    res = requests.get(user_url)
    if res.status_code != 200:
        raise RandomUserError('Error returned from randomuser.me')
    else:
        if not format or format in ['json', 'pretty']:
            return res.json()['results']
        else:
            return res.text

if __name__ == "__main__":
    print(get_user())
