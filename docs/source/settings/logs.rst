Logs
===========

You can check the error logs from this page. This is useful for troubleshooting issues with the plugins.

Each log entry will include the timestamp, log level, source, and message.

To download the logs, click on the **DOWNLOAD LOGS** button. This will download a compressed file containing all the log entries.

You can filter the logs by date, log level, and source using the search field.

Setting Log level
-----------------

You can set the log level for the entire application or for specific plugins.

- To set the log level for the entire application, set the value "pconn" for the component field.
- To set the log level for a specific plugin, set the value "pconn.plugins.<plugin_name>" for the component field, where "plugin_name" is the name of the plugin.

.. note::

    Press the **SAVE** button to apply the log level. This will persist the log level across restarts.
    Press the **RESET LOGS** button to revert to the default log level (Error).
