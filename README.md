# django_migrations
Django migrations homework

_This assignment was completed as part of my work at The Iron Yard._

**Objectives**
- Understand the basics of how to create a Django model definition
- Understand how to create instances of Django models to use as rows in your database
- Creation of blank migrations to use as a Data Migration
- Creation of Schema migrations to create or alter the structure of your database

**Description**

In this assignment you will be tasked to initialize a Django application and to define your first Model. After you've defined your model you are going to have to load

Migrations are a core concept to creating and altering the schema of your data layer in your Django web applications. The documentation is very comprehensive and includes many code examples to refer to when creating your schema and data migrations.

https://docs.djangoproject.com/en/1.9/topics/migrations/

**Schema Migration**

The Schema migrations are generated with the makemigrations command in your manage.py task shell. They will take your class definitions that you've created in your models.py file and translate them into instructions that the ORM will interpret as SQL. It isn't until you actually run your migrations with the migrate command will your database be changed.

**Data Migration**

https://docs.djangoproject.com/en/1.9/topics/migrations/#data-migrations

Similar to a schema migration, a Data migration is a set of instructions that are generated for you to execute python code to be interpreted as SQL. The core difference is that only the base skeleton of the file is created for you - and you must fill in the details. The details that you fill in will be commands to create data inside of your database.

**Normal Mode**

In this assignment you will want to take the structure of your database table from the previous "Sports Search Engine" assignment and adapt it from a SQL CREATE TABLE string into an actual Django model class. Once you've created your class definition you need to create a schema migration and run it to create the initial structure of your app's database.

The next step will be to create an empty migration and follow the Django documentation (and my advice) in creating the initial data that you will load into your Django application. This data should be the same data (or it can be more data if you like) that you loaded into your "Sports Search Engine" assignment.

To complete this assignment, I used both Python and Django.
