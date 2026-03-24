Hikvision Openapi
=================

Overview
--------    

This platform manages ``Persons`` in HikCentral using OpenAPI.

Configuration
-------------

Start by adding a plugin that uses this platform


- Host (Required): The hostname or IP address of the HikCentral server.
- Port (Required): The port on which the HikCentral server is listening (default: 443).
- User Key (Required): The User key for authenticating with the HikCentral OpenAPI.
- User Secret (Required): The User secret for authenticating with the HikCentral OpenAPI.

.. note::

    Refer the `Hikvision OpenAPI documentation <https://pinfo.hikvision.com/hkwsen/unzip/20240806113350_60387_doc/index.html?guid=GUID-055468AB-671B-447F-87D7-6469B510EDB5.html&hl=installation>`_ for more details about how to obtain the User Key and User Secret.


Functionality
-------------

This platform uses the ``hikcentral-openapi`` python package to interact with HikCentral. Refer to the `package documentation <https://pypi.org/project/hikcentral-openapi/>`_ for more details.

