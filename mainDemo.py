from Bll.CompanyBll import CompanyBll
from Model.Company import Company


if __name__ == "__main__":

    bll=CompanyBll()
    company=Company()
    company.setAddress("云南大学")
    company.setAge(18)
    company.setJoin_date("2020-04-14")
    company.setName("dugking")
    company.setSalary(10000)
    print(bll.insertCompany(company))
    userList=bll.selectCompanyById(21)
    for model in userList:
        print(model)