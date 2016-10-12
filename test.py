from db_module import dbmodule
d=dbmodule()
d.openHighDb()
info=d.selectEmail("anquan")
print info