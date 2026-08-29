import json

practice = open("output.json", "r")
device = json.load(practice)
practice.close()
device["voltage"] = 200
output = open("output.json", "w")
json.dump(device, output, indent=4)
output.close()

