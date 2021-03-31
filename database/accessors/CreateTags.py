
#adds tag to the database. Currently there are no checks to actually validate if that operation succeded
def createTag(dBase, name, value):
    statement = 'INSERT INTO tag(name, value) VALUES (\'%s\', \'%s\');' 
    dBase.runSQLNoReturn(statement)
    return True

#gets tag ID based on the name (which must be unique)
def findTagID(dBase, name):
    statement = 'SELECT id FROM tag WHERE name=\'%s\';' % (name)
    return dBase.runSQL(statement)


def findTag(dBase, id):
    statement = 'SELECT * FROM tag WHERE name=\'%s\';' % (id)
    return dBase.runSQL(statement)