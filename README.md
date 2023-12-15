# university_partnerships
This is a project for the service learning seminar of the university CAU in Kiel, Germany.

### Idea

Partner universities of any chosen university are sometimes very hard to find. Project between these universities are split into many different sub-pages of content, faculties, etc. This project wants to solve this problem by creating an environment visualizing different universities, their partner universities and the project they plan/have with each other. 

### Implementation

To get the data needed, the program uses a web crawler searching for keywords and adding the information to the intern database (manually adding data is also possible). The UI consists of a large world map showing the current universities the crawler found.

### Presentation

https://prezi.com/view/ArjuHGhTMEkvHujykSAK/

## Concept

### Install

1. install python >= 3.9
2. clone the repository
3. cd into `back_end/university_partnerships`
4. run `pip install -r requirements.txt`
5. merge and create the db with `sh setupdb.sh` or `python manage.py migrate`
6. run server with `sh startServer.sh` or `python manage.py runserver`

### Back-end

We use django for the back-end.

#### Database

We use a simple database structure to ensure maximal speed for db request through api or direct access
1. universities
   1. university_info
   2. partner_universities
2. projects
   1. university 1
   2. university 2
   3. project_info

#### API

The application allowes to add new enities through the default admin gui brought by django, but also with a rest api
(keep in mind that all data is given in application/json format)
you can post on all API-addresses to add a project/university

##### Project API
 - `{site_url}/api/allProject` - returns all projects in db
 - `{site_url}/api/getProjectById` - returns a project based on given id
 - `{site_url}/api/getProjectByName` - returns all project based on given name

##### University API
 - `{site_url}/api/allUniversity` - returns all universities in db
 - `{site_url}/api/getUniversityById` - returns university based on given id
 - `{site_url}/api/getUniversityByName` - returns all universities based on given name

#### more

TODO: