# urlshortener
A simple **Django** API that listens on '/shortener' for GET requests with URLs to shorten, and in '/' for GET requests to return the correponding shortened URL.

It was made to be hosted free on Pythonanywhere.com, for ever.

The available URL of the project is: https://javiervidrua.pythonanywhere.com

To shorten a URL go to https://javiervidrua.pythonanywhere.com/shortener/?id=url-to-shorten where the id parameter holds the URL to be shortened, in this case it is 'url-to-be-shortened'.

The API is coded in such a way that it will only create one and only one shortened URL for each URL to shorten.

To get the URL of a shortened one, go to https://javiervidrua.pythonanywhere.com/?id=url-shortened where 'url-shortened' is the id that identifies the shortened URL, given to the user after shortening a URL.

## Example

Let's say we want to shorten the URL https://github.com/javiervidrua/urlshortener.

What we do is go to https://javiervidrua.pythonanywhere.com/shortener/?id=https://github.com/javiervidrua/urlshortener

And we get something like: https://javiervidrua.pythonanywhere.com/?id=2d268682-51e0-4931-8114-93a059d2330d

Now if we go to https://javiervidrua.pythonanywhere.com/?id=2d268682-51e0-4931-8114-93a059d2330d, it will redirect us to https://github.com/javiervidrua/urlshortener.

## Notes

The project was made just to get some hands-on experience with Python and Django, and even though it is entirely functional, some improvements can be done to make the URLs shorter.

Other than that, it works well and it's really fast, and I'm really happy with it.
