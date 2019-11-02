'''


new_range is the new version python rage class:
in previous range class you are restricted to produce range of numbers
from one to another either by adding one value or by subtracting one value
in this version you can do same by doing continous multiplication,division and also by obtaining  
remainder is well.
for example (tested on Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) 
[MSC v.1916 64 bit (AMD64)] on win32:
	a) new_range(3,50,'*3')  
	   produce [3,9,45]
       take care that third parameter is string default to '+1'

    b) new_range(100,1,'/3')
    	[100, 33.333333333333336, 11.111111111111112, 3.703703703703704, 1.234567901234568]

    c) new_range(100,1,'//3')
    	[100, 33, 11, 3]



'''



class new_range:
	def __init__(self,*args):
		if len(args)>=1 and len(args)<4:
			self.begin=(args[0] if len(args)>1 else 0)
			self.end=(args[1] if len(args)>1 else args[0])
			self.step=(args[2] if len(args)==3  else '+1')
			self.list=[]
			i=self.begin
			c='i'+self.step
			comp=('<' if self.step[0] in ['+','*'] else '>')
			comp1='i'+comp+str(self.end)
			
			
			while eval(comp1) :
				
				self.list.append(i)
				i=eval(c)

		else:
			raise Exception("invalid number of arguments")
	def __str__(self):
		return str(self.list)
	def __contains__(self,j):
		return j in self.list
	def __iter__(self):
		return iterable_range(self)


class iterable_range:
	def __init__(self,nrange):
		self.list=nrange.list
		self.index=0
	def __next__(self):
		if self.index < len(self.list):
			result=self.list[self.index]
			self.index+=1
			return result
		else:
			raise StopIteration

