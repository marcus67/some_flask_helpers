#!/usr/bin/env bash
SCRIPT_DIR=$(dirname "$0")

USER=${USER:-__token__}
REPOSITORY_URL=${REPOSITORY_URL:-https://test.pypi.org/legacy/}
FILE=$(ls dist/*.tar.gz)
echo "Uploading $FILE as $USER to $REPOSITORY_URL..."
pip install twine
cd ${SCRIPT_DIR}
twine upload --repository-url ${REPOSITORY_URL} \
    --username ${USER} ${FILE}
