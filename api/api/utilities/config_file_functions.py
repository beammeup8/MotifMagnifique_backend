import yaml

def getYamlFileContents(filename):
  with open(filename) as file:
    return yaml.load(file, Loader=yaml.FullLoader)