import csv
from flow import *
from secret import *
from vetting import *
from ocr import *
from parse_uber import *
from parse_lyft import *
vetted=[]
not_vetted=[]
survey_responses=[]
start_date = get_start_date()
end_date = get_end_date()
headers = headers()
params = (('since', "2019-"+start_date+"T00:00:00"),('until', "2019-"+end_date+"T00:00:00"),('page_size',1000),)
response = make_request(headers,params)


for survey_response in response['items']:
	survey_responses.append(build_response(survey_response))

for survey_response in survey_responses:
	if survey_response["filled"]:
		print("./images/"+survey_response['image_url'])
		try:
			text = run_ocr("./images/"+survey_response['image_url'].split('/')[-2])
			text = text.lower()
			if survey_response['company']=="Uber":
				ocr = [get_driver_earnings(text.split('\n')),get_uber_total(text.split('\n')),get_rider_payment(text.split('\n'))]		
				survey=[survey_response['driver_made'],survey_response['uber_made'],survey_response['rider_paid']]
				if vet(ocr,survey):	
					vetted.append(survey_response['id'])
				else:
					not_vetted.append(survey_response['id'])

			else:
				
				ocr = [lget_driver_earnings(text.split('\n')),lget_uber_total(text.split('\n')),lget_rider_payment(text.split('\n'))]	
				survey=[survey_response['driver_made'],survey_response['uber_made'],survey_response['rider_paid']]
				
				if vet(ocr,survey):
					vetted.append(survey_response['id'])
				else:
					not_vetted.append(survey_response['id'])
		
		except:
			print("Error :: OCR")


print ("vetted: "+ str(len(vetted)))
print ("not vetted: "+ str(len(not_vetted)))
for v in vetted:
	print(v)


with open('../analysis/data/vetted.csv', mode='a') as vetted_file:
    cw = csv.writer(vetted_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for v in vetted:
    	cw.writerow([v])













