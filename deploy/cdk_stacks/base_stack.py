import shutil
import subprocess
from pathlib import Path
from typing import Self

from aws_cdk import Stack, aws_apigateway, aws_lambda
from constructs import Construct

APP_PATH = Path(__file__).parent.parent.parent / "app"


class WhastMyIp(Stack):
    def __init__(self: Self, scope: Construct, identifier: str) -> None:
        super().__init__(scope, identifier)

        handler = aws_lambda.Function(
            self,
            "Function",
            runtime=aws_lambda.Runtime.PYTHON_3_12,
            code=aws_lambda.Code.from_asset(str(APP_PATH / "app")),
            handler="app.ip_utils.lambda_handler",
            layers=[self.lambda_layers_for_dependencies()],
        )

        api = aws_apigateway.RestApi(
            self,
            "Gateway",
            rest_api_name="WhatsMyIp",
            description="This service tells you information based on your IP.",
        )

        lambda_integration = aws_apigateway.LambdaIntegration(
            handler, request_templates={"application/json": '{ "statusCode": "200" }'}
        )

        api.root.add_method("GET", lambda_integration)  # GET /

    def lambda_layers_for_dependencies(self: Self) -> aws_lambda.LayerVersion:
        target_folder = ".lambda_layer"
        requirements_file = "requirements.txt"
        commands = [
            ["poetry", "export", "-f", requirements_file, "-o", requirements_file],
            ["pip", "install", "-r", requirements_file, "-t", target_folder],
        ]
        if (APP_PATH / target_folder).exists():
            shutil.rmtree(str(APP_PATH / target_folder))

        for command in commands:
            subprocess.check_call(command, cwd=str(APP_PATH))  # noqa: S603

        code = aws_lambda.Code.from_asset(str(APP_PATH / target_folder))

        return aws_lambda.LayerVersion(self, "app_dependencies", code=code)
