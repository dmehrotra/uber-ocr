import sys
company_col='Which company is this fare from?'
metro_col='Is this fare from one of the following cities: New York, Boston, Chicago, Los Angeles, Miami, Philadelphia, San Francisco, Seattle and Washington DC.?'
surge_col = 'Is this a Surge/Prime Time fare?'
rider_col = 'How much did the rider pay?'
ul_col= 'How much did Uber/Lyft receive?'

def get_company():
	company = raw_input("Enter Company: ")
	return company

def get_surge():
	cases = {
		"t":1,
		"f":0
	}
	surge = raw_input("Surge (t/f): ")
	return cases.get(surge, None) 

def get_metro():
	cases = {
		"t":1,
		"f":0
	}
	metro = raw_input("Major Metro (t/f): ")
	return cases.get(metro, None) 

