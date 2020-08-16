#!/usr/bin/env python3

from aws_cdk import core

from cdk.test_cdk_project_stack import TestCdkProjectStack


app = core.App()
TestCdkProjectStack(app, "test-cdk-project", env={'region': 'ap-northeast-1'})

app.synth()
