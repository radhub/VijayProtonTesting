#!/usr/bin/env python3

from aws_cdk import core

from vijay_cdk_project.vijay_cdk_project_stack import VijayCdkProjectStack


app = core.App()
VijayCdkProjectStack(app, "vijay-cdk-project")

app.synth()
