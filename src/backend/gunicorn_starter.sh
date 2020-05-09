#!/bin/sh

#ifconfig
gunicorn task-server:app -w 1 -b 0.0.0.0:8000