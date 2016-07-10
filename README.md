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


![alt tag](images/1.png)

4) Once it has been created, find and save the access keys, mainly:
- Storage Account Name
- Access keys (KEY1)  

5) Your Azure storage account is ready to go! Now it's time to wire up the Raspberry Pi.

## Wiring up the Raspberry Pi

If you are using a normal DS18B20 sensor, you will need to use a 4.7k resistor for pullup. The other option is the DS18B20-PAR sensor, which is parasitic and can be plugged in directly into the Raspberry Pi. We have used the PAR sensor for this tutorial for simplicity. 

Please follow this diagram to connect your sensor to the Raspberry Pi:

## The Raspberry Pi Code

Now that our hardware and cloud instance is setup, we want to write code on the Raspberry Pi to read the temperature sensor and send this data to our Table Storage in Microsoft Azure. We will use two pieces of code to do this. We also want to ensure the code runs as soon as the Raspberry Pi turns on.

1) The temperature reading code
2) The upload code
3) Code to continuously upload

## Linking it all together

Alright! Now that we have the Raspberry Pi setup and the Azure instance ready, we're ready to go! Simply reboot the Raspberry Pi. Soon, you shall see data coming into your Azure tables.

## Reading the data



## Final Comments
