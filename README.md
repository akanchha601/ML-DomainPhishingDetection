# ML-DomainPhishingDetection

## Project Details
This work was completed by Akanchha Sinha as part of her Master's thesis work [12]. This project involved Akanchha as the lead student researcher, advised by Dr. Nur Zincir-Heywood (zincir@cs.dal.ca) and Dr. Raghav Sampangi (raghav@cs.dal.ca).


## Overview
Due to the phishing sites appearing genuine to users, detecting them is a challenging
task. The SSL certificate that is generally used to secure and encrypt the communication, 
can also be generated for the phishing sites. The consequences of using a secure web service
phishing sites could be harmful to users. 
Attackers can easily trap users and steal sensitive information using the cloned website that looks legitimate along with its SSL certificate. 
This may also result in the degradation of the user's trust and belief in "green padlock" and 
"lock icon” shown on the browser after connecting to a web site through the secure web service. 
In order to detect phishing sites, a web API is built using the Flask Python web framework. 
This framework provides functionality for building a web application and integrates this application to create the web API.
The application allows a user to identify whether a domain visited is legitimate or phishing 
and the backend classification part in the web API, the decision tree machine learning classifier is implemented in the Python programming language.


## Web API 
A web API is an application programming interface for a server. It accepts user request and returns result as a response through web service.
In this work, there are three main methods are called in the web API:
1. Certificate extraction method is extracted SSL certificate from a domain.
2. Feature creation methods are created features for recognizing the pattern of a domain's SSL certificate.  
3. Decision rules method is classified a domain as legitimate or phishing based on the created feature values.

The feature creation methods are:
*  Domain Validated: Check if SSL certificate is domain validated or not
*  Issuer State: Check if the issuer component has state field or not
*  Subject element: Calculates number of details in subject component
*  Subject length: Calculates number of characters of subject components
*  Issuer length: Calculates number of characters of issuer components
*  Extension number: Calculates number of extensions 
*  Domain Ranking: Uses alexa.com to determine domain ranking
*  Suject is "com": Checks if subject component's CN field is a `.com’ domain
*  Issuer is "com": Checks if issuer component's CN field is a `.com’ domain
*  Certifcate Validity: Determines certificate validity period


Main functionalities of the framework are:
* It must identify phishing and legitimate domain based on decision tree classification rules.
* It must return an error message on wrong input data.
* It must successfully create features using different Python library method.
* It must extract the certificate from the website without any error because phishing domains are active for very short span of time.
* It would not detect any types of web attack such as Distributed Denial of Service (DDOS) etc.
* Input data should be a website domain name.

The flow chart of this framework is below

![Capture](/uploads/aba4e424f48d67fe4cfb65f267ded764/Capture.PNG)

                               
The description of the flow chart is provided below:

* Input is the domain of a website.
* Extraction of certificate from the input domain. 
* Features are created for a certificate.
* Decision Tree classifier rules are employed to classify category of the domain.
* The result shows that a domain is legitimate or phishing domain.
                                                            
                                                       
                                                             

## Proof-of-Concept Web Application
HTML and CSS are used for creating page structure and styling of web page. 
In addition, JavaScript provides dynamic functionality to web page by handling HTML elements. 
Based on the output of backend methods(feature creation, decision rules and certificate extraction), JavaScript action method calls on check button to response the user input request and shows the result on screen.
Below screenshots show the running server through web service:
In text box, users can enter the domain name of a website to verify. By clicking on check box, it shows whether the entered domain is a legitimate or phishing on the screen.
![example_of_legitimate_domain](/uploads/cbbcc52edc04507a37f5073ff86efa2f/example_of_legitimate_domain.png)
![example_of_phishing_domain](/uploads/9a432848e2536ade70b30abce0478d7e/example_of_phishing_domain.png)
The web application also returns an error message on wrong input data. 
It shows error messages on screen when input request is empty or input data is other than domain name of the website.
Below are examples of error messages.
![example_of_error_case_1_copy](/uploads/efd57de4ae89ebbb498aeb3a720abc34/example_of_error_case_1_copy.png)
![example_of_error_case_2](/uploads/2a86e5c0483195eef76c2dc9acb68b36/example_of_error_case_2.png)



## Installation Details
The guidelines are given below to run the API:

1. Install Python: pip install python 3
2. Start project with a virtual environment(manages the dependencies for our project): py -3 -m venv venv 
3. Activate the environment: venv\Script\activate
4. Install Flask: pip install flask
5. Create directory for creating a web API: mkdir api
6. Create directory named static(static folder includes
script.js, image.img, and styling.css files): mkdir static 
7. Create directory named template(flask uses this folder to render HTML file): mkdir template
8. Export the environment variable before running the server: set FLASH_APP=api.py
9. Run the server: Flask run

In order to successfully run the application, there are some libraries or modules which should be imported in the backend code. 
These libraries have to install before running the code.

1. Install OpenSSL Cryptographic library(To load certificate and obtain X509 object): pip3 install openssl
2. Install ssl library(To encrypt and decrypt the data over socket with SSL protocol): pip3 install ssl
3. Install socket library(To create communication between server and client): pip3 install sockets
4. Install publicsuffix2 library(To obtain top level domain of URL): pip3 install publicsuffix2
5. Install csv library(To read and write in a csv file): pip3 install python-csv
6. Install urllib.request library(To open URLs): pip3 install urllib.request
7. Install xmltodict library(To work with JSON): pip3 install xmltodict
8. Install asn1crypto.x509 library(To retrive SSL certificate information): pip3 install asn1crypto.x509==0.17.0
9. Install datetime library(To work with data and time): pip3 install datetime


References
1. Ssl - TLS/SSL wrapper for socket objects. (n.d.). Retrieved April 29, 2020, from https://docs.python.org/3/library/ssl.html
2. Python One-liner to get your site's Alexa Rank. Retrieved April 29, 2020, from https://gist.github.com/masnun/3170870
3. Cryptographic library.  http://openssl.cs.utah.edu/docs/crypto/crypto.html.
4. Publicsuffix2.  https://pypi.org/project/publicsuffix2/.
5. Explainwhatflaskisanditsbenefits?,Oct2019.https://www.i2tutorials.com/technology/explainwhatflaskisanditsbenefits/
7. Flask – Templates. (n.d.). Retrieved May 06, 2020, from https://www.tutorialspoint.com/flask/flask_templates.htm
8. Publicsuffix2.  https://pypi.org/project/publicsuffix2/.
9. AJAX with jQuery. (n.d.). Retrieved May 06, 2020, from https://flask.palletsprojects.com/en/1.1.x/patterns/jquery/
10. Installation. (n.d.). Retrieved May 06, 2020, from https://flask.palletsprojects.com/en/1.1.x/installation/
11. Web API. (25 April 2020). Retrieved May 06, 2020, from https://en.wikipedia.org/wiki/Web_API
12. Akanchha. (April 2020) "Exploring a robust machine learning classifier for detecting phishing domains using SSL certificates." Master's thesis completed at Dalhousie University's Faculty of Computer Science. https://dalspace.library.dal.ca/handle/10222/78875

















