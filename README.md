# Cisco Catalyst 9840 - Zero Touch Provisioning (ZTP)
This repository is elated to ZTP or Zero Touch Provisioning on the Cisco Catalyst 9800 series Wireless LAN Controller. 

## DHCP Option 67
In this demo I am using the 9840 WLC running IOS XE 16.12.1s, using Linux Ubuntu running the ISC DHCP Server and NGINX Webserver. The DHCP server is configured with option 67 (bootfile name) which points to a Pytho scripts, and this combination triggers the ZTP workflow on the IOS XE device

## ztp-simple.py
The Python script is served from the NGINX webserver and is used to configure the hostname, IP, and some additional access details.

## Demo Video
See 9 minute recording (no sound) at [https://www.youtube.com/watch?v=qVkXd1nWGVY](https://www.youtube.com/watch?v=qVkXd1nWGVY)
