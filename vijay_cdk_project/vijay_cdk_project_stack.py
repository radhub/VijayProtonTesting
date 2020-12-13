from aws_cdk import (
    aws_s3 as _s3, 
    aws_iam as _iam,
    core
)


class VijayCdkProjectStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        _s3.Bucket(
            self, # Logical identifier
            "VijayBucketID",
            bucket_name="vijay-cdk-testing",
            versioned=False,
            encryption=_s3.BucketEncryption.S3_MANAGED,
            block_public_access=_s3.BlockPublicAccess.BLOCK_ALL
        )
        
        mybucket = _s3.Bucket(
            self,
            "VijayBucketID-1",
	)

        output_1 = core.CfnOutput(
            self,
            "VijayBucketOutput1",
            value=mybucket.bucket_name,
            description=f"My First CDK Bucket",
            export_name="VijayBucketOutput1"
        )

        _iam.Group(
            self,
            "VijayGroupID"
        )
