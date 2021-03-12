# Tool of the Week
Every week someone from the competition team will look into a tool used for solving CTF challenges. A brief presentation will be given about the tool and a write up consisting of only a few sentences will be presented as well. Here you can find the tools that we have discussed and the write up provided by the individual who did researched said tool.

# TOTW
Meeting on 3/04/21 <br>
<b>Cryptii.com</b><br>
Cryptii.com is an open source web app that provides the user with the means to encode or decode strings of characters within their browser. Encoding/decoding options include ASCII, binary, hexadecimal, base64, Caesar Cipher, Morse Code, and more! <br>
To explore the web app for yourself, go to: https://cryptii.com/. <br>

<b> LOR </b>

----

Meeting on 2/25/21<br>
<b>CeWL</b><br>
“The Custom Word List generator, CeWL is a ruby app which spiders a given URL to a specified depth, optionally following external links, and returns a list of words which can then be used for password crackers such as John the Ripper.” This is useful when you have a webpage with some content (articles, blogs, or other forms of writing) available through http or https and you are trying to escalate your privilege. Example:<br>
cewl -d 2 -m 5 -w docswords.txt https://<i></i>example.com <br>
Depth of 2, Maximum word-length of 5, output to docswords.txt, target https://<i></i>example.com <br>

<b>The Guilty Remnant</b>

----

Meeting on 2/18/21<br>
<b>Hashcat</b><br>
Hashact is a popular password cracker and is designed to break even the most complex passwords. For example, let's say you are given a password that has been hashed using md5 (71b816fe0b7b763d889ecc227eab400a) and you know the format of the password is "SKY-HQNT-" followed by 4 digits, you can use hashcat to brute force it and find out the entire password. Using the following command will get you the answer:<br>
hashcat -m 0 -a 3 ./<hash file name>.txt 'SKY-HQNT-?d?d?d?d' <br>
- m is for mode and 0 is mode md5 <br>
- a is for action and 3 is for brute force <br>
- hash file is the text file where you are storing the hashed password <br>

<b>Percy Knox</b>

----

Meeting on 2/11/21<br>
[Snort](https://www.snort.org/) <br>
Snort is an open source intrusion prevention system. It is capable of real-time traffic analysis and packet logging. You can easily read through the logs, and you can also have the logs fowarded to the logging system of your choice such as splunk; CCDC members will probably be familiar with that name. I also propose that whoever manages splunk should be gifted the incredible nickname that I thought of, Spunk Master Flex; named after Funk Master Flex. <br>

<b>Percy Knox</b>

----

Meeting on 2/4/21<br>
<b>Python</b> <br>
When it comes to solving capture the flag challenges, there are many great tools that you can use, some of which might already be downloaded on your pentesting machine! If not, you can find many great tools to download online. However, there are going to be times where the tools that you have at your disposal are almost what you need but not exactly what you need. If you ever get to this point, you should never give up. You just need to find another way to solve the problem and Python just might be your answer. Python is great for writing scripts quickly and effeciently. With Python, you can do almost anything. You can use Python to create scripts to solve an array of problems including password cracking, web exploitation, and many more. <br>

<b>inspectelement</b>

----

Meeting on 1/28/21 <br>
<b>Nmap</b> <br>
Using the command ifconfig you can get the range of your network. You can then use Nmap to discover other machines. If there is a target machine in the network range, you can use Nmap to discover the machine’s IP address. Similar tools include netdiscover and ARP. Using these two tools first can allow you to narrow down the target machine, and you can then use Nmap along with these two commands to get the information you need about the target machine. The command –sS will tell Nmap to look for open ports and services and the command –AT4 looks for OS information, which can tell you a lot about your target machine. <br>

<b>Percy Knox</b>
