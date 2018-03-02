# GIS Data and Scholars GeoPortal Collection

**This repository is a resource to create Google-indexed static web pages for all GIS data and Scholars GeoPortal data layers that are available to McMaster users, to improve discoverability.**

## Resource: GIS_Data_Pages.csv

This CSV file is the latest downloaded file from the [GIS Data Pages Google Sheet](https://docs.google.com/spreadsheets/d/1bJvn9tRgGJrIaJagY_7xdU9-4vx1JpAKaBy4or_pIpo/edit#gid=1710763351) containing selected metadata for each GIS data item provided by the Maps, Data, and GIS Department. 

## Resource: SGP_Extract.csv

This CSV file is the output file for Harvester.py, containing selected metadata for each record in the GeoPortal made available to McMaster users.

## Resource: Master.csv

This CSV file is the output file for Master Updater.py, containing a combined list of items from both the GIS Data Pages and SGP Extract CSV files. Master.csv is then used to create web pages in bulk within the McMaster University domain.

## Tool: Harvester.py

Using Python 3.5, content from Scholars GeoPortal in XML file format is parsed and selected data fields are written to an output CSV file. The script automatically downloads this content in XML format using a provided link. These selected data fields currently include for each item in the GeoPortal, its identifier, title, producer, abstract, range of years of available publications, GeoPortal permalink, a link to the item's thumbnail image, available formats, and users with view permission to each item.

## Tool: Master Updater.py

Using Python 3.5, the latest GIS Data Pages and Scholars GeoPortal content is compiled into Master.csv. An update summary of what's been added and deleted from the previous Master collection is provided when running the script.

## File: Content.xml

This XML file contains the downloaded metadata in ISO 19115 for all records available to McMaster University users, provided by Scholars GeoPortal. Information from this file is first downloaded by the python script, Harvester.py, then parsed and selected to be included in a condensed file. To view the document tree for this XML file, copy and paste the following link in your browser while connected to a McMaster Wi-Fi network: 
http://geo2.scholarsportal.info/proxy.html?http:__giseditor.scholarsportal.info/search/index.html?limit=entitled&env=production&q=*&i=2000&fm=xml

## File: Content-Public.xml

This XML file contains the downloaded metadata in ISO 19115 for all records available to the public, provided by Scholars GeoPortal. This document may serve as a check to view the list of items available to the public. To view the document tree for this XML file, copy and paste the following link in your browser while connected to a Wi-Fi network off-campus: 
http://geo2.scholarsportal.info/proxy.html?http:__giseditor.scholarsportal.info/search/index.html?limit=entitled&env=production&q=*&i=200&fm=xml

### _Find the Scholars Geoportal Content Harvesting project workflow in the Google Doc [here.](https://docs.google.com/a/mcmaster.ca/document/d/1dbZg2W9OVB27Uw5pu6To6OITzRWoG32yiSrOISzLGlk/edit?usp=sharing)_


