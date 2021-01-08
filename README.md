# [Pearl](https://sctlcd-pearl2.herokuapp.com/)

<img src="https://github.com/sctlcd/pearl/blob/master/design/mockups.png" alt="Pearl" width="800">
<dl>
<dd>Do you like creative activities, arts and crafts and making things by yourself with creativity, happiness and your own two hands ?</dd>
<dd>Then this website is a <strong>pearl</strong> to you!</dd>
<dd>At Pearl's you can <strong>purchase arts and crafts supplies</strong> and <strong>sharing customers' work of art</strong> in the meantime as <strong>getting inspiration</strong> from other customers' creative work in the <strong>gallery</strong>.</dd>

[Let me show you!](https://sctlcd-pearl2.herokuapp.com/)
<br />
<br />
**Warning**
<br />
Because of an issue relative to submitting a form with an uploaded image in my deployed environment I did set up the image field in the gallery model as not required for limiting the impact of the issue which has been solved just before my project deadline submission. I set up initially the gallery image field as required. I will set it back to required in the future.

---

# Table of Contents <a name="TableOfContents"></a>

1. [About](#About)
	- [Why this project?](#WhyThisProject)

1. [UX](#UX)

	- [User Stories](#UserStories)
	- [Design](#Design)
		- [Framework](#Framework)
		- [Color Scheme](#ColorScheme)
		- [Icons](#Icons)
		- [Typography](#Typography)

2. [Features](#Features)

	- [Existing Features](#ExistingFeatures)

3. [Technologies Used](#TechnologiesUsed)

	- [Front-End Technologies](#Front-end-technologies)
  - [Back-End Technologies](#Back-end-technologies)

4. [Relational scheme](#RelationalScheme)

5. [Testing](#Testing)

	- [User story validation](#UserStoryValidation)
	- [Layout responsiveness](#LayoutResponsiveness)
	- [Compatibility](#Compatibility)
	- [Testing left](#Testingleft)
	- [Validators](#Validators)
	- [Known Issues](#KnownIssues)

6. [Deployment](#Deployment)

	- [Deployment – Live website](#Deploymentlivewebsite)
	- [Deployment – Run locally](#Deploymentrunlocally)

7. [Credits](#Credits)

	- [Content](#Content)
	- [Media](#Media)
	- [Code](#Code)
	- [Acknowledgements](#Acknowledgements)

---

## About <a name="About"></a>

The primary purpose of Pearl is to purchase arts and crafts supplies. Its secondary purpose is to share customers' work of art in the meantime as getting inspiration from other customers' creative work in the gallery. And this anytime, anywhere as this application is available on various devices as desktops, tablets and mobile.

Back to [top](#TableOfContents)

---

### Why this project? <a name="WhyThisProject"></a>

This project is part of my [Code Institute](https://codeinstitute.net/) Full Stack Software Development studies, the **Full Stack Frameworks With Django** module. The objective of this milestone project is building a full-stack site based around business logic used to control a centrally-owned dataset, setting up an authentication mechanism and provide paid access to the site's data and/or other activities based on the dataset, such as the purchase of a product/service.

My modern responsive e-commerce arts and crafts supplies site is built using HTML, CSS, Material Design for Bootstrap, JavaScript, jQuery, Django, Python, PostgreSQL.

Back to [top](#TableOfContents)

---

## UX  <a name="UX"></a>

### User Stories <a name="UserStories"></a>

"***As a user, I want to _____***"

:heavy_check_mark: successfully implemented
:x: not yet implemented

- :heavy_check_mark: view the site from any device (mobile, tablet, desktop).
- :heavy_check_mark: be able to log in.
- :heavy_check_mark: be able to log out.
- :heavy_check_mark: be able to register.
- :heavy_check_mark: filter and search amongst all products.
- :heavy_check_mark: view all products.
- :heavy_check_mark: view a product details.
- :heavy_check_mark: add products with an image as an admin.
- :heavy_check_mark: add products without an image as an admin.
- :heavy_check_mark: edit products with an image as an admin.
- :heavy_check_mark: edit products without an image as an admin.
- :heavy_check_mark: delete products as an admin.
- :heavy_check_mark: view gallery images.
- :heavy_check_mark: view a gallery image.
- :heavy_check_mark: share a gallery image as a logged in user.
- :heavy_check_mark: add a gallery item with an image as an admin.
- :heavy_check_mark: add a gallery item without an image as an admin.
- :heavy_check_mark: edit a gallery item with an image as an admin.
- :heavy_check_mark: edit a gallery item without an image as an admin.
- :heavy_check_mark: delete a gallery image as an admin.
- :heavy_check_mark: approved a gallery image as an admin.
- :heavy_check_mark: view my profile as a logged in user.
- :heavy_check_mark: update my profile as a logged in user.
- :heavy_check_mark: update my profile as logged in user.
- :heavy_check_mark: add products to my bag.
- :heavy_check_mark: checkout my order.
- :heavy_check_mark: send a contact request.


Back to [top](#TableOfContents)

---

### Design <a name="Design"></a>

I did choose a warm, joyful and energetic orange ![#fc9601](https://placehold.it/15/fc9601/fc9601) `#fc9601` combined with sober and reliable colors ranging between off-white ![#fafafa](https://placehold.it/15/fafafa/fafafa) `#fafafa` and black ![#000](https://placehold.it/15/000/000) `#000` with shades of grey (more color details in [Color Scheme](#ColorScheme) section).
<br />
I first choose my [logo](https://www.flaticon.com/free-icon/craft_3079199) from Flaticon(https://www.flaticon.com) which I customized in [Pearl logo](https://github.com/sctlcd/pearl/blob/master/media/logo/pearl-min.png).
<br />
Then I selected [images](https://github.com/sctlcd/pearl/tree/master/media) relative to arts and crafts and creative activities which fit well in my color scheme and in the space allocated.
<br />
I finally selected the main home page image, a [fire spin](https://github.com/sctlcd/pearl/blob/master/media/home/hero_image/hero-image-background-min.jpg) picture, as I found it absolutely stunning, very eye-catchy and intriguing. Catching customers/visitors' attention and raising their interest and curiosity are I believe a good recipe for new visitors as much as for regular customers of an e-commerce site.  
<br />
I decided to implement a customers' gallery and offering the possibility to share your own piece of art while getting inspiration from other customers' art work. I believe this feature is a very interesting one as it involves the customers/makes the customers participate in the website building. They are actor, in a way, of the gallery page building and its content.  

Back to [top](#TableOfContents)

---

#### Framework <a name="Framework"></a>

- [Material Design for Bootstrap 4.19.1](https://mdbootstrap.com/)
	- I really like the modern and clean layout of Material Design and the ease of use and standards of Bootstrap so I wanted to give a try and getting familiar with Material Design for Bootstrap
- [jQuery 3.5.1](https://jquery.com/)
	- For the purpose of keeping the JavaScript minimal
- [Django 3.1.1](https://www.djangoproject.com/)

Back to [top](#TableOfContents)

---

#### Color Scheme <a name="ColorScheme"></a>

- ![#fc9601](https://placehold.it/15/fc9601/fc9601) `#fc9601`
- ![#6a6a6e](https://placehold.it/15/6a6a6e/6a6a6e) `#6a6a6e`
- ![#fafafa](https://placehold.it/15/fafafa/fafafa) `#fafafa`
- ![#efefef](https://placehold.it/15/efefef/efefef) `#efefef`
- ![#6c757d](https://placehold.it/15/6c757d/6c757d) `#6c757d`
- ![#d8d8d8](https://placehold.it/15/d8d8d8/d8d8d8) `#d8d8d8`
- ![#d6d4d4](https://placehold.it/15/d6d4d4/d6d4d4) `#d6d4d4`
- ![#dee2e6](https://placehold.it/15/dee2e6/dee2e6) `#dee2e6`
- ![#000](https://placehold.it/15/000/000) `#000`

Back to [top](#TableOfContents)

---

#### Icons <a name="Icons"></a>

- [Font Awesome 5.14.0](https://fontawesome.com/)
	- It fits my needs for this project

Back to [top](#TableOfContents)

---

#### Typography <a name="Typography"></a>

- [Google Fonts](https://fonts.google.com/) were used across the site:
	- [Open Sans](https://fonts.google.com/specimen/Open+Sans) - default font
	- [Smythe](https://fonts.google.com/specimen/Smythe) - showcase section on home page
	- [Crafty Girls](https://fonts.google.com/specimen/Crafty+Girls) - customer review section on home page

Back to [top](#TableOfContents)

---

## Features <a name="Features"></a>

### Existing Features <a name="ExistingFeatures"></a>

#####  Navigation bar

- A top navbar with the logo and the name of the website, menu items and dropdown menu items : Gallery, My Account, Basket and a product search bar.
- a navbar with the products menu items and dropdown menu items

##### Footer

- Social medias to get connected
- 3 sections : Company presentation, links to other pages of the website (not implemented), contact section with a contact button redirecting to the contact page.
- copyright mention with my name and my gitbhub repository

Back to [top](#TableOfContents)

---

##### Home page

- 6 sections: Shop now, website order feature offered, target activities, customer reviews, Share your work of art, Stay tune (newsletter subscription not implemented, for presentation purpose)

##### Products page

- A Product collection presented in a "mosaic format"

##### Products details page

- A page with product details: name, description, price, rating, product image

Back to [top](#TableOfContents)

---

##### Products management page

- Add Product page with add product form
- Edit Product page with edit product form

##### Gallery page

- A gallery of customers' work of art

##### Share gallery page

- A share gallery item form can be submitted

##### Gallery management page

- Add Gallery item page with add gallery item form
- EditGallery item page with edit gallery item form

Back to [top](#TableOfContents)

---

##### Profile page

- To view and update your profile


##### Shopping bag page

- To view and adjust your shopping bag

##### Checkout page

- To checkout orders

Back to [top](#TableOfContents)

---

##### No result found page

- Humoristic picture and message letting know the user no result have been found matching with his/her search.
- Link redirecting to Products Home page

Back to [top](#TableOfContents)

---

##### Error pages

- 404 page - No page found
	- Link redirecting to Products Home page  
- 500 page - Internal server error
	- Link redirecting to Products Home page  


##### Pearl Admin Portal

- I customise the Default Django Administration in [pearl/urls.py](https://github.com/sctlcd/pearl/blob/master/pearl/urls.py):
```
admin.site.site_header = 'Pearl Administration'
admin.site.site_title = 'Pearl Admin Portal'
admin.site.index_title = 'Welcome to Pearl Admin Portal'
admin.site.site_url = '/admin'
```

- I changed the time zone to match with the physical location of Pearl shop in New Orleans in USA and the format of time and date in [pearl/settings.py](https://github.com/sctlcd/pearl/blob/master/pearl/settings.py)
```
# Time Zone in New Orleans, Louisiana, USA : CST — Central Standard Time
# corresponding to America/Chicago according to
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
TIME_ZONE = 'America/Chicago'
USE_I18N = True
USE_L10N = False
USE_TZ = True
DATETIME_FORMAT = "Y-m-d H:i"
```

Back to [top](#TableOfContents)

---

## Technologies Used <a name="TechnologiesUsed"></a>

- [GitHub](https://github.com/) - Used as remote storage of my code online.
- [Atom](https://atom.io/) - Used as a local IDE.
- [Compressjpeg](https://compressjpeg.com/) - Used to compress images for loading faster
- [Techsini](https://techsini.com/multi-mockup/) - Used to generate multi-device website mockup
- [Ngrok 2.3.35](https://ngrok.com/) - Expose a local web server to the public internet over secure tunnels

Back to [top](#TableOfContents)

---

### Front-End Technologies <a name="Front-end-technologies"></a>

- [HTML](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5) - Used as the base for markup text.
- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS3) - Used as the base for cascading styles.
- [Material Design for Bootstrap 4.19.1](https://mdbootstrap.com/) - used as a front-end framework for building responsive, mobile-first websites and apps
- [JavaScript](https://www.javascript.com/) - Used for user interactions.
- [jQuery 3.5.1](https://jquery.com/) - JavaScript library, used to simplify some of the DOM manipulations.
- [Stripe API](https://stripe.com/docs/api?lang=python) - Used to make secured payments
- [Amazon AWS S3](https://aws.amazon.com/) - Used to store staticfiles and media folders and files.

Back to [top](#TableOfContents)

---

### Back-End Technologies <a name="Back-end-technologies"></a>

- [Python 3.8](https://www.python.org/) - Used as the back-end programming language.
- [Django 3.1.1](https://www.djangoproject.com/) - Used as Python web framework.
- [Heroku](https://www.heroku.com/) - Used for app hosting.
- [PostgreSQL](https://www.postgresql.org/) - Used as relational SQL database plugin via Heroku.

Back to [top](#TableOfContents)

---

## Relational scheme <a name="RelationalScheme"></a>

The Relational scheme diagram can be found [here](https://github.com/sctlcd/pearl/blob/master/design/relational-scheme.png)

Pear database table details:

**category**
```
_id PK int
name NULL varchar
friendly_name NULL varchar
```

**product**
```
_id PK int
sku NULL varchar
name varchar
description text
price money
category NULL int FK >- category._id
rating NULL decimal
image NULL file
created_at date
updated_at NULL date
```

**user_account**
```
_id PK int
email email
user_name varchar
password varchar
first_name NULL varchar
last_name NULL varchar
is_superuser boolean
is_staff boolean
is_active boolean
```

**user_profile**
```
_id PK int
user int FK - user_account._id
default_phone_number NULL varchar
default_street_address1 NULL varchar
default_street_address2 NULL varchar
default_town_or_city NULL varchar
default_postcode NULL varchar
default_county NULL varchar
default_country NULL country
```

**order**
```
_id PK int
order_number varchar
user_profile NULL int FK >- user_profile._id
full_name varchar
email email
phone_number varchar
country country
postcode NULL varchar
town_or_city varchar
street_address1 varchar
street_address2 NULL varchar
county NULL varchar
created_at date
updated_at NULL date
delivery_cost money
order_total money
grand_total money
original_bag text
stripe_pid varchar
```

**order_line_item**
```
order int FK >- order._id
product int FK >- product._id
quantity int
lineitem_total money
```

**contact**
```
_id PK int
first_name varchar(254)
last_name varchar(254)
email email
message text
date date
```

**gallery**
```
_id PK int(254) FK >- user_account._id
user_name varchar
email email
author_name varchar
gallery_category NULL int FK >- gallery_category._id
image NULL file
note NULL varchar
created_at date
updated_at NULL date
is_approved boolean
```

**gallery_category**
```
_id PK int
name NULL varchar
friendly_name NULL varchar
```

## Testing <a name="Testing"></a>

### User story validation <a name="UserStoryValidation"></a>

:heavy_check_mark: *as expected*
:x: *not as expected*

- :heavy_check_mark: view the site from any device (mobile, tablet, desktop).
- :heavy_check_mark: be able to log in.
- :heavy_check_mark: be able to log out.
- :heavy_check_mark: be able to register.
- :heavy_check_mark: filter and search amongst all products.
- :heavy_check_mark: view all products.
- :heavy_check_mark: view a product details.
- :heavy_check_mark: add products with an image as an admin.
- :heavy_check_mark: add products without an image as an admin.
- :heavy_check_mark: edit products with an image as an admin.
- :heavy_check_mark: edit products without an image as an admin.
- :heavy_check_mark: delete products as an admin.
- :heavy_check_mark: view gallery images.
- :heavy_check_mark: view a gallery image.
- :heavy_check_mark: share a gallery image as a logged in user.
- :heavy_check_mark: add a gallery item with an image as an admin.
- :heavy_check_mark: add a gallery item without an image as an admin.
- :heavy_check_mark: edit a gallery item with an image as an admin.
- :heavy_check_mark: edit a gallery item without an image as an admin.
- :heavy_check_mark: delete a gallery image as an admin.
- :heavy_check_mark: approved a gallery image as an admin.
- :heavy_check_mark: view my profile as a logged in user.
- :heavy_check_mark: update my profile as a logged in user.
- :heavy_check_mark: update my profile as logged in user.
- :heavy_check_mark: add products to my bag.
- :heavy_check_mark: checkout my order.
- :heavy_check_mark: send a contact request.

---

### Layout responsiveness <a name="LayoutResponsiveness"></a>

|  | Moto G4 | Galaxy S5 | Pixel 2 | Pixel 2 XL | iPhone 5/SE | iPhone 6/7/8 | iPhone 6/7/8 Plus | iPhone X | Surface Duo | iPad | iPad Pro | Desktop 1024px | Desktop > 1200px |
| :--- | :--- | :---| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| website is responsive <= 767 px | Good | Good | Good | Good | Good | Good | Good | Good | Good | Good | n/a | n/a | n/a | n/a |
| website is responsive >= 768 px | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | Good | Good | Good | Good |
|**bag app** |
| Navigation bar: logo / links / search | Good |  | Good  |  |  | Good |  | Good |  | Good |  | Good |  |
| Content page: Images / icons text / links / buttons / text |  | Good |   | Good |  | Good |  | Good |  | Good |  | Good |  |
| Footer: text / links | Good |  |  Good |  | Good |  | Good |  | Good |  | Good |  | Good |
|**checkout app** |
| Navigation bar: logo / links / search | Good |  | Good  |  | Good |  | Good |  | Good |  | Good |  | Good |
| Content page: Images / icons text / links / buttons / text | Good |  |  Good |  | Good |  | Good |  | Good |  | Good |  | Good |
| Footer: text / links | Good |  | Good  |  | Good |  | Good |  | Good |  | Good |  | Good |
|**Contact app** |
| Navigation bar: logo / links / search | Good |  | Good  |  | Good |  | Good |  | Good |  | Good |  | Good |
| Content page: Images / icons text / links / buttons / text |  | Good |   | Good |  | Good |  | Good |  | Good |  | Good |  |
| Footer: text / links | Good |  |  Good | Good |  | Good |  | Good |  | Good |  |Good  |  |
|**Gallery app** |
| Navigation bar: logo / links / search | Good |  | Good  |  | Good |  | Good |  | Good |  | Good |  | Good |
| Content page: Images / icons text / links / buttons / text |  | Good |   | Good |  | Good |  | Good |  | Good |  | Good |  |
| Footer: text / links | Good |  |  Good | Good |  | Good |  | Good |  | Good |  |Good  |  |
|**Home app** |
| Navigation bar: logo / links / search | Good |  | Good  |  | Good |  | Good |  | Good |  | Good |  | Good |
| Content page: Images / icons text / links / buttons / text |  | Good |   | Good |  | Good |  | Good |  | Good |  | Good |  |
| Footer: text / links | Good |  |  Good | Good |  | Good |  | Good |  | Good |  |Good  |  |
|**Product app** |
| Navigation bar: logo / links / search | Good |  | Good  |  | Good |  | Good |  | Good |  | Good |  | Good |
| Content page: Images / icons text / links / buttons / text |  | Good |   | Good |  | Good |  | Good |  | Good |  | Good |  |
| Footer: text / links | Good |  |  Good | Good |  | Good |  | Good |  | Good |  |Good  |  |
|**Profile app** |
| Navigation bar: logo / links / search | Good |  | Good  |  | Good |  | Good |  | Good |  | Good |  | Good |
| Content page: Images / icons text / links / buttons / text |  | Good |   | Good |  | Good |  | Good |  | Good |  | Good |  |
| Footer: text / links | Good |  |  Good | Good |  | Good |  | Good |  | Good |  |Good  |  |

Back to [top](#TableOfContents)

---

### Compatibility <a name="Compatibility"></a>

I tested the website across the 6 main browsers in both desktop and mobile configuration to ensure a large number of users can use it successfully.

- Chrome v.87.0
- Edge v.87.0
- Firefox v.84.0
- Safari v.5.1.7 for Windows 10
- Opera v.73.0
- Internet Explorer v.11

|All pages | Chrome | Edge | Firefox | Safari | Opera | IE |
| :--- | :--- | :---| :--- | :--- | :--- | :--- |
| Expected appearance | Good | Fair | Good | Poor | Good | Poor |
| Expected responsiveness | Good | Good | Good | Poor | Good | Poor |

- IE: Some CSS3 properties and HTML5 elements are not fully supported

- Safari v.5.1.7: It’s an outdated version and lacks many of the features present in the latest version of Safari. The last version of Safari for Windows was released on May 9, 2012.

Back to [top](#TableOfContents)

---

### Testing left <a name="Testingleft"></a>

- There is no way to install the latest version of the Safari browser on Windows 10 as Apple stopped developing Safari for Windows operating system long ago.
For testing this website on the latest version of Safari, I will have to install the newest version of macOS on Windows 10 in a virtual machine.

Back to [top](#TableOfContents)

---

### Validators <a name="Validators"></a>

**HTML**
- [W3C HTML Validator](https://validator.w3.org/)
	- Django template syntax not understood
	- No error

**CSS**
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
	- No error

**Javascript**
- [Javascript Validator](https://jshint.com/)
	- No error

**Chrome DevTools**
- [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools/)
	- Console Navigating through the Website rendered no critical fails/errors in the console that were necessary to fix.

**Python**
- [Python validator](http://pep8online.com/)
 - No error

Back to [top](#TableOfContents)

---

### Known Issues <a name="KnownIssues"></a>

- top/down page visible when scroll down then scroll up to window scroll = 0 when mobile menu is collapse
- Set image gallery back to required.
- Create products and gallery sub-directories in media folder containing respectively product images and gallery images.

Back to [top](#TableOfContents)

---

## Deployment <a name="Deployment"></a>

### Deployment – Live Website <a name="Deploymentlivewebsite"></a>

This site is currently deployed on [Heroku](https://www.heroku.com/) using the **master** branch on GitHub. Once you have the project setup locally, you can proceed to deploy it remotely with the following steps:

- Create a **requirements.txt** file so Heroku can install the required dependencies to run the app:
    - `sudo pip3 freeze --local > requirements.txt`
    - The *requirements.txt* file for this project can be found here: [requirements.txt](https://github.com/sctlcd/pearl/blob/master/requirements.txt)
- Create a **Procfile** to tell Heroku what type of application is being deployed using *pearl*, and how to run it:
    - `echo web: gunicorn main.wsgi:application > Procfile`
    - The *Procfile* for this project can be found here: [Procfile](https://github.com/sctlcd/pearl/blob/master/Procfile)
- Sign up for a free Heroku account, create your project app, and click the **Deploy** tab, at which point you can *Connect GitHub* as the Deployment Method, and select *Enable Automatic Deployment*.
- In the Heroku **Resources** tab, navigate to the *Add-Ons* section and search for **Heroku Postgres**. Make sure to select the free *Hobby* level. This will allow you to have a remote database instead of using the local sqlite3 database, and can be found in the Settings tab. You'll need to update your *.env* file with your new *database-url* details.
- In the Heroku **Settings** tab, click on the *Reveal Config Vars* button to configure environmental variables. You will need to copy/paste all of the *.env* key value pairs into the config variables, but please omit the *development=1* variable; this is only for local deployment.
- Your app should be successfully deployed to Heroku at this point, but you're not quite finished yet!
- Update the *settings.py* file to connect the remote database using this Python package: `dj_database_url`
- Re-build the migrations and create a superuser to your new remote database using the instructions in the *local deployment* section above.
- Sign up for a free [Amazon AWS](https://aws.amazon.com/) account in order to host your *staticfiles* and *media* files. From the **S3 buckets** section, you'll need to create a new unique bucket. Follow these next steps to complete the setup:

**Permissions** > **CORS configuration**:

```
[
  {
      "AllowedHeaders": [
          "Authorization"
      ],
      "AllowedMethods": [
          "GET"
      ],
      "AllowedOrigins": [
          "*"
      ],
      "ExposeHeaders": []
  }
]
```

**Permissions** > **Bucket Policy**:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadGetObject",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::<x>/*"
        }
    ]
}
```

*! IMPORTANT ! - on the **Resource** line above, be sure to replace `<x>` with your **AWS bucket arn** details, but retain the `/*` at the end.* It should look similar to this:
    - `"Resource": "arn:aws:s3:::my-bucket-name/*"`

- From here, you'll need to navigate to the **IAM** section of AWS.
    - Create a *New Group* and be sure to select your existing S3 Bucket details to attach.
    - Create a *New Policy* and a *New User* in the IAM section as well, then attach these to the Group you just built.
- In your CLI-terminal, you should now be able to push the static files to AWS if everything is configured properly using this command:
    - `python manage.py collectstatic`
- Sign up for a free [Stripe](https://stripe.com) account. Navigate to the **Developers** section, and click on **API Keys**. You should have two confidential keys which need to be added to your *.env* file, as well as your Heroku config vars. These keys are:
    - `Publishable Key`: **pk_test_key**
    - `Secret Key`: **sk_test_key**

Congratulations! Your project should be completely setup and ready for remote deployment!

### Deployment – Run Locally <a name="Deploymentrunlocally"></a>

It's highly recommended to work in a virtual environment, but not absolutely required.

In order to run this project locally on your own system, you will need the following installed (as a bare minimum):

- [Python3](https://www.python.org/downloads) to run the application.
- [PIP](https://pip.pypa.io/en/stable/installing) to install all app requirements.
- [GIT](https://www.atlassian.com/git/tutorials/install-git) for cloning and version control.

Next, there's a series of steps to take in order to proceed with local deployment:

- Clone this GitHub repository by either clicking the green "*Clone or download*" button above in order to download the project as a zip-file (remember to unzip it first), or by entering the following command into the Git CLI terminal:
    - `git clone https://github.com/sctlcd/pearl.git`
- Navigate to the correct file location after unpacking the files.
    - `cd <path to folder>`
- Create a `.env` file with your own credentials. An example *.env* file can be found here ([.env_sample](project/.env_sample)).
    - *Note: the example .env file contains environmental variables for both local and remote deployment. (see below for remote deployment details)*
- Install all requirements from the [requirements.txt](project/requirements.txt) file using this command:
    - `sudo -H pip3 -r requirements.txt`
- In the IDE terminal, use the following command to launch the Django project:
    - `python manage.py runserver`
- The Django server should be running locally now on **http://127.0.0.1:8000** (or similar). If it doesn't automatically open, you can copy/paste it into your browser of choice.
- When you run the Django server for the first time, it should create a new *SQLite3* database file: **db.sqlite3**
- Next, you'll need to make migrations to create the database schema:
    - `python manage.py makemigrations`
    - `python manage.py migrate`
- In order to access the Django *Admin Panel*, you must generate a superuser:
    - `python manage.py createsuperuser`
    - (assign an admin username, email, and secure password)

Once the database migrations and superuser have been successfully completed, Django should migrate the existing *migrations.py* files from each app to configure the following relational schema:

[Relational Schema](https://github.com/sctlcd/pearl/blob/master/design/relational-scheme.png)

Back to [top](#TableOfContents)

---

## Credits <a name="Credits"></a>

- My inspiration comes from:
- [Etsy](https://www.etsy.com/) - E-commerce website focused on handmade or vintage items and craft supplies
- [Cultura](https://www.cultura.com/) - E-commerce website specialized in cultural, arts and crafts goods and leisure activities

Back to [top](#TableOfContents)

---

### Content <a name="Content"></a>

- [Baker Ross](https://www.bakerross.ie/) - E-commerce website specialized in arts and crafts supplies

Back to [top](#TableOfContents)

---

### Media <a name="Media"></a>

Sources of the images used on this site:

- From media/home/hero_image sub-directory
	- [hero-image-background-min.jpg](https://pixabay.com/fr/photos/laine-d-acier-sombre-firespin-458840/) - [Pixabay](https://pixabay.com/) | copyright [463259](https://pixabay.com/fr/users/463259-463259/)  

- From media/home/image_showcases sub-directory
	- [create-beads-min.jpg](https://www.flickr.com/photos/woolgenie/11130456836/) - [Flickr](https://www.flickr.com/) | copyright [Heather](https://www.flickr.com/photos/woolgenie/)
	- [create-grafiti-min.jpg](https://www.flickr.com/photos/rem60/31635422637/) - [Flickr](https://www.flickr.com/) | copyright [Rosemary Miklitsch](https://www.flickr.com/photos/rem60/)
	- [create-mosaic-min.jpg](https://www.flickr.com/photos/mikecogh/43105291024/) - [Flickr](https://www.flickr.com/) | copyright [Michael Coghlan](https://www.flickr.com/photos/mikecogh/)

- From media/home/testimonials sub-directory
	- [female-2-min.jpg](https://pixabay.com/fr/photos/mod%C3%A8le-femme-portrait-336658/) - [Pixabay](https://pixabay.com/) | copyright [Free-Photos](https://pixabay.com/fr/users/free-photos-242387/)
	- [female-1-min.jpg](https://pixabay.com/fr/photos/jeune-fille-%C3%A9changisme-coiffure-1245835/) - [Pixabay](https://pixabay.com/) | copyright [Free-Photos](https://pixabay.com/fr/users/free-photos-242387/)
	- [male-1-min.jpg](https://www.pexels.com/photo/portrait-photo-of-man-in-white-crew-neck-t-shirt-with-assorted-hand-tools-in-background-1139743/) - [Pexels](www.pexels.com) | copyright [Juan Pablo Serrano Arenas](https://www.pexels.com/@juanpphotoandvideo)

- From media/home/gallery sub-directory
	- [gallery-background-1920-min.jpg](https://www.pexels.com/photo/apple-device-camera-camera-lens-desk-593325/) - [Pexels](https://www.pexels.com/) | copyright [Jessica Lewis](https://www.pexels.com/@thepaintedsquare)

- From media/logo sub-directory
	- [pearl-min.png](https://www.flaticon.com/free-icon/craft_3079199) - [Flaticon](https://www.flaticon.com/) | copyright [Freepik](https://www.flaticon.com/authors/freepik)

- From media/error sub-directory
	- [no-results-found-min.jpg](https://all-free-download.com/free-vector/download/exploration-job-background-searching-man-sketch-cartoon-design_6844384.html) - [Free vectors](https://all-free-download.com/free-vector/) | copyright [BSGStudio](http://buysellgraphic.com/)

- From media directory
	- [bakerross](https://www.bakerross.ie/) - all product images
	- [](https://pixabay.com/fr/photos/parc-guell-mosa%C3%AFque-carreau-gaudi-887725/) - [Pixabay](https://pixabay.com/) | copyright [LisaRedfern](https://pixabay.com/fr/users/lisaredfern-910282/)
	- [](https://pixabay.com/fr/photos/ouzb%C3%A9kistan-mosa%C3%AFque-mod%C3%A8le-196875/) - [Pixabay](https://pixabay.com/) | copyright [LoggaWiggler](https://pixabay.com/fr/users/loggawiggler-15/)
	- [](https://pixabay.com/fr/photos/mosa%C3%AFque-carreau-art-c%C3%A9ramique-200866/) - [Pixabay](https://pixabay.com/) | copyright [GLady](https://pixabay.com/fr/users/glady-768/)
	- [](https://pixabay.com/fr/photos/mur-de-graffiti-graffiti-1209761/) - [Pixabay](https://pixabay.com/) | copyright [Free-Photos](https://pixabay.com/fr/users/free-photos-242387/)
	- [](https://www.pexels.com/photo/child-sipping-from-pipe-graffiti-2103127/) - [Pexels](https://www.pexels.com/) | copyright [Shukhrat Umarov](https://www.pexels.com/@shukran)
	- [](https://unsplash.com/photos/JlufluFHiZc) - [Unsplash](https://unsplash.com/) | copyright [Eyasu Etsub](https://unsplash.com/@jphotography2012)
	- [](https://unsplash.com/photos/cdXwe6nROs8) - [Unsplash](https://unsplash.com/) | copyright [Nasim Keshmiri](https://unsplash.com/@nasimkeshmiri)
	- [](https://unsplash.com/photos/DWjucw3fsaQ) - [Unsplash](https://unsplash.com/) | copyright [Fallon Michael](https://unsplash.com/@fallonmichaeltx)
	- [](https://unsplash.com/photos/CQ3xrqbV58s) - [Unsplash](https://unsplash.com/) | copyright [Nasim Keshmiri](https://unsplash.com/@nasimkeshmiri)
	- [](https://unsplash.com/photos/9EiJn8OJ8wo) - [Unsplash](https://unsplash.com/) | copyright [Nadia Clabassi](https://unsplash.com/@foifezza)
	- [](https://unsplash.com/photos/xlkuA0VQshU) - [Unsplash](https://unsplash.com/) | copyright [Elsa Lilja](https://unsplash.com/@elsa_lilja)
	- [](https://www.pexels.com/photo/doodle-comic-art-sketch-16516/) - [Pexels](https://www.pexels.com/) | copyright [khairul nizam Follow](https://www.pexels.com/@niezam)
	- [](https://pixabay.com/fr/photos/broderie-travaux-d-aiguille-942255/) - [Pixabay](https://pixabay.com/) | copyright [bluemorphos](https://pixabay.com/fr/users/bluemorphos-1137133/)
	- [](https://www.pexels.com/photo/toy-bear-and-thread-on-table-in-room-in-daytime-4792086/) - [Pexels](https://www.pexels.com/) | copyright [Anete Lusina](https://www.pexels.com/@anete-lusina)
	- [](https://pixabay.com/fr/photos/peinture-peinture-acrylique-art-4105253/) - [Pixabay](https://pixabay.com/) | copyright [stux](https://pixabay.com/fr/users/stux-12364/)
	- [](https://pixabay.com/fr/photos/mosa%C3%AFque-carreau-art-c%C3%A9ramique-200868/) - [Pixabay](https://pixabay.com/) | copyright [GLady](https://pixabay.com/fr/users/glady-768/)
	- [](https://unsplash.com/photos/o7IsP-DbIgk) - [Unsplash](https://unsplash.com/) | copyright [Nasim Keshmiri](https://unsplash.com/@nasimkeshmiri)
	- [](https://unsplash.com/photos/lUvvRj2RzK0) - [Unsplash](https://unsplash.com/) | copyright [Nasim Keshmiri](https://unsplash.com/@nasimkeshmiri)
	- [](https://www.pexels.com/photo/art-creative-pattern-purple-5278835/) - [Pexels](https://www.pexels.com/) | copyright [Anni Roenkae](https://www.pexels.com/@anniroenkae)
	- [](https://www.pexels.com/photo/photo-of-multicolored-illustration-2832382/) - [Pexels](https://www.pexels.com/) | copyright [Anni Roenkae](https://www.pexels.com/@anniroenkae)
	- [](https://www.flickr.com/photos/earthafricacurio/6367436537/) - [Flickr](https://www.flickr.com/) | copyright [Ian Nicholson](https://www.flickr.com/photos/earthafricacurio/)
	- [](https://www.flickr.com/photos/paullew/12517089325/) - [Flickr](https://www.flickr.com/) | copyright [Lawrence OP](https://www.flickr.com/photos/paullew/)
	- [](https://www.flickr.com/photos/hundreds/111294390/) - [Flickr](https://www.flickr.com/) | copyright [max_thinks_sees](https://www.flickr.com/photos/hundreds/)
	- [](https://www.flickr.com/photos/3sth3r/17888752/) - [Flickr](https://www.flickr.com/) | copyright [3sth3r](https://www.flickr.com/photos/3sth3r/)
	- [](https://unsplash.com/photos/D9EgMp2V85o) - [Unsplash](https://unsplash.com/) | copyright [Toa Heftiba](https://unsplash.com/@heftiba)

Back to [top](#TableOfContents)

---

### Code <a name="Code"></a>

- Environment variables - [Igor Basuga](https://github.com/bravoalpha79) Tutor at [Code Institute](http://codeinstitute.net)
- Environment variables - Code Institute archive resources
- Ngrok - [ngrok](https://ngrok.com/)
- Using ngrok on Windows-10 - [youtube](https://www.youtube.com/watch?v=9gaaVbX0USI&ab_channel=ChuckSeverance)
- Testing our Django App to be publicly accessible using NGROK - [medium](https://medium.com/@iot24hours/testing-our-django-app-to-be-publicly-accessible-using-ngrok-9b73851c46e0)
- jQuery documentation - [jQuery](https://jquery.com/)
- Favicon in django app - [stackoverflow](https://stackoverflow.com/questions/21938028/how-can-i-get-a-favicon-to-show-up-in-my-django-app)
- Material Design for Bootstrap documentation - [mdbootstrap](https://mdbootstrap.com/)
- How to integrate mdbootstrap with django - [mdbootstrap](https://mdbootstrap.com/articles/jquery/how-to-integrate-mdbootstrap-with-django/)
- mdb input number [mdbootstrap](https://mdbootstrap.com/docs/jquery/forms/inputs/)
- Creating a modal image gallery with bootstrap components - [css-tricks](https://css-tricks.com/creating-a-modal-image-gallery-with-bootstrap-components/)
- How to - Portfolio Gallery with Filtering - [w3schools](https://www.w3schools.com/howto/howto_js_portfolio_filter.asp)
- Portfolio Filter Gallery HTML CSS & JavaScript | Image Category Filtering [webdevtrick](https://webdevtrick.com/portfolio-filter-gallery/)
- How to - Lightbox - [w3schools](https://www.w3schools.com/howto/howto_js_lightbox.asp)
- Material Design Full Screen Modal - [mdbootstrap](https://mdbootstrap.com/snippets/jquery/mustafaozkaya/789907#html-tab-view)
- How to change your commit messages in Git? - [github](https://gist.github.com/nepsilon/156387acf9e1e72d48fa35c4fabef0b4)
- How to limit the maximum value of a numeric field in a Django model? [stackoverflow] - (https://stackoverflow.com/questions/849142/how-to-limit-the-maximum-value-of-a-numeric-field-in-a-django-model)
- Python perform append at beginning of list - [geeksforgeeks] - https://www.geeksforgeeks.org/python-perform-append-at-beginning-of-list/
- How to upload files with django - [simpleisbetterthancomplex](https://simpleisbetterthancomplex.com/tutorial/2016/08/01/how-to-upload-files-with-django.html)
- How to crop an image in css - [educative](https://www.educative.io/edpresso/how-to-crop-an-image-in-css)
- Set favicon in django admin - [stackoverflow](https://stackoverflow.com/questions/34959897/set-favicon-in-django-admin)
- Change the display format of time fields - [stackoverflow](https://stackoverflow.com/questions/7216764/in-the-django-admin-site-how-do-i-change-the-display-format-of-time-fields)
- Automatic datetime fields - [simpleisbetterthancomplex](https://simpleisbetterthancomplex.com/tips/2016/05/23/django-tip-4-automatic-datetime-fields.html)
- Delete a git commit but keep the changes [stackoverflow](https://stackoverflow.com/questions/15772134/can-i-delete-a-git-commit-but-keep-the-changes)
 - You're using the staticfiles app without having set the STATIC_ROOT setting to a filesystem path - [stackoverflow](https://stackoverflow.com/questions/48455469/youre-using-the-staticfiles-app-without-having-set-the-static-root-setting-to-a)
 - Python django error oserror winerror 123 the filename directory name or vol - [stackoverflow](https://stackoverflow.com/questions/56166319/python-django-error-oserror-winerror-123-the-filename-directory-name-or-vol)
 - Modify Title and Header Django Admin Interface - [medium](https://adiramadhan17.medium.com/modify-title-and-header-django-admin-interface-a6ad6e470d92)
 - Customizing HTTP error web pages 404, 500, 403 and 400 in Django - [lavatechtechnology](http://lavatechtechnology.com/post/customizing-http-error-web-pages-404-500-403-and-400-in-django/)
 - Equivalent of export command in Windows - [superuser](https://superuser.com/questions/1500272/equivalent-of-export-command-in-windows)
 - Heroku Django Deploy Stripe Issue - No module named 'stripe'
 - [stackoverflow](https://stackoverflow.com/questions/51509121/heroku-django-deploy-stripe-issue-no-module-named-stripe/51509169)
 - Readme file information - [Tim Nelson](https://github.com/TravelTimN) Software Developer and Tutor at [Code Institute](http://codeinstitute.net)

Back to [top](#TableOfContents)

---

### Acknowledgements <a name="Acknowledgements"></a>

- [Anthony Ngene](https://github.com/tonymontaro)
	- Thanks to my Code Institute mentor for his time, suggestions, constructive feedback and availability.  
- CI Tutor support for their help in order to understand some issues and their friendliness.

Back to [top](#TableOfContents)

---
