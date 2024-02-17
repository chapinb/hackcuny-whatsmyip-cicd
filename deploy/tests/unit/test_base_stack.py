from aws_cdk import App, assertions

from cdk_stacks.base_stack import WhastMyIp


def test_lambda_created() -> None:
    app = App()
    stack = WhastMyIp(app, "unittest")
    template = assertions.Template.from_stack(stack)
    template.has_resource(
        "AWS::Lambda::Function",
        {
            "Properties": {
                "Runtime": "python3.12",
                "Handler": "app.ip_utils.lambda_handler",
            }
        },
    )
