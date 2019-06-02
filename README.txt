kuzuri is an open source penetration testing tool that automates testing accounts to the site's login page, based on Dictionary Attack. kuzuri can be used on almost any platform because it doesn't use selenium as a module but requests.

kuzuri will automatically search the url action and all inputs on the website which will be used to send login data to the server

installation on linux:
$git clone https://github.com/zevtyardt/kuzuri
$cd kuzuri
$pip3 install -r requirements
$python3 kuzuri.py
