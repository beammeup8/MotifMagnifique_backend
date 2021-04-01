def tuples_to_dict(keys, values):
  return {keys[i] : values[i] for i, _ in enumerate(keys)}

def list_to_sql_fields_and_values(lst):
  listToStr = ', '.join(map(str, lst))
  valuesString = ','.join(map(str, ['?'] * len(lst)))
  return "(" + listToStr + ")", "(" + valuesString + ")"