import os

from aws_cdk import (
    aws_s3, aws_s3_notifications, aws_lambda,
    aws_stepfunctions,
    aws_stepfunctions_tasks,
    aws_events, aws_events_targets,
    aws_cloudfront, aws_cloudfront_origins, RemovalPolicy
)

from constructs import Construct


class BucketStack(Construct):
    s3_bucket: aws_s3.Bucket
    selfie_validation_step_function: aws_stepfunctions.StateMachine
    cloudfront_distribution: aws_cloudfront.Distribution

    def __init__(self, scope: Construct) -> None:
        super().__init__(scope, "MauaFood_Product_Bucket")

        self.github_ref_name = os.environ.get("GITHUB_REF_NAME")

        REMOVAL_POLICY = RemovalPolicy.RETAIN if 'prod' in self.github_ref_name else RemovalPolicy.DESTROY

        self.s3_bucket = aws_s3.Bucket(self, "MauaFood_Product_Photo_S3_Bucket",
                                       versioned=True,
                                       block_public_access=aws_s3.BlockPublicAccess.BLOCK_ALL,
                                       event_bridge_enabled=True,
                                       cors=[aws_s3.CorsRule(
                                             allowed_methods=[
                                                 aws_s3.HttpMethods.GET, aws_s3.HttpMethods.PUT, aws_s3.HttpMethods.POST],
                                             allowed_origins=["*"],
                                             allowed_headers=["*"],
                                             max_age=3000
                                             )],
                                       removal_policy=REMOVAL_POLICY
                                       )

        oai = aws_cloudfront.OriginAccessIdentity(self, "MauaFood_Product_Photo_OAI",
                                                  comment="This is MauaFood product photo OAI")
        
        self.s3_bucket.grant_read_write(oai)

        self.cloudfront_distribution = aws_cloudfront.Distribution(self, "MauaFood_Product_Photo_CloudFront_Distribution",
                                                                     default_behavior=aws_cloudfront.BehaviorOptions(
                                                                          origin=aws_cloudfront_origins.S3Origin(
                                                                            self.s3_bucket,
                                                                            origin_access_identity=oai),
                                                                          origin_request_policy=aws_cloudfront.OriginRequestPolicy.CORS_S3_ORIGIN,
                                                                          viewer_protocol_policy=aws_cloudfront.ViewerProtocolPolicy.REDIRECT_TO_HTTPS,
                                                                          response_headers_policy=aws_cloudfront.ResponseHeadersPolicy.CORS_ALLOW_ALL_ORIGINS,
                                                                          cache_policy=aws_cloudfront.CachePolicy.CACHING_OPTIMIZED,
                                                                          allowed_methods=aws_cloudfront.AllowedMethods.ALLOW_ALL
                                                                     )
                                                                     )

        # oac = aws_cloudfront.CfnOriginAccessControl(self, "MauaFood_Product_Photo_OAC",
        #                                             origin_access_control_config=aws_cloudfront.CfnOriginAccessControl.OriginAccessControlConfigProperty(
        #                                                 name="MauaFood_Bucket_OAC_" + self.github_ref_name,
        #                                                 origin_access_control_origin_type="s3",
        #                                                 signing_behavior="always",
        #                                                 signing_protocol="sigv4",

        #                                                 description="This is MauaFood product photo OAC"
        #                                             ))

        # self.cloudfront_distribution = aws_cloudfront.Distribution(self, "MauaFood_Product_Photo_CloudFront_Distribution",
        #                                                            default_behavior=aws_cloudfront.BehaviorOptions(
        #                                                                origin=aws_cloudfront_origins.S3Origin(
        #                                                                    self.s3_bucket,
        #                                                                    origin_access_control=oac),
        #                                                                origin_request_policy=aws_cloudfront.OriginRequestPolicy.CORS_S3_ORIGIN,
        #                                                                viewer_protocol_policy=aws_cloudfront.ViewerProtocolPolicy.REDIRECT_TO_HTTPS,
        #                                                                response_headers_policy=aws_cloudfront.ResponseHeadersPolicy.CORS_ALLOW_ALL_ORIGINS,
        #                                                                cache_policy=aws_cloudfront.CachePolicy.CACHING_OPTIMIZED,
        #                                                                allowed_methods=aws_cloudfront.AllowedMethods.ALLOW_ALL
        #                                                            )
        #                                                            )

        # cfn_distribution = self.cloudfront_distribution.node.default_child

        # cfn_distribution.addPropertyOverride(
        #     'DistributionConfig.Origins.0.OriginAccessControlId', oac.getAtt('Id'))
