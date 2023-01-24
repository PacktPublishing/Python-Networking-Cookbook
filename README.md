


# Python Network Programming Techniques

<a href="https://www.packtpub.com/product/python-network-programming-techniques/9781838646639?utm_source=github&utm_medium=repository&utm_campaign=9781838646639"><img src="https://static.packt-cdn.com/products/9781838646639/cover/smaller" alt="Python Network Programming Techniques" height="256px" align="right"></a>

This is the code repository for [Python Network Programming Techniques](https://www.packtpub.com/product/python-network-programming-techniques/9781838646639?utm_source=github&utm_medium=repository&utm_campaign=9781838646639), published by Packt.

**Practical recipes for secure network infrastructure, global application delivery, and accessible connectivity in Azure**

## What is this book about?
Network automation offers a powerful new way of changing your infrastructure network. Gone are the days of manually logging on to different devices to type the same configuration commands over and over again. With this book, you'll find out how you can automate your network infrastructure using Python. 

This book covers the following exciting features:
* Get to grips with building Azure networking services
* Understand how to create and work on hybrid connections
* Configure and manage Azure networking services
* Explore ways to design high availability network solutions in Azure
* Discover how to monitor and troubleshoot Azure network resources
* Work with different methods to connect local networks to Azure virtual networks

If you feel this book is for you, get your [copy](https://www.amazon.com/dp/1838646639) today!

<a href="https://www.packtpub.com/?utm_source=github&utm_medium=banner&utm_campaign=GitHubBanner"><img src="https://raw.githubusercontent.com/PacktPublishing/GitHub/master/GitHub.png" 
alt="https://www.packtpub.com/" border="5" /></a>

## Instructions and Navigations
All of the code is organized into folders. For example, Chapter02.

The code will look like the following:
```
import requests
from requests.auth import HTTPBasicAuth
auth = HTTPBasicAuth("root", "test")
```

**Following is what you need for this book:**
This cookbook is for cloud architects, cloud solution providers, and anyone who deals with networking on Azure. A basic understanding of Azure will help you to make the most of this book.

With the following software and hardware list you can run all code files present in the book (Chapter 1-12).
### Software and Hardware List
| Chapter | Software required | OS required |
| -------- | ------------------------------------ | ----------------------------------- |
| 1-12 | Python3 | Windows, Mac OS X, and Linux (Any) |
| 1-12 | Ansible | Windows, Mac OS X, and Linux (Any) |


We also provide a PDF file that has color images of the screenshots/diagrams used in this book. [Click here to download it](http://www.packtpub.com/sites/default/files/downloads/9781838646639_ColorImages.pdf).

### Code in Action
Click on following link to see the Code in Action:

[Youtube link](https://bit.ly/3s93enF)

### Related products
* Mastering Python for Networking and Security - Second Edition [[Packt]](https://www.packtpub.com/product/mastering-python-for-networking-and-security-second-edition/9781839217166?utm_source=github&utm_medium=repository&utm_campaign=9781839217166) [[Amazon]](https://www.amazon.com/dp/1839217162)

* Azure Networking Cookbook - Second Edition [[Packt]](https://www.packtpub.com/product/azure-networking-cookbook-second-edition/9781800563759?utm_source=github&utm_medium=repository&utm_campaign=9781800563759) [[Amazon]](https://www.amazon.com/dp/1800563752)

## Errata
* Page 40 (Step 7): **shell.send(cmd + "\n")** _should be_ **channel.send(cmd + "\n")**
* Page 40 (Step 7): **out = shell.recv(1024)** _should be_ **out = channel.recv(1024)**

## Get to Know the Author
**Marcel Neidinger**
started to program at the age of 10 and currently works as an API and programmability lead for the EMEAR Systems Engineering organization at Cisco Systems. Specifically, he works with customers and partners to build custom solutions using programmability and APIs. Besides having a bachelor's degree in computer science, he is also a Cisco Certified DevNet Associate as well as a Cisco Certified DevNet Specialist for enterprise network automation. You can find him on Twitter at squ4rks and on GitHub at squ4rks.
### Download a free PDF

 <i>If you have already purchased a print or Kindle version of this book, you can get a DRM-free PDF version at no cost.<br>Simply click on the link to claim your free PDF.</i>
<p align="center"> <a href="https://packt.link/free-ebook/9781838646639">https://packt.link/free-ebook/9781838646639 </a> </p>
