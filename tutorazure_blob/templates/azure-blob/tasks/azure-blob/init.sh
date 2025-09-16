#!/bin/bash
set -e

echo "Initializing Azure Blob Storage..."

# Check if Azure CLI is available
if ! command -v az &> /dev/null; then
    echo "Azure CLI not found. Installing azure-cli..."
    pip install azure-cli
fi

# Check required environment variables
if [[ -z "${AZURE_CONTAINER_NAME}" ]]; then
    echo "Error: AZURE_CONTAINER_NAME environment variable is required"
    exit 1
fi

# Authenticate with Azure using either connection string or account credentials
if [[ -n "${AZURE_CONNECTION_STRING}" ]]; then
    echo "Using Azure connection string for authentication"
    # Extract account name from connection string for az cli
    ACCOUNT_NAME=$(echo "${AZURE_CONNECTION_STRING}" | grep -oP 'AccountName=\K[^;]*')
    ACCOUNT_KEY=$(echo "${AZURE_CONNECTION_STRING}" | grep -oP 'AccountKey=\K[^;]*')
elif [[ -n "${AZURE_ACCOUNT_NAME}" && -n "${AZURE_ACCOUNT_KEY}" ]]; then
    echo "Using Azure account name and key for authentication"
    ACCOUNT_NAME="${AZURE_ACCOUNT_NAME}"
    ACCOUNT_KEY="${AZURE_ACCOUNT_KEY}"
else
    echo "Error: Either AZURE_CONNECTION_STRING or both AZURE_ACCOUNT_NAME and AZURE_ACCOUNT_KEY are required"
    exit 1
fi

# Check if container exists
echo "Checking if container '${AZURE_CONTAINER_NAME}' exists..."
if az storage container exists \
    --name "${AZURE_CONTAINER_NAME}" \
    --account-name "${ACCOUNT_NAME}" \
    --account-key "${ACCOUNT_KEY}" \
    --output tsv 2>/dev/null | grep -q "True"; then
    echo "✅ Container '${AZURE_CONTAINER_NAME}' already exists"
else
    echo "📦 Creating container '${AZURE_CONTAINER_NAME}'..."
    az storage container create \
        --name "${AZURE_CONTAINER_NAME}" \
        --account-name "${ACCOUNT_NAME}" \
        --account-key "${ACCOUNT_KEY}" \
        --public-access off \
        --output none
    echo "✅ Container '${AZURE_CONTAINER_NAME}' created successfully"
fi

echo "Azure Blob Storage initialization completed"