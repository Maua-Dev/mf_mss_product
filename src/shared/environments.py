import enum
from enum import Enum
import os

from src.shared.domain.repositories.product_repository_interface import IProductRepository
from src.shared.domain.repositories.user_repository_interface import IUserRepository



class STAGE(Enum):
    DOTENV = "DOTENV"
    DEV = "DEV"
    HOMOLOG = "HOMOLOG"
    PROD = "PROD"
    TEST = "TEST"


class Environments:
    """
    Defines the environment variables for the application. You should not instantiate this class directly. Please use Environments.get_envs() method instead.

    Usage:

    """
    stage: STAGE
    s3_bucket_name: str
    region: str
    endpoint_url_product: str = None
    endpoint_url_user: str = None
    dynamo_table_name_product: str
    dynamo_table_name_user: str
    dynamo_partition_key: str
    dynamo_sort_key: str
    cloud_front_distribution_domain: str
    s3_assets_cdn: str

    def _configure_local(self):
        from dotenv import load_dotenv
        load_dotenv()
        os.environ["STAGE"] = os.environ.get("STAGE") or STAGE.DOTENV.value

    def load_envs(self):
        if "STAGE" not in os.environ or os.environ["STAGE"] == STAGE.DOTENV.value:
            self._configure_local()

        self.stage = STAGE[os.environ.get("STAGE")]

        if self.stage == STAGE.TEST:
            self.s3_bucket_name = "bucket-test"
            self.region = "sa-east-1"
            self.endpoint_url_product = "http://localhost:8000"
            self.endpoint_url_user = "http://localhost:8000"
            self.dynamo_table_name_product = "mf_mss_product-table"
            self.dynamo_table_name_user = "mf_mss_user-table"
            self.dynamo_partition_key_product = "PK"
            self.dynamo_sort_key_product = "SK"
            self.dynamo_partition_key_user = "PK"
            # self.dynamo_sort_key_user = "SK"
            self.s3_assets_cdn = "https://mauafood-assets.cloudfront.net/"
            self.cloud_front_distribution_domain = "https://d3q9q9q9q9q9q9.cloudfront.net"
            self.dynamo_gsi_partition_key = "GSI1-PK"
            self.dynamo_gsi_sort_key = "GSI1-SK"

        else:
            self.s3_bucket_name = os.environ.get("S3_BUCKET_NAME")
            self.s3_assets_cdn = os.environ.get("S3_ASSETS_CDN")
            self.region = os.environ.get("AWS_REGION")
            self.endpoint_url_product = os.environ.get("ENDPOINT_URL_PRODUCT")
            self.endpoint_url_user = os.environ.get("ENDPOINT_URL_USER")
            self.dynamo_table_name_product = os.environ.get("DYNAMO_TABLE_NAME_PRODUCT") 
            self.dynamo_table_name_user = os.environ.get("DYNAMO_TABLE_NAME_USER") 
            self.dynamo_partition_key_product = os.environ.get("DYNAMO_PARTITION_KEY")
            self.dynamo_sort_key_product = os.environ.get("DYNAMO_SORT_KEY")
            self.dynamo_partition_key_user = os.environ.get("DYNAMO_PARTITION_KEY")
            # self.dynamo_sort_key_user = os.environ.get("DYNAMO_SORT_KEY")
            self.cloud_front_distribution_domain = os.environ.get("CLOUD_FRONT_DISTRIBUTION_DOMAIN")
            self.dynamo_gsi_partition_key = os.environ.get("DYNAMO_GSI_PARTITION_KEY")
            self.dynamo_gsi_sort_key = os.environ.get("DYNAMO_GSI_SORT_KEY")

    @staticmethod
    def get_product_repo() -> IProductRepository:
        if Environments.get_envs().stage == STAGE.TEST:
            from src.shared.infra.repositories.product_repository_mock import ProductRepositoryMock
            return ProductRepositoryMock
        elif Environments.get_envs().stage in [STAGE.PROD, STAGE.DEV, STAGE.HOMOLOG]:
            from src.shared.infra.repositories.product_repository_dynamo import ProductRepositoryDynamo
            return ProductRepositoryDynamo        
        else:
            raise Exception("No repository found for this stage")
        
    @staticmethod
    def get_user_repo() -> IUserRepository:
        if Environments.get_envs().stage == STAGE.TEST:
            from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock
            return UserRepositoryMock
        elif Environments.get_envs().stage in [STAGE.PROD, STAGE.DEV, STAGE.HOMOLOG]:
            from src.shared.infra.repositories.user_repository_dynamo import UserRepositoryDynamo
            return UserRepositoryDynamo
        else:
            raise Exception("No repository found for this stage")


    @staticmethod
    def get_envs() -> "Environments":
        """
        Returns the Environments object. This method should be used to get the Environments object instead of instantiating it directly.
        :return: Environments (stage={self.stage}, s3_bucket_name={self.s3_bucket_name}, region={self.region}, endpoint_url={self.endpoint_url})

        """
        envs = Environments()
        envs.load_envs()
        return envs

    def __repr__(self):
        return self.__dict__