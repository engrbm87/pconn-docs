Gallagher Hikvision Plugin
==========================

Overview
--------

This plugin syncs the cardholders from Gallagher Command Center to HikCentral as ``Persons``.
Each person will have his ``Face Photo``, ``Card Number``, and ``Access Level`` mapped from Command Center.
The plugin is designed to perform a one-way sync from Command Center to HikCentral, meaning that any changes made to the cardholders in Command Center will be reflected in HikCentral. Changes done manually in HikCentral might get overridden by the plugin during the sync process.

With this plugin the site can install **Hikvision Face readers** connected to Gallagher control panels using Wiegand (or OSDP if the OSDP port used by the reader is supported by the Gallagher controller) and have the cardholders configured in Command Center pushed to the readers through HikCentral.

Licensing
---------

- The license should include ``gallagher_hikvision`` under the "plugins" section.
- This plugin has a limit on the `number of cardholders` that are synced.

Platform requirements
---------------------

- Gallagher Command Center **9.00+** with ``RESTCardholders=1`` included in the Command Center license file.
- HikCentral version that supports OpenAPI **V2.6.1+**. The HikCentral license should include Access Control feature.

Configuration
-------------

1. Navigate to Settings → Plugin Entries
2. Click on ``Add Plugin`` button
3. Select **Gallagher Hikvision** from the list
4. Configure the connection to Gallagher Command Center. Refer to (:doc:`/platforms/gallagher-rest`)
5. Configure the HikCentral connection. Refer to (:doc:`/platforms/hikvision-openapi`)
6. The configuration is done and the plugin is loaded.

Options
-------

This plugin options allow you to enable/disable the item types that should be exposed as BACnet points. Below the currently available types:

- **Unique ID Field**: Personal data field with type ``text`` and ``unique`` option enabled to hold the ``Person`` internal ID coming from HikCentral.
- **Photo field**: Personal data field with type ``image`` that will hold the cardholder face image to be pushed to HikCentral.
- **Card Type**: Cards of this card type will be assigned as card numbers to the ``Person`` in HikCentral.


Dashboard
---------

- The plugin dashboard displays a summary of the sync status, including:
  - Total number of synced cardholders
  - Total number of failed cardholders
  - Total number of skipped cardholders
- A ``Start Sync`` button that should be clicked to initialize the sync for the first time.
- A ``Resync`` button that will clear the current sync data and start over.
- ``Pause Sync`` and ``Resume Sync`` buttons are provided to pause/resume the delta sync process.
- A panel showing the list of access groups that are assigned to the cardholders being synced. The ones showing in red are not currently configured in HikCentral as access levels.


Configuration Prerequisites
---------------------------

Gallagher Command Center:
^^^^^^^^^^^^^^^^^^^^^^^^^

- A personal data field with type ``text`` and ``unique`` option enabled must be configured and assigned to any access group that contains cardholders to be synced. This field will be used to store the internal ID of the corresponding ``Person`` in HikCentral. This field should not be modified by the operators.
- A personal data field with type ``image`` must be configured and assigned to any access group that contains cardholders to be synced. This field will be used to store the face image of the corresponding ``Person`` in HikCentral. This uploaded image should meet the HikCentral requirements for face images to ensure a successful identification at the reader.
- An existing card type or a new card type can be used for the cardholders that shall be synced with HikCentral. The card number assigned to the cardholder will be pushed to HikCentral and stored in the ``Person`` as a credential. Upon successful identification, the Hikvision Face Reader will send that card number to the control panel to grant/deny access.

.. note::

    - If the site wants to use card as a credential in addition to the face on the Hikvision readers, the card number detected by the reader should match the card number assigned to the ``Person`` in HikCentral. To achieve that, the cardholder in Command Center must have the same card number assigned using the selected ``card type``. For that case, it is recommended to configure a new card type with a dummy Facility code (e.g. A00010) and use it when assigning a card number to the cardholder. This number will be the identifier for this cardholder whether the face or card is presented at the reader.

HikCentral:
^^^^^^^^^^^

- All readers must be initialized and configured in HikCentral.
- The access groups assigned to the cardholders in Command Center must be already configured in HikCentral. The plugin will try to match the access level names coming from Command Center with the ones in HikCentral.
  
.. note::

    Each access level should have the corresponding readers assigned. This will allow HikCentral to push the persons to the corresponding readers based on their assigned access levels. Do note that the reader will show a success when a valid face is identified but the Gallagher controller is still the decision maker for granting/denying access.
    In case the face is not identified, no data is sent to the controller and event will be recorded in Command Center. (HikCentral might have these events recorded as failed access attempts)


Functionality
-------------

The plugin performs a one-way sync from Gallagher Command Center to HikCentral. The sync process includes the following steps:

1. Clicking ``Start Sync`` for the first time will retrieve the list of cardholders from Gallagher Command Center using REST API.
2. For each cardholder, the plugin will do the following checks:
   - Lookup the unique ID field value to find if there is an existing ``Person`` in HikCentral that corresponds to this cardholder. If found, the plugin will update the existing ``Person`` with the new values from Command Center.
   - Else, the plugin will check if the cardholder meets the criteria to be synced:

     - Check if the cardholder has a filled out face image. If no image is found the cardholder is skipped.
     - Check if the cardholder has a card assigned with the specified card type. If no card is found the cardholder is skipped.

.. note::

      A skipped counter is used to indicate the number of skipped cardholders.

1. If the cardholder meets the criteria, create/update a corresponding ``Person`` in HikCentral with the mapped fields (unique ID, photo, card number).
2. If the plugin is not able to create/update the ``person`` in HikCentral an error is logged and the ``failed`` counter will be incremented.
3. The plugin will keep track of the sync status and display it in the dashboard.
4. Once the initial sync is completed, the plugin will start listening for cardholder changes in Command Center and sync the same with HikCentral. (The ``Pause Sync`` and ``Resume Sync`` buttons can be used to pause/resume this functionality)
5. If a cardholder is deleted in Command Center, the corresponding ``Person`` in HikCentral will be deleted as well.

License limit considerations
----------------------------

Only ``synced`` cardholders count towards the license limit. If the limit is reached the plugin will automatically stop within 30 minutes. To avoid reaching the limit, the site can do the following: 

   - Consider using divisions to isolate the group of cardholders that the REST API assigned operator has access to.
   - The plugin will skip cardholders that don't have a card of the specified card type assigned to them. If the site is using a dedicated card type, only assign a card number to the ones that should be synced. 
   - The plugin will also skip cardholders that don't have a face image stored in the specified personal field.

If the limit is reached and the plugin stops, the site can either reduce the number of synced cardholders by following the above recommendations and then reload the plugin, or they can purchase an updated license with a higher limit and apply it then reload the plugin.
