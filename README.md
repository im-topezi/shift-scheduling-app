# shift-scheduling-app
Web app for scheduling workshifts.
Functions:
1. Users can create an account and sign in (At the moment only username is required to make development easier)
2. Users can have different roles in the system (Shift admins, shift maangers, shift workers)(Roles only modify access rights right now and admin is the only role that changes the user access)
3. Shift admins and shift managers can assign shifts to workers. Workers have different duties.(Only admins can add shifts at the moment and shifts can be added to anyone)
4. Calender from which to view the shifts (Calender doesn't load any data at the moment)


How to install and use:

Make a clone of this repository (Easiest way is to create a folder on your own computer and use the git clone tool)

Make an .env file and add your "DATABASE_URL=" and a "SECRET_KEY="

Navigate to the folder that contains your clone and install the virtual enviroment: $ python3 -m venv venv

Next activate the virtual enviroment with the command $ source venv/bin/activate

Now install the depencies using command $ pip install -r ./requirements.txt

Install database schema with command $ psql < schema.sql

Start hosting the web application $ flask run
