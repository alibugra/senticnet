import urllib.request
import xmltodict
import argparse

# Construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-k", "--keyword", required=True)
args = vars(ap.parse_args())

# Start a new request on senticnet
file = urllib.request.urlopen('http://sentic.net/api/en/concept/' + args["keyword"])
data = file.read()
file.close()

# Get the xml response as data
data = xmltodict.parse(data)
obj = data["rdf:RDF"]
root_elements = obj["rdf:Description"]

# Print the specified datas
print(root_elements["pleasantness"]["#text"]) # pleasantness value
print(root_elements["attention"]["#text"]) # attention value
print(root_elements["sensitivity"]["#text"]) # sensitivity value
print(root_elements["aptitude"]["#text"]) # aptitude value
print(root_elements["polarity"]["#text"]) # polarity value
