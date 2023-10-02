#!/bin/bash

cd ./src
python tests.py >> "../test_report.html"
echo "Report generated to test_repot.html"
