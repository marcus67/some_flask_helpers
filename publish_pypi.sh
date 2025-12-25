#!/usr/bin/env bash
SCRIPT_DIR=$(dirname "$0")

USER=${USER:-__token__}
TARGET=${1:-TEST}

if [ "$TARGET" == "TEST" ] ; then
  REPOSITORY="--repository-url https://test.pypi.org/legacy/"
fi

FILE=$(ls dist/*.tar.gz)
echo "Uploading $FILE as $USER to $REPOSITORY_URL..."
pip install twine
cd ${SCRIPT_DIR}
twine upload --verbose ${REPOSITORY} \
    ${FILE}
