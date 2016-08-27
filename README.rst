=====
Lionreport
=====

Lionreport is the test/proof/report manager of the lionschool project. Use it to keep
track of your grades or to see why you failed that test!

Quick start
-----------

1. Add "lionschool.report" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'lionschool.report',
    ]


2. Include the polls URLconf in your project urls.py like this::

    url(r'^report/', include('lionschool.report')),

2. Run `python manage.py migrate` to create the lionreport models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create users, teachers, tests and more (you'll need the Admin
   app enabled).

5. Visit http://127.0.0.1:8000/report/ and see your grades!

6. Install other lionschool apps for more fun
