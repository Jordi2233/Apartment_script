Overview of Apartment Script
============================

The Apartment Script is a Python project that uses Beautiful Soup to scrape OLX, a popular online marketplace, for the best apartment offers. The script then sends these offers via email to the user.

Dependencies
------------

The project uses several Python libraries, including Beautiful Soup, Requests, and smtplib. These dependencies are listed in the requirements.txt file.

Installation
------------

To install the required dependencies, run the following command in your terminal:

bashCopy code

```pip install -r requirements.txt```

Usage
-----

To use the script, you will need to modify the `config.py` file to include your email credentials and search parameters. Once this is done, run the following command:

bashCopy code

```python apartment_script.py```

This will start the script, which will scrape OLX and send you an email with the best offers.

Docker
------

The project also includes a Dockerfile, which can be used to build a Docker image of the script. To build the Docker image, run the following command:

bashCopy code

```docker build -t apartment_script .```

To run the script in a Docker container, use the following command:

bashCopy code

```docker run --rm apartment_script```

Conclusion
----------

The Apartment Script is a simple but effective tool for finding the best apartment offers on OLX. By using Beautiful Soup and Python, the script can quickly and easily scrape the website and send you an email with the best offers. With the addition of Docker, the project can be easily deployed and run on any system.
