First We need to create virtual environment and then activate it.

Then we need to install the required packages
To do this we will do the following:
`pip intstall -r requirements.txt`
This will install all required packages

For execution pytest is used:
`pytest`
This will run all tests

For reporting we use - 
`coverage run -m pytest`
then to see the report - 
`coverage report -m` 

To see html report - 
`coverage html`

To execute in parallel use I have created specific groups to be executed(since they depend on each other)-
`pytest -n 4 --dist loadgroup`