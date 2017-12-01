#!/bin/bash
#
BASEDIR=$(cd "$(dirname "$0")"; pwd)
# source $BASEDIR/env_dev.sh
# ln -sf  $BASEDIR/gateway/dev_settings.py $BASEDIR/gateway/settings.py
python $BASEDIR/manage.py runserver 0.0.0.0:$1
