import os
import argparse
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--txt", required=True,
	help="path to input txt to be OCR'd")
args = vars(ap.parse_args())
count = 0
txt = args["txt"]
f=open(args["txt"], "r")
content=f.readlines()
nl=[]

def try_basic_e():
	for l in content:
		if "Your Earnings" in l and "$" in l:
			return l.split("Your Earnings")[1].strip()
def try_basic_u():
	for l in content:
		if "Uber Receives" in l and "$" in l:
			return l.split("Uber Receives")[1].strip()
def try_basic_r():
	for l in content:
		if "Rider Payment" in l and "$" in l:
			return l.split("Rider Payment")[1].strip()


def try_order_u():
	line_index = None 
	for l in content:
		if line_index == None:
			if "Uber Receives" in l:
				line_index = content.index(l)
		else:
			if "Total" in l:
				return l.split("Total")[1].strip()

def try_order_r():
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

def try_order_e():
	line_index = None 
	for l in content:
		if line_index == None:
			if "You Receive" in l:
				line_index = content.index(l)
		else:
			if "Total" in l:
				return l.split("Total")[1].strip()

def try_order_e1():
	line_index = None 
	for l in content:
		if line_index == None:
			if "Your Earnings" in l:
				line_index = content.index(l)
		else:
			if "$" in l:
				return l.strip()

def get_uber_total():
	uber_receives = try_basic_u()
	if uber_receives == None or uber_receives == "":
		uber_receives = try_order_u()
	return uber_receives
def get_rider_payment():
	rider_total = try_basic_r()
	if rider_total == None or rider_total == "":
		rider_total = try_order_r()
	return rider_total

def get_driver_earnings():
	your_earnings = try_basic_e()
	if your_earnings == None or your_earnings == "":
		your_earnings = try_order_e()
	if your_earnings == None or your_earnings == "":		
		your_earnings = try_order_e1()

	return your_earnings

ar = [args["txt"],get_driver_earnings(),get_uber_total(),get_rider_payment()]

for a in ar:
	if a == None or a == "":
		count = count + 1

if count <= 1:
	os.rename(ar[0], "c.txt")
	print ar


