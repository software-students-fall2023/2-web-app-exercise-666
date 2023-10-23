# Web Application Exercise

## Product vision statement


### Empowering educators with a seamless course management platform, Albert admin system ensures streamlined access, addition, editing, and search capabilities for comprehensive course and professor information in one unified space.


## User stories

As an administrator, I want to view all courses available for the current semester so that I can manage course offerings effectively.

As an administrator, I want to add new courses to the database so that students can see the latest course offerings for the semester.

As an administrator, I want to modify the details of existing courses to ensure that course information is accurate and up to date.

As an administrator, I want to remove a course from the system so that students do not see courses that are no longer being offered.

As an administrator, I want to search for a specific course using its name or ID to quickly manage or modify course information.

As an administrator, I want to view details about a specific professor to ensure that instructors are correctly associated with their courses.

As an administrator, I want to check the location of a specific course to ensure that room allocations are correctly documented.

As an administrator, I want to assign specific professors to courses so that I can efficiently manage course-instructor pairings for the semester.

As an administrator, I want to set the maximum enrollment capacity for each course to ensure we don't overbook classrooms.

As an administrator, I want to regularly backup the system's data and have the ability to restore it, ensuring data safety and minimizing potential loss in case of system failures.


## Task boards

[Team 666 Task Boards - Sprint 1](https://github.com/orgs/software-students-fall2023/projects/36/views/1)

[Team 666 Task Boards - Sprint 2](https://github.com/orgs/software-students-fall2023/projects/52)

## App Instruction
##1.0 Installation

In order to run this app successfully, please follow the following instructions.

###1.1 Prechecks
1. Check if you have `Python 3.11` installed on your computer, if not, please install or update to `Python 3.11` so you can run this app smoothly.

2. Be advised that there is an `env.example` file in the package you download from the repository, this is an example file to inform you of the format for the `.env` file which had been ignored due to sensitivity. Hence, please creat a file with the name `.env`, with the content `PASSWORD = "you_db_password"`, replace `"you_db_password"` with the specific password which our developer will send to you via private message later on. For now, please prepare this file.

3. Make sure to have your MongoDB, flask, and pymongo ready and active.

###1.2 Installation
1. Install the virtual environment `pipenv` by inputing `pip install pipenv` in your terminal.

2. Activate the virtual environment by inputing `pipenv shell` in your terminal.

3. Download modules and packages of the right version required to run this app. Simply input `pip install -r requirements.txt` in your terminal.

4. Run `Flask` by inputing `flask run` in your terminal.

5. You should now receive a development server given in your terminal, it should look like something similar with `http://127.0.0.1:5000`. Copy and paste this line to a browser, now you should have access to the app!

##2.0 Using the App

Keep in mind that the there are a total of 2 databases in this design, one that stores all the courses' information, and another stores all the professors' information. The course database will be empty by default, while the professor database will hold 10 professors' information. This is by assume all professors in NYU, and you may not edit professors' information. Note that all webpages of this system are with navegation tabs, simply click `Back` to return to the main page.

###2.1 All Courses @NYU
When you click this tab, it automatically shows all courses NYU currently provides, and by default, none to begin with (since the purpose of this Admin System is for admins to add courses).

###2.2 All Professors @NYU
By clicking this tab, it gives the information for all 10 professros stored in the database.

###2.3 Add a course @NYU
This tab allows you to add a new course to the system by entering course ID, course name, professor instructing, and location. Note that if a professor other than the professors in the database was assigned to the new course, the system will tell you that you are not able to add the course since the professor is not from NYU (not in NYU's professor database). Otherwise, the system will return a message informing that the adding is successful.

###2.4 Edit a course @NYU
This tab allows you to edit information of a course that already exists in the database. To do so, enter the course ID to indicate the course you which to edit. An error message will be returned if an invalid course ID was given. Once varified, you are able to edit either course name, instructing professor, location, or both, or all three of the information. However, you are not able to edit the course ID. If you wish to assign the course with a new ID, you can only delete the course which I will introduce later, and add it again as a new course. Once you entered the information you wish to update, click update, then the system will inform you of the successful update (as before, the updated professor can only be professor of NYU as well).

###2.5 Delete a course @NYU
Do this by simply type in the course ID of the course you wish to delete. A message will be returned informing you of this action.

###2.6 Search a course @NYU
Search the course by entering the course ID you wish to search for. Then, all information regarding that course will be returned to the page.
