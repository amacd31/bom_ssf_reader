Seasonal Streamflow Forecast web access
=======================================

Basic library for reading Seasonal Streamflow Forecasts supplied by the Australian Bureau of Meteorology.

For the most part this library provides a wrapper around Pandas read methods. This saves effort when trying to get the arguments right when accessing some semi-standard formats available from the Bureau of Meteorology.

Dependencies
------------

Requires Python 2.7, 3.4 or greater (mostly tested with Python 2.7 on Linux). Also depends on the bom_data_parser package: https://github.com/amacd31/bom_data_parser

Usage
-----

The SSFReader class can be imported then instantiated as an object containing meta-information about the available forecast locations. Site information for all available locations are stored on the object after instantiation. Forecasts are retrived from the Bureau of Meterology web site on each request for the the forecast data.

.. code:: python

    from datetime import date

    import bom_ssf_reader
    ssf_reader = bom_ssf_reader.SSFReader()

    ssf_reader.get_site_info('410730')
    ssf_reader.get_forecast('410730', date(2016,1,1))

Notes
-----

This is an experiment against what is currently available on the Bureau of Meterology website and should not be considered a stable API.
