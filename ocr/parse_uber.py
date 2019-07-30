
def try_basic_e(content):
	for l in content:
		if "your earnings" in l and "$" in l:
			return l.split("your earnings")[1].strip()
def try_basic_u(content):
	for l in content:
		if "uber receives" in l and "$" in l:
			return l.split("uber receives")[1].strip()
def try_basic_r(content):
	for l in content:
		if "rider price" in l and "$" in l:
			return l.split("rider price")[1].strip()
		elif "rider payment" in l and "$" in l:
			return l.split("rider payment")[1].strip()


def try_order_u(content):
	line_index = None 
	for l in content:
		if line_index == None:
			if "uber receives" in l:
				line_index = content.index(l)
		else:
			if "total" in l:
				return l.split("total")[1].strip()

def try_order_r(content):
	line_index = None 
	for l in content:
		if line_index == None:
			if "rider pays" in l:
				line_index = content.index(l)
		else:
			if "total" in l:
				return l.split("total")[1].strip()
			elif "price" in l:
				return l.split("price")[1].strip()

def try_order_e(content):
	line_index = None 
	for l in content:
		if line_index == None:
			if "you receive" in l:
				line_index = content.index(l)
		else:
			if "total" in l:
				return l.split("total")[1].strip()

def try_order_e1(content):
	line_index = None 
	for l in content:
		if line_index == None:
			if "your earnings" in l and "calculated" not in l:
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



