from Utils.PGSQLUtil import PGSQLUtil
from Model.Company import Company
from psycopg2 import sql
class CompanyDal:
    
    def insertCompany(self,company:Company):
        pgSql=PGSQLUtil()
        sqlexe="insert into company (name,age,address,salary,join_date) values('{}',{},'{}',{},'{}')".format(company.getName(),company.getAge(),company.getAddress(),company.getSalary(),company.getJoin_date())
        row=pgSql.insertOperate(sqlexe)
        return row
    
    def selectCompanyAll(self):
        pgSql=PGSQLUtil()
        sqlexe="select * from company"

        rows=pgSql.execute(sqlexe,None)
        listUser=[]
        for irow in rows:
            model=Company()
            model.setId(irow[0])
            model.setName(irow[1])
            model.setAge(irow[2])
            model.setAddress(irow[3])
            model.setSalary(irow[4])
            model.setJoin_date(irow[5])
            listUser.append(model)

        return listUser
    
    def selectCompanyById(self,id:int):
        pgSql=PGSQLUtil()
        sqlexe="select * from company where id=%s;"

        rows=pgSql.execute(sqlexe,(id,))
        listUser=[]
        for irow in rows:
            model=Company()
            model.setId(irow[0])
            model.setName(irow[1])
            model.setAge(irow[2])
            model.setAddress(irow[3])
            model.setSalary(irow[4])
            model.setJoin_date(irow[5])
            listUser.append(model)

        return listUser

