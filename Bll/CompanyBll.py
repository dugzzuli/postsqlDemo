from Dal.CompanyDal import CompanyDal
from Model.Company import Company


class CompanyBll:
    def insertCompany(self,company: Company):
        return CompanyDal().insertCompany(company)

    def selectCompanyAll(self):
        listUser=CompanyDal().selectCompanyAll()

        return listUser
    def selectCompanyById(self,id:int):
        listUser=CompanyDal().selectCompanyById(id)

        return listUser