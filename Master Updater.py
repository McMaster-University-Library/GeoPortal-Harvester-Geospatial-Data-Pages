# THIS PYTHON SCRIPT UPDATES A MASTER LIST OF COMBINED SCHOLARS GEOPORTAL AND GIS DATA WEBPAGE COMPONENTS WITH THE
# LATEST CSV DOCUMENT OF EXTRACTED SCHOLARS GEOPORAL METADATA. TAKING THESE TWO CSV DOCUMENTS AS INPUTS, THE SCRIPT
# RETURNS A NEWLY UPDATED CSV FILE CONTAINING METADATA THAT IS LATER POPULATED INTO A DIGITAL DATA REPOSITORY.

# Note: Currently, the script works only with Python 3.5.2 or newer, due to version-unique libraries and commands.

import sys
import csv
import shutil
import datetime

master =  []            # This holds contents of the Master CSV file.
currentSGPIDs = []      # This holds current SGP IDs included in the Master CSV file.
extracted = []          # This holds the latest Scholars GeoPortal records.
extractedSGPIDs = []    # This holds the latest extracted SGP IDs.
SGPstoadd = []          # This holds extracted SGP IDs to be added to the Master list.
SGPstodelete = []       # This holds extracted SGP IDs to be deleted from the Master list.
GISData = []            # This holds current GIS Data titles included in the Master CSV file.

# COLLECTING LAST UPDATED MASTER LIST OF COMBINED SCHOLARS GEOPORTAL AND GIS DATA WEBPAGE METADATA.

# Defining variables for the Master CSV file.
filepath = 'C:\Home\\GeoPortal-Harvester'
filename1 = 'Master - Working Copy.csv'
# Opening and reading contents of the Master CSV file.
with open(filepath.strip('\\') + '\\' + filename1, "r", encoding = "utf8") as lookupfile:
    reader1 = csv.reader(lookupfile, delimiter = ",")
    
    for row in reader1:

        # Skipping the first (header) line.
        if str(row[0]) == 'Nid':
            pass

        # Placing contents of the Master CSV file as rows in a list.
        else:
            master.append(row)

            # Placing current SGP IDs of the Master CSV file in a list.
            if str(row[19]) != '':
                currentSGPIDs.append(str(row[19]))

# COLLECTING LATEST EXTRACTED LIST OF SCHOLARS GEOPORTAL METADATA.

# Defining the latest Scholars Geoportal extract CSV file.
filename2 = 'SGP_Extract - Working Copy.csv'
# Opening and reading contents of the latest Scholars Geoportal extract.
with open(filepath.strip('\\') + '\\' + filename2, 'r') as lookupfile:
    reader2 = csv.reader(lookupfile, delimiter = ",")
    # Placing extracted Scholars Geoportal records as rows in a list.
    for row in reader2:
        extracted.append(row)
        # Appending the items' SGP ID to the SGPIDs list.
        extractedSGPIDs.append(str(row[0]))

# UPDATING THE MASTER LIST WITH THE LATEST EXTRACTED SCHOLARS GEOPORTAL DATA.

# Opening a blank master list the updated metadata will be written to, then defining a writer object responsible
# for converting the input data into delimited strings for the output file.
outfile = open('Master_Temp.csv', 'wt', encoding = "utf8")
writer = csv.writer(outfile, dialect = 'excel', lineterminator = '\n')

# Writing the header line of the Master list.
writer.writerow(['Nid', 'Title', 'Year', 'Author', 'Format', 'Who Can Use This Data', 'URL', 'Abstract', 'Metadata',
                 'How to Cite This', 'Scholars Geoportal URL', 'Scholars Geoportal URL','To Delete',
                 'Geospatial Availability', 'Geospatial Subjects New', 'Geospatial Geography', 'Filepath',
                 'field_geospatial_image_alt', 'field_geospatial_image_title', 'SGP_id'])

for item in master:

    # STEP 1:
    # Writing existing GIS Data item metadata.
    if str(item[19]) == '':
        
        GISData.append(str(item[1]))
        writer.writerow(item)
        
    # STEP 2:
    # Overwriting existing Scholars Geoportal webpage metadata with latest SGP data extract.
    for extract in extracted:

        # Capturing the instance where an existing SGP IDs is listed within the latest SGP data extract.
        if str(item[19]) == str(extract[0]):
            
            item[1] = extract[1]      # Overwriting the title.
            item[2] = extract[4]      # Overwriting the year.
            item[3] = extract[2]      # Overwriting the author.
            item[4] = extract[7]      # Overwriting the format.
            item[5] = extract[8]      # Overwriting the data user group.
            item[6] = extract[5]      # Overwriting the URL.
            item[7] = extract[3]      # Overwriting the abstract.
            item[10] = extract[5]     # Overwriting the Scholars Geoportal URL.
            item[16] = extract[6]     # Overwriting the Scholars Geoportal thumbnail link.
    
            writer.writerow(item)

        else:
            pass

    # STEP 3:
    # Determining the number of now obsolete items within the previous Scholars Geoportal webpage metadata extract.
    # These are thus skipped over and not written to the new Master list. 
    # Capturing the instance where a previous SGP ID is not listed as an extracted SGP ID.
    if str(item[19]) in currentSGPIDs and str(item[19]) not in extractedSGPIDs:

        # Appending the items' SGP ID to the SGPstodelete list.
        SGPstodelete.append(str(item[19]))
        
    else:
        pass

# STEP 4:
# Writing new Scholars Geoportal webpage metadata to the Master CSV file.
for extract in extracted:

    # Capturing the instance where an extracted SGP ID is not listed as an existing item's SGP ID.
    if str(extract[0]) not in currentSGPIDs:
        
        # Appending the items' SGP ID to the SGPstoadd list.
        SGPstoadd.append(str(extract[0]))       

        item = ['', '', '', '', '', '','', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
        item[19] = extract[0]     # Writing the SGP ID.
        item[1] = extract[1]      # Writing the title.
        item[2] = extract[4]      # Writing the year.
        item[3] = extract[2]      # Writing the author.
        item[4] = extract[7]      # Writing the format.
        item[5] = extract[8]      # Writing the data user group.
        item[6] = extract[5]      # Writing the URL.
        item[7] = extract[3]      # Writing the abstract.
        item[10] = extract[5]     # Writing the Scholars Geoportal URL.
        item[16] = extract[6]     # Writing the Scholars Geoportal thumbnail link.

        # Writing the row of metadata for each item into the Master csv file.
        writer.writerow(item)

# PROVIDING INTERFACIAL USER INFORMATION ON THE RESULTS OF THIS UPDATE.

print (' ')
print ('MASTER LIST UPDATE SUMMARY')
print (' ')
print ('Number of GIS Data Items: ' + str(len(GISData)))
print ('Number of Previous SGP Items: ' + str(len(currentSGPIDs)))
print ('Number of SGP Items from Latest Extract: ' + str(len(extractedSGPIDs)))
print ('Number of New SGP Items Added: ' + str(len(SGPstoadd)))
print ('Number of Obsolete SGP Items Deleted: ' + str(len(SGPstodelete)))
print (' ')
print ("The newly updated list of Scholars Geoportal and GIS data pages has been written to", filename1)

# CREATING A TIMESTAMPED COPY OF THE MASTER LIST AND CLOSING FILES.

outfile.close()
shutil.copyfile(outfile.name, 'Master - Working Copy.csv')
shutil.copyfile(outfile.name, 'Master_' + datetime.datetime.today().strftime('%Y%m%d') + '.csv')
