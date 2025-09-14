from __future__ import annotations
from glob import glob
import os
import importlib_resources

from tutor import hooks as tutor_hooks
from .__about__ import __version__

########################################
# CONFIGURATION
########################################

tutor_hooks.Filters.CONFIG_DEFAULTS.add_items([
    ("AZURE_ACCOUNT_NAME", ""),
    ("AZURE_ACCOUNT_KEY", ""),
    ("AZURE_CONNECTION_STRING", ""),
    ("AZURE_CONTAINER_NAME", "openedx"),
    ("AZURE_CUSTOM_DOMAIN", ""),
    ("RUN_AZURE_STORAGE", False),
    ("AZURE_BLOB_VERSION", __version__),
])

# No unique configs needed for Azure Blob Storage


# No initialization tasks needed for Azure Blob Storage


# No custom images needed for Azure Blob Storage


# No build context needed - using django-storages


########################################
# PATCH LOADING
########################################

# Load all patch files from patches directory
patch_files = glob(
    os.path.join(
        str(importlib_resources.files("tutorazure_blob")),
        "patches",
        "*",
    )
)
for path in patch_files:
    with open(path, encoding="utf-8") as patch_file:
        tutor_hooks.Filters.ENV_PATCHES.add_item((os.path.basename(path), patch_file.read()))


# No custom jobs or CLI commands needed for Azure Blob Storage
