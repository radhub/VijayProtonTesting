#!/usr/bin/env python3

from aws_cdk import core

from vijay_cdk_project.vijay_cdk_project_stack import VijayCdkProjectStack

env_IN = core.Environment(region="ap-south-1")
app = core.App()
VijayCdkProjectStack(app, "vijay-cdk-project-dev", env=env_IN)
VijayCdkProjectStack(app, "vijay-cdk-project-prod", is_prod=True, env=env_IN)

app.synth()
