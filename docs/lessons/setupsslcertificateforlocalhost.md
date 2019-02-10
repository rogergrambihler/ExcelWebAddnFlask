
todo

##Trust the Certificate
Office addins require a trusted SSL so you need to do some extra steps to install the wwwroot\certs\ca.crt as a trusted root authority.  

To trust the cert follow the steps at: https://github.com/OfficeDev/generator-office/blob/HEAD/src/docs/ssl.md 
but use the cert at wwwwroot\certs\ca.crt instead of the location they use in their directiong.
