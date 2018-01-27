This python module is a wrapper for the https://randomuser.me/ random user generator. It simplifies the api calls down to a small set of parameters. All the capabilities of the API have been bundled up into one small package.

As with any scraping tool, please be mindful of the site owners. If you find yourself using their service often, consider supporting their project. The randomuser.me service is completely free and open sourced.

### Background
The goal of this project was to make it easy to use the randomuser.me api from within any python project. If a user needs to generate some random user data to seed their project or database with, this gives them the capability.

The API can currently return the following set of information:
```json
{
  "results": [
    {
      "gender": "male",
      "name": {
        "title": "mr",
        "first": "romain",
        "last": "hoogmoed"
      },
      "location": {
        "street": "1861 jan pieterszoon coenstraat",
        "city": "maasdriel",
        "state": "zeeland",
        "postcode": 69217
      },
      "email": "romain.hoogmoed@example.com",
      "login": {
        "username": "lazyduck408",
        "password": "jokers",
        "salt": "UGtRFz4N",
        "md5": "6d83a8c084731ee73eb5f9398b923183",
        "sha1": "cb21097d8c430f2716538e365447910d90476f6e",
        "sha256": "5a9b09c86195b8d8b01ee219d7d9794e2abb6641a2351850c49c309f1fc204a0"
      },
      "dob": "1983-07-14 07:29:45",
      "registered": "2010-09-24 02:10:42",
      "phone": "(656)-976-4980",
      "cell": "(065)-247-9303",
      "id": {
        "name": "BSN",
        "value": "04242023"
      },
      "picture": {
        "large": "https://randomuser.me/api/portraits/men/83.jpg",
        "medium": "https://randomuser.me/api/portraits/med/men/83.jpg",
        "thumbnail": "https://randomuser.me/api/portraits/thumb/men/83.jpg"
      },
      "nat": "NL"
    }
  ],
  "info": {
    "seed": "2da87e9305069f1d",
    "results": 1,
    "page": 1,
    "version": "1.1"
  }
}
```

Queries can be specified to select which values you want reuturned and how you want them to be generated. A full listing of the possible parameters can be found in the api documentation here: https://randomuser.me/documentation.

### Implementation
Each of the query parameters have been broken down into arguments that are provided when calling the `get_user` function. Any of these values can be used in combination to define your query.

All of these paraters are defined below:
* `results`: Defines the number of results to be returned. Default is 1. Can be 1-5000.
   * Example: `get_user(results="20")`
* `gender`: Defines a specific gender. Can be "male" or "female"
   * Example: `get_user(gender="male")`
* `pass_charset`: Defines the sets of characters to be pulled from. Must be used with `pass_length`. Can be any combination of sets from the following list: `["special", "upper", "lower", "number"]`
   * Example: `get_user(pass_charset="special,upper,number", pass_length="20")`
* `pass_length`: Defines the length of the generated user password. Must be used with `pass_charsets`. Can be 1-64.
   * Example: `get_user(pass_charset="special", pass_length="30")`
* `seed`: Defines the seed to be used when generating a user/list of users. Will return the same set every time. Can be any string of characters.
   * Example: `get_user(seed="*983#&@9)@dskj")`
* `format`: Defines the format that the response will be returned in. Default is `json`. Can be any format form this list: `['json', 'pretty', 'csv', 'yaml', 'xml']`
   * Example: `get_user(format="csv")`
* `nat`: Defines the nationalities to generate from. This can be any combination of nations from the following list: `'au', 'br', 'ca', 'ch', 'de', 'dk', 'es', 'fi', 'fr', 'gb', 'ie', 'ir', 'nl', 'nz', 'tr', 'us']`
   * Example: `get_user(nat="au,es,fi,fr,nz,us")`
* `inc`: Defines which values you want to be generated. They can be any combination of parameters from the following list: `['gender', 'name', 'location', 'email', 'login', 'registered', 'dob', 'phone', 'cell', 'id', 'picture', 'nat']`
   * Example: `get_user(inc="id,gender,nat,email")`
* `exc`: Defines which values you do not want to be generated. They can be any combination of parameters from the following list: `['gender', 'name', 'location', 'email', 'login', 'registered', 'dob', 'phone', 'cell', 'id', 'picture', 'nat']`
   * Example: `get_user(exc="location,login,registered,picture")`

#### A few things to note:
* Not including a `results` value will cause 1 result to be returned
* Not specifically defining the password will cause a random 8-64 character password to be generated
* Data will be returned in `json` format by default
* If you select anything other than `json` or `pretty` formats, it will be returned as a text string