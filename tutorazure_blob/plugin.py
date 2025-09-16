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


########################################
# INITIALIZATION TASKS
########################################

# To add a custom initialization task, create a bash script template under:
# {{ cookiecutter.module_name }}/templates/{{ cookiecutter.plugin_name }}/tasks/
# and then add it to the MY_INIT_TASKS list. Each task is in the format:
# ("<service>", ("<path>", "<to>", "<script>", "<template>"))
MY_INIT_TASKS: list[tuple[str, tuple[str, ...]]] = [
    ("lms", ("azure-blob", "tasks", "azure-blob", "init.sh")),
]


# For each task added to MY_INIT_TASKS, we load the task template
# and add it to the CLI_DO_INIT_TASKS filter, which tells Tutor to
# run it as part of the `init` job.
for service, template_path in MY_INIT_TASKS:
    full_path: str = str(
        importlib_resources.files("tutorazure_blob")
        / os.path.join("templates", *template_path)
    )
    with open(full_path, encoding="utf-8") as init_task_file:
        init_task: str = init_task_file.read()
    tutor_hooks.Filters.CLI_DO_INIT_TASKS.add_item((service, init_task), priority=tutor_hooks.priorities.HIGH) # needs to initlize early in the launch sequance


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
