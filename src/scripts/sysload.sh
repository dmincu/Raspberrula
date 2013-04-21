#!/bin/bash

top -n 1 -b > topbuff
sed -n '2,7p' topbuff > headbuff
cat headbuff
rm topbuff
rm headbuff
