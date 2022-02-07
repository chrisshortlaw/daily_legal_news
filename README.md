# Daily Legal News

# Insert am-i-responsive link here
![am-i-responsive](/readme_files/am-i-responsive-shot.png)
---

[Link to Deployed App on Heroku](https://daily-legal-news.herokuapp.com/)

Daily Legal News is a news-blog focussing on news and intelligence in the legal & compliance sector.
The blog will offer subscription services with multiple tiers and will have a shop for certain legal products (books, software etc.).

The project will be built with Django with BootStrap/Bulma on the front end.
We will use a relational database, PostgresSQL, to store the data for our webapp/blog. Django's built-in ORM will be used to manage, store and retrieve the data.

---

## Table of Contents

1. [Design and Development](#Design-and-Development)
    - [User Stories](#User-Stories)
    - [Strategy](#Strategy)
    - [Scope](#Scope)
    - [Structure](#Structure)
    - [Skeleton](#Skeleton)
    - [Surface](#Surface)

2. [Features](#Features)
    - [Features to be implemented](#Features-to-be-implemented)

3. [Testing](#Testing)
4. [Deployment](#Deployment)
    - [Using Git & Github](#using-git-&-github)
        - [Git](#Git)
        - [Initialising Git](#initialising-git)
        - [Adding Files to Git](#adding-files-to-git)
        - [Git Commit](#git-commit)
        - [Git Remotes](#git-remotes)
        - [Creating and Uploading a Repository](#creating-&-uploading-a-repository)
        - [Git Branch](#git-branch)
    - [Deploying to Heroku](#deploying-to-heroku)
5. [Credits](#credits)

## Design and Development

The approach to design and development will be the one that was devised and popularised by Jesse James Garrett in his book, 'The Elements of User Experience'. Garrett argues User Experience had 5 elements which build upon one another, rather than being separate, independent components. These are: strategy, scope, structure, skeleton, and surface. We will take each of these elements (or planes) in turn.

### User Stories

As the user of this product, I want:

1. [x] To read articles on the app;
2. [x] To login, logout and have the means of managing my sign-in;
3. [x] To add comments to articles which engage me;
4. [x] To browse products for sale;
5. [x] To edit my orders before completion;
6. [x] To have a profile page;
7. [x] To review the status of my orders and subscriptions;
8. [x] To have a way to search the app and its contents.

As an owner of this product, I want:

1. [x] To have a clean UX which encourages engagement;
2. [x] To encourage users to contribute their views;
3. [x] To receive user feedback in the form of comments, likes or shares;
4. [x] To have a means to collect user data;
5. [x] To display articles in a way that enhances user engagement;
6. [x] To offer subscriptions;
7. [x] To offer a method of making payments online;

### Strategy

The strategy plane of UX design concerns itself with high-level decisions about the product and trade-offs between features to be developed now and others to be developed later. Compare feasibility of features with importance.

The LEAN model of software design will be adopted here with the identification of a minimum viable product (MVP) which can be released to the public. 'Lean startups' are very _en vogue_ at the present and business types are greater fashion-victims than teenagers. Yet, it makes sense to focus on developing a basic, working product and seek to add features to it. In this regard, we will plot out the different objectives on the basis of feasibility and importance. Importance here will be based on how we perceive each products appeal to the wider public.

![FeasibilityGraph](/readme_files/feasibility_graph.pdf)

#### _User Needs_

Here we segment our users into different groups, each having a certain characteristic in common. Marketers often segment groups by demographics: age, ethnicity, income level and so on.

The site will focus on news from the legal and regulatory spheres. The users will be professionals (lawyers, accountants) or people involved in the compliance sector (government, management). Typically, a user will be using the app to assist in their job. It is anticipated the bulk of users will be aged between 25 and 45 years of age. These professionals will be more adept with technology and will be more likely to use a web app to assist them rather than relying on traditional research methods. They will be more comfortable with reading from a screen.

It is anticipated that users will access the app from their work smart-phone, their tablet and/or their desktop. It will be necessary to have a satisfying user experience for each of these.

The identified potential user-base brings with it a set of assumptions about the user experience and design. A navigation bar at the top, a collapsible menu at the top-right on mobile and other common traits of webpages should be deployed to ensure a smooth and comfortable experience. The identified user-base will expect a pleasant user-experience but may be repelled by too bright a colour-palette or features such as gamification. Users may find video and pictorial content to be useful and to add to their experience.

#### *Personas*

1. Paul: Paul is 36 and works as a compliance manager for a software company. Paul wishes to keep abreast of the latest developments in law and regulation, particularly as it applies to the tech sector. The company has provided Paul with a smart-phone with a large screen, a foldable tablet with attached screen as well as a laptop with a dock and dual screens. Paul uses each of these devices to consume content relating to his work and finds it frustrating when a piece of software, a webpage or content does not work well on all of the above. Paul's job involves plenty of calls and meetings, so he wants a method to save articles he is interested in reading so he can catch up on them.

2. Sarah: Sarah is 28 and works as an in-house counsel for a finance company. Part of Sarah's role requires her to collate news and updates regarding changes and trends in the legal and regulatory landscape. Sarah has a smart-phone, a tablet, a laptop and a desktop. Since the pandemic, Sarah has been working from home and so uses her laptop and tablet for work. She does not anticipate returning to the office and believes her work-place will do away with desk-tops over the next few months. 

### Scope

The scope follows on from the strategy plane. In this plane, we identify the specific requirements of the product and get a firm idea of what we are going to build. Here we focus on developing features in small, incremental blocks until we have a finished or viable product. This permits the realistic budgeting of time and the development of products quickly and effectively. It will also prevent 'project creep'.

#### *What are we going to make?*

A news-paper web-app with a store page. Users of the app can leave comments and likes. The store function will have a cart and a means to review user orders before payment.

#### *Requirements*

1. The app will have a means to view and read articles.
2. The app will have a means of navigation between articles
3. The app will have a means of grouping articles by author
4. The app will have a means of grouping articles by subject/category
5. The app will have a means of viewing products
6. The app will have a means of adding products to a virtual shopping cart
7. Have a means of reviewing and editing an order in the virtual shopping cart.
8. Main page should show users the most relevant or up-to-date content
9. Users should be encouraged to register an account and login.
10. Users will have a means of adding comments to articles. 

##### *Content

- Users will expect:
  - A profile page
  - A profile page which can be personalised
  - A profile page which will show their games
  - A profile page which will show their reviews
  - To be able to browse articles
  - To see comments made by other users.

##### *Functions

- The app must be quickly navigable
- The app must be simple to traverse
- The key parts of the app must be easy to find and access
- The app must allow Users to create, read, update and delete in accordance with their expectations

### Structure

Progressing down the planes, the developer moves from the abstract to the concrete as part of the eternal struggle by humanity to make its desires manifest. Does this mean that all developers are closeted Hegelians? Maybe mad platonists? Who knows? You are still reading this. Why?

The structure plane involves the detailing of how each feature will work together in the project.

#### How will we structure this app?

All code should be open for extension and scalability. We should have the ability to add additional features as we progress. Many pain points arise not out of code that does not work but our of code that is not open for extension or which cannot be made to adapt. 

A key aspect of this app will be the data model deployed. This app will use a relational database (PostgresSQL) and Django's built-in Object Relational Manager. The Relational Database can be traced back to [E.F. Codd's paper](https://www.seas.upenn.edu/~zives/03f/cis550/codd.pdf) from 1970. Relational database are ACID compliant: that is, they exhibit the properties of Atomicity, Consistency, Isolation and Durability. PostgresSQL is a popular choice.

Relational Databases (or SQL (structured query language) Databases) require a schema to operate and store data. Each piece of data is stored in a row or a tabular format. This allows for effective querying and a means to ensure data is consistent; however, this comes at the cost that it is often necessary to normalise the data in some way in order for it to be stored in a Relational Database.

Of particular use here is an ORM such as SQLAlchemy or Django ORM. The Object Relation manager allows for the creation of a relational database schema using the more 'natural' format of a python or javascript class, instead of creating a schema using SQL. 

The primary relationships in this project are displayed below.

![datamodel](/readme_files/data_modelling_diagrams_dln.pdf)

As can be seen, there are two models interacting here. The First if the User-Subscription-Profile model. Here the User is linked to a Profile, which is really an extension of the User object and designed to contain additional data. Also linked to th User by ForeignKey relationship is a Subscription. A subscription manages the User payments and their privileges. Connected to the subscription is are Groups. Groups are built-in to Django but they can be customised with permissions and can be used to grant access or refuse it to Users who are, or are not, members of a certain User Group. In this case, paying Users join the ranks of subscribers and gain access to locked content.

The Authors-Articles-Tags-Comments relationship is another data model used in this app. Here, the model uses many-to-many relationships (a Many-to-Many table in SQL parlance) to relate the different data objects. Authors can have multiple articles to their name, articles can be written by multiple authors, and each article can have multiple tags which themselves can be found on other articles. The Article-Comments relations is a foreign key relationship. Articles can have multiple comments, but it is undesirable to permit comments to be shared across articles.

### Skeleton

Here we begin to design the User Interface of the app and make decisions about how Users will interact with it.

Below are the wireframes for the app:

![wireframes](/readme_files/draft_paper_blog_site_wireframes.pdf)

Most news sites are structured around the main page displaying most of their content there and using it draw in the User and turn them into a subscriber or attract views for advertising content. Our app will follow a similar structure with a articles appearing on the main page followed. A sticky navbar at the top of the page permits users to browse without getting lost. It allows allows for quicker traversal of the webpage. In addition, the footer contains links to the various sections of the site, giving Users an additional opportunity to explore. Unsubscribed Users are encouraged to subscribe through the use of buttons and banners along with the locking of content behind a paywall. 

### Surface

#### Appearance

The page uses Bootstrap and some custom CSS for styling. Bootstrap has a clean look and comes with many responsive features allowing the app to be more easily migrated to mobile. As this is a news site, the color scheme of the site is muted: a cleaner UI emphasises readbility and allows Users to focus on the content. Nevertheless, some color is used to maintain visual interest. A complimentary colour set was chosen using color wheels. A soothing blue is used in login screens and authorisation screens.

The app makes use of Stripe's Checkout function and its checkout sessions. This allows Stripe to hold the relevant payment data and return an object or a webhook with the relevant data. The database can be updated or checked against this information and reconciled.

#### Security

Security is an important part of any app.

##### *Password Hashing

The trend now is to not store passwords or to write your own home-grown verification procedures but to use 2-factor authentication or authentication  via google, github or microsoft. While a future version of this app shall incorporate 2-factor, the app in its current form will use an email and password login system to manage users and prevent digital vandalism. Passwords, however, will not be stored in plain form. Instead they will be hashed using Django's built in authorisation, login and authentication functions. When a user registers, they will enter a password in a string form. This password is then hashed (converted to a string of symbols, letters and digits) and the hash is stored on the database. This mechanism means there is no point, save for intercepting the registration message, where a person could easily discover a password by accessing the database. At login, Django's built in function is able to check whether the password is correct by seeing if the passed string can be used to decode the hash to a message Django understands.

##### *Cross-Site Request Forgery Prevention

Cross-Site Request Forgery or 'CSRF' is when a malicious party intercepts a message between a user and a server and can use that to execute an unwanted action. For example, you log in to your online banking app by clicking on a link sent to you by email. The link is actually sent by a malicious party. They, in turn, use your information to execute a request transferring funds to another bank account. It is a good security practice to prevent CSRF attacks by taking such measures in your Django app.

Django prevents CSRF by attaching a hidden field to each form which contains a 'CSRF token'. This token is a cryptographic hash which is generated based on some hard to forge information. On the server side, running 'form.validate\_on\_submit' will run a check to see if a correct CSRF token is present. If it is not, the form is not validated and the command is not executed.

##### *Session Cookies

Session cookies are needed to allow for users to navigate through the app without having to constantly log in and log out. Sessions, or url parameters, are string that are attached to the end of http requests and which can be used to ascertain the 'state' of a request. These cookies are cryptographically signed which allows a user to see the contents of the cookie but will be unable to modify it. Sessions in this app are used to store a User's username and database '\_id'. They are signed using the Django's secret key which is set as part of a hidden environment variable on the app. 

---


### Features

#### Features To Be Implemented
[] Likes System
[] Closer webhook integratio
[] A fully fledged CMS


### Testing

Supporting documentation can be found in the [tests.py](tests.py) file located in each app.

The nature of the project meant that the code was subjected to extensive unit tests on each individual part.

Unit tests were conducted on the business logic of the application using Django's built-in testing suite. This suite is similar to python unittest library, although Django provides more helpful classes for querying databases or even setting up a client to test a view. These tests are documented and can be seen in tests.py at the top level of Github.

As of _31/1/22_, running 'python manage.py test' returned:

```bash
---

Creating test database for alias 'default'...
System check identified no issues (0 silenced).
Successfully Added test_sub to Subscriber Group
..........
----------------------------------------------------------------------
Ran 10 tests in 17.241s

OK
Destroying test database for alias 'default'...

---
```

A portion of the functionality of the app relies upon Stripe's API. As such, automated tests with such an API were not deployed lest they inadvertently cause access to be revoked. However, it is possible to simulate Stripe's webhook through the use of Stripe's CLI tool. This tool provides for a localhost to 'trigger' Stripe webhooks and to test receipt of said webhooks. However, not all webhooks are available in testing mode (in particular invoice.paid).

Testing has confirmed that:

- Users can view each of the pages of the site
- The site can connect to a payment service provider
- The site can update its database based on the response by the payment service provider.
- Unsubscribed Users (not members of SubscriberGroup) are denied access to certain articles
- Subscribed Users can view all articles
- A user who successfully completes the subscription process with the payment service provider will be admitted to the SubscriberGroup and their profile will be updated accordingly.
- A user who cancels their subscription will be removed from the Subscriber Group.

Further testing is needed with Stripe webhooks  before an optimum path for retrieving and managing subscription data 

### Deployment

### Using Git & Github

#### Git

Git is really useful. When you mess up some code trying to make some pointless improvement because some kid posted an article on medium.com saying this feature was essential to know if you wanted to be a competent coder in 2022, Git allows you to roll-back to your original, working code and undo the spaghetti you created.

#### Initialising Git

You will need to install Git. 

Having installed Git, we are going to use the command line, Git BASH, to initialise it. We could use the GUI but using the command line makes you feel you are smart and more efficient, even when you type 18 words-per-minute with lots of typos. Git Bash for the uninitiated is the shell that Git uses. Depending on your operating system, you might have another shell installed such as Microsoft's Powershell if you are using the Windows operating system or Terminal if you use a Mac. A shell is a program that processes text commands. Sometimes you will also hear this referred to as the command line. The command line is the line in which you input text commands to the shell. Using Git BASH, you will see a command line that resembles this:

    ```bash
    {username}@{computername} MINGW64 /c/code/jscalc
    $
    ```

The username will be your username (could be admin or your name) and your computer name. The 'MINGW64' above is the name of a programme which allows Git BASH to run on Microsoft Windows. You may have something different if you use a different operating system. After that, the path of the current working directory (CWD) is shown. In this case it is a folder called 'jscalc' (name of the project), which is located in a folder called 'code' which in turn is located at the top level of the C: drive. In Unix based systems, there is no distinction between drives and folders, so the address will resemble something like '/home/code/jscalc'.

From the shell, navigate to your project folder. To do this, you should use the command:

    ```bash
    cd <insert name of folder here>
    ```

Here 'cd' stands for 'change directory' and directory is another name for a folder. If you have not made a project folder, you can make one by navigating to where you would like to place your new folder and using the following command:

    ```bash
    mkdir <insert name of folder here>
    ```

This commands make a directory/folder bearing the name you gave it.

Having made that directory, navigate into the directory with the shell (use 'cd' as outlined above) and type the following command:

    ```bash
    git init
    ```

This initialises Git. Note the lower-case, capitalisation will matter in shells such as BASH but may not matter as much in Powershell. For simplicity's sake, use lower-case and name all your files and directories in lower-case.

#### Adding Files to Git

Git has been initialised. In doing so, you told the Git programme to create a series of files in your desired directory. These files will allow git to track your project. Now, it needs files to track. To tell Git to track files, enter the following command in bash:

    ```bash
    git add <name of file>
    ```

If you do not have a file in there yet, use the following:

    ```bash
    touch README
    ```

This will create a simple text file. On a windows OS, you might want to add a '.txt' or a '.md'. On a \*Nix based OS, such as Mac OS, these are less important.

Git is now tracking this file. To check if this is the case, while in the folder that you initialised git in, use the command:

    ```bash
    git status
    ```

You should see something like this:

    ```bash
    On branch master
    Changes to be committed:
    (use "git restore --staged <file>..." to unstage)
            modified:   README.md

    Changes not staged for commit:
    (use "git add <file>..." to update what will be committed)
    (use "git restore <file>..." to discard changes in working directory)
            modified:   viewModel.js
    ```

Git status provides you with useful information. Starting at the top, you will see output telling you which branch (more on this later) you are on. In this case, I am on 'branch master'. This can sometimes be called branch 'origin' or 'origin/master'. The names do not matter much save that these branches tell you this is the original branch.

Next up, we have 'Changes to be committed:' and below this we see a 'modified: README.md'. When we use git add, we are doing what is referred to as staging the changes to a file. If git add has been used correctly, you will have output much like this with a change ready to be committed.

#### Git Commit

Commits are snapshots of a file or files at a point in time. They are what allows Git to roll-back your work when you break your code or to see where you were at a certain point in time. Commits should be in small pieces, hopefully corresponding to either a new feature or some update to a file or code. How large or small it might be shall depend on your plan and the software you are writing.

All commits should be accompanied with a message. This message should give a succinct description of the changes the commit introduces or a conventional description. For example, the first commit of a file it is conventionally acceptable to write the message 'Initial Commit'. To make a commit, type:

    ```bash
    git commit -m <insert message here>
    ```

This commits the changes you added along with the message you entered.

#### Git Remotes

Git remotes are versions of a project which can be found on another machine - whether this is a server or a workstation. Remotes allow people to work on a local or separate version of a repository and then upload the changes they made to that repository.

Remotes will automatically appear when a project is cloned. Cloning a project makes a copy of it on your local machine. To clone a project, type:

    ```bash
    git clone <insert project url>
    ```

Having cloned this project, you now have a remote located in the directory you were in when you typed the command. If you want to put your cloned repository somewhere other than your current working directory you could type:

    ```bash
    git clone <insert project url> my-cloned-project
    ```

This will clone the project into a folder called 'my-cloned-project' which will be located in the current working directory.

#### Creating & Uploading a Repository

Sometimes you do not want to copy the work of others. Why imitate lesser mortals? In this instance, you will want to create your own github repository.

Creating your own github repository requires you set up a github account. This account is free for most personal use and is relatively eay to do. Navigate to github.com in your browser, set up an account, sign-in to that account, and stay signed in.

The next thing to do is create a new repository. The easiest way to do this is to navigate to 'your repositories' page. On the upper left corner of any github page, you should see a circle with an arrow, pointing down, beside it. Click on this symbol and a drop-down list will appear, on this dropdown list, after telling you if you are signed in and under your status bar, you will see a link to 'your profile' and below that 'your repositories'. Click on 'your repositories'. You will now be on a page listing out all your repositories. If you cloned any repositories, these can be found here. Near the top right, you will see a green button with the word 'New' on it. Click on this button, follow the instructions and give your new repository a name.

Now your repository has a name, it needs files. To upload files from an existing repository, type the following commands:

    ```bash
    git remote add origin <insert github url here>
    git branch -M main
    git push -u origin main
    ```

If you want to create a repository on your computer, follow the instructions above regarding creating files and using git add ([Git Add](#Adding files to Git)). Then type the commands immediately above.

#### Git Branch

Want to try something out and make commits without breaking your existing code? Are other people using this code and a change to it might upset or undermine their work? If you have answered, 'yes' to either of the above then Git Branch is definitely for you. In my case, I will often work on two different machines and I desire a way to share the code I am working on between the two machines without having a messy commit history cluttering up my master/origin branch. Git Branch helps me avoid this.

Branch takes a snapshot of your code and splits its timeline from the originating branch. Any commits you make will be made to that branch and will not affect the originating branch. Branching like this permits multiple people to simultaneously develop different features on a product without the concern they will interfere with each others work.

To create a branch, type:

    ```bash
    git branch <insert name of branch>
    ```

### Deploying to Heroku

Deployed on Heroku: daily-legal-news.herokuapp.com 

#### Deployment Process

To deploy this page to Heroku, one should follow the following steps:

1. Locate the [GitHub Repo](https://github.com/chrisshortlaw/played-it,"Link to GitHub Repo") of the app you wish to deploy.
2. Install git locally, if you have not done so.
3. Install the Heroku Command Line from [here](https://devcenter.heroku.com/articles/heroku-cli#download-and-install)
4. Run the Heroku Command Line and type 'heroku login'
5. Once you have logged in, the command line will keep you logged in.
6. Once you are set up there, you will need a requirements.txt file. This specifies the different libraries you will be relying upon. Pip has an easy way to create a requirements.txt with ```python -m pip freeze > requirements.txt``. And there you have it.
7. The next thing you shall require is a Procfile. A Procfile supplies Heroku with the instructions on how to run your app. So for example, if it needs to run on the web and what programme should be running. Your Procfile should be a line of these commands. For example:
  
    ```
    web: gunicorn played_it:app
    ```
   This tells heroku this is a web app running on Gunicorn (Green Unicorn) WSGI HTTP Server.
8. But wait! What is that gunicorn thing? Hitherto, all our tests on our local machine has been using Django's built in http server. When you type 'python manage,py runserver' run in the command line, this is the server you are running. However, in a production environment this is not possible. This is where something like Gunicorn comes in, which is a reasonably fast and lightweight WSGI server that we can use for deployment. Downloading Gunicorn is simple: 
    ```
    pip install gunicorn
    ```
   Make sure to update your requirements.txt file so heroku has gunicorn installed. 

**Note**: Gunicorn will not run on a Microsoft Windows machine. So if you want to test if you have placed your Procfile correctly or whether it will deploy, and you are using Windows, you will experience some frustration. There are Windows alternatives to Gunicorn, such as Waitress, which you might do well to look into.

9. At this point, you can considered creating a remote branch on Git to host your production app. I like to live dangerously, so I just deployed from the main branch. Branching with Git is discussed above.

10. If your app configuration relies upon environment variables or a hidden configuration, you should set these with heroku config. This can be done from the heroku CLI by typing:
  ```
  heroku config: set SECRET_KEY=a_super_secret_key
  ```
    If you prefer to use the GUI, you can set the configuration by clicking on the settings tab, clicking 'reveal config vars', and inserting the relevant variables.

11. Once you have established that, you should push your most recent, working state/branch to your deployment branch.

12. Heroku will take some time to build your app. Once it is done, you can view the app by navigating to the relevant app page. Heroku also has a GUI where you can lauch the app by clicking on the open app 'button'.



#### Using a custom CDN to deliver content

Google Cloud Platform's storage and CDN solution was used to host and serve any images and static content used by this web app. Setting up such a CDN is a straight-forward process. 

- Sign up for Google Cloud Platform. There is a free tier. You will be fine.
- You should set up a storage bucket from your dashboard. 
- Click Create bucket
- On the Create a bucket page, enter your bucket information. To go to the next step, click Continue.
- For Name your bucket, enter a name that meets the bucket name requirements.
- For Choose where to store your data, select a Location type and Location where the bucket data will be permanently stored.
- For Choose a default storage class for your data, select a storage class for the bucket. The default storage class is assigned by default to all objects uploaded to the bucket.
- For Choose how to control access to objects, select whether or not your bucket enforces public access prevention, and select an Access control model for your bucket's objects.
- For Choose how to protect object data, configure Protection tools if desired, and select a Data encryption method.
- Create your bucket.

A custom CDN will improve the loading speed of your web app considerably and avoid issues with size if your content is image heavy. This speed improvement will, in turn, assist in the Search Engine Optimization of your web-page/web-app.


### CREDITS

#### Pictures Used

- Scales of Justice Vector by [mohamed Hassan](https://pixabay.com/users/mohamed_hassan-5229782/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=5786847) from [Pixabay](https://pixabay.com/vectors/judgment-justice-judge-hammer-law-6823792/)

- Legal Library Photo by [Giammarco](https://unsplash.com/@giamboscaro?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) at [Unsplash](https://unsplash.com/s/photos/law?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)  

- Barrister Image by [Clker-Free-Vector-Images](https://pixabay.com/users/clker-free-vector-images-3736/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=28838) from [Pixabay](https://pixabay.com/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=28838)

##### Home Page

##### Products

##### Articles

- Police & Burglar by [mohamed Hassan](https://pixabay.com/users/mohamed_hassan-5229782/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=5786847) from [Pixabay](https://pixabay.com/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=5786847)

 - Justice Vector Image by [mohamed Hassan](https://pixabay.com/users/mohamed_hassan-5229782/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=5786847) from [Pixabay](https://pixabay.com/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=5786847)

 - Contract Vector Image by [mohamed Hassan](https://pixabay.com/users/mohamed_hassan-5229782/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=5786847) from [Pixabay](https://pixabay.com/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=5786847)



##### Other

 - Trinity College Library by [Henry Be](https://unsplash.com/@henry_be?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/collections/1783182/law?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)
   
