# urlshortener
A simple API that listens on /shortener for GET requests with URLs to shorten, and in / for GET requests to return the correponding shortened URL. Made to be hosted free on Pythonanywhere.com.

The available URL of the project is: https://javiervidrua.pythonanywhere.com

To shorten a URL go to https://javiervidrua.pythonanywhere.com/shortener/?id=url-to-shorten where the id parameter holds the URL to be shortened, in this case it is 'url-to-be-shortened'.

The API is coded in such a way that it will only create one and only one shortened URL for each URL to shorten.

To get the URL of a shortened one, go to https://javiervidrua.pythonanywhere.com/?id=url-shortened where 'url-shortened' is the id that identifies the shortened URL, given to the user after shortening a URL.
