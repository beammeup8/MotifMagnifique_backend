

def createTags(dBase, name, value):
    statement = 'INSERT INTO tag(name, value) VALUES (%s, %s); SELECT id FROM tag WHERE name = %s;' % (name, value, name)
    result = dBase.runSQL(statement)
    return result

def findTag(dBase, name):
    statement = 'SELECT * FROM tag WHERE name = %s;' % (name)
    return dBase.runSQL(statement)

def modifyTag(dBase, id, name = None, value = None):
    pass