from flask import Flask, render_template, request, jsonify
import ssl,socket
from asn1crypto.x509 import Certificate
from cryptography.hazmat.backends import default_backend
from OpenSSL.crypto import (load_certificate, X509)
from publicsuffix2 import PublicSuffixList
import xmltodict, json, re
import csv
import urllib.request, sys, xmltodict, math
from datetime import datetime



application = Flask(__name__)
# Global variables
global domain,cert
domain=None
cert=None


#This certificate extraction method is called for extracting SSL certificate from a domain.
#This code is a modified version of the code to retrieve SSL certificates found on: https://docs.python.org/3/library/ssl.html written by Python Software Foundation
def readDomain(domain):
    host = domain
    port= 443
    dst = (host,port)
    try:
        conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error:
        return "Error in socket connection"
    except ValueError:
        return "Please enter valid site name"    
    try:
        conn.connect(dst)
    except socket.gaierror:
        return "Address-related error connecting to server" 
        sys.exit(1)
    except socket.error:
        return "Connection error" % e
    except ValueError:
        return "Please enter valid site name"    
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    conn = ctx.wrap_socket(conn, server_hostname=dst[0])
    cert = ssl.DER_cert_to_PEM_cert(conn.getpeercert(True))
    return cert

#This feature method checks whether the certificate is domain validated or not. In any domain validated certificate, the subject name must not have a business category and organization name fields.
def isdomainvalidated(inputDomain):
    Is_domian_validated=False
    domain=inputDomain 
    cert=readDomain(domain)
    x509_One=crypto.load_certificate(crypto.FILETYPE_PEM, cert)
    if x509_One.get_subject().businessCategory:
        Is_domian_validated =False
    elif x509_One.get_subject().O:
        Is_domian_validated =False
    else:
        Is_domian_validated=True  
    return Is_domian_validated

#This feature method checks whether the issuer component has state field or not in the certificate
def issuerHasState(inputDomain):
    cert=readDomain(inputDomain)
    x509_One=crypto.load_certificate(crypto.FILETYPE_PEM, cert)
	IssuerHasState=False
    if x509_One.get_issuer().ST:
        IssuerHasState=True
    else:
        IssuerHasState=False
    return IssuerHasState

#This feature method calculates number of details in subject component, number of characters in Issuer and subject components and also number of extensions present in the certificate.
def subIsslength(inputDomain):
    subject = []
    cert=readDomain(inputDomain)
    x509_One=crypto.load_certificate(crypto.FILETYPE_PEM, cert)
    issue = x509_One.get_issuer()
    sub= x509_One.get_subject()
    issuer = []
    for item in issue.get_components():
        issuer.append('%s' %  (item[1]) )
    for item in sub.get_components():
        subject.append('%s' %  (item[1]) )
    total=0
    total1=0
    for word in subject:
        total+= len(str(word))
    for word in issuer:
        total1 += len(str(word))
	# Calculates number of details present in subject component
	SubjectElements=len(subject)
	# Calculates number of characters of whole subject component string
	SubjectLength=total
	# Calculates number of details present in issuer component
    IssuerElements=len(issuer)
	# Calculates number of extensions contained in the certificate
	ExtensionNumber=x509_One.get_extension_count())
    return SubjectElements, SubjectLength,IssuerElements,ExtensionNumber


#Ranking of a domain. The ranking is analyzed by estimating traffic of the domain.
#This code is used verbatim to meet the requirements of the functionality of our application from the code to get Alexa Rank of domain found on: https://gist.github.com/masnun/3170870 written by risheek20(25 September 2018)
def domainRanking(inputDomain):
    host=inputDomain
    url_link='http://data.alexa.com/data?cli=10&dat=s&url={}'
    xml = urllib.request.urlopen(url_link.format(host)).read()
    result= xmltodict.parse(xml)
    data = json.dumps(result).replace("@","")
    data_tojson = json.loads(data)
    try:
        url = data_tojson["ALEXA"]["SD"][1]["POPULARITY"]["URL"]
        rank= data_tojson["ALEXA"]["SD"][1]["POPULARITY"]["TEXT"]
    except KeyError:
            rank=42089
    Domain_ranking=rank
    return Domain_ranking

#This feature method checks whether subject component's CN field is a `.com’ domain
def subDotCom(inputDomain):
    cert=readDomain(inputDomain)
    x509_One=crypto.load_certificate(crypto.FILETYPE_PEM, cert)
	psl = PublicSuffixList(idna=True)
	Subject_is_com= False
	j= 'com'
	if j in psl.get_tld(cert.get_subject().CN):
		Subject_is_com = True
	else:
		Subject_is_com = False
	return  Subject_is_com 

#This feature method checks whether issuer component's CN field is a `.com’ domain
def issDotCom(inputDomain):
    cert=readDomain(inputDomain)
    x509_One=crypto.load_certificate(crypto.FILETYPE_PEM, cert)
	psl = PublicSuffixList(idna=True)
	Issuer_is_com= False
	j= 'com'
	if j in psl.get_tld(cert.get_issuer().CN):
		Issuer_is_com = True
	else:
		Issuer_is_com = False
	return Issuer_is_com 

#This feature method calculates difference between Not Before and Not After fields of Validity in the certificate.
def daysValidity(inputDomain)
    cert=readDomain(inputDomain)
    x509_One=crypto.load_certificate(crypto.FILETYPE_PEM, cert)
    notBefore = datetime.strptime(x509_One.get_notBefore().decode('ascii'), '%Y%m%d%H%M%SZ')
    notAfter = datetime.strptime(x509_One_notAfter().decode('ascii'), '%Y%m%d%H%M%SZ')
    DaysValidity=abs((b-a).days)
    return DaysValidity
	
	
#This decision rules method classifies the domain as a legitimate or phishing.
def decisionRules(feature_1,feature_2,feature_3,feature_4,feature_5,feature_6,feature_7,feature_8,feature_9,feature_10):
    output=None
    myDict = {'Is_domian_validated':feature_1,'Issuer_is_com':feature_9,'DaysValidity':feature_10,'Subject_is_com':feature_8
        ,'IssuerElements':feature_5,'Domain_ranking':feature_7,
         'IssuerHasState':feature_2,'SubjectLength':feature_4, 'SubjectElements'=feature_3, 'ExtensionNumber'=feature_5}
    if (myDict['Domain_ranking']>42089):
        output='Phishing Domain'
    elif(myDict['Domain_ranking']<=42089 and myDict['Is_domian_validated']==False and myDict['IssuerHasState']==False and myDict['Subject_is_com']==True):
        output='Legitimate Domain'
    elif(myDict['Domain_ranking']<=42089 and myDict['Is_domian_validated']==False and myDict['IssuerHasState']==True and myDict['SubjectElements']<=5):
        output='Phishing Domain'
    elif(myDict['Domain_ranking']<=42089 and myDict['Is_domian_validated']==False and myDict['IssuerHasState']==True and myDict['SubjectElements']>5):
        output='Legitimate Domain'
    elif(myDict['Domain_ranking']<=42089 and myDict['Is_domian_validated']==False and myDict['IssuerHasState']==False and myDict['Subject_is_com']==False and myDict['SubjectLength']<=66):
        output='Legitimate Domain'
    elif(myDict['Domain_ranking']<=42089 and myDict['Is_domian_validated']==False and myDict['IssuerHasState']==False and myDict['Subject_is_com']==False and myDict['SubjectLength']>66):
        output='Phishing Domain'
    elif(myDict['Is_domian_validated']==True and myDict['Subject_is_com']==False):
        output='Phishing Domain'
    elif(myDict['Is_domian_validated']==True and myDict['Subject_is_com']==True and myDict['IssuerHasState']==False and myDict['IssuerElements']<=3):
        output='Legitimate Domain'
    elif(myDict['Is_domian_validated']==True and myDict['Subject_is_com']==True and myDict['IssuerHasState']==False and myDict['IssuerElements']>3 and myDict['SubjectLength']>16):
        output='Phishing Domain'
    elif(myDict['Is_domian_validated']==True and myDict['Subject_is_com']==True and myDict['IssuerHasState']==False and myDict['IssuerElements']>3 and myDict['SubjectLength']<=16 and myDict['DaysValidity']>735):
        output='Legitimate Domain'	
    elif(myDict['Is_domian_validated']==True and myDict['Subject_is_com']==True and myDict['IssuerHasState']==False and myDict['IssuerElements']>3 and myDict['SubjectLength']<=16 and myDict['DaysValidity']<=735):
        output='Phishing Domain'
    elif(myDict['Is_domian_validated']==True and myDict['Subject_is_com']==True and myDict['IssuerHasState']==True and myDict['ExtensionNumber']>10):
        output='Legitimate Domain'
    elif(myDict['Is_domian_validated']==True and myDict['Subject_is_com']==True and myDict['IssuerHasState']==True and myDict['ExtensionNumber']<=10 and myDict['Issuer_is_com']==False):
        output='Phishing Domain'
    elif(myDict['Is_domian_validated']==True and myDict['Subject_is_com']==True and myDict['IssuerHasState']==True and myDict['ExtensionNumber']<=10 and myDict['Issuer_is_com']==True):
        output='Phishing Domain'
    else:
        output='Please try again'
        
    return output

#Running the background process of Web API by calling feature creation methods, certificate extection method and decision rules method.
@app.route('/application_process')
def application_process():
    try:
        domainInput = request.args.get('domain', 0, type=str)
        if domainInput == '':
            return jsonify(result='Please enter a site name')
        else:
            domain=domainInput
            try:
			#calling certificate extraction method to obtain entered domain's SSL certificate.
                cert=readDomain(domain)
            except ValueError:
                return jsonify(result='Please enter valid site name') 
		#calling feature creation methods to create features.
            feature_1=isdomainvalidated(domain)
            feature_2=issuerHasState(domain)
            feature_3,feature_4,feature_5,feature_6=subIsslength(domain)
            feature_7=domainRanking(domain)
            feature_8=subDotCom(domain)
            feature_9=issDotCom(domain)
            feature_10=daysValidity(domain)
		#calling decision rules method to classify the domain as a legitimate or phishing
            decision_rule= decisionRules(feature_1,feature_2,feature_3,feature_4,feature_5,feature_6,feature_7,feature_8,feature_9,feature_10)
            return jsonify(result=decision_rule) 
    except Exception as e:
        return str(e)
@application.route('/',methods = ['POST', 'GET'])
def application_output():
    return render_template('api.html')


if __name__ == "__main__":
    application.run(debug=True)
