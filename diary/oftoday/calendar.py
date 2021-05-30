from datetime import datetime, timedelta
from calendar import HTMLCalendar
from .models import Event, Fotd, Ootd, Motd, Totd

class Calendar_F(HTMLCalendar):
	def __init__(self, year=None, month=None,user=None):
		self.year = year
		self.month = month
		self.user = user
		super(Calendar_F, self).__init__()

	# '일'을 td 태그로 변환하고 이벤트를 '일'순으로 필터
	def formatday(self,year,month, day, fotds):
		fotds_per_day = fotds.filter(day__year=year, day__month=month,day__day=day)
		d = ''
		for fotd in fotds_per_day:
			d += f'<li> {fotd.title} </li>'

		if day != 0:
			return f"<td><span class='date'><a style='color:#858492;' href='main_detail/{year}/{month}/{day}'>{day}</a></span><ul class='event_line'> {d} </ul></td>"
		return '<td></td>'

	# '주'를 tr 태그로 변환
	def formatweek(self,year,month, theweek, fotds):
		week = ''
		for d, weekday in theweek:
			week += self.formatday(year, month, d, fotds)
		return f'<tr> {week} </tr>'

	# '월'을 테이블 태그로 변환
	# 각 '월'과 '연'으로 이벤트 필터
	def formatmonth(self, withyear=True):
		fotds = Fotd.objects.filter(day__year=self.year, day__month = self.month, author= self.user)
		cal = f'<table class="calendar">\n'
		cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
		cal += f'{self.formatweekheader()}\n'
		for week in self.monthdays2calendar(self.year, self.month):
			cal += f'{self.formatweek(self.year,self.month, week, fotds)}\n'
		return cal

class Calendar_O(HTMLCalendar):
	def __init__(self, year=None, month=None,user=None):
		self.year = year
		self.month = month
		self.user = user
		super(Calendar_O, self).__init__()

	# '일'을 td 태그로 변환하고 이벤트를 '일'순으로 필터
	def formatday(self,year,month, day, ootds):
		ootds_per_day = ootds.filter(day__year=year, day__month=month,day__day=day)
		d = ''
		for ootd in ootds_per_day:
			d += f'<li> {ootd.title} </li>'

		if day != 0:
			return f"<td><span class='date'><a style='color:#858492;' href='main_detail/{year}/{month}/{day}'>{day}</a></span><ul class='event_line'> {d} </ul></td>"
		return '<td></td>'

	# '주'를 tr 태그로 변환
	def formatweek(self,year,month, theweek, ootds):
		week = ''
		for d, weekday in theweek:
			week += self.formatday(year, month, d, ootds)
		return f'<tr> {week} </tr>'

	# '월'을 테이블 태그로 변환
	# 각 '월'과 '연'으로 이벤트 필터
	def formatmonth(self, withyear=True):
		ootds = Ootd.objects.filter(day__year=self.year, day__month = self.month,author= self.user)
		cal = f'<table class="calendar">\n'
		cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
		cal += f'{self.formatweekheader()}\n'
		for week in self.monthdays2calendar(self.year, self.month):
			cal += f'{self.formatweek(self.year,self.month, week, ootds)}\n'
		return cal

class Calendar_T(HTMLCalendar):
	def __init__(self, year=None, month=None,user=None):
		self.year = year
		self.month = month
		self.user = user
		super(Calendar_T, self).__init__()

	# '일'을 td 태그로 변환하고 이벤트를 '일'순으로 필터
	def formatday(self,year,month, day, totds):
		totds_per_day = totds.filter(day__year=year, day__month=month,day__day=day)
		d = ''
		for totd in totds_per_day:
			d += f'<li> {totd.title} </li>'

		if day != 0:
			return f"<td><span class='date'><a style='color:#858492;' href='main_detail/{year}/{month}/{day}'>{day}</a></span><ul class='event_line'> {d} </ul></td>"
		return '<td></td>'

	# '주'를 tr 태그로 변환
	def formatweek(self,year,month, theweek, totds):
		week = ''
		for d, weekday in theweek:
			week += self.formatday(year, month, d, totds)
		return f'<tr> {week} </tr>'

	def formatmonth(self, withyear=True):
		totds = Totd.objects.filter(day__year=self.year, day__month = self.month,author= self.user)
		cal = f'<table class="calendar">\n'
		cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
		cal += f'{self.formatweekheader()}\n'
		for week in self.monthdays2calendar(self.year, self.month):
			cal += f'{self.formatweek(self.year,self.month, week, totds)}\n'
		return cal

class Calendar_nonlogin(HTMLCalendar):
	def __init__(self, year=None, month=None):
		self.year = year
		self.month = month
		super(Calendar_nonlogin, self).__init__()

	# '일'을 td 태그로 변환하고 이벤트를 '일'순으로 필터
	def formatday(self,year,month, day):

		if day != 0:
			return f"<td><span class='date'><a style='color:#858492;' href='main_detail/{year}/{month}/{day}'>{day}</a></span></td>"
		return '<td></td>'

	# '주'를 tr 태그로 변환
	def formatweek(self,year,month, theweek):
		week = ''
		for d, weekday in theweek:
			week += self.formatday(year, month, d)
		return f'<tr> {week} </tr>'

	# '월'을 테이블 태그로 변환
	# 각 '월'과 '연'으로 이벤트 필터
	def formatmonth(self, withyear=True):
		cal = f'<table class="calendar">\n'
		cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
		cal += f'{self.formatweekheader()}\n'
		for week in self.monthdays2calendar(self.year, self.month):
			cal += f'{self.formatweek(self.year,self.month, week)}\n'
		return cal

class Calendar_M(HTMLCalendar):
	def __init__(self, year=None, month=None,user=None):
		self.year = year
		self.month = month
		self.user = user
		super(Calendar_M, self).__init__()

	# '일'을 td 태그로 변환하고 이벤트를 '일'순으로 필터
	def formatday(self,year,month, day, motds):
		motds_per_day = motds.filter(day__year=year, day__month=month,day__day=day)
		d = ''
		for motd in motds_per_day:
			d += f'<li> {motd.title} </li>'

		if day != 0:
			return f"<td><span class='date'><a style='color:#858492;' href='main_detail/{year}/{month}/{day}'>{day}</a></span><ul class='event_line'> {d} </ul></td>"
		return '<td></td>'

	# '주'를 tr 태그로 변환
	def formatweek(self,year,month, theweek, motds):
		week = ''
		for d, weekday in theweek:
			week += self.formatday(year, month, d, motds)
		return f'<tr> {week} </tr>'

	# '월'을 테이블 태그로 변환
	# 각 '월'과 '연'으로 이벤트 필터
	def formatmonth(self, withyear=True):
		motds = Motd.objects.filter(day__year=self.year, day__month = self.month,author= self.user)
		cal = f'<table class="calendar">\n'
		cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
		cal += f'{self.formatweekheader()}\n'
		for week in self.monthdays2calendar(self.year, self.month):
			cal += f'{self.formatweek(self.year,self.month, week, motds)}\n'
		return cal
