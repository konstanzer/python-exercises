import numpy as np

#1
days = np.array([3,5,1])
price = 3
total = np.sum(price*days)

#2
rates = dict(goog=400, amzn=380, fb=350)
hours = dict(goog=6, amzn=4, fb=10)

def earnings(rates, hours):
	earned = 0
	for k, v in hours.items():
		earned += rates[k]*v
	return earned

#3

if __name__ == "__main__":
	print("Those movies cost ${0:.2f}".format(total))
	print("You made ${0:.2f}".format(earnings(rates, hours)))
