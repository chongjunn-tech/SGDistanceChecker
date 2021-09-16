import pandas as pd
import json
import requests
import http.client, urllib.parse
from math import radians, cos, sin, asin, sqrt

def load_all_postal_codes():
    '''load postal codes downloaded from GeoNames Postal Code into memory
    Credit to www.geonames.org
    '''
    data=pd.read_csv('SGPostalCode.txt',sep="\t",header=None)
    data=data.dropna(axis=1).drop(columns=0)
    data.columns=['Postal Code','Address','Latitude','Longtitude']
    
    return data

def find_lat_long(code):
    '''
    Getting Latitude and Longtitude from Geocode.xyz
    '''
    conn = http.client.HTTPConnection('geocode.xyz')

    params = urllib.parse.urlencode({
    'auth': '191249184319614221290x60675',
    'locate': code,
    'region': 'SG',
    'json': 1,
    })

    conn.request('GET', '/?{}'.format(params))

    res = conn.getresponse()
    read = res.read()

    response_dict = json.loads(read)
    
    return code,response_dict['latt'],response_dict['longt']

def prompt_user():
    while True:
        ref=input(' Please key in your desired reference postal code: ')
        if len(ref)==6 and ref.isnumeric():
            break         
    return ref

#Formula Extracted from
#link:https://stackoverflow.com/questions/4913349/haversine-formula-in-python-bearing-and-distance-between-two-gps-points 

def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance in kilometers between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles. Determines return value units.
    return c * r

if __name__=='__main__':

    #Retrieve all postal codes (with its corresponding latitude and longtitude) in Singapore and load it into memory
    df=load_all_postal_codes()
    #Ask the user to input a reference postal code
    reference_postal_code=prompt_user()

    postal_code,lat,long=find_lat_long(reference_postal_code)

    df['distance'] = df.apply(lambda x: round(haversine(x['Longtitude'],x['Latitude'],float(long),float(lat)),2), axis=1)
    output_name=input('Please select your desired file name for output: ')
    df.to_csv(f'{output_name}.csv',index=False)
    print(f'The data had been saved as {output_name}.csv')