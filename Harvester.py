# THIS PYTHON SCRIPT PARSES THROUGH AN XML DOCUMENT INPUT OF ITEMS IN THE SCHOLARS GEOPORTAL AND RETURNS A CSV FILE
# CONTAINING SELECTED METADATA. THIS CSV FILE IS LATER USED TO POPULATE STATIC WEBPAGES TO BE GOOGLE INDEXED, MAKING
# THE GEOPORTAL ITEMS MORE DISCOVERABLE. THE SELECTED METADATA INCLUDE THE FIELDS: IDENTIFIER, TITLE, PRODUCER,
# ABSTRACT, PUBLICATION YEARS, GEOPORTAL PERMALINK, LINK TO THE ITEM'S THUMBNAIL IMAGE, AVAILABLE FORMATS, AND USERS
# WITH VIEW PERMISSION TO EACH ITEM.

# Note: - Currently, the script works only with Python 3.5.2 or newer, due to version-unique libraries and commands.
#       - The xml.etree.ElementTree module implements an API for parsing XML data. Its documentation may be found at
#         https://docs.python.org/3/library/xml.etree.elementtree.html.

import sys
import csv
import shutil
from urllib import request
import xml.etree.ElementTree as ET
import datetime

# DOWNLOADING THE XML FILE FROM SCHOLAR GEOPORTAL'S URL TO USER ACCESSIBLE CONTENT.

# Defining the URL to user accessible content as provided by Scholars GeoPortal.
URL = "http://geo2.scholarsportal.info/proxy.html?http:__giseditor.scholarsportal.info/search/index.html?limit=entitled&env=production&q=*&i=2000&fm=xml"

# Creating a function that retrieves the content from the URL above.
def get(URL):
    with request.urlopen(URL) as content:
        return content.read()

# Downloading the XML document into C:\Home\GeoPortal.
with open ('Content.xml', 'wb') as xmlfile:
    xmlfile.write(get(URL))

# IMPORTING THE XML DATA BY READING FROM Content.xml.

# Here, .getroot() obtains the top element of the XML file. In this case, the top element is response, which
# contains the total list of results provided by the XML document.
xmldata = ET.parse('Content.xml')
response = xmldata.getroot()

# DETERMINING THE NUMBER OF EXTRACTED ITEMS.
extractedids = []

# WRITING THE DESIRED FIELDS OF METADATA TO SGP_Extract.csv and SGP_Extract_Duplicates.csv.

# Opening the output file the condensed metadata will be written and appended to, then defining a writer object
# responsible for converting the input data into delimited strings for the output file.
SGPPath = 'SGP_Extracts'
outfile = open(SGPPath.strip('\\')+'\\'+'SGP_Extract.csv', 'wt')
outfile = open(SGPPath.strip('\\')+'\\'+'SGP_Extract.csv', 'a')
writer = csv.writer(outfile, dialect = 'excel', lineterminator = '\n')

# Opening the output file that metadata with duplicate SGP IDs will be written and appended to, then defining a writer object
# responsible for converting the input data into delimited strings for the output file.
SGPPath = 'SGP_Extracts'
outfile2 = open(SGPPath.strip('\\')+'\\'+'SGP_Extract_Duplicates.csv', 'wt')
outfile2 = open(SGPPath.strip('\\')+'\\'+'SGP_Extract_Duplicates.csv', 'a')
writer2 = csv.writer(outfile2, dialect = 'excel', lineterminator = '\n')

# Opening the Geospatial Subjects Mappings file and placing rows as items in a list.
#MappingPath = 'C:\\Home\\Geospatial-Collection\\'
infile = 'Geospatial_Subject_Mappings.csv'
#with open(MappingPath.strip('\\') + '\\' + infile, "r", encoding = "utf8") as lookupfile:
with open(infile, "r", encoding = "utf8") as lookupfile:

    reader = csv.reader(lookupfile, delimiter = ",")
    mappinglist = []
    for row in reader:
        mappinglist.append(row)

# Writing the header line of the SGP Extract and SGP Duplicates files.
writer.writerow(['SGP_id', 'Title', 'Producer', 'Category', 'Place', 'Type', 'Abstract', 'Coverage (Years)', 'layer_url', 'layer_thumb', 'Available Formats', 'Users with View Permissions'])
writer2.writerow(['SGP_id', 'Title', 'Producer', 'Category', 'Place', 'Type', 'Abstract', 'Coverage (Years)', 'layer_url', 'layer_thumb', 'Available Formats', 'Users with View Permissions'])

linecollection = [] # This is the empty list to which each row of item information will be temporarily appended to.

# Writing desired metadata from the XML file to the output file.
for result in response.findall('result'):

    line = [] # This is the empty list to which information will be appended to within an item's row.
    extractedids.append(result.find('id').text) # Appending the item identifier.
    line.append(result.find('id').text)         # Appending the item identifier.
    line.append(result.find('title').text)      # Appending the title.
    line.append(result.find('producer').text)   # Appending the producer.

    # Standardizing the subjects category to options available on the library page.
    # This is done according to Geospatial_Subject_Mappings.txt found within the local folder.
    subject = result.find('category').text
    for row in mappinglist:
        if subject == str(row[0]):
            subject = str(row[1])
        else:
            pass
    line.append(subject)                        # Appending the subject.

    # Standardizing the place category to options available on the library page.
    place = str(result.find('place').text)
    place = place.split()
    placecategories = ['Canada', 'Hamilton', 'Ontario', 'USA', 'World']
    if result.find('place').text is None:
        placecategory = ' '
    elif place[-1] in placecategories:
        placecategory = place[-1]
    elif place[-2] in placecategories:
        placecategory = place[-2]
    line.append(placecategory)                  # Appending the place category.

    line.append(result.find('type').text)       # Appending the geospatial format.
    line.append(result.find('abstract').text)   # Appending the abstract.

    # Obtaining the earliest publication year available.
    earliestdate = result[10][0].text
    earliestyear = earliestdate[:4]

    try:

        # Obtaining the most recent publication year available.
        # Capturing the instance where result[11] is 'revision-date'.
        if len(result[11][0].text) == 10:

                latestdate = result[11][0].text
                latestyear = latestdate[:4]

        else:

            pass

    # Capturing the instance where result[11] is another field.
    # In this case, there is only one publication, and one publication date.
    except:

        latestyear = earliestyear

    # Obtaining and appending the range of years for available publications.
    publicationrange = earliestyear + ' - ' + latestyear

    # Creating each item's permalink.
    permalink = '<p><a href="http://geo.scholarsportal.info/#r/details/_uri@=' + result.find('id').text + '">Access this resource</a> on Scholars Geoportal.</p>'
    formats = "Various geospatial formats available."

    # Obtaining information on users with view permission for each item.
    # Currently, Scholars GeoPortal has noted that all items within the OpenContent and DLI collections are open.
    if result.find('collections').text == "OpenContent":
        permission = "Public"

    elif result.find('collections').text == "DLI":
        permission = "Public"

    else:
        permission = "McMaster Students / Staff / Faculty only. Login required for off-campus access."

    line.append(publicationrange)               # Appending the range of publication years.
    line.append(permalink)                      # Appending the permalink.
    line.append(result.find('thumbnail').text)  # Appending the thumbnail link.
    line.append(formats)                        # Appending the format information.
    line.append(permission)                     # Appending the users with view permission.

    # Appending the row of metadata for each item into a temporary list.
    linecollection.append(line)

uniqueSGPs = [] # This list contains unique SGP IDs in the latest extract.
duplicatelines = [] # This list contatins SGP items with the same SGP ID as one other item in the extract.

# Catching items with duplicate SGP IDs and writing or removing them from the appropriate files.
for line in linecollection:
    uniqueline = [] # This list contains lines of items with the same SGP ID.

    # Appending an item's SGP ID to the list of unique SGP IDs.
    if line[0] not in uniqueSGPs:
        uniqueSGPs.append(line[0])

        # Catching the instance where the SGP ID of each item is equal to itself or that of other items in the list.
        for duplicateline in linecollection:
            if duplicateline[0] == line[0]:

                # Appending the lines with the same SGP IDs to a list.
                uniqueline.append(duplicateline)

                # Catching the instance where the SGP ID of an item is equal to that of one other item in the list.
                if len(uniqueline) == 2:
                    # Removing the first item of a duplicate from the master extract list.
                    linecollection.remove(uniqueline[0])
                    # Appending duplicate items to a list.
                    duplicatelines.append(uniqueline[0])
                    duplicatelines.append(uniqueline[1])

    else:
        pass

# Writing each unique SGP item to SGP_Extract.csv.
for line in linecollection:
    writer.writerow(line)

# Writing each duplicate item to SGP_Extract_Duplicates.csv.
for line in duplicatelines:
    writer2.writerow(line)

# PROVIDING INTERFACIAL USER INFORMATION ON THE RESULTS OF THIS UPDATE.
print ('Number of Extracted SGP Items (Excluding Duplicates): ' + str(len(linecollection)))
if duplicatelines == []:
    print ('Note: No duplicate SGP IDs were found for GeoPortal items.')
else:
    print ('Note: Duplicate SGP IDs were found for ' + str(len(duplicatelines)/2) + ' GeoPortal items.')
    print (' ')
print ('The newly harvested Scholars GeoPortal metadata has been written to', outfile.name)
print ('A list of duplciate metadata has been written to', outfile2.name)

# CREATING A TIMESTAMPED COPY OF THE SGP EXTRACT AND CLOSING FILES.
outfile.close()
outfile2.close()
shutil.copyfile(outfile.name, 'SGP_Extracts\\SGP_Extract_' + datetime.datetime.today().strftime('%Y%m%d') + '.csv')
shutil.copyfile(outfile2.name, 'SGP_Extracts\\SGP_Extract_Duplicates' + datetime.datetime.today().strftime('%Y%m%d') + '.csv')
