#!/bin/bash

lspci -v -s `lspci | awk '/VGA/{print $1}'`
