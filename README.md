# SchedulesApp
TravelPlanner-日程管理与旅行规划软件


Graphical Abstract:
项目主界面截图，展示日程列表和添加按钮。


Purpose of the Software:


Software Development Process
本项目采用敏捷开发（Agile Development）流程。敏捷开发强调快速迭代和适应变化，适合需求可能频繁变动的项目。通过短周期的迭代（Sprint），团队能够快速响应用户反馈，及时调整功能和优化用户体验。


Why Agile?
选择敏捷开发的原因如下：

• 快速迭代：能够快速交付可用的软件版本，及时收集用户反馈。

• 适应变化：项目需求可能随着开发过程而变化，敏捷开发能够灵活应对。

• 团队协作：促进团队成员之间的紧密合作，提高开发效率。


Possible Usage of the Software
TravelPlanner是一款面向旅行者的日程管理与旅行规划软件。其目标市场包括：

• 旅行爱好者：帮助他们规划行程、记录旅行计划。

• 商务人士：方便他们管理出差日程和会议安排。

• 学生：用于规划学习和活动日程。


Software Development Plan

Development Process

• 需求分析：确定软件功能和用户需求。

• 设计：设计软件架构和用户界面。

• 开发：编写代码实现功能。

• 测试：进行单元测试和集成测试。

• 部署：生成APK文件并发布到GitHub。

• 维护：根据用户反馈进行优化和更新。Maintenance and Updating: Update the software according to the users' feedback and 


Members(Roles&Responsibilities&Portion):
5 Members, 3 Full-time Developer, 1 Product Manager, 1(Scrum) Master


Development Planning:

• Requirement Analysis and Design：1 week 

• Development Stage: 3 weeks

• Testing and Optimizing: 1week

• Beta Release: 3 days

• Maintenance and Updating: Ongoing after software launching 


Travel Planner Core Algorithms include：

1. Schedule ：Use ‘ItemTouchHelper’ to drag and order the schedules. Enhance the clarity of the schedule, making the software more user friendly.

2.Positioning Algorithms: Use Google Maps API to locate the schedule and show it through the map.

3.Database Management：Use SQLite as the database management system (DBMS) to store and manage the data of the schedules. SQLite holds its advantage since it is self-contained which means the configuration and installation of SQLite is relatively easy. Therefore, the easy of use it  


Current Status of Travel Planner
1. Adding, deleting and ordering the schedule
2. Local storage of the data 
3. Showing the location of the schedule on the map

Future Plan of Travel Planner
1. Developing schedule reminder
2. Cloud storage of the data
3. Adding multi-language switching
4. Optimizing user interface (UI)

Demo
[YouTube Demo Video]()
点击链接查看TravelPlanner的演示视频。


Environments of the Software Development and Running

Programming Language

• Java


Minimum H/W Requirements

• 处理器：1.2 GHz

• 内存：2 GB RAM

• 存储：500 MB可用空间


Minimum S/W Requirements

• 操作系统：Android 5.0（API level 21）及以上

• 开发工具：Android Studio 4.0及以上


Required Packages

• AndroidX：用于支持最新的Android功能。

• Google Play Services：用于地图功能。

• Gradle：用于项目构建和依赖管理。


Declaration
本项目中使用了以下开源库和工具：

• AndroidX：用于构建和运行应用。

• Google Maps API：用于地图显示和定位功能。

• SQLite：用于本地数据存储。
