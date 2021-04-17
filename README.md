# ShorelineIoT

Step 1: Clone project repository
    git clone url

Step 2: Create Virtual Environment and activate.
    virtualenv -p /usr/bin/python3.7 venv
    source venv/bin/activate

Step 3: Install all requirements.
    pip3 install -r requirement.txt

Step 4: Create local postgres database and give access to user.

Step 5: Migrate models in database.
    python manage.py migrate

Step 6: Create SuperUser.
    python manage.py createsuperuser

Step 7: Use below APIs to run code.

1. Get JWT token and Provide access token to each API:
    endpoints: localhost:8000/token/
    method: POST
    payload:
        {
            "username": "admin@admin.com",
            "password": "Admin123"
        }

2. Create Device
    endpoints: localhost:8000/api/create/device/
    method: POST
    payload:
        {
            "device_name":"AC - LG"
        }

3. Update Device
    endpoints: localhost:8000/api/update/device/
    method: PUT
    payload:
        {
            "unique_id":5,
            "device_name":"AC - LG"
        }

4. Create Sensor Data
    endpoints: localhost:8000/api/create/sensor/data/
    method: PUT
    payload:
        {
            "unique_id":13,
            "data":"data for sensor 13"
        }

5. Get Particular Sensor Data
    endpoints: localhost:8000/api/get/sensor/data/
    method: POST
    payload:
        {
            "from_date":"2021-04-17 11:34:47",
            "to_date":"2021-04-17 18:34:50",
            "sensor_type":1
        }
