#! /bin/bash

. ${TOOLDIR}/www/env/bin/activate
eval flask run $@
