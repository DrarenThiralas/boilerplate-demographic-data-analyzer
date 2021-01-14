import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
	df = pd.read_csv("adult.data.csv")

	racedict = {}
	avgmenage = 0.
	nummen = 0

	ednumtotal = 0
	ednumbach = 0

	hednumtotal = 0
	hednumrich = 0
	noednumtotal = 0
	noednumrich = 0

	mwh = 0

	lazytotal = 0
	lazyrich = 0

	TBCD = {}
	top = 0
	topCountry = ""

	occupationDict = {}

	for label, content in df.items():
		if label == "race":
			for thing in content:
				if thing in racedict:
					racedict[thing] += 1
				else:
					racedict[thing] = 1
		if label == "age":
			for i in range(len(content)):
				if df["sex"][i] == "Male":
					avgmenage += int(content[i])
					nummen += 1
		if label == "education":
			for i in range(len(content)):
				thing = content[i]
				ednumtotal += 1
				if thing == "Bachelors":
					ednumbach += 1

				if thing in ["Bachelors", "Masters", "Doctorate"]:
					hednumtotal += 1
					if df["salary"][i] != "<=50K":
						hednumrich += 1
				else:
					noednumtotal += 1
					if df["salary"][i] != "<=50K":
						noednumrich += 1
		if label == "hours-per-week":
			mwh = min(content)
			for i in range(len(content)):
				thing = content[i]
				if thing == mwh:
					lazytotal += 1
					if df["salary"][i] != "<=50K":
						lazyrich += 1
		if label == "native-country":
			for i in range(len(content)):
				thing = content[i]
				if thing in TBCD:
					TBCD[thing][0] += 1
				else:
					TBCD[thing] = [1, 0]
				if df["salary"][i] != "<=50K":
					TBCD[thing][1] += 1
			countryValues = list(map(lambda x: [x[0], round(x[1][1]/x[1][0] * 100, 1)], TBCD.items()))

			for tpl in countryValues:
				if tpl[1] > top:
					top = tpl[1]
					topCountry = tpl[0]
		if label == "occupation":
			for i in range(len(content)):
				thing = content[i]
				if df["salary"][i] != "<=50K" and df["native-country"][i] == "India":
					if thing in occupationDict:
						occupationDict[thing] += 1
					else:
						occupationDict[thing] = 1



    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
	race_count = pd.Series(racedict.values(), racedict.keys())

    # What is the average age of men?
	average_age_men = round(avgmenage/nummen, 1)

    # What is the percentage of people who have a Bachelor's degree?
	percentage_bachelors = round(ednumbach/ednumtotal * 100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
	higher_education = None
	lower_education = None

    # percentage with salary >50K
	higher_education_rich = round(hednumrich/hednumtotal * 100, 1)
	lower_education_rich = round(noednumrich/noednumtotal * 100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
	min_work_hours = mwh

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
	num_min_workers = None

	rich_percentage = round(lazyrich/lazytotal * 100, 1)

    # What country has the highest percentage of people that earn >50K?
	highest_earning_country = topCountry
	highest_earning_country_percentage = top

    # Identify the most popular occupation for those who earn >50K in India.
	top_IN_occupation = max(occupationDict, key=occupationDict.get)

    # DO NOT MODIFY BELOW THIS LINE

	if print_data:
		print("Number of each race:\n", race_count)
		print("Average age of men:", average_age_men)
		print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
		print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
		print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
		print(f"Min work time: {min_work_hours} hours/week")
		print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
		print("Country with highest percentage of rich:", highest_earning_country)
		print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
		print("Top occupations in India:", top_IN_occupation)

	return {
		'race_count': race_count,
		'average_age_men': average_age_men,
		'percentage_bachelors': percentage_bachelors,
		'higher_education_rich': higher_education_rich,
		'lower_education_rich': lower_education_rich,
		'min_work_hours': min_work_hours,
		'rich_percentage': rich_percentage,
		'highest_earning_country': highest_earning_country,
		'highest_earning_country_percentage':
		highest_earning_country_percentage,
		'top_IN_occupation': top_IN_occupation
	}
