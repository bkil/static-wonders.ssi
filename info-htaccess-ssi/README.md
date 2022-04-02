# Information based on .htaccess and SSI

Just copy these files over to your static web host to find out what you are allowed to do.
You can skip `dev` and `README.md`.

## CGI debug

Is all CGI functionality failing?

* You may need to place `cgi-bin` on the top level of your web document root
* Or even one level above that to a special subfolder visible through via FTP.
* If that still doesn't help, you may not have permission to run user uploaded cgi at all. Consider politely asking your host to enable CGI.

## .htaccess debug

Does your .htaccess rules seem to have no effect?

* Check the web server error log for hints.
* To rule out interference with the one in the web root or not propagating to subdirectories, try to deploy the experiment within your web root.
* Ensure it is readable by the the web server process by making it world-readable via `chmod a+r .htaccess`
