# stock
Provide stock code to get support and resistance


##### Project setup
```sh
$ git clone https://github.com/agilecrm/python.git
$ curl https://bootstrap.pypa.io/get-pip.py -s | python3
$ pip install -r requirements.txt
$ python3 run-in-local.py
```


##### Curl:
```
curl --location --request POST 'http://127.0.0.1:5000/stock' \
--form 'start_date="2021-7-15"' \
--form 'end_date="2021-8-30"' \
--form 'stock_name="HDB"' \
--form 'time_interval="15m"' \
--form 'range="20"```


#### Video
``` Video
https://drive.google.com/file/d/1Wdpwfs7kWlC7wkwIo9i-OsD6XUqqxNYo/view?usp=drivesdk
