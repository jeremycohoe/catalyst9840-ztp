# catalyst9840-ztp
This repository is elated to ZTP or Zero Touch Provisioning on the Cisco Catalyst 9800 series Wireless LAN Controller. 

In this demo I am using the 9840 WLC running IOS XE 16.12.1s, using Linux Ubuntu running the ISC DHCP Server and NGINX Webserver. The DHCP server is configured with option 67 (bootfile name) which points to a Pytho scripts, and this combination triggers the ZTP workflow on the IOS XE device

The Python script is served from the NGINX webserver and is used to configure the hostname, IP, and some additional access details.
