## Install PreRequisites

todo

Why Flask
Why JQuery
todo: Is there an easy way to read markdown?

To use the Project you will need the following installed:  
Visual Studio Community (Include Python and Office Shared Development)  
Office 365 Excel

## FAQ

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

