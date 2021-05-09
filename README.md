# Databases-Advanced
Repository for the class Databases Advanced

In this repository you have the option to follow 2 tutorials to scrap webdata from Blockchain. This is a website that holds Hashvalues, with our scripts we will be storing the most valuable Hash into MongoDB.

In tutorial you will be using Redis and MongoDB which will be installed via bash files. This makes it so you will have to run Redis and MongoDB yourself locally on your machine.

If you want to use our webscrapers, you'll need to install Ubuntu. There is a link to a tutorial in the file "Tutorials.txt".

Next if you have Ubuntu up and running open the terminal and type in cd Desktop/. This will put you in the desktop directory. Download the python_install.sh file to your desktop and run this in terminal by typing bash python_install.sh

Now i would suggest checking the tutorials and docker commands before starting the tutorials

*********************
Tutorial 1:
*********************

By now Ubuntu should be installed on your machine locally. You'll also have installed python on Ubuntu.

Now we'll have to install mongoDB and Redis on your machine with the bash files "mongo_install.sh" and "redis_install.sh". Install these onto you Desktop, open the terminal type in: cd Desktop/. You'll now be in the desktop directory, type in mongo_install.sh and wait until the install is complete and do the same for redis.

Now install the "webscraper_redis.py" and "extract_mongo.py" to the desktop. 

Make sure mongoDB and redis are running. Mongo => sudo systemctl status mongod. Redis => redis-server. Do not close these terminals to make sure they keep running. (sudo systemctl start mongod if status is disabled).

Follow the mongoDB-compass install in Tutorials if you want to have a visual interface for MongoDB

Now you can run the scraper and extract files.

In 2 seperate terminals: go to the desktop directory by the cd Desktop/ command. Type in python3 webscraper_redis.py, in the other terminal python3 extract_mongo.py

Congratulations you now scraped your first highest value Hash and stored it into MongoDB.


*********************
Tutorial 2:
*********************

By now Ubuntu should be installed on your machine locally. You'll also have installed python on Ubuntu.

Now we'll have to install Docker on your machine with the bash file "docker_install.sh". Install this onto you Desktop, open the terminal type in: cd Desktop/. You'll now be in the desktop directory, type in bash docker_install.sh and wait until the install is complete.

Now that docker is installed we will have to pull the Redis and MongoDB images the follwoing commands: sudo docker pull redis and sudo docker pull mongo

Now we'll have to make two new directories. A redis directory and a mongo directory. Use the following commands: mkdir redis-docker and mkdir mongodb-docker

Go into the redis directory by typing cd redis-docker. Now that you're in here type in the following command. sudo docker run -d --network="host" --name redis redis. Now exit by typing exit. 

Go into the mongo directory by typing cd mongo-docker. Now that you're in here type in the following command. sudo docker run -d -p 27017:27017 --network="host" -v ~/mongodb-docker:/data/db --name mongodb mongo:latest. 

Now we created our redis and mongo containers.

Download the webscraper_docker.py and extract_docker.py files to the desktop. Run both these files in a seperate terminal by after typing cd Desktop/. Run these by typing python3 webscraper_docker.py en python3 extract_docker.py

Now open 2 new terminals and open the Mongo and Redis shill by following the steps in the file "Docker_commands.txt". You'll now see your hashvalues (or other values) cached in Redis and your highest value Hash in MongoDB. Congratulations!
