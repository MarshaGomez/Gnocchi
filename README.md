
# Cloud Computing

An OpenStack instance implemented the Gnocchi open-source time series database with Ceph. Two types of applications were developed in this repository.

- Consumer development using [DJango Web Framework](https://www.djangoproject.com/) that retrieved from Gnocchi REST API periodically some aggregated values like average, max, min, sum, std, count;  
- Producer development with [Python](https://www.python.org/) that store on Gnocchi REST API random numbers for three different metrics: _Tempeture_, _Huminity_, _Wind Speed_

## Gnocchi

Gnocchi is an open-source time series database.

The problem that Gnocchi solves is the storage and indexing of time series data and resources at a large scale. This is useful in modern cloud platforms which are not only huge but also are dynamic and potentially multi-tenant. Gnocchi takes all of that into account.

Gnocchi has been designed to handle large amounts of aggregates being stored while being performant, scalable and fault-tolerant. While doing this, the goal was to be sure to not build any hard dependency on any complex storage system.

Gnocchi takes a unique approach to time series storage: rather than storing raw data points, it aggregates them before storing them. This built-in feature is different from most other time series databases, which usually support this mechanism as an option and compute aggregation (average, minimum, etc.) at query time.

Because Gnocchi computes all the aggregations at ingestion, getting the data back is extremely fast, as it just needs to read back the pre-computed results.

## Poject Specifications

### OpenStack: Timeseries as a service

Install an OpenStack instance the Gnocchi database and create two simple applications, one consumer and one producer, that exploit the REST interface exposed by Gnocchi to  the data. The producer must mimic the periodic production of measurement data (random data is OK) to be stored in the timeseries database, the consumer must retrieve periodically some aggregated values like average, max, min, sum, std, count.

You can read the full documentation online:

- [Gnocchi official documentation](http://gnocchi.osci.io)
- [Gnocchi installation](https://jaas.ai/gnocchi/37)
- [Gnocchi REST interface](https://gnocchi.xyz/rest.html)

### Application Screenshot

- Index

On this web page you can see the three different metrics _Tempeture_, _Huminity_, _Wind Speed_

![Index](documentation/img/Gnocchi-index.PNG)

- Tempeture Graph

![Tempeture](documentation/img/Gnocchi-Graphical-Tempeture.PNG)

- Huminity Graph

![Huminity](documentation/img/Gnocchi-Graphical-Huminity.PNG)

- Wind Speed Graph

![Wind Speed](documentation/img/Gnocchi-Graphical-WindSpeed.PNG)
