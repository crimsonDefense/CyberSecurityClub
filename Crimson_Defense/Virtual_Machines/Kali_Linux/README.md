## Kali Linux
Once you have VirtualBox downloaded, it is time to download Kali Linux. There are two options to choose from. The "customized" one is created by zSecurity. I took a course that he taught, and it was great. It works very well, but the other Kali machine has a ton of pre-installed tools. Either OVA file will work. They are both great! If you are interested in knowing what bugs he fixed, here is the link to it:<br>
[Kali Linux by Zsecurity](https://zsecurity.org/download-custom-kali/)<br>

## Links to both downloads
Link to the regular Kali Linux 2020 Machine:<br>
[Kali Machine](https://www.offensive-security.com/kali-linux-vm-vmware-virtualbox-image-download/#1572305786534-030ce714-cc3b) <br>

Link to the zSecurity Kali Linux machine: <br>
[zSecurity Machine](https://zsecurity.org/download-custom-kali/) <br>
<br>

## kali-linux-2020
The default user has been changed to a standard, unprivileged user. The default username and password are both "kali".<br>

Prevent Kali from going idle:
- Click on the power button (top right), then "Power Manager Settings", and then Display
- Change all of them to "never"
- Go to security, change the same thing, if you want to. 

To change the password:
- sudo su (su meaning switch user)
- Type in the password ("kali")
- passwd root (we are changing the password for the root user, you.)
- type in your new password

Now it is time to update. You will need to be patient for this step. Open up a terminal and type in the following:

```unix
$ apt update && apt -y full-upgrade
```

After all of that, you should be set. When powering down the machine, do not use the <i>X</i> button in the corner. Doing that is like pulling the plug on your computer when it is on. You are going to go to VirtualBox, right click on the machine, then close, then power off.<br>
<br>

## Kali 2020 x64 Customized by zSecurity
After downloading and then double clicking on the OVA file, click on import. If you haven't downloaded Oracle VM extension pack, go ahead and do so now. I explain where it is [one directory up](../../Virtual_Machines). If you have everything downloaded we can now turn on the machine. If you would like to change the name of the machine, I would do so now. Click on the machine, then settings, and then general; this is where you can change the name. After you do that, hit start.<br>

The log in information is going to be:<br>
username: "root"<br>
password: "toor"<br>

Prevent Kali from going idle:
- Click on the power button (top right), then "Power", and then switch it to never.

The next thing you want to do is update the sources where Kali can search and download programs from with the following command:

```unix
# apt-get update
```

If you would like to, you can install a terminal that will allow you to have multiple terminal windows open in the same window. You are going to download this with the following command. 

```unix
# apt-get install terminator 
```

Press y and hit enter to confirm the download, and then it will install on your system. <br>
<br>


## Windows won't let you power on Kali Linux?
If you are using Windows, you might come across an error in which the machine won't even start. Does it say something like "Failed to open a session for the virtual machine"? If so, try the following and see if it fixes the issue. If it doesn't fix the issue, you can always message in the general slack and ask for help!<br>

What you are going to want to do is first close out your virtual machine manager, in this case it should be VirtualBox. Go to Windows Search and type in "features". Click on "Turn Windows features on or off". Now you are going to disable the following. If any of them are already disabled, then you can skip those:
- Virtual Machine Platform
- Windows Defender Application Guard
- Windows Hypervisor Platform
- Windows Sandbox

Click ok and restart your computer. 
