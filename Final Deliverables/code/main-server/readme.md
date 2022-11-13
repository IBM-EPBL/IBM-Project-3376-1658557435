# Main Server (Nutrition assistant Application)

### Project structure

- **/pages** view
- **/controllers** logic
- **/models** DB model (data)
- **/utils** third party api methods

## How to execute?

### Get keys
----

**IBM DB2**

You can get credentials from [https://cloud.ibm.com/catalog/services/db2](https://cloud.ibm.com/catalog/services/db2)

Format of the IBM_DB_URL

```
DATABASE=<databasename>;HOSTNAME=<your-hostname>;PORT=<portnumber>;SECURITY=SSL;UID=<username>;PWD=<password>
```

**IBM Cloud Object Storage**

You can get credentials from [https://cloud.ibm.com/objectstorage/create](https://cloud.ibm.com/objectstorage/create)

Keys

```
COS_ENDPOINT=https://s3.jp-tok.cloud-object-storage.appdomain.cloud

COS_API_KEY_ID=<GET FROM IBM COS>

COS_INSTANCE_CRN=<GET FROM IBM COS>
```
**Spoonacular API**

You can get credentials from [https://spoonacular.com/food-api](https://spoonacular.com/food-api)

For more reference visit [here](https://github.com/ddsky/spoonacular-api-clients/tree/master/python)

Format of SPOONACULAR_API_KEY

```
bafif283hfndcdckkc
```

### Set ENV variable (⚠ use CMD)
----
set the following ENV variables with the following commands

```
set SERVER_SECRET=<SAME STRING USED IN AUTH SERVER>
set AUTH_SERVER_URL=http://127.0.0.1:<AUTH SERVER PORT>/
set AUTH_SERVER_REDIRECT_URL=http://127.0.0.1:<AUTH SERVER PORT>/

set DB2_URL=DATABASE=<databasename>;HOSTNAME=<your-hostname>;PORT=<portnumber>;SECURITY=SSL;UID=<username>;PWD=<password>

set COS_ENDPOINT=https://s3.jp-tok.cloud-object-storage.appdomain.cloud
set COS_API_KEY_ID=<GET FROM IBM COS>
set COS_INSTANCE_CRN=<GET FROM IBM COS>

set SPOONACULAR_BASE_URL=https://api.spoonacular.com/
set SPOONACULAR_API_KEY=<GET FROM SPOONACULAR API>

```

### Execute
----

- `cd ../../sprint1/app`
- `python install -r requirements.txt`
- `python -m flask run`  (or)  `python app.py`

## Routes

- http:/localhost:5000/
- http:/localhost:5000/my_history
- http:/localhost:5000/stats
- http:/localhost:5000/add_food
- http:/localhost:5000/add_food/upload_image
- http:/localhost:5000/add_food/add_details