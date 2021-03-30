## AMX Framework (Automation Mobile Experience Framework)

Nowadays, some organizations still execute the test life cycle of their projects without test automation, which means that they also do it without the possibility of implementing the best Quality Assurance & DevOps practices using Continuous Integration and Continuous Development.

If you would like to start a test automation effort in your organization with a formal and mature process, this paper will help you to start and not die trying!

In the process, this paper will introduce and discuss the Android Open Source project "UP Automation Framework" a wrapper of libraries developed by the Panamerican University (Universidad Panamericana in Spanish), that will help you implement a mobile test automation framework and structure in your organization. This paper explains the fundamental principles and demonstrates how to apply them.  We’ll look at identifying what type of mistakes are most frequently made in your organization and choosing from a toolkit of prevention and detection practices to address these mistakes.  We’ll also talk about how to choose the practices that best fit your organization’s software development process.

## Structure

The following section contains an explanation of the different folders that compose the project, and the content of each one of them.

### GUI Folder
An angular application that has the demo to execute the test cases of the framework. 

### Lib Folder

#### Adb Folder
Adb Controller Class has a function to run an adb command and other functions that will execute specific commands like install app, open app, close app, make phone call, download logcat, install app from PC, get the list of installed apps, toggle Bluetooth and take a screenshot. 

#### Data Repository Folder
Data Device Class to create an object with the ID of the device and other properties like the brand, the operative system, the version of the operative system and others.
Data Repository Class that has functions to insert, update and to get all the records from the database that we have on Firebase.

#### File Manager Folder
File Manager Class that has functions to read and write files, to search a value on a file and to check if a directory exists on the device. 

#### Logs Folder
Logger Class has functions that will write messages on the log file and a function to get the actual content of the logger. The type of messages are debug, info, success, warning and error. 

#### My App Folder
My App Class to create an object with the package name of the app and it has a function to check it the app is opened.

#### My Device Folder
My Device Class to create an object with the ID of the device, the path of the logcat on the pc, an adb controller object, the path of the downloads on the PC and the path of the screenshots on the PC. It has functions to install an app, download an apk, install an apk from the PC, open an app, close an app, download log, open log, close log, press the back button, make phone call using the UI, clear apps, press the home button, check if an app is installed, toggle Bluetooth, toggle WIFI, end a call, pause a call, check if a call is answered in less than a minute, make a click, take a screenshot, copy files from device to PC, copy one file from device to PC and find a value on the log. 

#### STF Device Folder
STF Device Class to create an object with the ID of the device, the URL of the mobile test farm and the token for the farm. It has functions to check if the farm is being used by a device, to add a device to the farm, to connect to a device from the farm, to disconnect a device from the farm, to get the connection address to the farm and to remove a device from the farm. 

## Team

* Juan Carlos García and Ricardo Macías – Product Owners

* Juan de Dios Delgado – Scrum Master and Project Manager

* Isaac Méndez – Technical Lead

* Marco Montoya – Technical Lead

* Rodrigo Quiroz – Python Developer

* Ricardo Bustos – Python Developer

* Carolina Delgadillo – Python Developer

* Diego Camacho – Python Developer

* Luis García – Mobile Tester

* Jorge Ramírez – Mobile Tester

* Miguel Salazar - Mobile Tester

## Test Cases

Open a console in your computer and navigate to the project folder.

For the first integration, run the following command.

```
python test/integration_tests/test_s1_integration.py
```

For the second integration, run the following command.

```
python test/integration_tests/test_s2_integration.py
```

For the third integration, run the following command.

```
python test/integration_tests/test_s3_integration.py
```

## Demo

Open a console in your computer and navigate to the project folder.

Run the following commands and the demo will open on your default browser. 

```
cd gui
ng serve --open
```
