import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    "day1",
    help="indicate whether the day provided is Monday",
    type=str)
parser.add_argument(
    "day2",
    help="indicate whether the day provided is a weekend",
    type=str)
args = parser.parse_args()

weekend = ["saturday", "sunday"]

print("is Monday" if args.day1.lower() == "monday"
                    else "not Monday")
print("is weekend" if args.day2.lower() in weekend
                    else "not weekend")

