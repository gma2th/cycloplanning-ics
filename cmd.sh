#!/bin/sh

cycloplanning -o cycloplanning.ics && aws s3api put-object --bucket cycloplanning --key cycloplanning.ics --body cycloplanning.ics
