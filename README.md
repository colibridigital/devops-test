# News Search
 
A command line Python application that allows a user to perform queries on documents stored in a text file. Users can use the AND and OR search operators and search terms to query existing documents. The program returns the indices of documents matching the queries.

## How to run the code

Open a command prompt in the root of the project and run:

```pip install -e .```

Then from your command line run:

```news_search [search_type] [terms]```

You can search using OR and AND type operators.

i.e ```news_search OR Care Quality Commission```

This will return the indices of any matching documents.

### Prerequisites

This project requires Python3 to be installed, you may want to run the application in a virtual Python environment. You can learn to install Python3 and virtualenv here:
https://docs.python-guide.org/dev/virtualenvs/

## Running the tests

To run the tests please install pytest with ```pip install pytest``` and run ```pytest``` in the root folder.

## Requirements

For this test we would like you to take a TDD approach to developing the following requirements (write a test, make it fail, make it pass).
Each requirement must be proven in at least one test.

Please make your changes in search.py and test_search.py

- When running ```news_search OR search term1 term2 term3 etc``` the program should return a list of indices where at least one of the terms were found in each line of data.txt.
- Refactor the code ```f = open(data_location, "r")``` to ensure that if the code fails the file handler will be closed.
- When running ```news_search AND search term1 term2 term3 etc``` the program should return a list of indices where all the terms were found in each line of data.txt.

An example of a successfull query would look like this:

```news_search OR Care Quality Commission```

output:

0
1
2
3
4
5
6

```news_search AND Care Quality Commission```

output:

1

## Bonus Requirements

- Add logging to the code
- Implement docstrings and type hinting
- Add pre-commit hooks to enforce testing and code quality 

# Terraform
Congrats on building the app!

Now it's time to do the infra. So let's begin by setting up a new Terraform project in the aptly named directory called `terraform`.

You will be using AWS

Requirements:
* setup a new terraform project. Store the state in the proper location (this is your decision, but state cannot live on your computer).

* setup a VPC. The VPC must span all AZs available for the region of choice and must contain one private and one public subnet per AZ.


# Docker
You have your app and you have your AWS infra. But now you will hand over your app to other developers, who perhaps believe Cloud is what spoils a day at the beach and nothing else. We need to enable them to work locally.

Requirement:
* setup a docker-compose file that will enable any developer to run your app by simply doing `docker-compose up`.
* after `docker-compose up`, developer will be able to connect to redis and database on localhost:PORT (where port is the default redis / db port)

note: The services should start in this order: db > redis > your py app