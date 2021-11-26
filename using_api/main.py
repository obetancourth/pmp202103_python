from api import get_api_data, get_phase_iv, get_covid_stats_by_country
from dao.db import StatsCovid
#get_api_data()
#get_phase_iv()
#data = get_covid_stats_by_country('HND')
CovidModel = StatsCovid()
# for row in data:
#   CovidModel.insert(
#     row["symbol"],
#     row["Country"],
#     row["date"],
#     row["total_cases"],
#     row["new_cases"]
#   )
processData = CovidModel.getByMonth()
for datarow in processData:
  print(datarow)
