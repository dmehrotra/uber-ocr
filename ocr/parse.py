
def try_basic_e(content):
	for l in content:
		if "Your Earnings" in l and "$" in l:
			return l.split("Your Earnings")[1].strip()
def try_basic_u(content):
	for l in content:
		if "Uber Receives" in l and "$" in l:
			return l.split("Uber Receives")[1].strip()
def try_basic_r(content):
	for l in content:
		if "Rider Payment" in l and "$" in l:
			return l.split("Rider Payment")[1].strip()


def try_order_u(content):
	line_index = None 
	for l in content:
		if line_index == None:
			if "Uber Receives" in l:
				line_index = content.index(l)
		else:
			if "Total" in l:
				return l.split("Total")[1].strip()

def try_order_r(content):
	line_index = None 
	for l in content:
		if line_index == None:
			if "Rider Pays" in l:
				line_index = content.index(l)
		else:
			if "Total" in l:
				return l.split("Total")[1].strip()
			elif "Price" in l:
				return l.split("Price")[1].strip()

def try_order_e(content):
	line_index = None 
	for l in content:
		if line_index == None:
			if "You Receive" in l:
				line_index = content.index(l)
		else:
			if "Total" in l:
				return l.split("Total")[1].strip()

def try_order_e1(content):
	line_index = None 
	for l in content:
		if line_index == None:
			if "Your Earnings" in l:
				line_index = content.index(l)
		else:
			if "$" in l:
				return l.strip()

def get_uber_total(content):
	uber_receives = try_basic_u(content)
	if uber_receives == None or uber_receives == "":
		uber_receives = try_order_u(content)
	return uber_receives
def get_rider_payment(content):
	rider_total = try_basic_r(content)
	if rider_total == None or rider_total == "":
		rider_total = try_order_r(content)
	return rider_total

def get_driver_earnings(content):
	your_earnings = try_basic_e(content)
	if your_earnings == None or your_earnings == "":
		your_earnings = try_order_e(content)
	if your_earnings == None or your_earnings == "":		
		your_earnings = try_order_e1(content)

	return your_earnings

# ar = [args["txt"],get_driver_earnings(),get_uber_total(),get_rider_payment()]



