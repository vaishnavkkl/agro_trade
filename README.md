# AGRO TRADE
* This repo is made (myself and [@Sanjay](https://github.com/codebysanjay))  as a part of IEEE event <b>HACKWARE</b> co-ordinated by IEEE GECBH SB.
* Agro trade is an stimulation of a virtual online market for farmers.
* This helps the farmers to sell their products for reasonable price.
* The buyer can buy the products by contacting the farmers directly on their contact numbers provided by them.
* Sellers can contact the admin for adding their products in the marketplace.
* This is full stack application built with django.

### Setup instructions

cd into folder 

    cd <to current directory>

create a virtual env    

    virtualenv env -p python3.5  
    source env/bin/activate    

install all the dependencies in the requirements.txt    

    pip install pillow

migrate the migrations

    ./manage.py migrate

start the django server

    ./manage.py runserver
