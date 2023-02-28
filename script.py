import pandas as pd
#https://towardsdatascience.com/all-pandas-json-normalize-you-should-know-for-flattening-json-13eae1dfb7dd

## INTRO
#dict
a_dict = {
    'school': 'ABC primary school',
    'location': 'London',
    'ranking': 2,
}

pd.json_normalize(a_dict)

#list of dic
json_list = [
    { 'class': 'Year 1', 'student number': 20, 'room': 'Yellow' },
    { 'class': 'Year 2', 'student number': 25, 'room': 'Blue' },
]

pd.json_normalize(json_list)

#keys not always present
json_list = [
    { 'class': 'Year 1', 'num_of_students': 20, 'room': 'Yellow' },
    { 'class': 'Year 2', 'room': 'Blue' }, # no num_of_students
]

pd.json_normalize(json_list)

## FLATTENING A JSON WITH MULTIPLE LEVELS
#a json
json_obj = {
    'school': 'ABC primary school',
    'location': 'London',
    'ranking': 2,
    'info': {
        'president': 'John Kasich',
        'contacts': {
          'email': {
              'admission': 'admission@abc.com',
              'general': 'info@abc.com'
          },
          'tel': '123456789',
      }
    }
}

pd.json_normalize(json_obj)
pd.json_normalize(json_obj, max_level=0)

#a list of json
json_list = [
    { 
        'class': 'Year 1', 
        'student count': 20, 
        'room': 'Yellow',
        'info': {
            'teachers': { 
                'math': 'Rick Scott', 
                'physics': 'Elon Mask' 
            }
        }
    },
    { 
        'class': 'Year 2', 
        'student count': 25, 
        'room': 'Blue',
        'info': {
            'teachers': { 
                'math': 'Alan Turing', 
                'physics': 'Albert Einstein' 
            }
        }
    },
]
pd.json_normalize(json_list)
pd.json_normalize(json_list, max_level=0)

#FLATTENING A JSON WITH A NESTEED LIST
json_obj = {
    'school': 'ABC primary school',
    'location': 'London',
    'ranking': 2,
    'info': {
        'president': 'John Kasich',
        'contacts': {
          'email': {
              'admission': 'admission@abc.com',
              'general': 'info@abc.com'
          },
          'tel': '123456789',
      }
    },
    'students': [
      { 'name': 'Tom' },
      { 'name': 'James' },
      { 'name': 'Jacqueline' }
    ],
}

data = pd.json_normalize(json_obj)
# Flatten students
pd.json_normalize(json_obj, 
                  record_path=['students'],
                  meta = ['school', ['info', 'contacts', 'tel']]
                  )


#when the data is a list of dicts
json_list = [
    { 
        'class': 'Year 1', 
        'student count': 20, 
        'room': 'Yellow',
        'info': {
            'teachers': { 
                'math': 'Rick Scott', 
                'physics': 'Elon Mask' 
            }
        },
        'students': [
            { 
                'name': 'Tom', 
                'sex': 'M', 
                'grades': { 'math': 66, 'physics': 77 } 
            },
            { 
                'name': 'James', 
                'sex': 'M', 
                'grades': { 'math': 80, 'physics': 78 } 
            },
        ]
    },
    { 
        'class': 'Year 2', 
        'student count': 25, 
        'room': 'Blue',
        'info': {
            'teachers': { 
                'math': 'Alan Turing', 
                'physics': 'Albert Einstein' 
            }
        },
        'students': [
            { 'name': 'Tony', 'sex': 'M' },
            { 'name': 'Jacqueline', 'sex': 'F' },
        ]
    },
]
pd.json_normalize(json_list)

pd.json_normalize(json_list, 
                  record_path=['students'],
                  meta = ['class', 'room', ['info', 'teachers']]
                  )

## THE ERROR ARGUMENT
#if you want to raise errors
data = [
    { 
        'class': 'Year 1', 
        'student count': 20, 
        'room': 'Yellow',
        'info': {
            'teachers': { 
                'math': 'Rick Scott', 
                'physics': 'Elon Mask',
            }
        },
        'students': [
            { 'name': 'Tom', 'sex': 'M' },
            { 'name': 'James', 'sex': 'M' },
        ]
    },
    { 
        'class': 'Year 2', 
        'student count': 25, 
        'room': 'Blue',
        'info': {
            'teachers': { 
                 # no math teacher
                 'physics': 'Albert Einstein'
            }
        },
        'students': [
            { 'name': 'Tony', 'sex': 'M' },
            { 'name': 'Jacqueline', 'sex': 'F' },
        ]
    },
]
pd.json_normalize(
    data, 
    record_path =['students'], 
    meta=['class', 'room', ['info', 'teachers', 'math']],
)

# 
json_obj = {
    'school': 'ABC primary school',
    'location': 'London',
    'ranking': 2,
    'info': {
        'president': 'John Kasich',
        'contacts': {
          'email': {
              'admission': 'admission@abc.com',
              'general': 'info@abc.com'
          },
          'tel': '123456789',
      }
    }
}

pd.json_normalize(json_obj, sep='->')

# WORKING WITH A LOCAL FILE
import json
with open("example_file_2.json") as f:
    dic = json.load(f)

pd.json_normalize(dic, max_level=1)

with open("example_file.json") as f:
    dic = json.load(f)

#WORKING WITH A URL
#The json. load() is used to read the JSON document from file and The json. loads() is used to convert the JSON String document into the Python dictionary
import requests
URL = 'http://raw.githubusercontent.com/BindiChen/machine-learning/master/data-analysis/027-pandas-convert-json/data/simple.json'
data = json.loads(requests.get(URL).text)
pd.json_normalize(data)
