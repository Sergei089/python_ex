year = 2006

def is_leap_year(year):
	return year //400 or ( year //4 , not year //100)
print(is_leap_year(year))