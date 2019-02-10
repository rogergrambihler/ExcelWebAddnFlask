
todo: probably want to rename or break this up better 

Use Github's Import Repository option on the + menu on top of the page
change to see how forking works

This creates a new repository with the exact contents of the copied repository. The downside is that it doesn't count as a fork for Github.

todo: best way to setup so user can make own alterations? Probably want to do a fork

##Install the project

 (todo: is this a good generic webSite template?)  
 
git clone the project to a local folder

##Running the sample 
Launch the ExcelWebAddinFlask.sln solution in Visual Studio  
Choose "Start Debugging" from the debug menu

The solution will do the following steps:  
Launches the python webservice (you should see the home page displayed correctly without a cert error) 
Opens an Excel document with the manifest (you should see in excel a "Show TaskPane button"  
Click the "Show Taskpane Button". This will open your Office Addin's custom taskpane.


##Changing the Background  

todo: move this somewhere ExcelWebAddinFlask

With the taskpane open highlight a cell in the Excel Spreadsheet  
Click the "Highlight" button in the taskpane  
The select cell in the Excel Spreadsheet will turn orange  

To learn more about how the Excel Object model works find the code for changing the color and make change the code for your own favorite background.