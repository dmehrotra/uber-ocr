def vet(ocr,survey):
	ar = []
	for i in range(len(ocr)):
		checked = check(ocr[i],survey[i])
		ar.append(checked)

	return tally(ar)

def check(o,s):
	try:
		co = o.strip("$").split('.')[0]
		co = int(co)
		if co == s or co+1 == s or co-1 ==s:
			return True
		else:
			return False
	except:
		try:
			if "rider price" in str(o):
				check(str(o).split("rider price")[1],s)
			else:
				print("Error :: Vetting :: "+str(o))
				return False
		except:
			print("Error :: Vetting Failed After Second :: "+str(o))
			return False


def tally(ar):
	count = 0
	for a in ar:
		if a == None or a == False:
			count = count + 1
	if count <= 1:
		return True
	else:
		return False