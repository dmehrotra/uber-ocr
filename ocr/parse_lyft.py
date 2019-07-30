def ltry_basic_u(content):
	for l in content:
		if "lyft receives" in l and "$" in l:
			return l.split("lyft receives")[1].strip()
def ltry_basic_r(content):
	for l in content:
		if "ride payment" in l and "$" in l:
			return l.split(" ")[-1].strip()


def ltry_order_u(content):
	line_index = None 
	for l in content:
		if line_index == None:
			if "lyft receive" in l:
				line_index = content.index(l)
		else:
			if "total" in l:
				return l.split("total")[1].strip()

def ltry_order_r(content):
	line_index = None 
	for l in content:
		if line_index == None:
			if "ride payment" in l:
				line_index = content.index(l)
		else:
			if "total" in l:
				return l.split("total")[1].strip()
			elif "price" in l:
				return l.split("price")[1].strip()

def ltry_order_e(content):
	line_index = None 
	for l in content:
		if line_index == None:
			if "you receive" in l:
				line_index = content.index(l)
		else:
			if "total" in l:
				return l.split("total")[1].strip()

def ltry_order_e1(content):
	line_index = None 
	for l in content:
		if line_index == None:
			if "earnings" in l and "calculate" not in l:
				line_index = content.index(l)
		else:
			if "$" in l:
				return l.split(" ")[-1]

def lget_uber_total(content):
	uber_receives = ltry_basic_u(content)
	if uber_receives == None or uber_receives == "":
		uber_receives = ltry_order_u(content)
	return uber_receives
def lget_rider_payment(content):
	rider_total = ltry_basic_r(content)
	if rider_total == None or rider_total == "":
		rider_total = ltry_order_r(content)
	return rider_total

def lget_driver_earnings(content):
	your_earnings = ltry_order_e(content)
	if your_earnings == None or your_earnings == "":		
		your_earnings = ltry_order_e1(content)

	return your_earnings

# ar = [args["txt"],get_driver_earnings(),get_uber_total(),get_rider_payment()]



