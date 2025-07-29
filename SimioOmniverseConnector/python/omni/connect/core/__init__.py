# SPDX-FileCopyrightText: Copyright (c) 2022-2024 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: LicenseRef-NvidiaProprietary
#
# NVIDIA CORPORATION, its affiliates and licensors retain all intellectual
# property and proprietary rights in and to this material, related
# documentation and any modifications thereto. Any use, reproduction,
# disclosure or distribution of this material and related documentation
# without an express license agreement from NVIDIA CORPORATION or
# its affiliates is strictly prohibited.

__all__ = [
    # version
    "version",
    "clientVersion",
    "deprecated",
    # startup
    "withNucleus",
    "initialized",
    "startup",
    "startupLog",
    "shutdown",
    "shutdownLog",
    # logging
    "logChannel",
    "enableStandardOutputStream",
    "addLogConsumer",
    "removeLogConsumer",
    # settings
    "getExportOptions",
    "getExportOptionsAsFileFormatArguments",
    "getImportOptions",
    "getImportOptionsAsFileFormatArguments",
    "loadSettings",
    "loadSettingsFromFile",
    "setExportOptions",
    "setExportOptionsFromFileFormatArguments",
    "saveExportPreferences",
    "setImportOptions",
    "setImportOptionsFromFileFormatArguments",
    "saveImportPreferences",
    "kAppNameSetting",
    "kAppNameToken",
    "kAppVersionSetting",
    "kAppVersionToken",
    "kBuildConfigToken",
    "kCacheFolderToken",
    "kClientNameSetting",
    "kClientNameToken",
    "kClientVersionSetting",
    "kClientVersionToken",
    "kConnectSdkVersionFullToken",
    "kConnectSdkVersionToken",
    "kCoreSettings",
    "kDataFolderToken",
    "kExportOptionsSetting",
    "kImportOptionsSetting",
    "kLiveSessionConfigVersion",
    "kLogConsumerLevelSettingParentPath",
    "kLogFolderToken",
    "kOmniClientLibVersionFullToken",
    "kPluginPathsSetting",
    "kPythonPathsSetting",
    "kStartTimeToken",
    "kUsdResolverPathSetting",
    "kUsdVersionToken",
    # usd authoring
    # prim
    "getValidPrimName",
    "getValidPrimNames",
    "getValidChildNames",
    "getValidPropertyName",
    "getValidPropertyNames",
    "getDisplayName",
    "setDisplayName",
    "clearDisplayName",
    "blockDisplayName",
    "computeEffectiveDisplayName",
    # layer
    "hasLayerAuthoringMetadata",
    "setLayerAuthoringMetadata",
    "exportLayer",
    "saveLayer",
    # stage
    "createStage",
    "configureStage",
    "saveStage",
    "canRemovePrim",
    "removeOrDeactivatePrim",
    "copyPrim",
    "renamePrim",
    # geom
    "defineXform",
    "defineCamera",
    "definePolyMesh",
    "definePointCloud",
    "defineLinearBasisCurves",
    "defineCubicBasisCurves",
    "RotationOrder",
    "getLocalTransform",
    "getLocalTransformMatrix",
    "getLocalTransformComponents",
    "setLocalTransform",
    "FloatPrimvarData",
    "IntPrimvarData",
    "Int64PrimvarData",
    "Vec3fPrimvarData",
    "Vec2fPrimvarData",
    "StringPrimvarData",
    "TokenPrimvarData",
    # materials
    "createMaterial",
    "createMdlShader",
    "createMdlShaderInput",
    "bindMaterial",
    "defineOmniPbrMaterial",
    "defineOmniGlassMaterial",
    "computeEffectiveMdlSurfaceShader",
    "computeEffectivePreviewSurfaceShader",
    "addDiffuseTextureToPbrMaterial",
    "addNormalTextureToPbrMaterial",
    "addOrmTextureToPbrMaterial",
    "addRoughnessTextureToPbrMaterial",
    "addMetallicTextureToPbrMaterial",
    "addOpacityTextureToPbrMaterial",
    "ColorSpace",
    "sRgbToLinear",
    "linearToSrgb",
    # lights
    "defineDomeLight",
    "defineRectLight",
    "isLight",
    "getLightAttr",
    "getLightAPIAttrNames",
    "getDistantLightAttrNames",
    "getDomeLightAttrNames",
    "getRectLightAttrNames",
    "getShapingAPIAttrNames",
    "getSphereLightAttrNames",
    "createLightExtentAttr",
    "createIntensityAttr",
    "createColorAttr",
    "createColorTemperatureAttr",
    "createEnableColorTemperatureAttr",
    "createDistantAngleAttr",
    "createDomeTextureFileAttr",
    "createDomeTextureFormatAttr",
    "createSphereRadiusAttr",
    "createShapingConeAngleAttr",
    "createShapingConeSoftnessAttr",
    "createRectWidthAttr",
    "createRectHeightAttr",
    "createRectTextureFileAttr",
]


import os

if hasattr(os, "add_dll_directory"):
    __scriptdir = os.path.dirname(os.path.realpath(__file__))
    __dlldir = os.path.abspath(os.path.join(__scriptdir, "../../../../lib"))
    if os.path.exists(__dlldir):
        with os.add_dll_directory(__dlldir):
            from ._omni_connect_core import *  # noqa
    else:
        # fallback to requiring the client to setup the dll directory
        from ._omni_connect_core import *  # noqa
else:
    from ._omni_connect_core import *  # noqa

# Import hand rolled python bindings
from ._StageAlgoBindings import *  # noqa

if withNucleus():  # noqa
    __all__.extend(
        [
            # nucleus
            "registerOmniUsdResolverPlugin",
            "isOmniUri",
            "isLocalUri",
            "doesUriExist",
            "isUriWritable",
            "getUser",
            "createUriCheckpoint",
            "LiveSession",
            "LiveSessionInfo",
            "LiveSessionChannel",
            "LiveSessionConfig",
            "getLiveSessionConfig",
            "createLiveSessionConfigFile",
            "setLiveSessionConfigValues",
            "isLiveSessionVersionCompatible",
        ]
    )


def deprecated(version: str, message: str):
    """
    Decorator used to deprecated python API in the given module

    Example:

    .. code-block:: python

        @deprecated("0.5", "Use `baz` instead")
        def foo(bar: str) -> str:
            return baz(bar)

    Args:
        version: The major.minor version in which the function was first deprecated
        message: A user facing message about the deprecation, ideally with a suggested alternative function.
            Do not include the version in this message, it will be prefixed automatically.
    """

    def _wrap(func):
        warning = f"`{func.__name__}` was deprecated in v{version} and will be removed in the future. {message}"

        def wrapper(*args, **kwargs):
            import omni.log

            omni.log.warn(warning)
            return func(*args, **kwargs)

        wrapper.__name__ = func.__name__
        wrapper.__doc__ = warning
        return wrapper

    return _wrap
