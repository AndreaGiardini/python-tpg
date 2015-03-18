Python-tpg
==========

This library gives access to [TPG api](http://www.tpg.ch/web/open-data/donnees-tpg) for python.
Through this module we are able to query the Api and get the tram/bus schedule in the area of Geneva.

The module is just a draft and some functionalities might not work as expected, feel free to open an issue or pull request if you find any problem.

How to use it
-------------

First of all to use this module you need to [request an Apikey](http://www.tpg.ch/fr/web/open-data/demande-de-cle)   
Once you receive your key you can start using this module following the example:

```
import tpg
tpgClient = tpg.Client(myapikey)
print tpgClient.getNextDepartures("CERN")
```

API Documentation
-----------------

You can find all the API documentation on [TPG website](http://www.tpg.ch/documents/7289503/7461091/Opendata_tpg_documentation_utilisateurs_v11.pdf)

