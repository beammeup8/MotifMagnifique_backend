
#adds tag to the database. Currently there are no checks to actually validate if that operation succeded
def createPattern(dBase, title, desc, price, link, creatorID):
    statement = f"INSERT INTO pattern(title, description, price, link, ownedBy) VALUES ({title}, {desc}, {price}, {link}, {creatorID});" 
    dBase.runSQLNoReturn(statement)
    return True

#gets Pattern ID based on the name (which must be unique)
def findPatternID(dBase, name):
    statement = f"SELECT id FROM tag WHERE name={name};" 
    return dBase.runSQL(statement)

def findTag(dBase, id):
    statement = 'SELECT * FROM tag WHERE name=\'%s\';' % (id)
    return dBase.runSQL(statement)