#-*- encoding: utf-8 -*-
 
from Utils import PGSQLUtil
 
if __name__ == "__main__":
    table_name='company'
    pgsqlUtil = PGSQLUtil.PGSQLUtil(host="127.0.0.1", user="postgres", password="postgres", database="dugking")
    ## 查询表数据
    result = pgsqlUtil.execute("SELECT * FROM company")

    # result = pgsqlUtil.get_table_fields("t_user")

    result = pgsqlUtil.table_metadata(table_name)
    with open('./ModelTemplate/{}.pytemp'.format(table_name.capitalize()),mode="w") as fw:
        fw.write("class {}:\n".format(table_name.capitalize()))
        fw.write("\n")

        for irow in result:
            co_name=irow[3]
            fw.write("\t__{}=''\n".format(co_name))
        
        fw.write("\n")

        for irow in result:
            co_name=irow[3]
            
            fw.write("\tdef set{}(self,value):\n".format(co_name.capitalize()))
            fw.write("\t\tself.__{}=value\n".format(co_name))
            fw.write("\tdef get{}(self):\n".format(co_name.capitalize()))
            fw.write("\t\treturn self.__{}\n\n".format(co_name))
        sql=""
        sql+="insert into {} (".format(table_name)
        for irow in result:
            sql+="{},".format(irow[3])
        sql=sql[:-1]
        sql+=") "
        
        sql+="values("
        for irow in result:
            sql+="{}.{},".format(table_name,irow[3])
        
        sql=sql[:-1]
        sql+=") "
        print(sql)



        
        

