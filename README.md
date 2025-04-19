# Schedule Manager

### Graphical Abstract

- **Main interface**
  [Main Interface]
  ![屏幕截图 2025-04-19 183142](https://github.com/user-attachments/assets/10323c12-ef2d-4e2d-94cf-d8acd37e1115)

- **Add a new schedule**
  [Add Schedule]
  ![屏幕截图 2025-04-19 185231](https://github.com/user-attachments/assets/88db4eda-05db-4af1-a901-f0661691a167)

- **Edit a schedule**
  [Edit Schedule]
  ![屏幕截图 2025-04-19 185047](https://github.com/user-attachments/assets/e7ee473e-8ee0-4899-9deb-8d3a9a42709e)

- **Jump to the location map**
  [Location Map]
  ![屏幕截图 2025-04-19 185120](https://github.com/user-attachments/assets/2d4ccf24-1160-4455-972c-888b12e930dd)


## Purpose of the Software

Schedule Manager is a comprehensive scheduling and travel planning software suitable for individuals of all age groups in society. The software offers a user-friendly interface and a robust set of features to help users efficiently manage their daily schedules and travel plans with functions like adding new schedule and locating a schedule.

## Software Development Model

This software project utilizes the Agile Development process. Since Schedule Manager is a time-to-market software, it requires rapid iteration and adaptation to the market changes. Agile development method is suitable for it. With short iterations (Sprints), our team can quickly respond to users’ feedback, developing more functions and optimize user experience.

### Market and Target Customers

1. **Travel enthusiasts**: Plan their itineraries and keep track of their travel plans. Schedule Manager enables users to meticulously plan their itineraries by researching destinations, attractions, accommodations, and transportation.
2. **Business people**: Manage business trips and meetings. This software enhances work efficiency and ensures smooth business operations.
3. **Students**: Make study plans and activity schedules. This software helps students map out their learning schedules by allocating time for different subjects and study tasks, and setting deadlines for assignments and exams.

## Software Development Plan

### Development Process

1. **Requirement Analysis**: During this phase, our team and stakeholders will work closely together to identify and define the essential functions of the software and the specific needs of the target users. This involves conducting thorough market research and user surveys to understand the pain points and expectations from the potential customers.

2. **Design**: This phase includes the design of the software architecture and the user interface. In terms of software architecture, our team will need to plan the general structure of the software and select appropriate technologies and frameworks to ensure the users' experience.

3. **Development**: Our team proceeds to the coding phase to implement the features of Schedule Manager A. During development, programmers write code based on the software architecture and design specifications, using appropriate programming languages and development tools. They break down the software into multiple functional modules, such as the schedule management module, travel planning module, and user settings module, and assign different developers or development teams to work on each module.

4. **Testing**: Our team developers will test individual code units and modules to ensure they function correctly. For instance, we will test whether adding, deleting and querying schedules work properly and whether the adjusted schedule order and added schedule locations are accurate.

5. **Releasing**: During this phase, our team will generate an APK file for the software and publish it to GitHub. Therefore, Users can download the APK file from GitHub and install Schedule Manager on their Android devices.

6. **Maintenance**: Update the software to meet the market's requirements and users' feedbacks.

### Team Members:

1. **Amy**: Requirement Analysis and Design; Maintenance and Updating
2. **Sylvia**: Adding, deleting and ordering the schedule; Maintenance and Updating
3. **Jasmine**: Showing the location of the schedule on the map
4. **Miku**: Showing the location of the schedule on the map
5. **Zhang Hanyuan**: Testing and Optimizing; Beta Release

## Development Planning:

- **Requirement Analysis and Design**: 3 days

- **Development Stage**:
  - Adding, deleting and ordering the schedule: 1 week
  - Showing the location of the schedule on the map: 2 weeks

- **Testing and Optimizing**: 1 week

- **Beta Release**: 3 days

- **Maintenance and Updating**: Ongoing after software launching

**Timeline**：

![7c86f1692cd3f5b4eb95ebc4f5c50de](https://github.com/user-attachments/assets/e0978152-295a-4a64-acf0-8f964311fee6)
![6a160e4325597da111d401d9f3e29dd](https://github.com/user-attachments/assets/eb13f3c5-e211-4fed-bdb5-c407e244f0cc)

## Travel Planner Core Algorithms:

1. **Schedule**: Use ‘ItemTouchHelper’ to drag and order the schedules. Enhance the clarity of the schedule, making the software more user-friendly.

2. **Positioning Algorithms**: Use Google Maps API to locate the schedule and show it through the map.

3. **Database Management**: Use SQLite as the database management system (DBMS) to store and manage the data of the schedules. SQLite holds its advantage since it is self-contained which means the configuration and installation of it.

## Current Status of Travel Planner

1. Adding, deleting and ordering the schedule
2. Local storage of the data
3. Showing the location of the schedule on the map
4. Countdown timer function

## Future Plan of Travel Planner

1. Developing schedule reminder
2. Cloud storage of the data
3. Adding multi-language switching
4. Optimizing user interface (UI)

## DEMO  
  
  
  
## Environments of the Software Development and Running

### Programming Language

- Python

### Required Packages

1. tkinter；
2. json；
3. webbrowser；
4. geopy；

## Declaration

The following open source libraries and tools were used in this project:

## Open Source Packages
·tkinter: Used to create the user interface of the Schedule Manager application；  
  
·json: Used in the code to save and load schedule data to and from files；
   
·webbrowser: Used in the code to open the OpenStreetMap website and display the geographic location of the schedule；  

·geopy: Use geopy's Nominatim geocoder in the code to get the latitude and longitude of the place name in the schedule for display on OpenStreetMap；  


## Components
·tkinter.Tk: In the code, the MainApplication class inherits from tkinter.Tk and is used to create the main window of the application；  

·tkinter.ttk: Used in the code to create controls such as buttons (ttk.Button) and input boxes (ttk.Entry)；  

·tkinter.messagebox: Used in the code to display error messages, such as errors in the time format or inability to display the geographic location；  

·tkinter.Listbox: Used in the code to display a list of schedules；  

·tkinter.Frame: Used in the code to create button frames and map display frames；  

·geopy.geocoders.Nominatim: Used in the code to obtain the latitude and longitude of the place according to the name of the place in the schedule for display on OpenStreetMap.  


