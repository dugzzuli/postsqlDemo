class Company:

	__id=''
	__name='dugking'
	__age=18
	__address=''
	__salary=0
	__join_date=''

	def setId(self,value):
		self.__id=value
	def getId(self):
		return self.__id

	def setName(self,value):
		self.__name=value
	def getName(self):
		return self.__name

	def setAge(self,value):
		self.__age=value
	def getAge(self):
		return self.__age

	def setAddress(self,value):
		self.__address=value
	def getAddress(self):
		return self.__address

	def setSalary(self,value):
		self.__salary=value
	def getSalary(self):
		return self.__salary

	def setJoin_date(self,value):
		self.__join_date=value
	def getJoin_date(self):
		return self.__join_date

	def __str__(self):
		return ("姓名:%s 年龄%s"%(self.getName(), self.getAge()))

