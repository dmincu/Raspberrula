#!/bin/bash

top  > topbuff &
kill -kill $(pidof top)
head -6 topbuff
rm topbuff
