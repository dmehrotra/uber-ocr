import requests
import json
import sys
def get_start_date():
	start = raw_input("Enter Start Date: ")
	return start

def get_end_date():
	end = raw_input("Enter End Date: ")
	return end

def make_request(headers,params):
	resp = requests.get('https://api.typeform.com/forms/jeOoHn/responses', headers=headers, params=params)
	
	if resp.status_code == 200:
		j_data = json.loads(resp.text)
		if len(sys.argv) >= 2:
			print("total responses: "+ str(j_data['total_items']))
			print("page count: "+ str(j_data['page_count']))
			sys.exit(1)
		else:
			return j_data

	else:
		print("Error :: Typeform")
		sys.exit(1)

def build_response(response):
	try:
		return {
		"filled":True,
		"company":response["answers"][0]["choice"]["label"],
		"surge":response["answers"][1]['boolean'],
		"major_metro":response["answers"][2]['boolean'],
		"rider_paid":response["answers"][3]['number'],
		"driver_made":response["answers"][4]['number'],
		"uber_made":response["answers"][5]['number'],
		"image_url":response["answers"][-1]['file_url'],
		"id":response["response_id"]
		}
	except:
		return{"filled":False,"id":response["response_id"]}
