Azure Blob Storage plugin for `Tutor <https://docs.tutor.edly.io>`__
#########################################################################

Store Open edX assets on Azure Blob Storage using django-storages

Features
********

- Uses official django-storages Azure backend
- Support for both account key and connection string authentication  
- Custom domain support for CDN integration
- Well-maintained and battle-tested storage solution

Installation
************

.. code-block:: bash

   pip install git+https://github.com/so-jd/tutor-contrib-azure-blob

Usage
*****

1. **Enable the plugin:**

.. code-block:: bash

    tutor plugins enable azure-blob

2. **Configure Azure credentials:**

.. code-block:: bash

    tutor config save \
      --set RUN_AZURE_STORAGE=true \
      --set AZURE_ACCOUNT_NAME="youraccount" \
      --set AZURE_ACCOUNT_KEY="yourkey" \
      --set AZURE_CONTAINER_NAME="openedx"

3. **Build and restart:**

.. code-block:: bash

    tutor images build openedx
    tutor local restart

Configuration Variables
***********************

- ``RUN_AZURE_STORAGE``: Enable Azure storage (default: false)
- ``AZURE_ACCOUNT_NAME``: Azure storage account name
- ``AZURE_ACCOUNT_KEY``: Azure storage account key
- ``AZURE_CONNECTION_STRING``: Alternative to account name/key
- ``AZURE_CONTAINER_NAME``: Container name for file storage (default: "openedx")
- ``AZURE_CUSTOM_DOMAIN``: Custom domain/CDN URL

License
*******

This software is licensed under the terms of the AGPLv3.
