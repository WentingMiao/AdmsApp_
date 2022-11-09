# AdmsApp_
Dynamic Administration Web Application For student organization 

**Project Introduction**:
![500](https://s2.loli.net/2022/11/09/wbA2To4Cy7iMqKG.png)

The system contains the following four part: 
Activities Management, Material Management, Member Management, and Admin Authority.
Each part corresponding to different functions:

1. Activities Management have application creation, check personal application and pubic application,  register activity and view the Calenda which shows the overall information about activities.
![500](https://s2.loli.net/2022/11/09/P1VDKZW5A24OgjG.png)
![500](https://s2.loli.net/2022/11/09/NT2H1DlBpizKwPG.png)

![500](https://s2.loli.net/2022/11/09/riCuk7wtG6RoPVB.png)
![500](https://s2.loli.net/2022/11/09/iBZhQGg29quFnfO.png)


2. Material Managment part contains Profile Management and Gallery:
![500](https://s2.loli.net/2022/11/09/vaziVEN4wrxOF3X.png)

3. Member Management can check the members in the system and do some CURD actions.
![500](https://s2.loli.net/2022/11/09/1ZRDJ7AhrBzE4LO.png)

4. Admin Authority is designed for administrators to manage the whole system and staff which nomal users don't have permission to access.
![500](https://s2.loli.net/2022/11/09/kjbMGUe1f4vY6Fl.png)


**Environment preparation**

If you already have relevant versions of Python and Django installed on
your device, you can skip this section.
1. Install Python and pip
2. Install Django
Go to the official website and download the tar.gz type file in the folder of the
python system file. https://www.djangoproject.com/download/
Unzip the downloaded file and run python setup.py install in the folder.
In order to make sure Django is installed successfully in our device, we can
open the windows terminal(Ctrl+R) and use the command ```
python -m django –version```
to check.

**Install and run the project**:
1. download the project from this repository
2. Install the required packages: 
```pip install -r requirement.txt```
3. Load the default data: 
```python manage.py loaddata data.json```
4. Create a superuser which will be used later: 
`python manage.py createsuperuse`
5. Make migrations and run the server:
`python manage.py makemigrations`
`python manage.py migrate`
`python manage.py runserver`
6. Open the browser and go to the website: http://127.0.0.1:8000/

