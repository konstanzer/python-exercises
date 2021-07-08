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
student_slots = np.zeros(10)
class_slots = [0,4] 
class_enrollment = 18;

def can_enroll(class_enrollment, class_slots, student_slots):
	max_class_size = 21
	if class_enrollment >= max_class_size:
		return False
	for time in class_slots:
		if student_slots[time] == 1:
			return False
	return True


if __name__ == "__main__":
	print("Those movies cost ${0:.2f}".format(total))
	print("You made ${0:.2f}".format(earnings(rates, hours)))
	print("Student can enroll: " +
		str(can_enroll(class_enrollment, class_slots, student_slots)))
