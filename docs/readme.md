
#ExcelWebAddinFlask

##Welcome

![](images/black.gif  =100x)

ExcelWebAddinFlask is a sample project showing of an Office Excel WebAddin that uses a python flask server.
The project is a combination of the ExcelWebAddin template and the Python web server template from Visual Studio.

##PreRequisites

To use the Project you will need the following installed:  
Visual Studio Community (Include Python and Office Shared Development)  
Office 365 Excel

##Install the project
git clone the project to a local folder

##Trust the Certificate
Office addins require a trusted SSL so you need to do some extra steps to install the wwwroot\certs\ca.crt as a trusted root authority.  

To trust the cert follow the steps at: https://github.com/OfficeDev/generator-office/blob/HEAD/src/docs/ssl.md 
but use the cert at wwwwroot\certs\ca.crt instead of the location they use in their directiong.

##Running the sample 
Launch the ExcelWebAddinFlask.sln solution in Visual Studio  
Choose "Start Debugging" from the debug menu

The solution will do the following steps:  
Launches the python webservice (you should see the home page displayed correctly without a cert error) 
Opens an Excel document with the manifest (you should see in excel a "Show TaskPane button"  
Click the "Show Taskpane Button". This will open your Office Addin's custom taskpane.

##Changing the Background

With the taskpane open highlight a cell in the Excel Spreadsheet  
Click the "Highlight" button in the taskpane  
The select cell in the Excel Spreadsheet will turn orange  

To learn more about how the Excel Object model works find the code for changing the color and make change the code for your own favorite background.

##FAQ

Where can I learn more about Excel Addins? https://docs.microsoft.com/en-us/office/dev/add-ins/excel/excel-add-ins-overview  
  
Where is the addin code? The addin code is part of the Flask server. Look at addin.html, addin.js, and addin.cs.

What are all the other server items? These came from the Python flask template which has the home and other pages.
Its useful to have a home page even if don't need a website to  debug that the website is working properly.
These could all be removed with the exception of the addin.* pages and routes and your Office addin would still work correctly.

What is FabricUI? Fabric UI provices some standard controls that match the style of the Excel document the addin runs in.
There is no requirement to use FabricUI in your Office Addin. More information can be found at: https://developer.microsoft.com/en-us/fabric

Flask Server and JQuery. The Flask server template uses JQuery. I left the Jquery in but there is no reason to use JQuery.
the addin code also has a reference to JQuery but ideally this would be cleaned up to remove the jquery dependency. 
Note: I'm not sure if flask has a dependency on JQuery.  

