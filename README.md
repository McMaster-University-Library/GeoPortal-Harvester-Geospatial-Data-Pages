# Scholars GeoPortal and Geospatial Data Pages Collection

**This repository is a resource to create Google-indexed static web pages for all Scholars GeoPortal and geospatial data layers that are available to McMaster University users, to improve discoverability. These 
web pages may be found online within the McMaster library website [here.](https://library.mcmaster.ca/maps/geospatial)**

## Broad overview 

![General workflow image](https://github.com/maclibGIS/GeoPortal-Harvester-Geospatial-Data-Pages/blob/master/OCUL%20Geo%202018%20Meeting%20-%20Jay's%20slides.png "General workflow")

**Find the complete user guide and project documentation in the Google Doc [here.](https://docs.google.com/document/d/1tUyMj4l-EGIcFsbqmHwR0rY7Ob2luBhv42GQR7E6EZo/edit?usp=sharing)**

The following is a quick guide to performing a collection update:

1. Download the latest version of all data pages available at the McMaster library website using the URL https://library.mcmaster.ca/geospatial-export-records.csv (NOTE: ensure that you are logged into the Library website before doing so).
2. Save the file to the top-level repository directory with the name ```Master_Production_Extract.csv``` (overwrite previous file)
3. Go through the manually-curated [GIS Data pages spreadsheet](https://docs.google.com/spreadsheets/d/1bJvn9tRgGJrIaJagY_7xdU9-4vx1JpAKaBy4or_pIpo/edit#gid=1710763351); for any row without a ```NID```, find it in the ```Master_Production_Extract.csv``` (if it exists) and add that NID into the ```NID``` column.
4. Run Harvester.py to download Scholars GeoPortal extract (xml, csv) and a csv file of the manually-curated GIS data pages (available at https://docs.google.com/spreadsheets/d/1bJvn9tRgGJrIaJagY_7xdU9-4vx1JpAKaBy4or_pIpo/edit#gid=1710763351) 
5. Run Collection_Creator.py
6. Commit changes and push to the GitHub repository
7. Send the newly created Collection_Additions.csv, Collections_Deletions.csv, and Collections_Updates.csv files to Debbie for Drupal processing.
	
Note: Once the Drupal process has completed and all data pages are on the McMaster library website, all metadata should be consistent with the Master_Collection_Creator_Output.csv file created by the script, Collection_Creator.py, with the exception of new Nids assigned to new items. 

:boom: :exclamation: **_As such, it is imperative to download the web production extract file, Master_Production_Extract.csv, as well as to update new Nid numbers for manual records._**

## Resource: Geospatial_Data.csv

This CSV file is the latest downloaded file from the [GIS Data Pages Google Sheet](https://docs.google.com/spreadsheets/d/1bJvn9tRgGJrIaJagY_7xdU9-4vx1JpAKaBy4or_pIpo/edit#gid=1710763351) which contains selected content for each GIS data item provided by McMaster's Maps, Data, and GIS Department. Selected content include the item's Nid, title, year, author, format, URL, abstract, a citation guide, and geospatial availability, among other information.

## Resource: SGP_Extract.csv

This CSV file is the output file of Harvester.py, containing selected metadata for each record in the GeoPortal made available to McMaster users. Selected metadata include the SGP_id, title, author, format, URL, abstract, and Scholars GeoPortal URL, among other information.

## Resource: Geospatial_Subject_Mappings.csv

This CSV file contains a lookup table mapping raw subject fields from the Scholars GeoPortal records to the list of current subject fields available on the online repository. This is used when pulling the latest Scholars GeoPortal extract within Harvester.py.

## Resource: Master_Collection_Creator_Output.csv

This CSV file is an output file of Collection_Creator.py that contains all current geospatial and GeoPortal records for McMaster’s web pages. These items are listed within the latest version of the geospatial spreadsheet download and the latest Scholars GeoPortal extract. 

## Resource: Master_Production_Extract.csv

This CSV file is the latest downloaded extract of the existing web pages available at the [McMaster library website.](https://library.mcmaster.ca/geospatial-export-records.csv)

## Tool: Harvester.py

Using Python 3.5, content from Scholars GeoPortal in XML file format is parsed and selected data fields are written to an output CSV file. The script automatically downloads this content in XML format using a provided link. These selected data fields currently include for each item in the GeoPortal, its identifier, title, producer, abstract, range of years of available publications, GeoPortal permalink, a link to the item's thumbnail image, available formats, and users with view permission to each item.

## Tool: Collection_Creator.py

Using Python 3.5, the latest GIS Data Pages and Scholars GeoPortal content is compiled into Master_Collection_Creator_Output.csv. An update summary of what's been added and deleted from the previous Master collection is provided when running the script. A sample summary is shown below.

> MASTER LIST UPDATE SUMMARY
>
> Number of Previous Geospatial Items: 111 <br />
> Number of Previous GeoPortal Items: 1085 <br />
> 
> Number of Geospatial Items from Latest Download: 111 <br />
> Number of GeoPortal Items from Latest Extract: 1032 <br />
> 
> Number of New Geospatial Records For Addition: 0 <br />
> Number of Obsolete Geospatial Records For Deletion: 0 <br />
> Number of New GeoPortal Items For Addition: 17 <br />
> Number of Obsolete GeoPortal Items For Deletion: 70 <br />

## Resource: Collection_Additions.csv

As one of the output files of Collection_Creator.py, this CSV file contains new geospatial and GeoPortal records to be added to McMaster’s web pages. These items do not currently have an Nid number and shall be assigned one in the Drupal uploading process.

## Resource: Collection_Deletions.csv

As the second output file of Collection_Creator.py, this CSV file contains obsolete geospatial and GeoPortal records to be deleted from McMaster’s web pages. These items are previously listed in old versions of the Master collection but are not within the latest geospatial spreadsheet download or the latest Scholars GeoPortal extract.

## Resource: Collection_Updates.csv

As the third output file of Collection_Creator.py, this CSV file contains existing geospatial and GeoPortal records still current for McMaster’s web pages. These items are previously listed in old versions of the Master collection and are within the latest geospatial spreadsheet download or the latest Scholars GeoPortal extract. 

## File: Content.xml

This XML file contains the downloaded metadata in ISO 19115 for all records available to McMaster University users, provided by Scholars GeoPortal. Information from this file is first downloaded by the python script, Harvester.py, then parsed and selected to be included in a condensed file. To view the document tree for this XML file, copy and paste the following link in your browser while connected to a McMaster Wi-Fi network: 
http://geo2.scholarsportal.info/proxy.html?http:__giseditor.scholarsportal.info/search/index.html?limit=entitled&env=production&q=*&i=2000&fm=xml

## File: Content-Public.xml

This XML file contains the downloaded metadata in ISO 19115 for all records available to the public, provided by Scholars GeoPortal. This document may serve as a check to view the list of items available to the public. To view the document tree for this XML file, copy and paste the following link in your browser while connected to a Wi-Fi network off-campus: 
http://geo2.scholarsportal.info/proxy.html?http:__giseditor.scholarsportal.info/search/index.html?limit=entitled&env=production&q=*&i=200&fm=xml




