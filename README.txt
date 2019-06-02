ENFORCER
========
  is an open source penetration testing tool that automates testing accounts to the site's login page, based on Dictionary Attack.
  this tools will automatically search the url action and all inputs on the website which will be used to send login data to the server

INSTALLATION ON LINUX
=====================
  [package needed]
    1. git
    2. python3 or above

  [step]
    $  git clone https://github.com/zevtyardt/enforcer
    $  cd enforcer
    $  pip3 install -r requirements.txt
    $  python3 enforcer.py -h

USAGE
=====
  $ python3 enforcer.py -t https://eaxmple.com/login.php -p password list

