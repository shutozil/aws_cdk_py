#!/bin/bash

# モジュールのimport
cd cdk && pip install --upgrade pip && pip install -r requirements.txt

# aws関連
## default (development)
aws configure set aws_access_key_id $DEV_AWS_ACCESS_KEY_ID
aws configure set aws_secret_access_key $DEV_AWS_SECRET_ACCESS_KEY
aws configure set region $CDK_DEFAULT_REGION
aws configure set output json

## staging
aws configure set aws_access_key_id $STG_AWS_ACCESS_KEY_ID --profile staging
aws configure set aws_secret_access_key $STG_AWS_SECRET_ACCESS_KEY --profile staging
aws configure set region $CDK_DEFAULT_REGION --profile staging
aws configure set output json --profile staging

## production
aws configure set aws_access_key_id $STG_AWS_ACCESS_KEY_ID --profile production
aws configure set aws_secret_access_key $STG_AWS_SECRET_ACCESS_KEY --profile production
aws configure set region $CDK_DEFAULT_REGION --profile production
aws configure set output json --profile production
