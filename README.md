# BABY TIMER

---

Baby timer is a simple but useful website that you can use to log your baby's feeds and diapers.
It features user accounts and the ability to add multiple babies.
View all your baby's sleeps and diapers in one list, with notes for each entry on the side.
Easily edit and delete log entries, and with it's responsive design you can take Baby Timer with you no matter what device you're using.

---

## Features

---

- ### Nav bar

  - The responsive naviagtion bar provides quick and easy access to the things you will need most.
  - Here you will find a logs dropdown, the homepage link, and the logout button.
  - On smaller pages the nav bar switches to a dropdown to save space

- ### Sign up / Sign in

  - The sign in and sign up pages are styled neatly, making extensive use of bootstrap templates.
  - New users can create an account that they can use to add babies and entries.
  - User authentication and sign in / sign up is powered by AllAuth

- ### Date / Time Input

  - Users can easily select dates and times for entries (like baby's birthday, or sleep times)
  - This is done using the bootstrap_datepicker_plus widgets, which provide an easy to use gui for date / time selection

- ### Footer

  - The footer is simple, featuring nothing more than the year of creation and a link to the project's GitHub repository.

- ### Home Page

  - Here the user can see all babies registered to them, and add babies by clicking on the green "Add new baby' buttons at the bottom of the page

- ### Logs page

  - Users can see all log entries collated in one list on the logs page.
  - From here users can click/tap on log entries to edit or delete them.

- ### Add entry pages

  - Users can add log entries or babies on a neatly styled form.
  - The form has all fields the entry or baby requires, including a notes text field, which can be used for any additional information.
  - The form features bright submit/delete/cancel buttons for intuitive control.
  - The form does valdation on user input, ensuring all necessary fields are filled and preventing things like a sleep entry ending before it began.

- ### Delete / logout confirmation

  - Anytime the user is about to make a critical change to the site, such as logging out or deleting an entry, a confirmation modal appears.
  - The modal makes it clear to the user what will happen if they continue, so as to prevent accidental deletions or logouts.

- ### Access control

  - Users are require to be logged in to access any of the site's functionality.
  - Users are also unable to view the logs of a baby registered to another user.
  - If this is attempted by modifying the url, the user is redirected to the home page.

## Future Features

---

- ### Additional entry types

  - Despite what some may think, babies do a good bit more than just sleeping and soiling diapers.
  - Functionality for feeds (breast, bottle, and solid foods) can be added easily
  - Functionality for any medication the baby may be taking can be added as well.
  - The models for medication and feeds are already set up, the views and templates need to be configured.

- ### AllAuth email verification

  - As it currently stands site is accessed using a username and password. While this is secure, there is a good bit more that can be done in terms of user accessibility.
  - AllAuth offers built in email verification, forgot password, and password reset functionality.

## Testing

---

- The site was tested for responsiveness on the Firefox and Chrome browsers, using the developer tools that come with the browsers.
- As the site is styled almost exclusively bootstrap, the responsiveness is very good by default.
- Of primary importance is how the site operates on the backend.
  - Extensive manual testing was conducted to ensure the site behaved as intended, with no strange redirects or buttons doing anything other than what they say they will do.
  - Users can add/edit/delete babies/diapers/sleep entries.
  - Users can view all entries registered to a particular baby.
  - Users are redirected if they attempt to access another user's baby or baby's logs via the url.

### Normal (Happy) Flow Manual Testing

  | Feature | Action | Expected result | Actual result |
  | --- | --- | --- | --- |
  | Sign in page | Enter correct credentials and click Sign In | User is logged in and redirected to home page | Works as expected |
  | Sign in page | Enter incorrect credentials | Wrong password/username error appears | Works as expected |
  | Sign in page | Click Sign Up | User is redirected to Sign Up page | Works as expected |
  | Sign Up page | Username, password1, and password 2 entered according to requirements | New User is created, logged in, and redirected to home page | Works as expected |
  | Sign Up page | Passwords not entered identically / fewer than 8 characters | Password mismatch / too short error(s) appear | Works as expected |
  | Sign Up page | Username entered with invalid characters | Invalid username error appears | Works as expected |
  | Sign Up page | Click Sign In | User redirected to Sign In page | Works as expected |
  | Home page - nav bar | Click BabyTimer | User redirected to Home Page | Works as expected |
  | Home page - nav bar | Click Logs dropdown | Dropdown listing all babies and Add a new baby button is displayed | Works as expected |
  | Home page - nav bar | Click on baby name in Logs dropdown | User is redirected to logs page for the specific baby | Works as expected |
  | Home page - nav bar | Click Logout | Logout confirmation modal appears | Works as expected |
  | Home page - logout confirmation modal | Click Cancel | Logout confirmation modal disappears | Works as expected |
  | Home page - logout confirmation modal | Click Logout | User is logged out and redirected to Sign In page | Works as expected |
  | Home page - body | Click Add new baby | User is redirected to add baby page | Works as expected |
  | Home page - body | Click on Baby name in baby listing | User is redirected to baby detail page | Works as expected |
  | Home page - body | Click on logs in baby listing | User is redirected logs page for the specific baby | Works as expected |
  | Home page - body | Click on edit in baby listing | User is redirected edit page for the specific baby | Works as expected |
  | Baby detail page | Click on Edit | User is redirected edit page for the specific baby | Works as expected |
  | Baby detail page | Click on Delete | Delete baby confirmation modal appears | Works as expected |
  | Baby detail page - delete confirmation modal | Click on Delete | Baby is deleted and user is directed to home page | Works as expected |
  | Baby detail page - delete confirmation modal | Click on Cancel | Delete baby confirmation modal disappears | Works as expected |
  | Add baby page | Baby details entered and click save | New baby entry added and user redirected to home page | Works as expected |
  | Add baby page | Click cancel | No baby entry created and user redirected to home page | Works as expected |
  | Date/Time form entry | Click in date\time entry field | Custom Date\Time widget appears | Works as expected |
  | Custom Date/Time widget  - date view | Click date on calendar | Date is selected for form entry | Works as expected |
  | Custom Date/Time widget - date view | Click clock icon below calendar | Time selection view is displayed | Works as expected |
  | Custom Date/Time widget - time view | Click calendar icon above time selection | Date selection view is displayed | Works as expected |
  | Custom Date/Time widget - time view | Adjust time using up/down arrow icons | Time entry is adjusted accordingly | Works as expected |
  | Baby edit page | Initial form values | Form values correspond with saved baby fields | Works as expected |
  | Baby edit page | Edit form field values, click save | Baby is updated with new field data | Works as expected |
  | Baby edit page | Click cancel | Baby is not updated, user redirected to home baby logs view | Works as expected |
  | Baby edit page | Click delete | Delete baby confirmation modal appears | Works as expected |
  | Baby logs page | Click Add Diaper | User is redirected to Add Diaper page | Works as expected |
  | Baby logs page | Click Add Sleep | User is redirected to Add Sleep page | Works as expected |
  | Add Diaper page | Click type dropdown | Diaper Type Dropdown appears | Works as expected |
  | Add Diaper page | Click cancel | User is redirected to Baby logs page | Works as expected |
  | Add Diaper page | Click save | Diaper entry is created, User is redirected to Baby logs page | Works as expected |
  | Baby logs page | Click on Diaper entry | User is redirected to Edit Diaper page | Works as expected |
  | Diaper edit page | Click Save | Diaper entry is updated with Edit form values | Works as expected |
  | Diaper edit page | Click Delete | Delete Diaper confirmation modal appears | Works as expected |
  | Delete Diaper confirmation modal | Click Delete | Diaper is deleted and user is redirected to Baby logs page | Works as expected |
  | Delete Diaper confirmation modal | Click Cancel | Delete Diaper confirmation modal disappears | Works as expected |
  | Diaper Edit page | Click Cancel | User is redirected to Baby logs page | Works as expected |
  | Baby logs page | Click on Sleep entry | User is redirected to Edit Sleep page | Works as expected |
  | Add Sleep page | Click cancel | User is redirected to Baby logs page | Works as expected |
  | Add Sleep page | Click save | Sleep entry is created, User is redirected to Baby logs page | Works as expected |
  | Baby logs page | Click on Sleep entry | User is redirected to Edit Sleep page | Works as expected |
  | Sleep edit page | Click Save | Sleep entry is updated with Edit form values | Works as expected |
  | Sleep edit page | Click Delete | Delete Sleep confirmation modal appears | Works as expected |
  | Delete Sleep confirmation modal | Click Delete | Sleep is deleted and user is redirected to Baby logs page | Works as expected |
  | Delete Sleep confirmation modal | Click Cancel | Delete Sleep confirmation modal disappears | Works as expected |
  | Sleep Edit page | Click Cancel | User is redirected to Baby logs page | Works as expected |
  | Baby logs page | Click Baby name | User is rediredcted to Baby detail page | Works as expected |

### Bad/Exception Flow Manual Testing
  
  | Feature | Action | Expected result | Actual result |
  | --- | --- | --- | --- |
  Unauthorised access protection | User tries to access entry/model instance where they are not the owner | User is redirected to 404 custom page | Works as expected |

- ### BUGS
  
  - [SOLVED] Users can access other user's records by changing pk in url
    - Solved by creating UserAccessMixin which checks to see if the user that the records being requested are registered to is the current session user.
  - [SOLVED] Delete confirmation modal deletes object when cancel button is clicked
    - Solved by moving cancel button outside the delete form heirarchy and adding 
    ```type="submit"```
    to the Delete button attributes.
 - [SOLVED] Custom CSS not loading
   - Solved by defining Static Root dir in settings.py, and letting Whitenoise take care of the rest.

- ### VALIDATOR TESTING
  
  - In testing the HTML and CSS on the main site pages, the only issues were the bootstrap custom classes.
  - The custom python code used in this project is PEP8 compliant.
  - One issue that was tricky to solve was the validator picking up on form elements with multiple name attributes, or aria-describedby attributes that referenced a non-existent element. This was caused by Django adding in these attributes when rendering [BoundFields]("https://docs.djangoproject.com/en/5.1/ref/forms/api/#django.forms.BoundField")

## DEPLOYMENT

---

 -  This [project](https://baby-timer-15aeb8ae861d.herokuapp.com/) is deployed to Heroku
  - Log in to Heroku and create a new application
  - Navigate to the Deply tab and link your github account and repository
  - Set which branch you wish to deploy from (typically "main" or "master")
  - Navigate to the settings tab
  - Add your required config vars:
    -  DATABASE_URL (From ElephantSQL)
    -  DEBUG (Set to True while in production, then False once shipped)
    -  DISABLE_COLLECTSTATIC (Set to 1 while in production, then 0 once shipped)
    -  SECRET-KEY (Your Django secret key - Keep it a secret! New keys can be generated on sites like [Djecrety](https://djecrety.ir/)
  - Navigate back to Deply, scroll down and hit Deply Branch !
 -  The Database is hosted on ElephantSQL
   - Log in / Create and account (linking your GitHub account is a good option)
   - Click "Create New Instance"
   - Give your instance a name (something similar to your repo name, perhaps)
   - Pick a Plan from the dropdown
   - Click "Select Region"
   - Select a region (the closer to you the faster the development will go, in theory)
   - Click Review, and confirm the instance settings.
   - navigate the the instance page, and there you will find your DATABASE URL (From the Heroku config vars, remember?)
   - Set this as a config var in Heroku (with the key "DATABAS_URL", and the actual URL as the value
   - Add the following to your settings.py file in your django project:
```
     DATABASES = {
    "default": dj_database_url.parse(os.environ.get("DATABASE_URL"))
    }
```
  - and remove/comment out the default sqlite setting
And there you have it. By using the requirements.txt file in this repo, you should have everything you need to set up your own PostgreSQL + Django application on Heroku

## KEY TECHNOLOGIES USED

---

This project made good use of the following:

 - Django Framework
 - Django AllAuth
 - Django Whitenoise (for handling static files)
 - Django Bootstrap Datepicker Plus (for the Date/timepickers)
 - Django Widget tweaks (Used extensively in customising the Login / Signup forms
 - Bootstrap Framework (For a tried and tested clean style on the entire project)

## CREDITS

---

 - ### CONTENT
   - The Login / Signup forms were downloaded from [Bootstrap Examples](https://getbootstrap.com/docs/5.1/examples/)
  
- ### MORAL SUPPORT
   - The timing of this project was not ideal, to say the least. Without going into details I want to give a HUGE thanks to my mentor, [Juliia](https://github.com/IuliiaKonovalova),
   - My partner, Nicole, who put up with far more than her fair share of me being a stressed-out sleep-deprived horrible goblin.
   - And of course the Student Support team at CI, for being so understanding and helpful on my extension requests.

 ---

 ---
   
