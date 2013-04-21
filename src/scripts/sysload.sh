#!/bin/bash

top -n 1 > topbuff
head -6 topbuff
rm topbuff
