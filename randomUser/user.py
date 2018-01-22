import requests
import sys

def get_user(results=1, gender="", pass_charset="", pass_length="", seed="", format="", nat=""):
    url = 'https://randomuser.me/api/?'

    # Validation
    if results < 0 or results >= 5000:
        return {'error': 'results must be between 1 and 5000.'}
    else: 
        user_url = url + "results={}".format(results)
    if str(gender) in ["male", "female"]:
        user_url = user_url + "&gender={}".format(gender)
    if pass_charset and pass_length:
        for item in pass_charset.split(','):
            if not item.strip(' ') in ["special", "upper", "lower", "number"]:
                return {'error': 'pass_charset should be one or more comma separated of the following: "special", "upper", "lower", "number"'}
        if "-" in str(pass_length):
            a = str(pass_length).split('-')
            try:
                if len(a) != 2 or int(a[0]) == 0 or int(a[0])>int(a[1]) or int(a[1])>64:
                    return {'error': 'Incorrect pass_length format. Should be either a single number or range of numbers from 1-64.'}
            except:
                return {'error': 'Incorrect pass_length format. Should be either a single number or range of numbers from 1-64.'}
        else:
            try:
                if int(pass_length) == 0 or int(pass_length)>64:
                    return {'error': 'Incorrect pass_length format. Should be either a single number or range of numbers from 1-64.'}
            except:
                return {'error': 'Incorrect pass_length value type. Should be either a single number or range of numbers from 1-64.'}
        user_url = user_url + "&password={},{}".format(pass_charset.replace(' ',''), pass_length)
    if (pass_charset and not pass_length) or (not pass_charset and pass_length):
        return {'error': 'Incorrect pass_length format. Should be either a single number or range of numbers from 1-64.'}
    if seed:
        user_url = user_url + "&seed={}".format(seed)
    if format and isinstance(format, str) and format in ['json', 'pretty', 'csv', 'yaml', 'xml']:
        user_url = user_url +"&format={}".format(format)
    elif format and not isinstance(format, str) or format in ['json', 'pretty', 'csv', 'yaml', 'xml']:
        return {'error': 'Invalid format. Format must be from the following list: json, pretty, csv, yaml, xml'}
    if nat and isinstance(nat, str):
        for item in nat.lower().replace(' ','').split(','):
            if not nat in ['au', 'br', 'ca', 'ch', 'de', 'dk', 'es', 'fi', 'fr', 'gb', 'ie', 'ir', 'nl', 'nz', 'tr', 'us']:
                return {'error': 'Invalid nat format. nat must be a single value or comma separated list of values from the following list of countries: AU, BR, CA, CH, DE, DK, ES, FI, FR, GB, IE, IR, NL, NZ, TR, US'}
        user_url = user_url + "&nat={}".format(nat.lower().replace(' ',''))
    elif nat and not isinstance(nat, str):
        return {'error': 'Invalid nat format. nat must be a single value or comma separated list of values from the following list of countries: AU, BR, CA, CH, DE, DK, ES, FI, FR, GB, IE, IR, NL, NZ, TR, US'}


    res = requests.get(user_url)
    if res.status_code != 200:
        return 0
    else:
        if not format or format in ['json', 'pretty']:
            return res.json()['results']
        else:
            return res.text

if __name__ == "__main__":
    # print(get_user())
    # print(get_user(results=5))
    # print(get_user(gender="female"))
    # print(get_user(pass_charset="special", pass_length="20"))
    # print(get_user(pass_charset="", pass_length="1"))
    # print(get_user(pass_charset="upper", pass_length=""))
    # print(get_user(pass_charset="uppper", pass_length="2"))
    # print(get_user(pass_charset="upper", pass_length="3-2"))
    # print(get_user(pass_charset="upper", pass_length="0"))
    # print(get_user(pass_charset="upper", pass_length="80"))
    # print(get_user(pass_charset="upper", pass_length="1-a"))
    # print(get_user(pass_charset="upper", pass_length="a"))
    # print(get_user(pass_charset="special", pass_length="20", seed="kappa"))
    # print(get_user(pass_charset="special", pass_length="20", seed="kappa"))
    # print(get_user(format="asdf"))
    # print(get_user(format="csv"))
    print(get_user(format="pretty"))
    print(get_user(nat="de"))
