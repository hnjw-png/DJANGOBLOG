EVENT MANAGEMENT SYSTEM:

## Purpose of the Website

The purpose of the website Events101, is to give a logged-in user access to this personlised events management system. As a logged in user you should be able to a create a new reservation, update your existing reservations, and delete your own reservation. Te website should act a easy way to keep to date with your own reservations, this website is to used to personally create and keep track of your own events like inside a virtual sketchbook. You will be able to see other peoples reservations, but your will not be able to edit them. You can only be able edit your own. This site is way to share your events with your friends and keep a personal plan you can access at a click of  button. These reservations shoud be detailed, and have a clear, date, time and location. Otherwise these will be subject to deletion by the adminstrator, this is stated on the website.
![Skärmbild (243)](https://github.com/hnjw-png/DJANGOBLOG/assets/120515252/ad2ac701-8eca-4ace-b884-6294f72708f0)


# User Experience/User Interface (UX/UI)

## First Time user goals:

When the visitor first visits the reservation planning system:

* The homepage should be clear of what the websites goals are.
* When logged out/not signed up, you will see the nav bar showing, home, register, login. 
* When logging in the nav bar, will show home, create a reseveration, logout.
* The color scheme of purples, blues, whites and black splits up section of the homepage so the user can see the site is a 'Personalised Events Creation Website', there after you have  explanation of how the site works, and then a create reservation button and buttons for already uploaded reservations from all users.
* When the user is logged out and clicks the create reservation button, they will automaticalled redirected to the login/signup page.
* When the user is logged in and clicks the create reservatio button, they will be automatically be directed to the Create A Reservation Form page.
* If a user is logged out and clicks a reservation from the already existing list of reservations, they will be able to see the reservation, but will not be able to create their own reservation, or any other functionality.
* When the user is logged in, and views a reservation that another user added , they will be able to view the reservation and click the button below to create their own reservation..but they still will not be able to edit another user's reservation.
* The site should look good and function on all devices.
* You should be able to log in and log in out with no problem, you will be redirected back to the website after you logout or when you log-in just the same.
* A logged user, has full control over their own events, they can update, delete and add new reservation whenever they please.
* When the create reservation button is clicked by a logged in user, they wll redirected to the reservarion form, and there they will be able to fill out a form and add their reservaion to the database. This will be redirected to their new reservation details.
* In the future we will have a social media account and have the buttons in place, but for now they not functional.
* The website actively explains its functionality to its user. 

## Frequent Visitor goals:

* There should be a place where customers can log in, and logout.
* You can always see upcoming events on the homepage and that is automatically updated.
* Ability to edit, delete or a create new reservation at any time.
* There are many avenues to create a event, in various nav and buttons around the website. 


## Website owner goals:

* The owner of the site can use this site to keep track of events going on in his/her community, business etc, this is with the intention of creating a community of people who creaet and attened each other events. The owners purpose to keep the site up to date, adminsitrate and make sure the reservation posts are details enough, as well as deleting events of which the dates have gone by.
* I have used the superuser function, to create a private admin log in for the website ownwer.
* You can add a reservation as a admin user on the admin panel, this will automatically be redered onto the site.
* This site should behave like a notebook/sketbook for creating events and keeping them up to date.
* The site is intended to make it easier for the owner to keep track of bookings and avoid extra costs of using a third party booking system.
* A future function woul be a function in the admin page that gives the administrator a oppurtunity to decline bookings. Right now theres a statement on the website that if the reservation post is no detailed enough it will be deleted by admin, but in the future things like a avalible dates calender shoud be part of the system.


# Color Scheme

The colour scheme is that of a white background to keep things professional and then pops of colour in the site. The colours will be based upon more natural hues, such as:

* light purple, pink/purple hue, blue, white. Black aand purple, consistent in the homepage, follows same hues in ajoining pages. Same color coordinated with navheader and main header(the brand name event101)
* light blue, white, light purple consistent in the reservation form page and the reservation detail page and home page.
* The sign in/out and sign up page is kept to the basic allauth layout, but in the future I intend to beautify that to match the rest of the site better.

  I researched color combination and hues, to understand how to balance colors, blend them and make whats needed to stand out, stand out clearly. I like the lighter hues of color, which give th site a light friendly feel, which is consistant of the website intention to create a relaxed notebook to create events. 

  The background image is consistent on each page of the site. Its colors match the overall style of the site.

# Typography

I choose the font 'lato' this font has a nice clear look, which is a little bit like clear fancy handwriting, this stands out well and fits the style of the website, which should hae a professional feel.



# Wireframes

* Diagram of site structure.

* This diagram shows the layout of the website, I have planned to use one model called Reservation and connect it to create reservation, register, create reservation, delete, update and login reqired views and urls. This will create a synamic website, which a user or owner can navigate easily throught the website without needing to press back button manually for example.
  ![Skärmbild (177)](https://github.com/hnjw-png/DJANGOBLOG/assets/120515252/40f5a775-d0e5-4021-8d15-71df454c36d7)



* Buttons and nav names

* Here I have layed out how navigation will look on the nav bar and the type of buttons I will use in my application.
  
![Skärmbild (176)](https://github.com/hnjw-png/DJANGOBLOG/assets/120515252/e8133055-034c-41bf-9a13-c26bd4887b69)

* Homepage/reservation list page design

![Skärmbild (179)](https://github.com/hnjw-png/DJANGOBLOG/assets/120515252/f12471d4-c28a-40ef-af8f-c736e99f98aa)


* Reservation detail page
* Here I have layed out how the reservation detail page, with a clear vision of how it will look for each reservation detail. The reservation detail page will automatically update, delete. As well as when a user or a admin adds a reservation it will automatically appear in the reservation page on the homepage.

![Skärmbild (180)](https://github.com/hnjw-png/DJANGOBLOG/assets/120515252/3c5cf1b9-c11d-427e-8bea-02810aa30ec0)


* Reservation form page

* The form page is designed to be in the middle of the screen and should consist of about 5 questions, title, description, time, date, location.
  
![Skärmbild (181)](https://github.com/hnjw-png/DJANGOBLOG/assets/120515252/0206662f-330b-4a3f-8168-dfe9a0fa3083)

## F

## Features

* Update, delete and create reservation functions.

* When a reservation is created you wil automatically redirected back to it.

* When you log in or log out you will be redirected back to the website.

* You can access your own reservation and other peoples reservations on the homepage, but can only edit or delete a reservation made by yourself.

* You can view the website as a non-logged in user, but you will not have access to logged in user pages or functions like delete, edit and create reservations.

* Anyone can join and log in and log out.

* Only the admin can edit any reservation, from the admin page.

*  Events management system 

# Responsiveness:

This website fits to size on all types of devices. From laptop to mobile phone. 

* See responsiveness screenshot: 
![Skärmbild (261)](https://github.com/hnjw-png/DJANGOBLOG/assets/120515252/aafa8420-22c8-40d8-81be-6237f7919724)


## Homepage; nav-bar :

The homepage consists of a clear nav-bar which is responsive in all screen settings. The homepages nav-bar will appear differently according to if your are a logged in user or not.
When you are logged in, you will see the nav-bar names: Home, Create Reservation, Logout. When you are logged out you will see the nav-bar names: Home, Create Reservation, Register, Login.
![Skärmbild (222)](https://github.com/hnjw-png/DJANGOBLOG/assets/120515252/66ac3426-50f0-431d-a567-0bbefeeb9ed4)


## Homepage Header Section :

The homepage header starts with the header title 'Event 101!' This title is decorated with multiple colors to match the overall color scheme of the website and of course the logo in the navbar, this makes the title stand out even more...and shows the purpose of the webpage absolutely directly. The background the concert colors photo which makes the site look very stylish and the color remains the same for the rules purpose statement below the header. 
![Skärmbild (243)](https://github.com/hnjw-png/DJANGOBLOG/assets/120515252/94702d2a-e448-4da0-8ef3-ab978b496ed6)

![Skärmbild (241)](https://github.com/hnjw-png/DJANGOBLOG/assets/120515252/10adc09d-96f9-4dc4-9f1b-30d89cd9ca42)


## Homepage main page (reservations list and create reservations buttons) :

In the main page of the site, you will have a button to create a reservation, whether you're are logged in or not, you will be able to see and click this button. But if you are not logged in you wil be redirected to the login page. If you are, you will be redirected to the reservation form as previously stated. The create reservation is a bit bigger than the list of reservation button, the reason is to make it stand out. 

![Skärmbild (256)](https://github.com/hnjw-png/DJANGOBLOG/assets/120515252/9e5463ca-5293-47c5-89d5-b485c4ebd9fd)

The reservations list buttons are also visable to a user whether they are logged in or not.

When you click the reservation you will be redirected to the reservation detail page, regarding the reservation you clicked. 

The background color is a concert color image to make the main page stand out more, it coincides with the white buttons and black, lato font.

## Footer :

The footer is light blue, to match the rest of the site and head nav bar. There you will see who created the website (me, Holly Nicole), you will also see icons to various social media website, right now they are inactive due to no social media account for the reservation management system.

![Skärmbild (215)](https://github.com/hnjw-png/DJANGOBLOG/assets/120515252/c199e6bc-6ef8-499a-92b3-2c9699dae1c0)


### Reservation Detail Page:

When you add a new reservation, it will render on the reservation details page, the way to access this page is to click the reservation you want to view on the homepage(reservation list). Here whilst you are logged in and accessing on of your own reservation, you will see the buttons, update reservation, delete reservation  and create reservation.
![Skärmbild (240)](https://github.com/hnjw-png/DJANGOBLOG/assets/120515252/efdf49f5-c857-4de9-a06e-3e46e3e95208)
When you are logged out, you can click any reservation from the reservation list(homepage)and you will be able to view the reservation details on the reservation detail view, but instead of seeing all the buttons as you would when your logged in, you will see the button log in below the reservation details.

The nar bar appears the same as in the homepage, due to  there being all the correct templates in place, including base.html.


### Reservation form page :
The reservation form will render when you click any of the create reservation buttons on the website, whilst logged in. As well as rendering when you click the create a reservation nav button, als when logged in. The reservation form requires all fields to be filled out correctly to add the event to the homepage(database) There will be a add/submit button at the bottom of the form and if you have mis-filled in something it will inform you, it also has a default setting so the user knows how to fill out the date and time in the form.
![Skärmbild (225)](https://github.com/hnjw-png/DJANGOBLOG/assets/120515252/7ab6df85-a230-4c64-acab-95f7980fc9c5)

Here you have a statement about the rules and the purpose of the site more specifically. This is a friendly notice to users to keep things detailed, otherwise admin will delete the post.

![Skärmbild (260)](https://github.com/hnjw-png/DJANGOBLOG/assets/120515252/8e6ba51e-c187-4327-98fe-e18aed59237a)


## Update and update button :

When you are logged in and you have selected your own reservation, the update button will appear and you will then be redirected to the Reservation form, except it will have the details of the reservation you want to edit inside it already. Then the user is free to edit the reservation then add/save it again. And thereafter they will be redirected so they can see their updates reservation.

![Skärmbild (257)](https://github.com/hnjw-png/DJANGOBLOG/assets/120515252/15d15399-3df9-409f-8294-cd6a80325090)



## Delete and delete button :

When you are logged in and you have selected your own reservation, the delete button will appear and once you press the button your reservation will be automatically deleted. A way to improve thisin the future is the have https response message appear asking if the user is sure they want to delete.
![Skärmbild (258)](https://github.com/hnjw-png/DJANGOBLOG/assets/120515252/63d6bc62-f41b-4d1a-b5eb-dd2396b09756)

## Create reservation button on reservation details page :

This button beahaves the same as the create reservation button on the homepage, you are directed to the reservation form page.(as long as you are logged in). When you hover over any button it will turn blue. You find mulitple rservation buttons through the site including the nav bar.

![Skärmbild (259)](https://github.com/hnjw-png/DJANGOBLOG/assets/120515252/7db8f9ad-3fb3-4532-b7c3-d91116866606)



## Log in, log out, sign up:

Here the automatic allauth setting has been implemented, so that we get a automatic sign in, sign out and register page, this is a basic page with redirects the user back to the website after log in or log out. To improve the system i would add  email verification system but fow now this is disabled.



## Admin page:

The admin page have all options to delete, edit and add all reservations. It uses summernote settings.
![Skärmbild (194)](https://github.com/hnjw-png/DJANGOBLOG/assets/120515252/b3c10a36-7b1d-4fa9-ba6f-e18d56f81182)
![Skärmbild (195)](https://github.com/hnjw-png/DJANGOBLOG/assets/120515252/2cdcd59b-e23f-4447-9e7e-fb92e8bd9c9f)
![Skärmbild (196)](https://github.com/hnjw-png/DJANGOBLOG/assets/120515252/ca4ac186-9a32-44a9-8477-d5eff77b3675)

# Possible Future Features:

* Interactive social account section.
* email verification.
* Image upload feature
* have a calender attached to the date in the form.
* change the time settings in the form.
* add a add clients button for logged on users.

# Techologies used

Languages used:

* HTML
* CSS
* PYTHON
* DJANGO

# Applications used:

* Google Fonts fonts downloaded from Google Fonts.
* Fontawesome icons downloaded from Font Awesome.com.
* GitHub to store the projects code.
* Gitpages to deploy the site.
* heroku to deploy app
* Chrome Developer Tools for layout and responsive testing.
* favICO.com for creating favicon.
* W3 Validator to test html and css code.
* elephantsQl/postgre for database
* cloudinary for storage

## Testing

### Django Testing

I am testing my code using the testing function in django, i am writing the code using the testcase and testing the forms.py, models.py, views.py. I am testing to check for example the title has to be filled in the form. When I performed django testing I used the sqlite database, and then swapped it back to the database-url when I finished testing. This time I didnt have enough time to test fully with django, but this is something I intend to do to improve the security and reliability of my site in the future.


### Manual Testing

* I have tested the site as a logged in user who is the admin and everything works as intended. All functions active.
* I have tested the site with a test login to see the website behaves as expected when you are a logged in user, who is not a admin.
* I have tested the website while being logged out, and everything works as expected. You see the log in button if you click a events details for example. And you cannot create edit or delete if you are not a logged in user.
* Log in page appears when log in button is clicked.
* When create reservation button is clicked, when the user is not logged in, it redirects to log in page.
* After you are logged in you are automatically redirected back to the website.
* When you log out you are redirected back ot the website as well.
* Update and delete button work as expected. Though when deleting it could be improved by having a http respinse message, asking if you are sure you want to delete.
* Admin set up correctly, and when a reservation is added through admin, it automatically appears in the website.
* Admin can edit and delete anyone's post from admin page.
* A logging user can edit and delete and create its own reservations.
* You can register a new account as a new user.
* The site is interactive on all devices and changes accordinly, including chnages to the nav bar when the screen is smaller, the bar appears on the right.
* Each reservation appears on the site whether from admin or direvtly on the website.




# Lighthouse: 
![Skärmbild (254)](https://github.com/hnjw-png/DJANGOBLOG/assets/120515252/b231b79c-c6cd-4d7f-b55a-97f30aaf07b6)

![Skärmbild (253)](https://github.com/hnjw-png/DJANGOBLOG/assets/120515252/47cc9b9c-9bd4-4e11-b8c7-136de617019f)

![Skärmbild (252)](https://github.com/hnjw-png/DJANGOBLOG/assets/120515252/f68ae964-a325-4343-ae0f-87652eecce92)

![Skärmbild (251)](https://github.com/hnjw-png/DJANGOBLOG/assets/120515252/293736f0-2dff-40d6-8181-3a82afd0f8ae)


# CSS and HTML Validator:
* CSS Validator for Home page, and ajoinging pages :
![Skärmbild (231)](https://github.com/hnjw-png/DJANGOBLOG/assets/120515252/e0cd9d8e-b103-4ee9-9ac8-c86ac4444168)
* CSS validator for other pages.
![Skärmbild (232)](https://github.com/hnjw-png/DJANGOBLOG/assets/120515252/2aa43a57-dc32-43ec-9dcf-390e10104bc8)
![Skärmbild (233)](https://github.com/hnjw-png/DJANGOBLOG/assets/120515252/500c880b-35bd-47e2-9f77-0d513df0212c)
![Skärmbild (234)](https://github.com/hnjw-png/DJANGOBLOG/assets/120515252/4f671f76-22bf-478a-baee-556d5687f794)

 ## HTML Checker
![Skärmbild (248)](https://github.com/hnjw-png/DJANGOBLOG/assets/120515252/e2f19328-f4db-44d8-8089-34039a654b3b)
![Skärmbild (246)](https://github.com/hnjw-png/DJANGOBLOG/assets/120515252/331dcb46-a9b4-48b1-8cb1-f9cd93fb1697)
![Skärmbild (245)](https://github.com/hnjw-png/DJANGOBLOG/assets/120515252/3b8ba3e7-8a82-4b41-90b7-16bd1e34b9ac)

* Below one error, as I cannot find the lagging a slash. And the lang is already set to eng. No other pages throw this error. 

![Skärmbild (249)](https://github.com/hnjw-png/DJANGOBLOG/assets/120515252/6ce0e23a-6289-4256-b2be-9ef366b1795b)


# Bug fixes

* A fix would be to add a  http response when you hit the delete button, to warn the user they are deleting their reservation.

* Add email verification, so users can reaccess their accouns if passowrd is forgotten, through verification process.

* Add easier functionality to date and time fields.

# Deployment:

* I have deployed my application to heroku:
* I began my project my pre-deploying my project to heroku, I created a app in heroku called rest, and I then conencted my heroku app to my githug repository 'djangoblog'. 
* I have make sure my heroku link is in my allowed hosts, in my settings.py.
* I have added a requirements.txt file and a Procfile. As well as a gitignore file.
* I have added my cloudinary, postgres configur vars.
* I have added my secret key to configur vars.
* I have added my cloudinary, postgres and configur vars into my github repository. (also added collect static < 1)
* In order to deploy my website to heroku, I have set in settings.py to DEBUG = 'False'
* In order for the deployment to work I have made sure my images are being sourced from cloudinary.
* I have removed the collect static > 1 from heroku config vars, so the static files and css appear on the heroku deployed app.

* Here is my deployed heroku app link : https://rest-1418ac04f509.herokuapp.com/

* This is my address to my github : https://8000-hnjwpng-djangoblog-ohrky9dltau.ws-eu106.gitpod.io/
* If you wish to see my project in gitpod, please set debug to TRUE. To see correctly. Gitpod repository is shared.

# sources

* background image = https://pixabay.com/photos/concert-confetti-party-event-club-2527495/
a free to use commericial image from pixbay.

* homepage image = https://pixabay.com/photos/people-happy-happy-people-joy-1230872/
a free to use image from pixbay.

* code institute learning content.

* staticoverflow for tips.

* base.html template code institute- editted  by me.

* base nav-bar setting from code institute project- editted by me.
