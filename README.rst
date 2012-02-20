======================================================
Quixote test code for The Great Web Framework Shootout
======================================================

| Placed in the public domain.
| Neil Schemenauer, 2012


Synopsis
========

This code was tested with Quixote 2.8b1 and Flask 0.9-dev (git
commit 04bb720d3813c8cfe3ae46d2fb85dbc9a03a9b70).


Setup
=====

The easiest way to test this application is with mod_scgi.  The
following Apache directive will enable the SCGI application::

	SCGIMount /quixote 127.0.0.1:3000

Run "python quixote_app.py" to start the application server.

To run Flask with mod_scgi, I created a quick WSGI adaptor for
my 'scgi' package.  You can download it from::

	http://python.ca/nas/python/wsgi_handler.py

It should be put in the 'scgi' package directory.  The script to run
the Flask app is simple (defaults to listening on port 3000)::

	from flask_app import app
	from scgi.wsgi_handler import run
	if __name__ == '__main__':
	    run(app)


Results
=======

I don't have a EC2 setup to test with so I compared the Flask
version on my workstation.  Flask is fairly similar in spirit to
Quixote.  Quixote's templating system should be faster.


The "Hello World" String Test
-----------------------------

=====================    ========
Framework                Reqs/sec
=====================    ========
Quixote/SCGI (2.8b1)	     3933
Flask/SCGI (0.9-dev)         3089
Flask/WSGI (0.9-dev)  	     1757
=====================    ========

The "Hello World" Template Test
-------------------------------

=====================    ========
Framework                Reqs/sec
=====================    ========
Quixote/SCGI (2.8b1)	     3929
Flask/SCGI (0.9-dev)         2657
Flask/WSGI (0.9-dev)   	     1373
=====================    ========


The "Hello World" Template Test With DB Query
---------------------------------------------

=====================    ========
Framework                Reqs/sec
=====================    ========
Quixote/SCGI (2.8b1)	     2616
Flask/SCGI (0.9-dev)         1729
Flask/WSGI (0.9-dev)   	      866
=====================    ========
