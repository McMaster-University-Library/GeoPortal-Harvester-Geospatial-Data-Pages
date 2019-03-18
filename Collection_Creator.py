# THIS PYTHON SCRIPT CREATES COLLECTIONS OF COMBINED SCHOLARS GEOPORTAL AND GEOSPATIAL DATA WEBPAGE COMPONENTS WITH THE
# LATEST CSV DOCUMENT OF EXTRACTED SCHOLARS GEOPORAL METADATA. TAKING THESE TWO CSV DOCUMENTS AS INPUTS, THE SCRIPT
# RETURNS THREE CSV FILES CONTAINING METADATA THAT IS USED FOR THE THREE DIFFERENT PROCESSES OF UPDATING, ADDING TO,
# OR DELETING FROM MCMASTER'S DIGITAL DATA REPOSITORY.

# Note: Currently, the script works only with Python 3.5.2 or newer, due to version-unique libraries and commands.

import sys
import csv
import shutil
import datetime

master =  []            # This holds contents of the latest existing Master CSV file.
oldgeospatial = []      # This holds existing geospatial item Nids included in the Master CSV file.
oldgeoportal = []       # This holds previous SGP IDs included in the Master CSV file.
oldgeoportaldata = []   # This holds previous SGP data included in the Master CSV file.

geospatialdata = []     # This holds latest downloaded geospatial data records.
geospatialnids = []     # This holds latest downloaded geospatial data Nids.
geospatialnonid = []    # This holds geospatial data records for addition.
geospatialtodelete = [] # This holds geospatial data records for deletion.

extracted = []          # This holds the latest geoportal records.
extractedSGPIDs = []    # This holds the latest extracted SGP IDs.
SGPstoadd = []          # This holds SGP IDs for addition.
SGPstodelete = []       # This holds SGP IDs for deletion.

# COLLECTING LAST UPDATED MASTER LIST OF COMBINED SCHOLARS GEOPORTAL AND GEOSPATIAL DATA WEBPAGE METADATA.
# Defining variables for the latest existing Master CSV file.
MasterPath = 'C:\\Home\\Geospatial-Collection'
filename1 = 'Master_Production_Extract.csv'
# Opening and reading contents of the Master CSV file.
with open(MasterPath.strip('\\') + '\\' + filename1, "r", encoding = "utf8") as lookupfile:
    reader1 = csv.reader(lookupfile, delimiter = ",")
    for row in reader1:

        # Skipping the first (header) line.
        if str(row[0]) == 'Nid':
            pass

        # Placing contents of the Master CSV file as rows in a list.
        else:
            master.append(row)

            # Placing previous geospatial data Nids of the Master CSV file in a list.
            if str(row[18]) == '':
                oldgeospatial.append(str(row[0]))

            # Placing previous SGP IDs and SGP Nids of the Master CSV file in a list.
            elif str(row[18]) != '':
                oldgeoportal.append(str(row[18]))
                oldgeoportaldata.append(row)

# COLLECTING LATEST DOWNLOADED LIST OF GEOSPATIAL DATA.
# Defining the latest geospatial data CSV file.
GeospatialPath = 'C:\\Home\\Geospatial-Collection'
filename2 = 'Geospatial_Data.csv'
# Opening and reading contents of the latest downloaded geospatial data.
with open(GeospatialPath.strip('\\') + '\\' + filename2, 'r', encoding = "utf8") as lookupfile:
    reader2 = csv.reader(lookupfile, delimiter = ",")
    for row in reader2:

        # Skipping the first (header) line.
        if str(row[0]) == 'Nid':
            pass
        
        # Placing contents of the Geospatial_Data CSV file as rows in a list.
        else:
            geospatialdata.append(row)

# COLLECTING LATEST EXTRACTED LIST OF SCHOLARS GEOPORTAL METADATA.
# Defining the latest Scholars Geoportal extract CSV file.
SGPPath = 'C:\\Home\\Geospatial-Collection\\SGP_Extracts'
filename3 = 'SGP_Extract.csv'
# Opening and reading contents of the latest Scholars Geoportal extract.
with open(SGPPath.strip('\\') + '\\' + filename3, 'r') as lookupfile:
    reader3 = csv.reader(lookupfile, delimiter = ",")
    for row in reader3:

        # Skipping the first (header) line.
        if str(row[0]) == 'SGP_id':
            pass

        # Placing contents of the SGP_Extract CSV file as rows in a list.
        else:
            extracted.append(row)
            
            # Appending latest extracted items' SGP ID to the SGPIDs list.
            extractedSGPIDs.append(str(row[0]))

# CREATING COLLECTION FILES OF GEOSPATIAL AND GEOPORTAL ITEMS TO BE UPDATED, ADDED, AND DELETED, AS WELL AS A
# COLLECTIVE MASTER LIST.

# Opening a new updates list the updated metadata will be written to, then defining a writer object responsible
# for converting the input data into delimited strings for the output file.
updatesoutfile = open('Collection_Updates.csv', 'wt', encoding = "utf8")
updateswriter = csv.writer(updatesoutfile, dialect = 'excel', lineterminator = '\n')

# Opening a new additions list the updated metadata will be written to, then defining a writer object responsible
# for converting the input data into delimited strings for the output file.
additionsoutfile = open('Collection_Additions.csv', 'wt', encoding = "utf8")
additionswriter = csv.writer(additionsoutfile, dialect = 'excel', lineterminator = '\n')

# Opening a new deletions list the updated metadata will be written to, then defining a writer object responsible
# for converting the input data into delimited strings for the output file.
deletionsoutfile = open('Collection_Deletions.csv', 'wt', encoding = "utf8")
deletionswriter = csv.writer(deletionsoutfile, dialect = 'excel', lineterminator = '\n')

# Opening a blank master list the updated metadata will be written to, then defining a writer object responsible
# for converting the input data into delimited strings for the output file.
masteroutfile = open('Master_Temp.csv', 'wt', encoding = "utf-8")
masterwriter = csv.writer(masteroutfile, dialect = 'excel', lineterminator = '\n')

# Defining the collections' header line.
header = ['Nid', 'Title', 'Year', 'Author', 'Format', 'Who Can Use This Data', 'URL', 'Abstract', 'Metadata',
          'How to Cite This', 'Scholars Geoportal URL', 'Geospatial Availability', 'Geospatial Subjects New',
          'Geospatial Geography', 'Geospatial Formats', 'Filepath', 'field_geospatial_image_alt',
          'field_geospatial_image_title', 'SGP_id', 'Projection', 'Datum', 'Entry Date', 'File Location', 'File Size']

# Writing the header line for all four files.
updateswriter.writerow(header)
additionswriter.writerow(header)
deletionswriter.writerow(header)
masterwriter.writerow(header)

# STEP 1:
# Writing downloaded geospatial data record metadata.
for record in geospatialdata:

    # Appending the item's Nid to the list of latest downloaded geospatial Nids.
    geospatialnids.append(record[0])

    # Writing it to the master file.
    masterwriter.writerow(record)

    # For instances where the geospatial record does not have an Nid, writing it to the additions file.
    if str(record[0]) == '':
        additionswriter.writerow(record)
        geospatialnonid.append(record)

    # For instances where the geospatial record does have an Nid, writing it to the updates file.
    else:
        updateswriter.writerow(record)

for item in master:

    nid = item[0]
    
    # STEP 2:
    # Overwriting existing Scholars Geoportal webpage metadata with latest SGP data extract.
    for extract in extracted:
        
        # Capturing the instance where an existing SGP IDs is listed within the latest SGP data extract.
        if str(item[18]) == str(extract[0]):

            item = ['', '', '', '', '', '','', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
            item[0] = nid             # Writing the Nid.
            item[18] = extract[0]     # Writing the SGP ID.
            item[1] = extract[1]      # Overwriting the title.
            item[2] = extract[7]      # Overwriting the year.
            item[3] = extract[2]      # Overwriting the author.
            item[4] = extract[10]     # Overwriting the format.
            item[5] = extract[11]     # Overwriting the data user group.
            item[6] = extract[8]      # Overwriting the URL.
            item[7] = extract[6]      # Overwriting the abstract.
            item[9] = '<p>' + str(extract[2]) + ' (' + str(extract[7])[-4:] + '). ' + str(extract[1]) + '. Retrieved from ' + str(extract[8])[12:-53] + '</p>' # Overwriting the citation.
            item[10] = extract[8]     # Overwriting the Scholars Geoportal URL.
            item[11] = 'Internet'     # Overwriting the Geospatial Availability.
            item[12] = extract[3]     # Overwriting the Geospatial Subject.
            item[13] = extract[4]     # Overwriting the Geospatial Geography.
            item[14] = extract[5]     # Overwriting the Geospatial Format.
            item[15] = extract[9]     # Overwriting the Scholars Geoportal thumbnail link.
            
            # Writing it to the master file.
            masterwriter.writerow(item)

            # For instances where the item does not have an Nid, writing it to the additions file.
            if item[0] == '':
                print ("It seems an error has occured. Please ensure to download the latest Master_Production_Extract.csv file before running the script again.")
                sys.exit()

            else:
                updateswriter.writerow(item)

        else:
            pass

    # STEP 3:
    # Determining the number of now obsolete items within the previous Geospatial and Geoportal collection.
    # These are skipped over and not written to the new Master list. Instead, they are written to the
    # deletions file.
    # Capturing the instance where a previous geospatial item Nid is not listed in the latest download.
    if str(item[0]) in oldgeospatial and str(item[0]) not in geospatialnids:

        # Appending the geospatial Nid to the geospatialtodelete list.
        geospatialtodelete.append(str(item[0]))

        # Writing the item to the deletions file.
        deletionswriter.writerow(item)
        
    # Capturing the instance where a previous SGP ID is not listed as an extracted SGP ID. 
    if str(item[18]) in oldgeoportal and str(item[18]) not in extractedSGPIDs:

        # Appending the items' SGP ID to the SGPstodelete list.
        SGPstodelete.append(str(item[18]))

        # Writing the item to the deletions file.
        deletionswriter.writerow(item)
        
    else:
        pass

# STEP 4:
# Writing new Scholars Geoportal webpage metadata to the Master CSV and additions file.
for extract in extracted:

    # Capturing the instance where an extracted SGP ID is not listed as an existing item's SGP ID.
    if str(extract[0]) not in oldgeoportal:
        
        # Appending the items' SGP ID to the SGPstoadd list.
        SGPstoadd.append(str(extract[0]))

        item = ['', '', '', '', '', '','', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
        item[18] = extract[0]     # Writing the SGP ID.
        item[1] = extract[1]      # Writing the title.
        item[2] = extract[7]      # Writing the year.
        item[3] = extract[2]      # Writing the author.
        item[4] = extract[10]     # Writing the format.
        item[5] = extract[11]     # Writing the data user group.
        item[6] = extract[8]      # Writing the URL.
        item[7] = extract[6]      # Writing the abstract.
        item[9] = '<p>' + str(extract[2]) + ' (' + str(extract[7])[-4:] + '). ' + str(extract[1]) + '. Retrieved from ' + str(extract[8])[12:-53] + '</p>' # Overwriting the citation.
        item[10] = extract[8]     # Writing the Scholars Geoportal URL.
        item[11] = 'Internet'     # Overwriting the Geospatial Availability.
        item[12] = extract[3]     # Overwriting the Geospatial Subject.
        item[13] = extract[4]     # Overwriting the Geospatial Geography.
        item[14] = extract[5]     # Overwriting the Geospatial Format.
        item[15] = extract[9]     # Writing the Scholars Geoportal thumbnail link.

        # Writing it to the master file.
        masterwriter.writerow(item)

        # Writing the row of metadata for each item into the additions file.
        additionswriter.writerow(item)

# PROVIDING INTERFACIAL USER INFORMATION ON THE RESULTS OF THIS UPDATE.
print (' ')
print ('MASTER LIST UPDATE SUMMARY')
print (' ')
print ('Number of Previous Geospatial Items: ' + str(len(oldgeospatial)))
print ('Number of Previous Geoportal Items: ' + str(len(oldgeoportal)))
print (' ')
print ('Number of Geospatial Items from Latest Download: ' + str(len(geospatialdata)))
print ('Number of Geoportal Items from Latest Extract: ' + str(len(extractedSGPIDs)))
print (' ')
print ('Number of New Geospatial Records For Addition: ' + str(len(geospatialnonid)))
print ('Number of Obsolete Geospatial Records For Deletion: ' + str(len(geospatialtodelete)))
print ('Number of New Geoportal Items For Addition: ' + str(len(SGPstoadd)))
print ('Number of Obsolete Geoportal Items For Deletion: ' + str(len(SGPstodelete)))
print (' ')

# CREATING A TIMESTAMPED COPY OF THE MASTER LIST AND CLOSING FILES.
updatesoutfile.close()
additionsoutfile.close()
deletionsoutfile.close()
masteroutfile.close()
shutil.copyfile(masteroutfile.name, 'Master_Collection_Creator_Output_YYYYMMDD.csv')	
shutil.copyfile(masteroutfile.name, 'Master_' + datetime.datetime.today().strftime('%Y%m%d') + '.csv')
