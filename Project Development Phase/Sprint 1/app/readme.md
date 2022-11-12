# Auth Server (Nutrition assistant Application)

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

**Courier (Mail Service)**

- Create account in [https://www.courier.com](https://www.courier.com)
- Integrate Gmail into the courier platform. [How to integrate gmail?](https://www.courier.com/docs/guides/providers/email/gmail/)
- get auth key from Courier [How to get?](https://www.courier.com/docs/reference/authorization/)
- For more reference, refer [docs](https://www.courier.com/docs/)

Format of the Courier auth key

```
pk_prod_xxxxxxyyyyyy
```

### Set ENV variable (⚠ use CMD)
----
set the following ENV variables with the following commands

```
set SERVER_SECRET=<RANDOM STRING>
```

```
set DB2_URL=DATABASE=<databasename>;HOSTNAME=<your-hostname>;PORT=<portnumber>;SECURITY=SSL;UID=<username>;PWD=<password>
```

```
set COURIER_AUTH_KEY=pk_prod_xxxxxxyyyyyy
```

MAIN_SERVER_REDIRECT_URL is the url of the main server

```
set MAIN_SERVER_REDIRECT_URL=http://localhost:<MAIN SERVER PORT>/
```

(or) you can set `/main` for testing

```
set MAIN_SERVER_REDIRECT_URL=/main
```

### Execute
----

- `cd ../../sprint1/app`
- `python install -r requirements.txt`
- `python -m flask run`  (or)  `python app.py`

## Routes

- http:/localhost:5000/
- http:/localhost:5000/login
- http:/localhost:5000/register
- http:/localhost:5000/verify
- http:/localhost:5000/isvalid (only authorized access)
- http:/localhost:5000/main