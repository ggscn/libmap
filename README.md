# libmap

This project is an open source prototype of [libmap.dev](https://libmap.dev), which gives the user the ability to map locations mentioned in public domain books. At a high level, the app works by using the gdelt hathitrust dataset to obtain locations, which are then mapped to an OpenLayer OSM map.

## Running the app
To run this application, you must do the following:

* Set the `GOOGLE_APPLICATION_CREDENTIALS` to the path of your service_account.json. This lets you authenticate with Google BigQuery
* Set the `FLASK_APP` environment variable to the path folder containing the app.py file.
* Install the python3 dependencies in the requirements.txt file using `pip3 install -r requirements.txt`
* Run using `python3 -m flask run `
