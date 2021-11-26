## SGDistanceChecker

-  This repository documents project to take a directory of postal codes and map out the haversine distance to a reference postal code
-  This project is inspired from an industry's need to take a directory of postal codes and map out the haversine distance to a fixed postal code
-  This is my first attempt in creating a Python Program where it takes in user's input (reference postal code) and output a CSV file in the local directory
-  Some challenges faced in the project include selecting the API that can provide latitude and longitude from a provided postal code


## Documentation of the repo
- SGDistanceChecker.py: Main program that will output a desired CSV file to your local directory outlining the distance to a reference postal code keyed in from a user
- SGPostalCode.txt: Contains information on the postal code and its corresponding latitude and longitude downloaded from [GeoNames.org](http://download.geonames.org/export/zip/)
- readme.txt: Contains the readme information also downloaded from [GeoNames.org](http://download.geonames.org/export/zip/)
## Acknowledgements
- [GeoNames.org](http://download.geonames.org/export/zip/)
- [Geocode.xyz API](https://geocode.xyz/new_account)
- [Stackoverflow answer](https://stackoverflow.com/questions/4913349/haversine-formula-in-python-bearing-and-distance-between-two-gps-points)
