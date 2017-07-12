# Scholars GeoPortal Content Harvesting

This repository is a resource to create Google-indexed static web pages for all data layers that are available to McMaster users in the Scholars GeoPortal, to improve discoverability.

## Resource: Content.xml

This XML file contains the downloaded metadata in ISO 19115 for all records available to McMaster University users, provided by Scholars GeoPortal. Information from this file is parsed and selected to be included in a condensed file. To view the document tree for this XML file, copy and paste the following link in your browser while connected to a McMaster Wi-Fi network: http://geo2.scholarsportal.info/proxy.html?http:__giseditor.scholarsportal.info/search/index.html?limit=entitled&env=production&q=*&i=1000&fm=xml

## Resource: Content-Public.xml

This XML file contains the downloaded metadata in ISO 19115 for all records available to the public, provided by Scholars GeoPortal. The identifiers of each open item from this file are parsed and used within Harvester.py to distinguish the users with view permission for each item. To view the document tree for this XML file, copy and paste the following link in your browser while connected to a Wi-Fi network off-campus: http://geo2.scholarsportal.info/proxy.html?http:__giseditor.scholarsportal.info/search/index.html?limit=entitled&env=production&q=*&i=100&fm=xml

## Tool: Harvester.py

Using Python 3.5, content from Scholars GeoPortal in XML file format is parsed and selected data fields are written to an output CSV file. These fields currently include for each item in the GeoPortal, its identifier, title, producer, abstract, range of years of available publications, GeoPortal permalink, a link to the item's thumbnail image, available formats, and users with view permission to each item.

## Resource: Harvested.csv

This CSV file is the output file containing selected metadata for each record in the GeoPortal made available to McMaster users. This file is then used to create web pages in bulk within the McMaster University domain.

### _Find the complete project workflow in the Google Doc [here.](https://docs.google.com/a/mcmaster.ca/document/d/1dbZg2W9OVB27Uw5pu6To6OITzRWoG32yiSrOISzLGlk/edit?usp=sharing)_


