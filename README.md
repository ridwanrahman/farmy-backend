# Farmy App For Farmers
An App for farmers that is currently an ongoing project because I have no idea what to build.
Hopefully something useful will come to my mind and I will be able to build something.

## Setup Instructions
To setup the project, please follow the steps:
1. Pycharm is recommended however, vscode is fine
2. Create virtual environment either in conda or pandas.
3. Run `pip install -r requirements.txt`
4. Run the tests `python -m pytest tests/integration_tests/apps/user/test_user.py`

#### To run the test classes/functions separately
1. Follow the instructions above to setup the project
2. Run `python -m pytest tests/integration_tests/apps/user/test_user.py::<Classname>::<Functionname>`

#### Development Conventions:

- To update any installed packages run `pip3 freeze > requirements.txt`