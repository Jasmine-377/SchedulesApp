# Schedule Manager
Schedule Manager


Graphical Abstract:



Purpose of the Software:
Schedule Manager is a comprehensive scheduling and travel planning software suitable for individuals of all age groups in society. The software offers a user-friendly interface and a robust set of features to help users efficiently manage their daily schedules and travel plans with functions like adding new schedule and locating a schedule. 

Software Development Model:
This software project utilizes the Agile Development process. Since Schedule Manager is a time-to-market software, it requires rapid iteration and adaption to the market changes. Agile development method is suitable for it. With short iterations (Sprint), our team can quickly respond to users’ feedback, developing more functions and optimize user experience.



Market and Target Customers:
1. Travel enthusiasts: Plan their itineraries and keep track of their travel plans. Schedule Manager enables users to meticulously plan their itineraries by researching destinations, attractions, accommodations, and transportation. 
2. Business people: Manage business trips and meetings. This software enhances work efficiency and ensures smooth business operations.
3. Students: Make study plans and activity schedules. This software helps students map out their learning schedules by allocating time for different subjects and study tasks, and setting deadlines for assignments and exams.




Software Development Plan
Development Process
1.Requirement Analysis：During this phase, our team and stakeholders will work closely together to identify and define the essential functions of the software and the specific needs of the target users. This involves conducting thorough market research and user surveys to understand the pain points and expectations from the potential customerd.

2.Design: This phase includes the design of the software architecture and the user interface. In terms of software architecture, our team will need to plan the general structure of the software and select appropriate technologies and frameworks to ensure the users' experience.

3.Development: Our team proceeds to the coding phase to implement the features of Schedule Manager A. During development, programmers write code based on the software architecture and design specifications, using appropriate programming languages and development tools. They break down the software into multiple functional modules, such as the schedule management module, travel planning module, and user settings module, and assign different developers or development teams to work on each module. 

4.Testing: Our team developers will test individual code units and modules to ensure they function correctly. For instance, we will test whether adding, deleting and querying schedules work properly and whether the adjusted schedule order and added schedule locations are accurate.

5.Releasing: During this phase, our team will generate an APK file for the software and publish it to GitHub. Therefore, Users can download the APK file from GitHub and install Schedule Manager A on their Android devices.

6.Maintenance: Update the software to meet the market's requirements and users' feedbacks.



Team Members:
Amy: Requirement Analysis and Design; Maintenance and Updating:
Sylvia: Adding, deleting and ordering the schedule; Maintenance and Updating:
Jasmine: Showing the location of the schedule on the map
Miku: Showing the location of the schedule on the map
Zhang Hanyuan:Testing and Optimizing; Beta Release




Development Planning:

• Requirement Analysis and Design：3 days

• Development Stage:
    Adding, deleting and ordering the schedule:  1 week
     
Showing the location of the schedule on the map:  2 weeks

• Testing and Optimizing: 1week

• Beta Release: 3 days

• Maintenance and Updating: Ongoing after software launching 




Travel Planner Core Algorithms：

1. Schedule ：Use ‘ItemTouchHelper’ to drag and order the schedules. Enhance the clarity of the schedule, making the software more user friendly.

2.Positioning Algorithms: Use Google Maps API to locate the schedule and show it through the map.

3.Database Management：Use SQLite as the database management system (DBMS) to store and manage the data of the schedules. SQLite holds its advantage since it is self-contained which means the configuration and installation of it.


Current Status of Travel Planner
1. Adding, deleting and ordering the schedule
2. Local storage of the data 
3. Showing the location of the schedule on the map
4. Countdown timer function

Future Plan of Travel Planner
1. Developing schedule reminder
2. Cloud storage of the data
3. Adding multi-language switching
4. Optimizing user interface (UI)


Environments of the Software Development and Running

Programming Language

• Python



Required Packages
tkinter；
json；
webbrowser；
geopy

Declaration
The following open source libraries and tools were used in this project：
Open Source Packages
tkinter: Used to create the user interface of the Schedule Manager application.
json: Used in the code to save and load schedule data to and from files.
webbrowser: Used in the code to open the OpenStreetMap website and display the geographic location of the schedule.
geopy: Use geopy's Nominatim geocoder in the code to get the latitude and longitude of the place name in the schedule for display on OpenStreetMap.
Components
tkinter.Tk: In the code, the MainApplication class inherits from tkinter.Tk and is used to create the main window of the application.
tkinter.ttk: Used in the code to create controls such as buttons (ttk.Button) and input boxes (ttk.Entry).
tkinter.messagebox: Used in the code to display error messages, such as errors in the time format or inability to display the geographic location.
tkinter.Listbox: Used in the code to display a list of schedules.
tkinter.Frame: Used in the code to create button frames and map display frames.
geopy.geocoders.Nominatim: Used in the code to obtain the latitude and longitude of the place according to the name of the place in the schedule.
