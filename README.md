# Scholars GeoPortal and Geospatial Data Pages Collection

**This repository is a resource to create Google-indexed static web pages for all Scholars GeoPortal and geospatial data layers that are available to McMaster University users, to improve discoverability.**

The following is a quick guide to performing a collection update:

	1. Download the latest version of Geospatial Data Pages from the GIS Data Pages Google Spreadsheet as a CSV file.
	2. Save the file to the local directory, C:\Home\GeoPortal-Harvester.
	3. Rename the file as Geospatial_Data.csv.
	4. Open Harvester.py by right-clicking the file and selecting Edit with IDLE 3.5.
	5. Run the script by hitting F5. 
	6. Open Collection_Creator.py by right-clicking the file and selecting Edit with IDLE 3.5.
	7. Run the script by hitting F5. 
	8. Send the newly created Collection_Additions.csv, Collections_Deletions.csv, and Collections_Updates.csv files for Drupal processing.

## Resource: Geospatial_Data.csv

This CSV file is the latest downloaded file from the [GIS Data Pages Google Sheet](https://docs.google.com/spreadsheets/d/1bJvn9tRgGJrIaJagY_7xdU9-4vx1JpAKaBy4or_pIpo/edit#gid=1710763351) which contains selected content for each GIS data item provided by McMaster's Maps, Data, and GIS Department. Selected content include the item's Nid, title, year, author, format, URL, abstract, a citation guide, and geospatial availability, among other information.

## Resource: SGP_Extract.csv

This CSV file is the output file of Harvester.py, containing selected metadata for each record in the GeoPortal made available to McMaster users. Selected metadata include the SGP_id, title, author, format, URL, abstract, and Scholars GeoPortal URL, among other information.

## Resource: Master.csv

[Edit]

## Tool: Harvester.py

Using Python 3.5, content from Scholars GeoPortal in XML file format is parsed and selected data fields are written to an output CSV file. The script automatically downloads this content in XML format using a provided link. These selected data fields currently include for each item in the GeoPortal, its identifier, title, producer, abstract, range of years of available publications, GeoPortal permalink, a link to the item's thumbnail image, available formats, and users with view permission to each item.

## Tool: Collection_Creator.py

Using Python 3.5, the latest GIS Data Pages and Scholars GeoPortal content is compiled into Master.csv. An update summary of what's been added and deleted from the previous Master collection is provided when running the script. A sample summary is shown below.

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

### _Find the Scholars Geoportal Content Harvesting project workflow in the Google Doc [here.](https://docs.google.com/a/mcmaster.ca/document/d/1dbZg2W9OVB27Uw5pu6To6OITzRWoG32yiSrOISzLGlk/edit?usp=sharing)_


