#!/bin/sh
mkdir -p tmp/db
cp -a db/* tmp/db
cp update_script tmp/
cp dbaccess tmp/
cd tmp
find . -not -name '.DS_Store' -not -name '*.sha256' -type f -print0 | xargs -0 sha256sum >dbaccess-2.0b4.sha256
tar --owner=root --group=root --exclude=.DS_Store -czvf ../dbaccess-2.0b4.tar.gz *
cd ..
rm -rf tmp
