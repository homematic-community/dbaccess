#!/bin/sh
mkdir -p tmp/db
cp -a db/* tmp/db
cp update_script tmp/
cp dbaccess tmp/
cd tmp
tar -czvf ../dbaccess-2.0b3.tar.gz *
cd ..
rm -rf tmp
