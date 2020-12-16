from aws_cdk import (
    aws_s3 as _s3, 
    core
)


class VijayCdkProjectStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, is_prod=False, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        if is_prod:
          artifactBucket = _s3.Bucket(
            self,
            "myProdArtifactBucketID", 
            versioned=True,
            encryption=_s3.BucketEncryption.S3_MANAGED,
            removal_policy=core.RemovalPolicy.RETAIN
        ) 
        else:
          artifactBucket = _s3.Bucket(
            self,
            "myDevArtifactBucketID"
        ) 
