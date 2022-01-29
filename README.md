# News-Letter [Title TBC]

# Insert am-i-responsive link here
---

# Insert link to deployed app here.

News-Letter (name TBC) is a news-blog focussing on news and intelligence in the legal & compliance sector.
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
3. [] To add comments to articles which engage me;
4. [x] To browse products for sale;
5. [x] To edit my orders before completion;
6. [] To have a profile page;
7. [] To review the status of my orders and subscriptions;
8. [] To login using an existing social media account if I want;
9. [] To have a way to search the app and its contents.

As an owner of this product, I want:

1. [x] To have a clean UX which encourages engagement;
2. [] To encourage users to contribute their views;
3. [] To receive user feedback in the form of comments, likes or shares;
4. [] To have a means to collect user data;
5. [x] To display articles in a way that enhances user engagement;
6. [x] To offer products 
7. [] To offer subscriptions;
7. [] To offer a method of making payments online;
8. [tbc]

### Strategy

The strategy plane of UX design concerns itself with high-level decisions about the product and trade-offs between features to be developed now and others to be developed later. Compare feasibility of features with importance.

The LEAN model of software design will be adopted here with the identification of a minimum viable product (MVP) which can be released to the public. 'Lean startups' are very _en vogue_ at the present and business types are greater fashion-victims than teenagers. Yet, it makes sense to focus on developing a basic, working product and seek to add features to it. In this regard, we will plot out the different objectives on the basis of feasibility and importance. Importance here will be based on how we perceive each products appeal to the wider public.

#### [INSERT IMPORTANCE/FEASIBILITY GRAPH HERE]

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
11. [Add more here] 

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

A key aspect of this app will be the data model deployed. This app will use a relational database (PostgresSQL) and Django's built-in Object Relational Manager. The Relational Database can be traced back to[E.F. Codd's paper](https://www.seas.upenn.edu/~zives/03f/cis550/codd.pdf) from 1970. Relational database are ACID compliant: that is, they exhibit the properties of Atomicity, Consistency, Isolation and Durability. PostgresSQL is a popular choice.

Relational Databases (or SQL (structured query language) Databases) require a schema to operate and store data. Each piece of data is stored in a row or a tabular format. This allows for effective querying and a means to ensure data is consistent; however, this comes at the cost that it is often necessary to normalise the data in some way in order for it to be stored in a Relational Database.

Of particular use here is an ORM such as SQLAlchemy or Django ORM. The Object Relation manager allows for the creation of a relational database schema using the more 'natural' format of a python or javascript class, instead of creating a schema using SQL. 


### Skeleton

### Surface

### Features

#### Features To Be Implemented

### Testing

### Deployment

#### Using a custom CDN to deliver content

Google Cloud Platform's storage and CDN solution was used to host and serve any images and static content used by this web app. Setting up such a CDN is a straight-forward process. 

[INSERT DETAILS OF CDN HERE]

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
   
