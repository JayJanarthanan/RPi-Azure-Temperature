# RPi-Azure-Temperature
This repo will show you how to upload temperature to Microsoft Azure via Raspberry Pi

## Introduction

This guide will teach you how to upload temperature data from a Raspberry Pi to Azure Table Storage. For this guide, you need the following:

- Azure Subscription
- Raspberry Pi (Any Model)
- DS18B20 Sensor (including PAR)
- WiFi / Ethernet connection to internet
- Constant Power Source

## Creating the Azure Table Storage

Visit http://portal.azure.com.

Create a new Storage account by:  
1) New > Data + Storage + Storage Account  
2) Enter the following details:    
**Name:** Any name you want, e.g. rpitemp (rpitemp.core.windows.net)  
**Deployment Model:** Standard  
**Performance:** Standard  
**Subscription:** Select as required  
**Resource Group:** Select as required  
**Location:** Select as required  

3) Press Create. Your storage instance will now be created.  


![Table Storage Creation](images/creation.png?raw=true "Table Storage Creatione")

4) Once it has been created, find and save the access keys, mainly:
- Storage Account Name
- Access keys (KEY1)  

![Access Keys](images/access_key.png?raw=true "Access Keys")

5) Your Azure storage account is ready to go! Now it's time to wire up the Raspberry Pi.

## Wiring up the Raspberry Pi

If you are using a normal DS18B20 sensor, you will need to use a 4.7k resistor for pullup. The other option is the DS18B20-PAR sensor, which is parasitic and can be plugged in directly into the Raspberry Pi. We have used the PAR sensor for this tutorial for simplicity. 

Please follow this diagram to connect your sensor to the Raspberry Pi:

![GPIO Diagram](images/gpio_diagram.png?raw=true "GPIO Diagram")

## The Raspberry Pi Code

Now that our hardware and cloud instance is setup, we want to write code on the Raspberry Pi to read the temperature sensor and send this data to our Table Storage in Microsoft Azure. We will use a python script with two functions to achieve this.

Save the script below in the /home/pi directory. 
  
1) ![The temperature reading code] (azuresend.py)  

We need to constantly upload temperature data while not freezing the system or having the possibility of the python script exiting. The ideal solution to this is to have a cronjob which triggers the upload code once every 10 minutes (or as you please).

To do this, type `sudo crontab -e` in your console

Then at the end of the cron file, write:

`*/10 * * * * sudo python /home/pi/azuresend.py`


## Linking it all together

Write `sudo reboot` into the console to restart the Raspberry Pi. On start, it should automatically start sending data from the sensor to Azure Table Storage every x minutes. You can check this by visiting your Azure Storage instance and viewing the table view.

## Reading the data



## Final Comments
