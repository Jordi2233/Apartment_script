Apartment Script
The Apartment Script is a Python project that automates apartment searches on OLX, a popular online marketplace for buying and selling goods and services. The script uses the Beautiful Soup library for web scraping and Docker for deployment.

With this script, users can specify their apartment search criteria, such as the location, price range, number of rooms, and other amenities. The script filters the search results to find the best offers based on the user's criteria and sends them via email. Users can run the script periodically on a server or locally using a scheduler such as cron to automate the apartment search process.

Getting Started
To use the Apartment Script, you'll need Python and Docker installed on your machine. You can install Python from the official website or by using a package manager such as Homebrew or apt-get. Docker can be downloaded from the official website or installed using your system's package manager.

Once you have Python and Docker installed, you can clone the repository and install the required dependencies by running:

Copy code
pip install -r requirements.txt
You can then set up your email configuration by creating a .env file with your email credentials:

makefile
Copy code
EMAIL_ADDRESS=<your_email_address>
EMAIL_PASSWORD=<your_email_password>
Usage
To run the script, you can use the following command:

css
Copy code
python main.py
The script will prompt you to enter the apartment search criteria, such as the location, price range, number of rooms, and other amenities. Once you have entered the search criteria, the script will run the OLX search and send the best apartment offers via email.

You can also set up the script to run periodically by using a scheduler such as cron. For example, to run the script every day at 8 AM, you can add the following entry to your crontab file:

ruby
Copy code
0 8 * * * /usr/bin/python /path/to/main.py
Contributing
If you'd like to contribute to the project, please feel free to open an issue or submit a pull request. We welcome all contributions and feedback.

License
This project is licensed under the MIT License. See the LICENSE file for more information.
