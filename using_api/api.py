import requests
import json

def get_api_data():
  url = "https://vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com/api/vaccines/get-fda-approved-vaccines"
  headers = {
      'x-rapidapi-host': "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com",
      'x-rapidapi-key': "1ead6b9fb3msh90d4404a2b71121p1b963bjsncf4dad082546"
  }
  response = requests.request("GET", url, headers=headers)
  jsonData = json.loads(response.text)
  #return jsonData
  print(json.dumps(jsonData, indent=2))
  #print(jsonData[2]['trimedName'])

def get_phase_iv():
  # Objeto indice 4,  description
  url = "https://vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com/api/vaccines/get-all-vaccines-phase-iv"
  headers = {
      'x-rapidapi-host': "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com",
      'x-rapidapi-key': "1ead6b9fb3msh90d4404a2b71121p1b963bjsncf4dad082546"
  }
  response = requests.request("GET", url, headers=headers)
  jsonData = json.loads(response.text)
  #print(jsonData[4])
  print(json.dumps(jsonData, indent=2))

def get_covid_stats_by_country(country_iso_code):
  url = "https://vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com/api/covid-ovid-data/sixmonth/" + country_iso_code
  headers = {
      'x-rapidapi-host': "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com",
      'x-rapidapi-key': "1ead6b9fb3msh90d4404a2b71121p1b963bjsncf4dad082546"
  }
  response = requests.request("GET", url, headers=headers)
  jsonData = json.loads(response.text)
  return jsonData
  #print(json.dumps(jsonData, indent=2))
