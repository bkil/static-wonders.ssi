# Tiny snippet wonders using static server side HTML includes

Demonstrating what you can achieve without dynamic server side scripting or applications. This is commonly available at free web hosting providers like what you get with your domain name registration.

## Implementation

### OpenLiteSpeed

* https://github.com/litespeedtech/openlitespeed/blob/1c61e9406f90f8cd1673d1c9bd460474544c6945/src/ssi/ssiengine.cpp#L893
* https://github.com/litespeedtech/openlitespeed/blob/1c61e9406f90f8cd1673d1c9bd460474544c6945/src/ssi/ssiscript.cpp#L466

### Apache2

* http://httpd.apache.org/docs/current/howto/ssi.html
* https://httpd.apache.org/docs/2.4/mod/mod_include.html
* https://github.com/apache/httpd/blob/21f16155c38e406e0a0daaa60a539d66128cf044/modules/filters/mod_include.c#L4165
* https://github.com/apache/httpd/blob/21f16155c38e406e0a0daaa60a539d66128cf044/modules/generators/mod_cgi.c#L640

### nginx

* https://nginx.org/en/docs/http/ngx_http_ssi_module.html
* https://github.com/nginx/nginx/blob/a64190933e06758d50eea926e6a55974645096fd/src/http/modules/ngx_http_ssi_filter_module.c#L241

### IIS

## Documentation

* https://www.gilesorr.com/blog/ssi-variables-apache-nginx.html
* https://en.wikipedia.org/wiki/Server_side_includes
* https://www.w3.org/Jigsaw/Doc/User/SSI.html
* https://web.archive.org/web/19970303194503/http://hoohoo.ncsa.uiuc.edu/docs/tutorials/includes.html

## Edge Side Includes

Supported: Akamai CDN, Fastly CDN, Varnish Cache, Squid Proxy, Mongrel ESI, LiteSpeed, IBM WebSphere, Oracle Fusion/WebLogic, F5, Node.js ESI & nodesi.

* https://en.wikipedia.org/wiki/Edge_Side_Includes
* http://www.w3.org/TR/esi-lang
* https://www.litespeedtech.com/products/features/edge-side-includes
* https://developer.fastly.com/reference/vcl/statements/esi/
* https://www.gosecure.net/blog/2018/04/03/beyond-xss-edge-side-include-injection/
* https://blog.cloudflare.com/edge-side-includes-with-cloudflare-workers/
  * https://workers.cloudflare.com/
