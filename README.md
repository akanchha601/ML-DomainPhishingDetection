# ML-DomainPhishingDetection

## Description of the code
Python version- 3.7
Flask version- 1.1.1
Operating system- Windows 10

Before installing flask, python has to install in the system.
The frontant and backend are connected using flask. The frontend code is saved in api.html and backend code is saved in api.py. The static folder contains
script.js, image.img, and stylling.css files. stylling.css file is used for styling and script.js controls behaviour of the web page of application. The api.html provides the basic structure of web page of application by using these static files. 
The api.html should be saved in templates folder and static files in static folder that are the requirements of flask in order to work.

## Proof-of-Concept Web Application
This web application allows a user to identify whether a domain visited is legitimate or phishing on frontend.
HTML and CSS are used for creating page structure and styling of web page. 
In addition, JavaScript provides dynamic functionality to web page by handling HTML elements. 
Based on the output of backend functions(feature creation, decision rules and certificate extraction), JavaScript action method calls on check box to response the user input request and shows the result on screen.
Below screenshots show the running server through web service:
In text box, users can enter the domain name of a website to verify. By clicking on check box, it shows whether the entered domain is a legitimate or phishing on the screen.
![example_of_legitimate_domain](/uploads/cbbcc52edc04507a37f5073ff86efa2f/example_of_legitimate_domain.png)
![example_of_phishing_domain](/uploads/9a432848e2536ade70b30abce0478d7e/example_of_phishing_domain.png)
The web application also returns an error message on wrong input data. 
It shows error messages on screen when input request is empty or input data is other than domain name of the website.
Below are examples of error messages.
![example_of_error_case_1_copy](/uploads/efd57de4ae89ebbb498aeb3a720abc34/example_of_error_case_1_copy.png)
![example_of_error_case_2](/uploads/2a86e5c0483195eef76c2dc9acb68b36/example_of_error_case_2.png)


## Web API 
Web API provides application interface to user over the internet. 
It handles user request and returns output through web service. 
As there are many popular web frameworks that supports an environment to develop a Web API. 
In my reseach, Flask framework was used to create Web API for auto-detection of a phishing domain. 
The flask is easy to install and contained several tools, libraries, and technologies to build a web application. 
As the backend classification part of the Web API, the decision tree machine learning classifier is implemented using the Python programming language.
Main functionalities of Web API are:
* It must identify phishing and legitimate domain based on decision tree classification rules.
* It must return an error message on wrong input data.
* It must successfully create features using different Python library method.
* It must extract the certificate from the website without any error because phishing domains are active for very short span of time.
* It would not detect any types of web attack such as Distributed Denial of Service (DDOS) etc.
* Input data should be a website domain name.

The flow chart of this framework is below




![Flow_chartAPI_new](/uploads/49158b8ad6339cb6c6955b562d6e1260/Flow_chartAPI_new.jpg)
                               
                               
                               
                               
                               
                               
                               
                               
                               
                               
                               
                               
                               
                               
                               
                               
                               
                               
                               
                               
                               
                               
                               
                               
                               
                               
                               
                               
                               
                               Fig 1.1
                               
The flow chart of the framework is explained below:

* Input is domain of the a website.
* Extraction of certificate from the input domain. 
* Features are created for a certificate.
* Decision Tree classifier rules are employed to classify category of the domain.
* The result shows that a domain was legitimate or phishing domain.
                                                            
                                                       
                                                             




References
1. Ssl - TLS/SSL wrapper for socket objects. (n.d.). Retrieved April 29, 2020, from https://docs.python.org/3/library/ssl.html
2. Python One-liner to get your site's Alexa Rank. Retrieved April 29, 2020, from https://gist.github.com/masnun/3170870
3. Cryptographic library.  http://openssl.cs.utah.edu/docs/crypto/crypto.html.
4. Publicsuffix2.  https://pypi.org/project/publicsuffix2/.
5. Explainwhatflaskisanditsbenefits?,Oct2019.https://www.i2tutorials.com/technology/explainwhatflaskisanditsbenefits/
6. (n.d.). Retrieved Feb 29, 2020, from https://www.google.com/imgres?imgurl=https%3A%2F%2Fmiro.medium.com%2Fmax%2F1200%2F1%2Amk1-6aYaf_Bes1E3Imhc0A.jpeg















