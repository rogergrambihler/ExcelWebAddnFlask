
# ExcelWebAddinFlask  

ExcelWebAddinFlask is a sample project showing how to combine the Microsoft Office Add-in platform with a Python Webserver.

Microsoft Office is used by over One billion users. ["Microsoft's Office Has over One Billion Users". Softpedia. SoftNews. July 10, 2012].

The Office Add-in platform allows you to publish your Add-ins to the Microsoft Store. From the store your addin can then be installed and used by over a billion users!

The goals of the tutorial is enable you to publish your own Add-in to the Office store along with a webSite users can browse to for help or additional services and information.

This tutorial is broken up into Lessons. Feel free to skip and move around based on how famliar you are. Also, if there are lessons or more details for existing lessons please leave comment or pull request.



## Lessons

### WebSite

video to deploy docker to Azure: Dan Taylor - From Zero to Azure with Python, Docker containers, and Visual Studio Code-I1cG1FRjFOQ

[Install Prerequisites](lessons/installprerequisites.md)    
[Make your own Fork of the ExcelWebAddinFlask repo](lessons/forkexcelwebaddinflaskrepo.md)  
f5 for local host
[Run the Website Setup/SSL Certificate for localhost](lessons/runthewebsite.md)  

SSL Options: 
    Have ways of running SSL, nginx as reverse proxy in container, SSL in flask web, ngrok.
    ngrok http 5000 <= this will work with live reload changes

LiveReload (Issue withs this so may want ot move further )

[deploy your webSite on Azure](lessons/runningyourwebsiteonazure.md)  


### Office Addin

[What is an Office Add-in](lessons/whatisanofficeaddin.md)  
[The Addin Manifest](lessons/theaddinmanifest.md)  
[Sideloading an Addin into Excel Online](lessons/sideloadinganaddintoexcelonline.md)   
[Show a Hello World Task Pane](lessons/showahelloworldtaskpane.md)  
[Excel JavaScript API](lessons/exceljavascriptapi.md)  
[Use the Excel Api in a Task Pane](lessons/usetheexcelapiinataskpane.md)  
[Functions](lessons/functions.md)  
[Show a Dialog](lessons/showadialog.md)  
[Submit your addin to the Office store](lessons/submityouraddintotheofficestore.md)    
[Fame and Glory](lessons/fameandglory.md)  

## Bonus Material 
WebSite Monitoring  
Content Delivery Networks (CDNs)  
Fabric UI  
Localization  

## Misc  
Excel Worksheet Permissions

## Notes  
Review why have Fonts
Clean up website to match what would want for store resources  
Need to figure out if want FabricUI as part of samples (Maybe have a specific fabric UI example)?  
Make JQuery links consistent and minimize to what need across webSite and samples  
Clean up static from manifest once used by other Blueprints  
determine what want to do with the default and what clients don't support <SourceLocation DefaultValue="{{ host_url }}addin.html" 
Would also be nice to do an Agave with a static dialog/taskpane so it can be on CDN and then make a webService
call to get the data. Maybe should just do this?
deteremine best practice for javascript reload when make changes.

