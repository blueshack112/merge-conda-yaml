import yaml


# Loading both YAML files
with open(r'example/environment.yml') as file:
    yaml1 = yaml.full_load(file)

with open(r'example/my-environment.yml') as file:
    yaml2 = yaml.full_load(file)

# Extracting keys out from both the YAMLs
keys1 = []
keys2 = []
keys3 = ['name', 'channels', 'dependencies']

for key, value in yaml1.items():
    keys1.append(key)
for key, value in yaml2.items():
    keys2.append(key)

""" Making sure that the YAMLs are in proper format"""
# TODO: add name of the YAML file that has faulty format
if ('channels' not in keys1 or 'dependencies' not in keys1):
    print ("The YAML file 1 seems to be corrupted. Please make sure that it is in proper format. (Proper format must contain 'name', 'channels' and 'dependencies' keys.")
    exit()
if ('channels' not in keys2 or 'dependencies' not in keys2):
    print ("The YAML file 2 seems to be corrupted. Please make sure that it is in proper format. (Proper format must contain 'name', 'channels' and 'dependencies' keys.")
    exit()

# Resolve name of the output file
# The first YAML's name will be used
# If name does not exist, use a generic placeholder
outputName = yaml1.get(keys3[0])
# TODO: change generic name
if outputName is None:
    outputName = "Generic Name"

# Merging channels


print (outputName)
exit()

for i in keys1:
    print (i)

print ("\n\n")

for i in keys1:
    print (yaml1.get(i))