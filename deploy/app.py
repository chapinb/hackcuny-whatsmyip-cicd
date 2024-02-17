#!/usr/bin/env python3

from aws_cdk import App

from cdk_stacks.base_stack import WhastMyIp


def create_app() -> App:
    app = App()
    WhastMyIp(app, "WhatsMyIp")
    app.synth()
    return app


if __name__ == "__main__":
    create_app()
