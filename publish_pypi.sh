#!/usr/bin/env bash
SCRIPT_DIR=$(dirname "$0")

USER=${USER:-marcus.rickert@web.de}
REPOSITORY_URL=${REPOSITORY_URL:-testpypi}
FILE=$(ls dist/*.tar.gz)
echo "Uploading $FILE as $USER to $REPOSITORY_URL..."
pip install twine
cd ${SCRIPT_DIR}
twine upload --repository-url ${REPOSITORY_URL} \
    --username ${USER} ${FILE}
