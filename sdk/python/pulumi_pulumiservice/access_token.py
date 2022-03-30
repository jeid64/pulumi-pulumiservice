# coding=utf-8
# *** WARNING: this file was generated by pulumigen. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['AccessTokenArgs', 'AccessToken']

@pulumi.input_type
class AccessTokenArgs:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a AccessToken resource.
        """
        if description is not None:
            pulumi.set(__self__, "description", description)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)


class AccessToken(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a AccessToken resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[AccessTokenArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a AccessToken resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param AccessTokenArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AccessTokenArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AccessTokenArgs.__new__(AccessTokenArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["token_id"] = None
            __props__.__dict__["value"] = None
        super(AccessToken, __self__).__init__(
            'pulumiservice:index:AccessToken',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'AccessToken':
        """
        Get an existing AccessToken resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = AccessTokenArgs.__new__(AccessTokenArgs)

        __props__.__dict__["token_id"] = None
        __props__.__dict__["value"] = None
        return AccessToken(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="tokenId")
    def token_id(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "token_id")

    @property
    @pulumi.getter
    def value(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "value")

