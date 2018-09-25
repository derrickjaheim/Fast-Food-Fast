# Fast-Food-Fast

https://derrickjaheim.github.io/Fast-Food-Fast/UI/

[![Build Status](https://travis-ci.org/derrickjaheim/Fast-Food-Fast.svg?branch=api)](https://travis-ci.org/derrickjaheim/Fast-Food-Fast)

[![Coverage Status](https://coveralls.io/repos/github/derrickjaheim/Fast-Food-Fast/badge.svg?branch=api)](https://coveralls.io/github/derrickjaheim/Fast-Food-Fast?branch=api)


<a href="https://codeclimate.com/github/derrickjaheim/Fast-Food-Fast/maintainability"><img src="https://api.codeclimate.com/v1/badges/f056675dbe9a5d3e8fa5/maintainability" /></a>


***Features***
 * User can fetch all orders.
 * User can fetch a specific order.
 * User can post an order.
 * User can can update an order.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development
and testing purposes.

### Prerequisites
What you need to install the software and get started.

```bash
- git : to update and clone the repository
- python3: The base language used to develop the api
- pip: a python package used to install project requirements
```
### Installation
```bash
Type:
```
The UI folder houses the user interface. To access the user interface, open the index.html.

The api folder contains the system backend services.
- To install the requirements, run:
- [Python](https://www.python.org/) A general purpose programming language

- [Pip](https://pypi.org/project/pip/) A tool for installing python packages

- [Virtualenv](https://virtualenv.pypa.io/en/stable/)  A tool to create isolated Python environments

#### Development setup
- Create a virtual environment and activate it
    ```bash
     virtualenv venv
     source /env/bin/activate
    ```
- Install dependencies
    ```bash
    pip3 install -r requirements.txt
    ```
- Run the application
    ```bash
    cd FastFoodFast
    python run.py
    ```
- Now you can access the system api Endpoints:

| End Point                                           | Verb |Use                                       |
| ----------------------------------------------------|------|------------------------------------------|
|`/api/v1/orders/`                                    |GET   |Gets a list of all orders              |
|`/api/v1/orders/<int:order_id>/`                     |GET   |Gets a specific specific order  |
|`/api/v1/orders/`                                    |POST  |Posting an order                        |
|`/api/v1/orders/<int:order_id>/`                     |PUT   |Updates the status of an order      |

## Running the tests

- To run the tests, run the following commands

```bash
pytest --cov=.
```

## Built With

* [Flask](http://flask.pocoo.org/docs/1.0/) - The web framework used
* [Python](https://www.python.org/) - Framework language
* HTML
* CSS

## Authors

* **Akankwasa Derrick** -  - [derrickjaheim](https://github.com/derrickjaheim)

## Acknowledgments

* Andela Development Uganda
