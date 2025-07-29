from __future__ import annotations
import omni.connect.core._omni_connect_core
import typing
import pxr.Gf
import pxr.Sdf
import pxr.Usd
import pxr.UsdGeom
import pxr.UsdLux
import pxr.UsdShade
import pxr.Vt

__all__ = [
    "ColorSpace",
    "FloatPrimvarData",
    "Int64PrimvarData",
    "IntPrimvarData",
    "LiveSession",
    "LiveSessionChannel",
    "LiveSessionConfig",
    "LiveSessionInfo",
    "RotationOrder",
    "StringPrimvarData",
    "TokenPrimvarData",
    "Vec2fPrimvarData",
    "Vec3fPrimvarData",
    "addDiffuseTextureToPbrMaterial",
    "addLogConsumer",
    "addMetallicTextureToPbrMaterial",
    "addNormalTextureToPbrMaterial",
    "addOpacityTextureToPbrMaterial",
    "addOrmTextureToPbrMaterial",
    "addRoughnessTextureToPbrMaterial",
    "bindMaterial",
    "blockDisplayName",
    "canRemovePrim",
    "clearDisplayName",
    "clientVersion",
    "computeEffectiveDisplayName",
    "computeEffectiveMdlSurfaceShader",
    "computeEffectivePreviewSurfaceShader",
    "configureStage",
    "copyPrim",
    "createColorAttr",
    "createColorTemperatureAttr",
    "createDistantAngleAttr",
    "createDomeTextureFileAttr",
    "createDomeTextureFormatAttr",
    "createEnableColorTemperatureAttr",
    "createIntensityAttr",
    "createLightExtentAttr",
    "createLiveSessionConfigFile",
    "createMaterial",
    "createMdlShader",
    "createMdlShaderInput",
    "createRectHeightAttr",
    "createRectTextureFileAttr",
    "createRectWidthAttr",
    "createShapingConeAngleAttr",
    "createShapingConeSoftnessAttr",
    "createSphereRadiusAttr",
    "createUriCheckpoint",
    "defineCamera",
    "defineCubicBasisCurves",
    "defineDomeLight",
    "defineLinearBasisCurves",
    "defineOmniGlassMaterial",
    "defineOmniPbrMaterial",
    "definePointCloud",
    "definePolyMesh",
    "defineRectLight",
    "defineXform",
    "doesUriExist",
    "enableStandardOutputStream",
    "exportLayer",
    "getDisplayName",
    "getDistantLightAttrNames",
    "getDomeLightAttrNames",
    "getExportOptions",
    "getExportOptionsAsFileFormatArguments",
    "getImportOptions",
    "getImportOptionsAsFileFormatArguments",
    "getLightAPIAttrNames",
    "getLightAttr",
    "getLiveSessionConfig",
    "getLocalTransform",
    "getLocalTransformComponents",
    "getLocalTransformMatrix",
    "getRectLightAttrNames",
    "getShapingAPIAttrNames",
    "getSphereLightAttrNames",
    "getUser",
    "getValidChildNames",
    "getValidPrimName",
    "getValidPrimNames",
    "getValidPropertyName",
    "getValidPropertyNames",
    "hasLayerAuthoringMetadata",
    "initialized",
    "isLight",
    "isLiveSessionVersionCompatible",
    "isLocalUri",
    "isOmniUri",
    "isUriWritable",
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
    "linearToSrgb",
    "loadSettings",
    "loadSettingsFromFile",
    "logChannel",
    "registerOmniUsdResolverPlugin",
    "removeLogConsumer",
    "removeOrDeactivatePrim",
    "renamePrim",
    "sRgbToLinear",
    "saveExportPreferences",
    "saveImportPreferences",
    "saveLayer",
    "saveStage",
    "setDisplayName",
    "setExportOptions",
    "setExportOptionsFromFileFormatArguments",
    "setImportOptions",
    "setImportOptionsFromFileFormatArguments",
    "setLayerAuthoringMetadata",
    "setLiveSessionConfigValues",
    "setLocalTransform",
    "startup",
    "startupLog",
    "version",
    "withNucleus"
]


class ColorSpace():
    """
    Texture color space (encoding) types

    Members:

      eAuto : Check for gamma or metadata in the texture itself

      eRaw : Use linear sampling (used for Normal, Roughness, Metallic, Opacity textures)

      eSrgb : Use sRGB sampling (typically used for Diffuse textures)
    """
    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __init__(self, value: int) -> None: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @property
    def value(self) -> int:
        """
        :type: int
        """
    __members__: dict # value = {'eAuto': <ColorSpace.eAuto: 0>, 'eRaw': <ColorSpace.eRaw: 1>, 'eSrgb': <ColorSpace.eSrgb: 2>}
    eAuto: omni.connect.core._omni_connect_core.ColorSpace # value = <ColorSpace.eAuto: 0>
    eRaw: omni.connect.core._omni_connect_core.ColorSpace # value = <ColorSpace.eRaw: 1>
    eSrgb: omni.connect.core._omni_connect_core.ColorSpace # value = <ColorSpace.eSrgb: 2>
    pass
class FloatPrimvarData():
    """
    `PrimvarData` that holds `Vt.FloatArray` values (e.g widths or scale factors).

                This is a read-only class to manage all `UsdGeom.Primvar` data as a single object without risk of detaching (copying) arrays.

                `UsdGeom.Primvars` are often used when authoring `UsdGeom.PointBased` prims (e.g meshes, curves, and point clouds) to describe surface varying
                properties that can affect how a prim is rendered, or to drive a surface deformation.

                However, `UsdGeom.Primvar` data can be quite intricate to use, especially with respect to indexed vs non-indexed primvars, element size, the
                complexities of `Vt.Array` detach (copy-on-write) semantics, and the ambiguity of "native" attributes vs primvar attributes (e.g. mesh normals).

                This class aims to provide simpler entry points to avoid common mistakes with respect to `UsdGeom.Primvar` data handling.

                All of the USD authoring "define" functions in this library accept optional `PrimvarData` to define e.g normals, display colors, etc.
            
    """
    def __eq__(self, arg0: FloatPrimvarData) -> bool: 
        """
        Check that all data between two `PrimvarData` objects is identical.

        This differs from the equality operator in that it ensures the `Vt.Array` values and indices have not detached.

        Args:
            other: The other `PrimvarData`.

        Returns:
            True if all the member data is equal (but not necessarily identical arrays).
        """
    @typing.overload
    def __init__(self, interpolation: str, values: pxr.Vt.FloatArray, elementSize: int = -1) -> None: 
        """
        Construct non-indexed `PrimvarData`.

        Note:
            To avoid immediate array iteration, validation does not occur during construction, and is deferred until `isValid()` is called.
            This may be counter-intuitive as `PrimvarData` provides read-only access, but full validation is often only possible within the context
            of specific surface topology, so premature validation would be redundant.

        Args:
            interpolation: The primvar interpolation. Must match `UsdGeom.Primvar.IsValidInterpolation()` to be considered valid.
            values: Read-only accessor to the values array.
            elementSize: Optional element size. This should be fairly uncommon.
                See [GetElementSize](https://openusd.org/release/api/class_usd_geom_primvar.html#a711c3088ebca00ca75308485151c8590) for details.

        Returns:
            The read-only `PrimvarData`.



        Construct indexed `PrimvarData`.

        Note:
            To avoid immediate array iteration, validation does not occur during construction, and is deferred until `isValid()` is called.
            This may be counter-intuitive as `PrimvarData` provides read-only access, but full validation is often only possible within the context
            of specific surface topology, so premature validation would be redundant.

        Args:
            interpolation: The primvar interpolation. Must match `UsdGeom.Primvar.IsValidInterpolation()` to be considered valid.
            values: Read-only accessor to the values array.
            indices: Read-only accessor to the indices array.
            elementSize: Optional element size. This should be fairly uncommon.
                See [GetElementSize](https://openusd.org/release/api/class_usd_geom_primvar.html#a711c3088ebca00ca75308485151c8590) for details.

        Returns:
            The read-only `PrimvarData`.
        """
    @typing.overload
    def __init__(self, interpolation: str, values: pxr.Vt.FloatArray, indices: pxr.Vt.IntArray, elementSize: int = -1) -> None: ...
    def __ne__(self, arg0: FloatPrimvarData) -> bool: 
        """
        Check for in-equality between two `PrimvarData` objects.

        Args:
            other: The other `PrimvarData`.

        Returns:
            True if any member data is not equal (but does not guarantee identical arrays).
        """
    def __str__(self) -> str: ...
    def effectiveSize(self) -> int: 
        """
        The effective size of the data, having accounted for values, indices, and element size.

        This is the number of variable values that "really" exist, as far as a consumer is concerned. The indices & elementSize are used as a storage
        optimization, but the consumer should consider the effective size as the number of "deduplicated" individual values.

        Returns:
            The effective size of the data.
        """
    def elementSize(self) -> int: 
        """
        The element size.

        Any value less than 1 is considered "non authored" and indicates no element size. This should be the most common case, as element size is a
        fairly esoteric extension of `UsdGeom.Primvar` data to account for non-typed array strides such as spherical harmonics float[9] arrays.

        See `UsdGeom.Primvar.GetElementSize()` for more details.

        Returns:
            The primvar element size.
        """
    @staticmethod
    def getPrimvarData(primvar: pxr.UsdGeom.Primvar, time: pxr.Usd.TimeCode = nan) -> FloatPrimvarData: 
        """
        Construct a `PrimvarData` from a `UsdGeom.Primvar` that has already been authored.

        The primvar may be indexed, non-indexed, with or without elements, or it may not even be validly authored scene description.
        Use `isValid()` to confirm that valid data has been gathered.

        Args:
            primvar: The previously authored `UsdGeom.Primvar`.
            time: The time at which the attribute values are read.

        Returns:
            The read-only `PrimvarData`.
        """
    def hasIndices(self) -> bool: 
        """
        Whether this is indexed or non-indexed `PrimvarData`

        Returns:
            Whether this is indexed or non-indexed `PrimvarData`.
        """
    def index(self) -> bool: 
        """
        Update the values and indices of this `PrimvarData` object to avoid duplicate values.

        Updates will not be made in the following conditions:
            - If element size is greater than one.
            - If the existing indexing is efficient.
            - If there are no duplicate values.
            - If the existing indices are invalid

        Returns:
            True if the values and/or indices were modified.
        """
    def indices(self) -> pxr.Vt.IntArray: 
        """
        Access to the indices array.

        This method throws a runtime error if the `PrimvarData` is not indexed. For exception-free access, check `hasIndices()` before calling this.

        Note:
            It may contain an empty or invalid indices array. Use `PrimvarData.isValid()` to validate that the indices are not out-of-range.

        Returns:
            The primvar indices
        """
    def interpolation(self) -> str: 
        """
        The geometric interpolation.

        It may be an invalid interpolation. Use `PrimvarData.isValid()` or `UsdGeom.Primvar.IsValidInterpolation()` to confirm.

        Returns:
            The geometric interpolation.
        """
    def isIdentical(self, other: FloatPrimvarData) -> bool: 
        """
        Check that all data between two `PrimvarData` objects is identical.

        This differs from the equality operator in that it ensures the `Vt.Array` values and indices have not detached.

        Args:
            other: The other `PrimvarData`.

        Returns:
            True if all the member data is equal and arrays are identical.
        """
    def isValid(self) -> bool: 
        """
        Whether the data is valid or invalid.

        This is a validation check with respect to the `PrimvarData` itself & the requirements of `UsdGeom.Prim`. It does not validate with respect to
        specific surface topology data, as no such data is available or consistant across `UsdGeom.PointBased` prim types.

        This validation checks the following, in this order, and returns false if any condition fails:

            - The interpolation matches `UsdGeom.Primvar.IsValidInterpolation()`.
            - The values are not empty. Note that individual values may be invalid (e.g `NaN` values on a `Vt.FloatArray`) but this will not be
              considered a failure, as some workflows allow for `NaN` to indicate non-authored elements or "holes" within the data.
            - If it is non-indexed, and has elements, that the values divide evenly by elementSize.
            - If it is indexed, and has elements, that the indices divide evenly by elementSize.
            - If it is indexed, that the indices are all within the expected range of the values array.

        Returns:
            Whether the data is valid or invalid.
        """
    def setPrimvar(self, primvar: pxr.UsdGeom.Primvar, time: pxr.Usd.TimeCode = nan) -> bool: 
        """
        Set data on an existing `UsdGeom.Primvar` from a `PrimvarData` that has already been authored.

        Any existing authored data on the primvar will be overwritten or blocked with the `PrimvarData` members.

        To copy data from one `UsdGeom.Primvar` to another, use `data: PrimvarData = PrimvarData.get(primvar: UsdGeom.Primvar)` to gather the data,
        then use `set(primvar: UsdGeom.Primvar)` to author it.

        Args:
            primvar: The previously authored `UsdGeom.Primvar`.
            time: The time at which the attribute values are written.

        Returns:
            Whether the `UsdGeom.Primvar` was completely authored from the member data.
            Any failure to author may leave the primvar in an unknown state (e.g. it may have been partially authored).
        """
    def values(self) -> pxr.Vt.FloatArray: 
        """
        Access to the values array.

        Bear in mind the values may need to be accessed via `indices()` or using an `elementSize()` stride.

        It may contain an empty or invalid values array.

        Returns:
            The primvar values.
        """
    __hash__ = None
    pass
class Int64PrimvarData():
    """
    `PrimvarData` that holds `Vt.Int64Array` values (e.g ids that might be very large).

                This is a read-only class to manage all `UsdGeom.Primvar` data as a single object without risk of detaching (copying) arrays.

                `UsdGeom.Primvars` are often used when authoring `UsdGeom.PointBased` prims (e.g meshes, curves, and point clouds) to describe surface varying
                properties that can affect how a prim is rendered, or to drive a surface deformation.

                However, `UsdGeom.Primvar` data can be quite intricate to use, especially with respect to indexed vs non-indexed primvars, element size, the
                complexities of `Vt.Array` detach (copy-on-write) semantics, and the ambiguity of "native" attributes vs primvar attributes (e.g. mesh normals).

                This class aims to provide simpler entry points to avoid common mistakes with respect to `UsdGeom.Primvar` data handling.

                All of the USD authoring "define" functions in this library accept optional `PrimvarData` to define e.g normals, display colors, etc.
            
    """
    def __eq__(self, arg0: Int64PrimvarData) -> bool: 
        """
        Check that all data between two `PrimvarData` objects is identical.

        This differs from the equality operator in that it ensures the `Vt.Array` values and indices have not detached.

        Args:
            other: The other `PrimvarData`.

        Returns:
            True if all the member data is equal (but not necessarily identical arrays).
        """
    @typing.overload
    def __init__(self, interpolation: str, values: pxr.Vt.Int64Array, elementSize: int = -1) -> None: 
        """
        Construct non-indexed `PrimvarData`.

        Note:
            To avoid immediate array iteration, validation does not occur during construction, and is deferred until `isValid()` is called.
            This may be counter-intuitive as `PrimvarData` provides read-only access, but full validation is often only possible within the context
            of specific surface topology, so premature validation would be redundant.

        Args:
            interpolation: The primvar interpolation. Must match `UsdGeom.Primvar.IsValidInterpolation()` to be considered valid.
            values: Read-only accessor to the values array.
            elementSize: Optional element size. This should be fairly uncommon.
                See [GetElementSize](https://openusd.org/release/api/class_usd_geom_primvar.html#a711c3088ebca00ca75308485151c8590) for details.

        Returns:
            The read-only `PrimvarData`.



        Construct indexed `PrimvarData`.

        Note:
            To avoid immediate array iteration, validation does not occur during construction, and is deferred until `isValid()` is called.
            This may be counter-intuitive as `PrimvarData` provides read-only access, but full validation is often only possible within the context
            of specific surface topology, so premature validation would be redundant.

        Args:
            interpolation: The primvar interpolation. Must match `UsdGeom.Primvar.IsValidInterpolation()` to be considered valid.
            values: Read-only accessor to the values array.
            indices: Read-only accessor to the indices array.
            elementSize: Optional element size. This should be fairly uncommon.
                See [GetElementSize](https://openusd.org/release/api/class_usd_geom_primvar.html#a711c3088ebca00ca75308485151c8590) for details.

        Returns:
            The read-only `PrimvarData`.
        """
    @typing.overload
    def __init__(self, interpolation: str, values: pxr.Vt.Int64Array, indices: pxr.Vt.IntArray, elementSize: int = -1) -> None: ...
    def __ne__(self, arg0: Int64PrimvarData) -> bool: 
        """
        Check for in-equality between two `PrimvarData` objects.

        Args:
            other: The other `PrimvarData`.

        Returns:
            True if any member data is not equal (but does not guarantee identical arrays).
        """
    def __str__(self) -> str: ...
    def effectiveSize(self) -> int: 
        """
        The effective size of the data, having accounted for values, indices, and element size.

        This is the number of variable values that "really" exist, as far as a consumer is concerned. The indices & elementSize are used as a storage
        optimization, but the consumer should consider the effective size as the number of "deduplicated" individual values.

        Returns:
            The effective size of the data.
        """
    def elementSize(self) -> int: 
        """
        The element size.

        Any value less than 1 is considered "non authored" and indicates no element size. This should be the most common case, as element size is a
        fairly esoteric extension of `UsdGeom.Primvar` data to account for non-typed array strides such as spherical harmonics float[9] arrays.

        See `UsdGeom.Primvar.GetElementSize()` for more details.

        Returns:
            The primvar element size.
        """
    @staticmethod
    def getPrimvarData(primvar: pxr.UsdGeom.Primvar, time: pxr.Usd.TimeCode = nan) -> Int64PrimvarData: 
        """
        Construct a `PrimvarData` from a `UsdGeom.Primvar` that has already been authored.

        The primvar may be indexed, non-indexed, with or without elements, or it may not even be validly authored scene description.
        Use `isValid()` to confirm that valid data has been gathered.

        Args:
            primvar: The previously authored `UsdGeom.Primvar`.
            time: The time at which the attribute values are read.

        Returns:
            The read-only `PrimvarData`.
        """
    def hasIndices(self) -> bool: 
        """
        Whether this is indexed or non-indexed `PrimvarData`

        Returns:
            Whether this is indexed or non-indexed `PrimvarData`.
        """
    def index(self) -> bool: 
        """
        Update the values and indices of this `PrimvarData` object to avoid duplicate values.

        Updates will not be made in the following conditions:
            - If element size is greater than one.
            - If the existing indexing is efficient.
            - If there are no duplicate values.
            - If the existing indices are invalid

        Returns:
            True if the values and/or indices were modified.
        """
    def indices(self) -> pxr.Vt.IntArray: 
        """
        Access to the indices array.

        This method throws a runtime error if the `PrimvarData` is not indexed. For exception-free access, check `hasIndices()` before calling this.

        Note:
            It may contain an empty or invalid indices array. Use `PrimvarData.isValid()` to validate that the indices are not out-of-range.

        Returns:
            The primvar indices
        """
    def interpolation(self) -> str: 
        """
        The geometric interpolation.

        It may be an invalid interpolation. Use `PrimvarData.isValid()` or `UsdGeom.Primvar.IsValidInterpolation()` to confirm.

        Returns:
            The geometric interpolation.
        """
    def isIdentical(self, other: Int64PrimvarData) -> bool: 
        """
        Check that all data between two `PrimvarData` objects is identical.

        This differs from the equality operator in that it ensures the `Vt.Array` values and indices have not detached.

        Args:
            other: The other `PrimvarData`.

        Returns:
            True if all the member data is equal and arrays are identical.
        """
    def isValid(self) -> bool: 
        """
        Whether the data is valid or invalid.

        This is a validation check with respect to the `PrimvarData` itself & the requirements of `UsdGeom.Prim`. It does not validate with respect to
        specific surface topology data, as no such data is available or consistant across `UsdGeom.PointBased` prim types.

        This validation checks the following, in this order, and returns false if any condition fails:

            - The interpolation matches `UsdGeom.Primvar.IsValidInterpolation()`.
            - The values are not empty. Note that individual values may be invalid (e.g `NaN` values on a `Vt.FloatArray`) but this will not be
              considered a failure, as some workflows allow for `NaN` to indicate non-authored elements or "holes" within the data.
            - If it is non-indexed, and has elements, that the values divide evenly by elementSize.
            - If it is indexed, and has elements, that the indices divide evenly by elementSize.
            - If it is indexed, that the indices are all within the expected range of the values array.

        Returns:
            Whether the data is valid or invalid.
        """
    def setPrimvar(self, primvar: pxr.UsdGeom.Primvar, time: pxr.Usd.TimeCode = nan) -> bool: 
        """
        Set data on an existing `UsdGeom.Primvar` from a `PrimvarData` that has already been authored.

        Any existing authored data on the primvar will be overwritten or blocked with the `PrimvarData` members.

        To copy data from one `UsdGeom.Primvar` to another, use `data: PrimvarData = PrimvarData.get(primvar: UsdGeom.Primvar)` to gather the data,
        then use `set(primvar: UsdGeom.Primvar)` to author it.

        Args:
            primvar: The previously authored `UsdGeom.Primvar`.
            time: The time at which the attribute values are written.

        Returns:
            Whether the `UsdGeom.Primvar` was completely authored from the member data.
            Any failure to author may leave the primvar in an unknown state (e.g. it may have been partially authored).
        """
    def values(self) -> pxr.Vt.Int64Array: 
        """
        Access to the values array.

        Bear in mind the values may need to be accessed via `indices()` or using an `elementSize()` stride.

        It may contain an empty or invalid values array.

        Returns:
            The primvar values.
        """
    __hash__ = None
    pass
class IntPrimvarData():
    """
    `PrimvarData` that holds `Vt.IntArray` values (e.g simple switch values or booleans consumable by shaders).

                This is a read-only class to manage all `UsdGeom.Primvar` data as a single object without risk of detaching (copying) arrays.

                `UsdGeom.Primvars` are often used when authoring `UsdGeom.PointBased` prims (e.g meshes, curves, and point clouds) to describe surface varying
                properties that can affect how a prim is rendered, or to drive a surface deformation.

                However, `UsdGeom.Primvar` data can be quite intricate to use, especially with respect to indexed vs non-indexed primvars, element size, the
                complexities of `Vt.Array` detach (copy-on-write) semantics, and the ambiguity of "native" attributes vs primvar attributes (e.g. mesh normals).

                This class aims to provide simpler entry points to avoid common mistakes with respect to `UsdGeom.Primvar` data handling.

                All of the USD authoring "define" functions in this library accept optional `PrimvarData` to define e.g normals, display colors, etc.
            
    """
    def __eq__(self, arg0: IntPrimvarData) -> bool: 
        """
        Check that all data between two `PrimvarData` objects is identical.

        This differs from the equality operator in that it ensures the `Vt.Array` values and indices have not detached.

        Args:
            other: The other `PrimvarData`.

        Returns:
            True if all the member data is equal (but not necessarily identical arrays).
        """
    @typing.overload
    def __init__(self, interpolation: str, values: pxr.Vt.IntArray, elementSize: int = -1) -> None: 
        """
        Construct non-indexed `PrimvarData`.

        Note:
            To avoid immediate array iteration, validation does not occur during construction, and is deferred until `isValid()` is called.
            This may be counter-intuitive as `PrimvarData` provides read-only access, but full validation is often only possible within the context
            of specific surface topology, so premature validation would be redundant.

        Args:
            interpolation: The primvar interpolation. Must match `UsdGeom.Primvar.IsValidInterpolation()` to be considered valid.
            values: Read-only accessor to the values array.
            elementSize: Optional element size. This should be fairly uncommon.
                See [GetElementSize](https://openusd.org/release/api/class_usd_geom_primvar.html#a711c3088ebca00ca75308485151c8590) for details.

        Returns:
            The read-only `PrimvarData`.



        Construct indexed `PrimvarData`.

        Note:
            To avoid immediate array iteration, validation does not occur during construction, and is deferred until `isValid()` is called.
            This may be counter-intuitive as `PrimvarData` provides read-only access, but full validation is often only possible within the context
            of specific surface topology, so premature validation would be redundant.

        Args:
            interpolation: The primvar interpolation. Must match `UsdGeom.Primvar.IsValidInterpolation()` to be considered valid.
            values: Read-only accessor to the values array.
            indices: Read-only accessor to the indices array.
            elementSize: Optional element size. This should be fairly uncommon.
                See [GetElementSize](https://openusd.org/release/api/class_usd_geom_primvar.html#a711c3088ebca00ca75308485151c8590) for details.

        Returns:
            The read-only `PrimvarData`.
        """
    @typing.overload
    def __init__(self, interpolation: str, values: pxr.Vt.IntArray, indices: pxr.Vt.IntArray, elementSize: int = -1) -> None: ...
    def __ne__(self, arg0: IntPrimvarData) -> bool: 
        """
        Check for in-equality between two `PrimvarData` objects.

        Args:
            other: The other `PrimvarData`.

        Returns:
            True if any member data is not equal (but does not guarantee identical arrays).
        """
    def __str__(self) -> str: ...
    def effectiveSize(self) -> int: 
        """
        The effective size of the data, having accounted for values, indices, and element size.

        This is the number of variable values that "really" exist, as far as a consumer is concerned. The indices & elementSize are used as a storage
        optimization, but the consumer should consider the effective size as the number of "deduplicated" individual values.

        Returns:
            The effective size of the data.
        """
    def elementSize(self) -> int: 
        """
        The element size.

        Any value less than 1 is considered "non authored" and indicates no element size. This should be the most common case, as element size is a
        fairly esoteric extension of `UsdGeom.Primvar` data to account for non-typed array strides such as spherical harmonics float[9] arrays.

        See `UsdGeom.Primvar.GetElementSize()` for more details.

        Returns:
            The primvar element size.
        """
    @staticmethod
    def getPrimvarData(primvar: pxr.UsdGeom.Primvar, time: pxr.Usd.TimeCode = nan) -> IntPrimvarData: 
        """
        Construct a `PrimvarData` from a `UsdGeom.Primvar` that has already been authored.

        The primvar may be indexed, non-indexed, with or without elements, or it may not even be validly authored scene description.
        Use `isValid()` to confirm that valid data has been gathered.

        Args:
            primvar: The previously authored `UsdGeom.Primvar`.
            time: The time at which the attribute values are read.

        Returns:
            The read-only `PrimvarData`.
        """
    def hasIndices(self) -> bool: 
        """
        Whether this is indexed or non-indexed `PrimvarData`

        Returns:
            Whether this is indexed or non-indexed `PrimvarData`.
        """
    def index(self) -> bool: 
        """
        Update the values and indices of this `PrimvarData` object to avoid duplicate values.

        Updates will not be made in the following conditions:
            - If element size is greater than one.
            - If the existing indexing is efficient.
            - If there are no duplicate values.
            - If the existing indices are invalid

        Returns:
            True if the values and/or indices were modified.
        """
    def indices(self) -> pxr.Vt.IntArray: 
        """
        Access to the indices array.

        This method throws a runtime error if the `PrimvarData` is not indexed. For exception-free access, check `hasIndices()` before calling this.

        Note:
            It may contain an empty or invalid indices array. Use `PrimvarData.isValid()` to validate that the indices are not out-of-range.

        Returns:
            The primvar indices
        """
    def interpolation(self) -> str: 
        """
        The geometric interpolation.

        It may be an invalid interpolation. Use `PrimvarData.isValid()` or `UsdGeom.Primvar.IsValidInterpolation()` to confirm.

        Returns:
            The geometric interpolation.
        """
    def isIdentical(self, other: IntPrimvarData) -> bool: 
        """
        Check that all data between two `PrimvarData` objects is identical.

        This differs from the equality operator in that it ensures the `Vt.Array` values and indices have not detached.

        Args:
            other: The other `PrimvarData`.

        Returns:
            True if all the member data is equal and arrays are identical.
        """
    def isValid(self) -> bool: 
        """
        Whether the data is valid or invalid.

        This is a validation check with respect to the `PrimvarData` itself & the requirements of `UsdGeom.Prim`. It does not validate with respect to
        specific surface topology data, as no such data is available or consistant across `UsdGeom.PointBased` prim types.

        This validation checks the following, in this order, and returns false if any condition fails:

            - The interpolation matches `UsdGeom.Primvar.IsValidInterpolation()`.
            - The values are not empty. Note that individual values may be invalid (e.g `NaN` values on a `Vt.FloatArray`) but this will not be
              considered a failure, as some workflows allow for `NaN` to indicate non-authored elements or "holes" within the data.
            - If it is non-indexed, and has elements, that the values divide evenly by elementSize.
            - If it is indexed, and has elements, that the indices divide evenly by elementSize.
            - If it is indexed, that the indices are all within the expected range of the values array.

        Returns:
            Whether the data is valid or invalid.
        """
    def setPrimvar(self, primvar: pxr.UsdGeom.Primvar, time: pxr.Usd.TimeCode = nan) -> bool: 
        """
        Set data on an existing `UsdGeom.Primvar` from a `PrimvarData` that has already been authored.

        Any existing authored data on the primvar will be overwritten or blocked with the `PrimvarData` members.

        To copy data from one `UsdGeom.Primvar` to another, use `data: PrimvarData = PrimvarData.get(primvar: UsdGeom.Primvar)` to gather the data,
        then use `set(primvar: UsdGeom.Primvar)` to author it.

        Args:
            primvar: The previously authored `UsdGeom.Primvar`.
            time: The time at which the attribute values are written.

        Returns:
            Whether the `UsdGeom.Primvar` was completely authored from the member data.
            Any failure to author may leave the primvar in an unknown state (e.g. it may have been partially authored).
        """
    def values(self) -> pxr.Vt.IntArray: 
        """
        Access to the values array.

        Bear in mind the values may need to be accessed via `indices()` or using an `elementSize()` stride.

        It may contain an empty or invalid values array.

        Returns:
            The primvar values.
        """
    __hash__ = None
    pass
class LiveSession():
    """
    This class wraps the Live Session operations on the USD Stage, USD Layer, Info, Channel, and Config classes.

    - The LiveSession class contains:

        - LiveSessionChannel class - handles messages between live clients (joining, leaving, merging)
        - LiveSessionInfo class - collects much of the context for the live session file paths and URIs
        - Live Session Config functions - reading and writing the live session configuration TOML file
        - Join, merge, and leave member functions - coordinate the live session classes and USD layer details

    The expected usage of this class:

    - Create an instance using LiveSession::create()
    - Browse available sessions using LiveSession::getInfo() ``->`` LiveSessionInfo::getSessionNames()
    - Pick a session from the list or decide to create a new session, call LiveSession::join() - set ``makeEditTarget`` to set the stage's edit target
    - At this point the root stage's session layer now has a .live sublayer and the edit target is set to this .live layer
    - Changes made to the stage are directed to the .live layer.  To sync with Nucleus use ``omniClientLiveProcess()``
    - Changes from other clients automatically appear in the .live layer, USD Tf Notifications allow the app to reason about incoming changes to the stage
    - The Live Channel should be periodically processed and handled using LiveSession::getChannel() ``->`` LiveSessionChannel::processMessages()
    - If the app wants to leave the session without merging, call LiveSession::leave()
    - The app can use either LiveSession::mergeToRoot() or LiveSession::mergeToNewLayer() to merge and leave the live session
    - At this point the LiveSession shared pointer can be destroyed or go out of scope
    """
    @staticmethod
    @typing.overload
    def create(rootStage: pxr.Usd.Stage) -> LiveSession: 
        """
        Create an Omniverse live session class.

        Note, live sessions are only supported on stages resident on Omniverse Nucleus servers, not local disk.

        Args:
            rootStage: The root USD stage in the live session (must reside on a Nucleus server)

        Returns:
            LiveSession: A live session interface shared pointer, None if rootStage is invalid



        Create an Omniverse live session class.

        Note, live sessions are only supported on stages resident on Omniverse Nucleus servers, not local disk.

        Args:
            rootStage: The root USD stage in the live session (must reside on a Nucleus server)
            info: The LiveSessionInfo to attach to

        Returns:
            LiveSession: A live session interface shared pointer, None if rootStage is invalid
        """
    @staticmethod
    @typing.overload
    def create(*args, **kwargs) -> typing.Any: ...
    @staticmethod
    def getChannel(*args, **kwargs) -> typing.Any: 
        """
        Get the Live Session Channel interface

        Note, the returned channel interface is disconnected after the LiveSession is deleted

        Returns:
            The LiveSessionChannel interface, None if session was not joined
        """
    @staticmethod
    def getInfo(*args, **kwargs) -> typing.Any: 
        """
        Get the Live Session Info interface

        Note, the returned info interface is invalid after the LiveSession is deleted

        Returns:
            The LiveSessionInfo interface, None if root stage was invalid upon creation
        """
    def hasPrimSpecsInRootLayer(self) -> bool: 
        """
        Returns whether there are any prim specs defined in the layer

        If a stage's root layer contains prim specs, then "overs" from a sublayer that affect those prim specs may be hidden.
        This is useful to know when merging a live session layer back to the stage.  The general guidance is that if there
        are any prim specs defined in a stage's root layer then the live layer should be merged into the stage's root layer.
        If there are no prim specs defined in a stage's root layer then either merging to the root layer or a new sublayer
        will work.

        See LiveSession::mergeToRoot() and LiveSession::mergeToNewLayer() for more merging live changes to the root stage

        Returns:
            Whether the stage's root layer has any prim specs defined
        """
    def join(self, sessionName: str, makeEditTarget: bool = True) -> pxr.Sdf.Layer: 
        """
        Join an existing or create a new live session

        This function performs these steps:

        - Init the LiveSessionInfo
        - If session config file exists, validate the version
        - Create new session config file if it doesn't exist
        - Create and join the LiveSessionChannel
        - Create a new .live layer if it doesn't exist
        - Add the session's .live layer the root stage's session layer if it's not already a sublayer
        - If ``makeEditTarget`` is set then make the new .live layer the stage's edit target

        If the app chooses to not set ``makeEditTarget``, then it must set the stage's edit target
        using something like: ``rootStage->SetEditTarget(pxr::UsdEditTarget(liveLayer))``

        Args:
            sessionName: The intended name of the live session.
            makeEditTarget: If True the rootStage edit target will be set to the live layer. Defaults to True.

        Returns:
            A valid live layer if the session was joined successfully. Note that this is a weak pointer that expires after merging or leaving
            the session.
        """
    def leave(self, resetEditTarget: bool = True) -> None: 
        """
        Leave the live session without merging

        This function performs these steps:

        - Remove the .live layer from the root stage's session layer
        - Set the stage's edit target to the root layer (if ``resetEditTarget`` true)
        - Send a message to the live channel that the merge is finished

        Args:
            resetEditTarget: Set the edit target to the stage's root layer if true.  Defaults to True.
        """
    def mergeToNewLayer(self, targetLayerUri: str = None, checkpointComment: str = None, resetEditTarget: bool = True, fileFormatArgs: typing.Dict[str, str] = {}) -> bool: 
        """
        Merge live changes to target layer, insert as a root stage sublayer

        This function will merge changes from a live session layer into a new sublayer of the root stage.  It will also execute
        all of the steps defined in ``mergeToRoot()``.

        Note, if the target layer already exists the contents will be cleared

        Note, if ``targetLayerUri`` is null, the layer name will be autogenerated as
        $(stage parent URI)/$(stageNameStem)_$(sessionName)_nn.usd (_nn only appended if required for uniqueness)

        Args:
            targetLayerUri: The absolute URI for the new targetLayerUri, if null then it will be autogenerated in the root stage's directory.
            checkpointComment: An optional checkpoint comment added to the root and live layers
            resetEditTarget: Set the edit target to the stage's root layer if true. Defaults to True.
            fileFormatArgs: Additional file format-specific arguments to be supplied during target layer creation.

        Returns:
            Whether the session was merged
        """
    def mergeToRoot(self, checkpointComment: str = None, resetEditTarget: bool = True) -> bool: 
        """
        Merge live changes to root layer.

        This function will merge changes from a live session layer into the root stage layer.

        Specifically, this function performs these steps:

        - Check if the current user has the authority to merge the session and ACL to write the changes
        - Send a message to the live channel that the merge has started
        - Checkpoint the .live layer
        - Checkpoint the root stage
        - Merge the changes into the root stage (root layer or a new layer and insert the new sublayer into the root stage)
        - Save and checkpoint the stage's root layer
        - Clear the .live layer
        - Remove the .live layer from the root stage's session layer
        - Set the stage's edit target to the root layer (if ``resetEditTarget`` true)
        - Send a message to the live channel that the merge is finished

        Args:
            checkpointComment: An optional checkpoint comment added to the root and live layers
            resetEditTarget: Set the edit target to the stage's root layer if True.  Defaults to True.

        Returns:
            Whether the session was merged
        """
    pass
class LiveSessionChannel():
    """
    A class for connecting, sending, processing, and receiving Live Session channel messages.
    These messages are used to coordinate different Live Session events:

     - Users joining and leaving the session
     - Users peeking into the session to see who is connected
     - Users merging live changes and ending a session

    The channel class implementation handles interaction with an Omniverse Nucleus channel,
    which is a mechanism to broadcast messages to all connected clients.  When messages
    are received it will queue them, allowing the client to poll for them any time.
    When messages that specifically identify connected users are received, this class will
    maintain a list of connected users which the client can also poll.

    This class also has a state machine that will automatically respond to `Join` and `GetUsers`
    messages from other clients with a `Hello` message.

    This class does not run message processing in a dedicated thread, so `processMessages()` is
    is used to process the `Join`/`Hello` state machine and populate the user list.
    """
    class Message():
        """
        Live session channel message structure that defines the type and who sent it
        """
        @property
        def type(self) -> LiveSessionChannel.MessageType:
            """
            The message type (LiveSessionChannelMessageType) (Join, Left, MergeStarted, etc.)

            :type: LiveSessionChannel.MessageType
            """
        @type.setter
        def type(self, arg0: LiveSessionChannel.MessageType) -> None:
            """
            The message type (LiveSessionChannelMessageType) (Join, Left, MergeStarted, etc.)
            """
        @property
        def user(self) -> LiveSessionChannel.User:
            """
            The user (LiveSessionChannelUser) that sent the message

            :type: LiveSessionChannel.User
            """
        @user.setter
        def user(self, arg0: LiveSessionChannel.User) -> None:
            """
            The user (LiveSessionChannelUser) that sent the message
            """
        pass
    class MessageType():
        """
        Live session channel message type

        Members:

          eJoin : Sent by the Channel class when joining a channel

          eHello : Sent as a response when another client sends a `Join` or `GetUsers` message

          eGetUsers : Sent by a client to determine what users are in the session

          eLeft : Sent when the user leaves the channel

          eMergeStarted : Sent when the Admin client is starting the merge process. When clients receive this message they should immediately disable further changes to the .live layer

          eMergeFinished : Sent when the merge is complete

          eInvalid : Invalid message
        """
        def __eq__(self, other: object) -> bool: ...
        def __getstate__(self) -> int: ...
        def __hash__(self) -> int: ...
        def __index__(self) -> int: ...
        def __init__(self, value: int) -> None: ...
        def __int__(self) -> int: ...
        def __ne__(self, other: object) -> bool: ...
        def __repr__(self) -> str: ...
        def __setstate__(self, state: int) -> None: ...
        @property
        def name(self) -> str:
            """
            :type: str
            """
        @property
        def value(self) -> int:
            """
            :type: int
            """
        __members__: dict # value = {'eJoin': <MessageType.eJoin: 0>, 'eHello': <MessageType.eHello: 1>, 'eGetUsers': <MessageType.eGetUsers: 2>, 'eLeft': <MessageType.eLeft: 3>, 'eMergeStarted': <MessageType.eMergeStarted: 4>, 'eMergeFinished': <MessageType.eMergeFinished: 5>, 'eInvalid': <MessageType.eInvalid: 6>}
        eGetUsers: omni.connect.core._omni_connect_core.LiveSessionChannel.MessageType # value = <MessageType.eGetUsers: 2>
        eHello: omni.connect.core._omni_connect_core.LiveSessionChannel.MessageType # value = <MessageType.eHello: 1>
        eInvalid: omni.connect.core._omni_connect_core.LiveSessionChannel.MessageType # value = <MessageType.eInvalid: 6>
        eJoin: omni.connect.core._omni_connect_core.LiveSessionChannel.MessageType # value = <MessageType.eJoin: 0>
        eLeft: omni.connect.core._omni_connect_core.LiveSessionChannel.MessageType # value = <MessageType.eLeft: 3>
        eMergeFinished: omni.connect.core._omni_connect_core.LiveSessionChannel.MessageType # value = <MessageType.eMergeFinished: 5>
        eMergeStarted: omni.connect.core._omni_connect_core.LiveSessionChannel.MessageType # value = <MessageType.eMergeStarted: 4>
        pass
    class User():
        """
        Live session channel user structure that defines connected clients
        """
        @property
        def app(self) -> str:
            """
            The name of the application used to connect to live session

            :type: str
            """
        @app.setter
        def app(self, arg0: str) -> None:
            """
            The name of the application used to connect to live session
            """
        @property
        def id(self) -> str:
            """
            The user ID assigned by the Omniverse Client Library, eg. `WD34WRMUJHLU7Q1M`

            :type: str
            """
        @id.setter
        def id(self, arg0: str) -> None:
            """
            The user ID assigned by the Omniverse Client Library, eg. `WD34WRMUJHLU7Q1M`
            """
        @property
        def name(self) -> str:
            """
            The user name used to connect to the Nucleus server

            :type: str
            """
        @name.setter
        def name(self, arg0: str) -> None:
            """
            The user name used to connect to the Nucleus server
            """
        pass
    @staticmethod
    def create(uri: str, sendJoinMessage: bool = True) -> LiveSessionChannel: 
        """
        Create and join an Omniverse live session message channel

        This is a factory to create and join a LiveSessionChannel.  There is no join() method.

        Note: Call `omni.connect.core.startup()` before this function to initialize required components

        Args:
            uri: The URI of the Nucleus channel (__session__.channel)
            sendJoinMessage: If true a `Join` message will be broadcast on the channel.  Set to false to "peek" into a channel to see connected users.

        Returns:
            A live session channel interface shared pointer (std::shared_ptr<LiveSessionChannel>)
        """
    @staticmethod
    def getMessageTypeName(msgType: LiveSessionChannel.MessageType) -> str: 
        """
        Convert a live session channel message type to a string

        Args:
            msgType: The type of message to convert to a string

        Returns:
            A string value for the message type
        """
    def getUser(self) -> LiveSessionChannel.User: 
        """
        Get current user

        Returns:
            Current channel user
        """
    def getUsers(self, includeSelf: bool) -> typing.List[LiveSessionChannel.User]: 
        """
        Get all of the connected users

        Args:
            includeSelf: Whether to include this client user in list

        Returns:
            A list of channel users
        """
    def isConnected(self) -> bool: 
        """
        Check if the channel is connected to an actual Nucleus channel file

        Returns:
            Whether the channel is connected
        """
    def leaveChannel(self) -> None: 
        """
        Leave the channel

        Note: This function will only send a "Left" message if `sendJoinMessage` was true in `create()`
        """
    def processMessages(self) -> typing.List[LiveSessionChannel.Message]: 
        """
        Process and retrieve all of the pending channel messages

        This function drives the state machine that responds to other clients
        and populates the connected users list. It must be run periodically.

        Note: It is safe to call this function from multiple threads simultaneously, the internal user and message queues are protected by mutexes

        Returns:
            A list of received messages
        """
    def sendMessage(self, messageType: LiveSessionChannel.MessageType) -> bool: 
        """
        Send a channel message

        Args:
            messageType: The type of message to send

        Returns:
            Whether the message was sent correctly
        """
    pass
class LiveSessionConfig():
    """
    Live session configuration keys

    Members:

      eVersion : Used for session file compatibility

      eAdmin : The session "owner" or "administrator" that is granted merge permissions

      eStageUri : The URI for the USD stage in the session

      eMode : 
                The live mode.
                    `default` or `root_authoring` : changes made in a live session are targeted to a single .live layer."
                    `auto_authoring` : changes made in a live session are targeted to one of many .live layers that are associated with sublayers within the root stage";
                

      eDescription : A description for the live session

      eName : The session name

      eInvalid : Invalid
    """
    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __init__(self, value: int) -> None: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @property
    def value(self) -> int:
        """
        :type: int
        """
    __members__: dict # value = {'eVersion': <LiveSessionConfig.eVersion: 0>, 'eAdmin': <LiveSessionConfig.eAdmin: 1>, 'eStageUri': <LiveSessionConfig.eStageUri: 2>, 'eMode': <LiveSessionConfig.eMode: 3>, 'eDescription': <LiveSessionConfig.eDescription: 4>, 'eName': <LiveSessionConfig.eName: 5>, 'eInvalid': <LiveSessionConfig.eInvalid: 6>}
    eAdmin: omni.connect.core._omni_connect_core.LiveSessionConfig # value = <LiveSessionConfig.eAdmin: 1>
    eDescription: omni.connect.core._omni_connect_core.LiveSessionConfig # value = <LiveSessionConfig.eDescription: 4>
    eInvalid: omni.connect.core._omni_connect_core.LiveSessionConfig # value = <LiveSessionConfig.eInvalid: 6>
    eMode: omni.connect.core._omni_connect_core.LiveSessionConfig # value = <LiveSessionConfig.eMode: 3>
    eName: omni.connect.core._omni_connect_core.LiveSessionConfig # value = <LiveSessionConfig.eName: 5>
    eStageUri: omni.connect.core._omni_connect_core.LiveSessionConfig # value = <LiveSessionConfig.eStageUri: 2>
    eVersion: omni.connect.core._omni_connect_core.LiveSessionConfig # value = <LiveSessionConfig.eVersion: 0>
    pass
class LiveSessionInfo():
    """
    A class that stores and validates Omniverse Live Session URIs and names.

    Live session context data is stored under a ``.live`` folder within the root stage's folder.  Stage-specific
    and session-specific folders are used under the ``.live`` folder to contain all of the data in one place.  These
    are the important files within the session folder:

        - Live Layer URI: ``<stage_folder> / <.live> / <my_usd_file.live> / <session_name.live> / root.live``
        - Live Config URI: ``<stage_folder> / <.live> / <my_usd_file.live> / <session_name.live> / __session__.toml``
        - Live Channel URI: ``<stage_folder> / <.live> / <my_usd_file.live> / <session_name.live> / __session__.channel``

    Possible usecase of browsing for existing sessions on a root USD stage and connecting to one:

        - Create a LiveSessionInfo with the root stage URI
        - Use ``getSessionNames()`` and present them to the user
        - The user selects a session and that session name is passed to ``init()``
        - Access the live session configuration file using ``getLiveSessionConfig()`` with ``LiveSessionInfo.getConfigUri()``
        - Join the live session message channel using ``LiveSessionChannel.create()`` with ``LiveSessionInfo.getChannelUri()``
        - Add the .live layer from ``LiveSessionInfo.getLiveLayerUri()`` to the root USD stage's session sublayers and set it as the edit target
    """
    @staticmethod
    def create(rootStageUri: str) -> LiveSessionInfo: 
        """
        Create an Omniverse live session info class

        The LiveSessionInfo class is first instantiated with the root stage URI (``omniverse://server/folder/stage.usd``), then
        LiveSessionInfo.getSessionNames() can be used to list the available sessions.

        Once a session name is determined, LiveSessionInfo.init() will finish the initialization of all of the paths
        and the other methods can be used.

        Note: The static factory method LiveSessionInfo.create() returns a ``std::shared_ptr`` so object lifetime is managed by scope.

        Args:
            uri: The live session's root stage URI

        Returns:
            A live session info interface shared pointer (std::shared_ptr<LiveSessionInfo>).  If rootStageUri is invalid then returns NoneType.
        """
    def exists(self) -> bool: 
        """
        Check for the existence of the session config (TOML) file

        This method returns an empty string until the session name is set with ``LiveSessionInfo.init()``

        Returns:
            Whether the session config file exists
        """
    def getAllSessionsFolderUri(self) -> str: 
        """
        Get the URI for the folder that contains all of the live sessions

        The Connector may want to watch this folder for new sessions, or poll it in a way
        that is different than how this class does.

        eg. ``<stage_folder> / <.live> / <my_usd_file.live>``

        Returns:
            The folder URI where all of the live sessions for the stage are stored
        """
    def getChannelUri(self) -> str: 
        """
        Get the URI for the live session Omniverse message channel file

        This channel file URI should be passed to ``LiveSessionChannel.create()``

        This method returns an empty string until the session name is set with ``LiveSessionInfo.init()``

        Returns:
            The live session message channel URI
        """
    def getConfigUri(self) -> str: 
        """
        Get the URI for the live session configuration file (currently implemented as TOML)

        This config file URI should be passed to ``getLiveSessionConfig()`` or ``createLiveSessionConfigFile()``

        This method returns an empty string until the session name is set with ``LiveSessionInfo.init()``

        Returns:
            The live session configuration file URI
        """
    def getLiveLayerUri(self) -> str: 
        """
        Get the URI for the .live layer file

        This method returns an empty string until the session name is set with ``LiveSessionInfo.init()``

        Returns:
            The .live layer URI for the session
        """
    def getName(self) -> str: 
        """
        Get the live session name

        This method returns an empty string until the session name is set with ``LiveSessionInfo.init()``

        Returns:
            The name of the live session
        """
    def getRootStageUri(self) -> str: 
        """
        Get the root stage URI for the live session

        Returns:
            The root stage URI that was passed to the create() method
        """
    @staticmethod
    def getSessionNameFromUri(sessionLink: str) -> str: 
        """
        Extracts the sessionName from a live session link uri
        ie: ``omniverse://ov/helloworld.usd?live_session_name=Default -> Default``

        Args:
            sessionLink: The session link to break

        Returns:
            sessionName: The session name or empty string if ``live_session_name`` not in query params
        """
    def getSessionNames(self) -> typing.List[str]: 
        """
        Get a list of existing sessions for the stage

        Note: this validates that each session actually exists by checking for the existence of the session config file

        Returns:
            A list of session names
        """
    def init(self, sessionName: str) -> bool: 
        """
        Set the session name and initialize the class so all member functions return complete URIs

        Many of the class methods don't function correctly until this method is called
        Session names must start with an alphabetical character, but may contain alphanumeric,
        hyphen, or underscore characters.

        Note: The session doesn't need to already exist to be valid, the intent is to generate all of the
        necessary URIs so the application can then either join or create the new session files.


        Args:
            sessionName: The intended name of the live session

        Returns:
            Whether the session info was initialized correctly
        """
    pass
class RotationOrder():
    """
    Enumerates the rotation order of the 3-angle Euler rotation.

    Members:

      eXyz

      eXzy

      eYxz

      eYzx

      eZxy

      eZyx
    """
    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __init__(self, value: int) -> None: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @property
    def value(self) -> int:
        """
        :type: int
        """
    __members__: dict # value = {'eXyz': <RotationOrder.eXyz: 0>, 'eXzy': <RotationOrder.eXzy: 1>, 'eYxz': <RotationOrder.eYxz: 2>, 'eYzx': <RotationOrder.eYzx: 3>, 'eZxy': <RotationOrder.eZxy: 4>, 'eZyx': <RotationOrder.eZyx: 5>}
    eXyz: omni.connect.core._omni_connect_core.RotationOrder # value = <RotationOrder.eXyz: 0>
    eXzy: omni.connect.core._omni_connect_core.RotationOrder # value = <RotationOrder.eXzy: 1>
    eYxz: omni.connect.core._omni_connect_core.RotationOrder # value = <RotationOrder.eYxz: 2>
    eYzx: omni.connect.core._omni_connect_core.RotationOrder # value = <RotationOrder.eYzx: 3>
    eZxy: omni.connect.core._omni_connect_core.RotationOrder # value = <RotationOrder.eZxy: 4>
    eZyx: omni.connect.core._omni_connect_core.RotationOrder # value = <RotationOrder.eZyx: 5>
    pass
class StringPrimvarData():
    """
    `PrimvarData` that holds `Vt.StringArray` values (e.g human readable descriptors).

                This is a read-only class to manage all `UsdGeom.Primvar` data as a single object without risk of detaching (copying) arrays.

                `UsdGeom.Primvars` are often used when authoring `UsdGeom.PointBased` prims (e.g meshes, curves, and point clouds) to describe surface varying
                properties that can affect how a prim is rendered, or to drive a surface deformation.

                However, `UsdGeom.Primvar` data can be quite intricate to use, especially with respect to indexed vs non-indexed primvars, element size, the
                complexities of `Vt.Array` detach (copy-on-write) semantics, and the ambiguity of "native" attributes vs primvar attributes (e.g. mesh normals).

                This class aims to provide simpler entry points to avoid common mistakes with respect to `UsdGeom.Primvar` data handling.

                All of the USD authoring "define" functions in this library accept optional `PrimvarData` to define e.g normals, display colors, etc.
            
    """
    def __eq__(self, arg0: StringPrimvarData) -> bool: 
        """
        Check that all data between two `PrimvarData` objects is identical.

        This differs from the equality operator in that it ensures the `Vt.Array` values and indices have not detached.

        Args:
            other: The other `PrimvarData`.

        Returns:
            True if all the member data is equal (but not necessarily identical arrays).
        """
    @typing.overload
    def __init__(self, interpolation: str, values: pxr.Vt.StringArray, elementSize: int = -1) -> None: 
        """
        Construct non-indexed `PrimvarData`.

        Note:
            To avoid immediate array iteration, validation does not occur during construction, and is deferred until `isValid()` is called.
            This may be counter-intuitive as `PrimvarData` provides read-only access, but full validation is often only possible within the context
            of specific surface topology, so premature validation would be redundant.

        Args:
            interpolation: The primvar interpolation. Must match `UsdGeom.Primvar.IsValidInterpolation()` to be considered valid.
            values: Read-only accessor to the values array.
            elementSize: Optional element size. This should be fairly uncommon.
                See [GetElementSize](https://openusd.org/release/api/class_usd_geom_primvar.html#a711c3088ebca00ca75308485151c8590) for details.

        Returns:
            The read-only `PrimvarData`.



        Construct indexed `PrimvarData`.

        Note:
            To avoid immediate array iteration, validation does not occur during construction, and is deferred until `isValid()` is called.
            This may be counter-intuitive as `PrimvarData` provides read-only access, but full validation is often only possible within the context
            of specific surface topology, so premature validation would be redundant.

        Args:
            interpolation: The primvar interpolation. Must match `UsdGeom.Primvar.IsValidInterpolation()` to be considered valid.
            values: Read-only accessor to the values array.
            indices: Read-only accessor to the indices array.
            elementSize: Optional element size. This should be fairly uncommon.
                See [GetElementSize](https://openusd.org/release/api/class_usd_geom_primvar.html#a711c3088ebca00ca75308485151c8590) for details.

        Returns:
            The read-only `PrimvarData`.
        """
    @typing.overload
    def __init__(self, interpolation: str, values: pxr.Vt.StringArray, indices: pxr.Vt.IntArray, elementSize: int = -1) -> None: ...
    def __ne__(self, arg0: StringPrimvarData) -> bool: 
        """
        Check for in-equality between two `PrimvarData` objects.

        Args:
            other: The other `PrimvarData`.

        Returns:
            True if any member data is not equal (but does not guarantee identical arrays).
        """
    def __str__(self) -> str: ...
    def effectiveSize(self) -> int: 
        """
        The effective size of the data, having accounted for values, indices, and element size.

        This is the number of variable values that "really" exist, as far as a consumer is concerned. The indices & elementSize are used as a storage
        optimization, but the consumer should consider the effective size as the number of "deduplicated" individual values.

        Returns:
            The effective size of the data.
        """
    def elementSize(self) -> int: 
        """
        The element size.

        Any value less than 1 is considered "non authored" and indicates no element size. This should be the most common case, as element size is a
        fairly esoteric extension of `UsdGeom.Primvar` data to account for non-typed array strides such as spherical harmonics float[9] arrays.

        See `UsdGeom.Primvar.GetElementSize()` for more details.

        Returns:
            The primvar element size.
        """
    @staticmethod
    def getPrimvarData(primvar: pxr.UsdGeom.Primvar, time: pxr.Usd.TimeCode = nan) -> StringPrimvarData: 
        """
        Construct a `PrimvarData` from a `UsdGeom.Primvar` that has already been authored.

        The primvar may be indexed, non-indexed, with or without elements, or it may not even be validly authored scene description.
        Use `isValid()` to confirm that valid data has been gathered.

        Args:
            primvar: The previously authored `UsdGeom.Primvar`.
            time: The time at which the attribute values are read.

        Returns:
            The read-only `PrimvarData`.
        """
    def hasIndices(self) -> bool: 
        """
        Whether this is indexed or non-indexed `PrimvarData`

        Returns:
            Whether this is indexed or non-indexed `PrimvarData`.
        """
    def index(self) -> bool: 
        """
        Update the values and indices of this `PrimvarData` object to avoid duplicate values.

        Updates will not be made in the following conditions:
            - If element size is greater than one.
            - If the existing indexing is efficient.
            - If there are no duplicate values.
            - If the existing indices are invalid

        Returns:
            True if the values and/or indices were modified.
        """
    def indices(self) -> pxr.Vt.IntArray: 
        """
        Access to the indices array.

        This method throws a runtime error if the `PrimvarData` is not indexed. For exception-free access, check `hasIndices()` before calling this.

        Note:
            It may contain an empty or invalid indices array. Use `PrimvarData.isValid()` to validate that the indices are not out-of-range.

        Returns:
            The primvar indices
        """
    def interpolation(self) -> str: 
        """
        The geometric interpolation.

        It may be an invalid interpolation. Use `PrimvarData.isValid()` or `UsdGeom.Primvar.IsValidInterpolation()` to confirm.

        Returns:
            The geometric interpolation.
        """
    def isIdentical(self, other: StringPrimvarData) -> bool: 
        """
        Check that all data between two `PrimvarData` objects is identical.

        This differs from the equality operator in that it ensures the `Vt.Array` values and indices have not detached.

        Args:
            other: The other `PrimvarData`.

        Returns:
            True if all the member data is equal and arrays are identical.
        """
    def isValid(self) -> bool: 
        """
        Whether the data is valid or invalid.

        This is a validation check with respect to the `PrimvarData` itself & the requirements of `UsdGeom.Prim`. It does not validate with respect to
        specific surface topology data, as no such data is available or consistant across `UsdGeom.PointBased` prim types.

        This validation checks the following, in this order, and returns false if any condition fails:

            - The interpolation matches `UsdGeom.Primvar.IsValidInterpolation()`.
            - The values are not empty. Note that individual values may be invalid (e.g `NaN` values on a `Vt.FloatArray`) but this will not be
              considered a failure, as some workflows allow for `NaN` to indicate non-authored elements or "holes" within the data.
            - If it is non-indexed, and has elements, that the values divide evenly by elementSize.
            - If it is indexed, and has elements, that the indices divide evenly by elementSize.
            - If it is indexed, that the indices are all within the expected range of the values array.

        Returns:
            Whether the data is valid or invalid.
        """
    def setPrimvar(self, primvar: pxr.UsdGeom.Primvar, time: pxr.Usd.TimeCode = nan) -> bool: 
        """
        Set data on an existing `UsdGeom.Primvar` from a `PrimvarData` that has already been authored.

        Any existing authored data on the primvar will be overwritten or blocked with the `PrimvarData` members.

        To copy data from one `UsdGeom.Primvar` to another, use `data: PrimvarData = PrimvarData.get(primvar: UsdGeom.Primvar)` to gather the data,
        then use `set(primvar: UsdGeom.Primvar)` to author it.

        Args:
            primvar: The previously authored `UsdGeom.Primvar`.
            time: The time at which the attribute values are written.

        Returns:
            Whether the `UsdGeom.Primvar` was completely authored from the member data.
            Any failure to author may leave the primvar in an unknown state (e.g. it may have been partially authored).
        """
    def values(self) -> pxr.Vt.StringArray: 
        """
        Access to the values array.

        Bear in mind the values may need to be accessed via `indices()` or using an `elementSize()` stride.

        It may contain an empty or invalid values array.

        Returns:
            The primvar values.
        """
    __hash__ = None
    pass
class TokenPrimvarData():
    """
    `PrimvarData` that holds `Vt.TokenArray` values (e.g more efficient human readable descriptors).

    This is a more efficient format than raw strings if you have many repeated values across different prims.

    Note:
        `TfToken` lifetime lasts the entire process. Too many tokens in memory may consume resources somewhat unexpectedly.


    This is a read-only class to manage all `UsdGeom.Primvar` data as a single object without risk of detaching (copying) arrays.

    `UsdGeom.Primvars` are often used when authoring `UsdGeom.PointBased` prims (e.g meshes, curves, and point clouds) to describe surface varying
    properties that can affect how a prim is rendered, or to drive a surface deformation.

    However, `UsdGeom.Primvar` data can be quite intricate to use, especially with respect to indexed vs non-indexed primvars, element size, the
    complexities of `Vt.Array` detach (copy-on-write) semantics, and the ambiguity of "native" attributes vs primvar attributes (e.g. mesh normals).

    This class aims to provide simpler entry points to avoid common mistakes with respect to `UsdGeom.Primvar` data handling.

    All of the USD authoring "define" functions in this library accept optional `PrimvarData` to define e.g normals, display colors, etc.
    """
    def __eq__(self, arg0: TokenPrimvarData) -> bool: 
        """
        Check that all data between two `PrimvarData` objects is identical.

        This differs from the equality operator in that it ensures the `Vt.Array` values and indices have not detached.

        Args:
            other: The other `PrimvarData`.

        Returns:
            True if all the member data is equal (but not necessarily identical arrays).
        """
    @typing.overload
    def __init__(self, interpolation: str, values: pxr.Vt.TokenArray, elementSize: int = -1) -> None: 
        """
        Construct non-indexed `PrimvarData`.

        Note:
            To avoid immediate array iteration, validation does not occur during construction, and is deferred until `isValid()` is called.
            This may be counter-intuitive as `PrimvarData` provides read-only access, but full validation is often only possible within the context
            of specific surface topology, so premature validation would be redundant.

        Args:
            interpolation: The primvar interpolation. Must match `UsdGeom.Primvar.IsValidInterpolation()` to be considered valid.
            values: Read-only accessor to the values array.
            elementSize: Optional element size. This should be fairly uncommon.
                See [GetElementSize](https://openusd.org/release/api/class_usd_geom_primvar.html#a711c3088ebca00ca75308485151c8590) for details.

        Returns:
            The read-only `PrimvarData`.



        Construct indexed `PrimvarData`.

        Note:
            To avoid immediate array iteration, validation does not occur during construction, and is deferred until `isValid()` is called.
            This may be counter-intuitive as `PrimvarData` provides read-only access, but full validation is often only possible within the context
            of specific surface topology, so premature validation would be redundant.

        Args:
            interpolation: The primvar interpolation. Must match `UsdGeom.Primvar.IsValidInterpolation()` to be considered valid.
            values: Read-only accessor to the values array.
            indices: Read-only accessor to the indices array.
            elementSize: Optional element size. This should be fairly uncommon.
                See [GetElementSize](https://openusd.org/release/api/class_usd_geom_primvar.html#a711c3088ebca00ca75308485151c8590) for details.

        Returns:
            The read-only `PrimvarData`.
        """
    @typing.overload
    def __init__(self, interpolation: str, values: pxr.Vt.TokenArray, indices: pxr.Vt.IntArray, elementSize: int = -1) -> None: ...
    def __ne__(self, arg0: TokenPrimvarData) -> bool: 
        """
        Check for in-equality between two `PrimvarData` objects.

        Args:
            other: The other `PrimvarData`.

        Returns:
            True if any member data is not equal (but does not guarantee identical arrays).
        """
    def __str__(self) -> str: ...
    def effectiveSize(self) -> int: 
        """
        The effective size of the data, having accounted for values, indices, and element size.

        This is the number of variable values that "really" exist, as far as a consumer is concerned. The indices & elementSize are used as a storage
        optimization, but the consumer should consider the effective size as the number of "deduplicated" individual values.

        Returns:
            The effective size of the data.
        """
    def elementSize(self) -> int: 
        """
        The element size.

        Any value less than 1 is considered "non authored" and indicates no element size. This should be the most common case, as element size is a
        fairly esoteric extension of `UsdGeom.Primvar` data to account for non-typed array strides such as spherical harmonics float[9] arrays.

        See `UsdGeom.Primvar.GetElementSize()` for more details.

        Returns:
            The primvar element size.
        """
    @staticmethod
    def getPrimvarData(primvar: pxr.UsdGeom.Primvar, time: pxr.Usd.TimeCode = nan) -> TokenPrimvarData: 
        """
        Construct a `PrimvarData` from a `UsdGeom.Primvar` that has already been authored.

        The primvar may be indexed, non-indexed, with or without elements, or it may not even be validly authored scene description.
        Use `isValid()` to confirm that valid data has been gathered.

        Args:
            primvar: The previously authored `UsdGeom.Primvar`.
            time: The time at which the attribute values are read.

        Returns:
            The read-only `PrimvarData`.
        """
    def hasIndices(self) -> bool: 
        """
        Whether this is indexed or non-indexed `PrimvarData`

        Returns:
            Whether this is indexed or non-indexed `PrimvarData`.
        """
    def index(self) -> bool: 
        """
        Update the values and indices of this `PrimvarData` object to avoid duplicate values.

        Updates will not be made in the following conditions:
            - If element size is greater than one.
            - If the existing indexing is efficient.
            - If there are no duplicate values.
            - If the existing indices are invalid

        Returns:
            True if the values and/or indices were modified.
        """
    def indices(self) -> pxr.Vt.IntArray: 
        """
        Access to the indices array.

        This method throws a runtime error if the `PrimvarData` is not indexed. For exception-free access, check `hasIndices()` before calling this.

        Note:
            It may contain an empty or invalid indices array. Use `PrimvarData.isValid()` to validate that the indices are not out-of-range.

        Returns:
            The primvar indices
        """
    def interpolation(self) -> str: 
        """
        The geometric interpolation.

        It may be an invalid interpolation. Use `PrimvarData.isValid()` or `UsdGeom.Primvar.IsValidInterpolation()` to confirm.

        Returns:
            The geometric interpolation.
        """
    def isIdentical(self, other: TokenPrimvarData) -> bool: 
        """
        Check that all data between two `PrimvarData` objects is identical.

        This differs from the equality operator in that it ensures the `Vt.Array` values and indices have not detached.

        Args:
            other: The other `PrimvarData`.

        Returns:
            True if all the member data is equal and arrays are identical.
        """
    def isValid(self) -> bool: 
        """
        Whether the data is valid or invalid.

        This is a validation check with respect to the `PrimvarData` itself & the requirements of `UsdGeom.Prim`. It does not validate with respect to
        specific surface topology data, as no such data is available or consistant across `UsdGeom.PointBased` prim types.

        This validation checks the following, in this order, and returns false if any condition fails:

            - The interpolation matches `UsdGeom.Primvar.IsValidInterpolation()`.
            - The values are not empty. Note that individual values may be invalid (e.g `NaN` values on a `Vt.FloatArray`) but this will not be
              considered a failure, as some workflows allow for `NaN` to indicate non-authored elements or "holes" within the data.
            - If it is non-indexed, and has elements, that the values divide evenly by elementSize.
            - If it is indexed, and has elements, that the indices divide evenly by elementSize.
            - If it is indexed, that the indices are all within the expected range of the values array.

        Returns:
            Whether the data is valid or invalid.
        """
    def setPrimvar(self, primvar: pxr.UsdGeom.Primvar, time: pxr.Usd.TimeCode = nan) -> bool: 
        """
        Set data on an existing `UsdGeom.Primvar` from a `PrimvarData` that has already been authored.

        Any existing authored data on the primvar will be overwritten or blocked with the `PrimvarData` members.

        To copy data from one `UsdGeom.Primvar` to another, use `data: PrimvarData = PrimvarData.get(primvar: UsdGeom.Primvar)` to gather the data,
        then use `set(primvar: UsdGeom.Primvar)` to author it.

        Args:
            primvar: The previously authored `UsdGeom.Primvar`.
            time: The time at which the attribute values are written.

        Returns:
            Whether the `UsdGeom.Primvar` was completely authored from the member data.
            Any failure to author may leave the primvar in an unknown state (e.g. it may have been partially authored).
        """
    def values(self) -> pxr.Vt.TokenArray: 
        """
        Access to the values array.

        Bear in mind the values may need to be accessed via `indices()` or using an `elementSize()` stride.

        It may contain an empty or invalid values array.

        Returns:
            The primvar values.
        """
    __hash__ = None
    pass
class Vec2fPrimvarData():
    """
    `PrimvarData` that holds `Vt.Vec2fArray` values (e.g texture coordinates).

                This is a read-only class to manage all `UsdGeom.Primvar` data as a single object without risk of detaching (copying) arrays.

                `UsdGeom.Primvars` are often used when authoring `UsdGeom.PointBased` prims (e.g meshes, curves, and point clouds) to describe surface varying
                properties that can affect how a prim is rendered, or to drive a surface deformation.

                However, `UsdGeom.Primvar` data can be quite intricate to use, especially with respect to indexed vs non-indexed primvars, element size, the
                complexities of `Vt.Array` detach (copy-on-write) semantics, and the ambiguity of "native" attributes vs primvar attributes (e.g. mesh normals).

                This class aims to provide simpler entry points to avoid common mistakes with respect to `UsdGeom.Primvar` data handling.

                All of the USD authoring "define" functions in this library accept optional `PrimvarData` to define e.g normals, display colors, etc.
            
    """
    def __eq__(self, arg0: Vec2fPrimvarData) -> bool: 
        """
        Check that all data between two `PrimvarData` objects is identical.

        This differs from the equality operator in that it ensures the `Vt.Array` values and indices have not detached.

        Args:
            other: The other `PrimvarData`.

        Returns:
            True if all the member data is equal (but not necessarily identical arrays).
        """
    @typing.overload
    def __init__(self, interpolation: str, values: pxr.Vt.Vec2fArray, elementSize: int = -1) -> None: 
        """
        Construct non-indexed `PrimvarData`.

        Note:
            To avoid immediate array iteration, validation does not occur during construction, and is deferred until `isValid()` is called.
            This may be counter-intuitive as `PrimvarData` provides read-only access, but full validation is often only possible within the context
            of specific surface topology, so premature validation would be redundant.

        Args:
            interpolation: The primvar interpolation. Must match `UsdGeom.Primvar.IsValidInterpolation()` to be considered valid.
            values: Read-only accessor to the values array.
            elementSize: Optional element size. This should be fairly uncommon.
                See [GetElementSize](https://openusd.org/release/api/class_usd_geom_primvar.html#a711c3088ebca00ca75308485151c8590) for details.

        Returns:
            The read-only `PrimvarData`.



        Construct indexed `PrimvarData`.

        Note:
            To avoid immediate array iteration, validation does not occur during construction, and is deferred until `isValid()` is called.
            This may be counter-intuitive as `PrimvarData` provides read-only access, but full validation is often only possible within the context
            of specific surface topology, so premature validation would be redundant.

        Args:
            interpolation: The primvar interpolation. Must match `UsdGeom.Primvar.IsValidInterpolation()` to be considered valid.
            values: Read-only accessor to the values array.
            indices: Read-only accessor to the indices array.
            elementSize: Optional element size. This should be fairly uncommon.
                See [GetElementSize](https://openusd.org/release/api/class_usd_geom_primvar.html#a711c3088ebca00ca75308485151c8590) for details.

        Returns:
            The read-only `PrimvarData`.
        """
    @typing.overload
    def __init__(self, interpolation: str, values: pxr.Vt.Vec2fArray, indices: pxr.Vt.IntArray, elementSize: int = -1) -> None: ...
    def __ne__(self, arg0: Vec2fPrimvarData) -> bool: 
        """
        Check for in-equality between two `PrimvarData` objects.

        Args:
            other: The other `PrimvarData`.

        Returns:
            True if any member data is not equal (but does not guarantee identical arrays).
        """
    def __str__(self) -> str: ...
    def effectiveSize(self) -> int: 
        """
        The effective size of the data, having accounted for values, indices, and element size.

        This is the number of variable values that "really" exist, as far as a consumer is concerned. The indices & elementSize are used as a storage
        optimization, but the consumer should consider the effective size as the number of "deduplicated" individual values.

        Returns:
            The effective size of the data.
        """
    def elementSize(self) -> int: 
        """
        The element size.

        Any value less than 1 is considered "non authored" and indicates no element size. This should be the most common case, as element size is a
        fairly esoteric extension of `UsdGeom.Primvar` data to account for non-typed array strides such as spherical harmonics float[9] arrays.

        See `UsdGeom.Primvar.GetElementSize()` for more details.

        Returns:
            The primvar element size.
        """
    @staticmethod
    def getPrimvarData(primvar: pxr.UsdGeom.Primvar, time: pxr.Usd.TimeCode = nan) -> Vec2fPrimvarData: 
        """
        Construct a `PrimvarData` from a `UsdGeom.Primvar` that has already been authored.

        The primvar may be indexed, non-indexed, with or without elements, or it may not even be validly authored scene description.
        Use `isValid()` to confirm that valid data has been gathered.

        Args:
            primvar: The previously authored `UsdGeom.Primvar`.
            time: The time at which the attribute values are read.

        Returns:
            The read-only `PrimvarData`.
        """
    def hasIndices(self) -> bool: 
        """
        Whether this is indexed or non-indexed `PrimvarData`

        Returns:
            Whether this is indexed or non-indexed `PrimvarData`.
        """
    def index(self) -> bool: 
        """
        Update the values and indices of this `PrimvarData` object to avoid duplicate values.

        Updates will not be made in the following conditions:
            - If element size is greater than one.
            - If the existing indexing is efficient.
            - If there are no duplicate values.
            - If the existing indices are invalid

        Returns:
            True if the values and/or indices were modified.
        """
    def indices(self) -> pxr.Vt.IntArray: 
        """
        Access to the indices array.

        This method throws a runtime error if the `PrimvarData` is not indexed. For exception-free access, check `hasIndices()` before calling this.

        Note:
            It may contain an empty or invalid indices array. Use `PrimvarData.isValid()` to validate that the indices are not out-of-range.

        Returns:
            The primvar indices
        """
    def interpolation(self) -> str: 
        """
        The geometric interpolation.

        It may be an invalid interpolation. Use `PrimvarData.isValid()` or `UsdGeom.Primvar.IsValidInterpolation()` to confirm.

        Returns:
            The geometric interpolation.
        """
    def isIdentical(self, other: Vec2fPrimvarData) -> bool: 
        """
        Check that all data between two `PrimvarData` objects is identical.

        This differs from the equality operator in that it ensures the `Vt.Array` values and indices have not detached.

        Args:
            other: The other `PrimvarData`.

        Returns:
            True if all the member data is equal and arrays are identical.
        """
    def isValid(self) -> bool: 
        """
        Whether the data is valid or invalid.

        This is a validation check with respect to the `PrimvarData` itself & the requirements of `UsdGeom.Prim`. It does not validate with respect to
        specific surface topology data, as no such data is available or consistant across `UsdGeom.PointBased` prim types.

        This validation checks the following, in this order, and returns false if any condition fails:

            - The interpolation matches `UsdGeom.Primvar.IsValidInterpolation()`.
            - The values are not empty. Note that individual values may be invalid (e.g `NaN` values on a `Vt.FloatArray`) but this will not be
              considered a failure, as some workflows allow for `NaN` to indicate non-authored elements or "holes" within the data.
            - If it is non-indexed, and has elements, that the values divide evenly by elementSize.
            - If it is indexed, and has elements, that the indices divide evenly by elementSize.
            - If it is indexed, that the indices are all within the expected range of the values array.

        Returns:
            Whether the data is valid or invalid.
        """
    def setPrimvar(self, primvar: pxr.UsdGeom.Primvar, time: pxr.Usd.TimeCode = nan) -> bool: 
        """
        Set data on an existing `UsdGeom.Primvar` from a `PrimvarData` that has already been authored.

        Any existing authored data on the primvar will be overwritten or blocked with the `PrimvarData` members.

        To copy data from one `UsdGeom.Primvar` to another, use `data: PrimvarData = PrimvarData.get(primvar: UsdGeom.Primvar)` to gather the data,
        then use `set(primvar: UsdGeom.Primvar)` to author it.

        Args:
            primvar: The previously authored `UsdGeom.Primvar`.
            time: The time at which the attribute values are written.

        Returns:
            Whether the `UsdGeom.Primvar` was completely authored from the member data.
            Any failure to author may leave the primvar in an unknown state (e.g. it may have been partially authored).
        """
    def values(self) -> pxr.Vt.Vec2fArray: 
        """
        Access to the values array.

        Bear in mind the values may need to be accessed via `indices()` or using an `elementSize()` stride.

        It may contain an empty or invalid values array.

        Returns:
            The primvar values.
        """
    __hash__ = None
    pass
class Vec3fPrimvarData():
    """
    `PrimvarData` that holds `Vt.Vec3fArray` values (e.g normals, colors, or other vectors).

                This is a read-only class to manage all `UsdGeom.Primvar` data as a single object without risk of detaching (copying) arrays.

                `UsdGeom.Primvars` are often used when authoring `UsdGeom.PointBased` prims (e.g meshes, curves, and point clouds) to describe surface varying
                properties that can affect how a prim is rendered, or to drive a surface deformation.

                However, `UsdGeom.Primvar` data can be quite intricate to use, especially with respect to indexed vs non-indexed primvars, element size, the
                complexities of `Vt.Array` detach (copy-on-write) semantics, and the ambiguity of "native" attributes vs primvar attributes (e.g. mesh normals).

                This class aims to provide simpler entry points to avoid common mistakes with respect to `UsdGeom.Primvar` data handling.

                All of the USD authoring "define" functions in this library accept optional `PrimvarData` to define e.g normals, display colors, etc.
            
    """
    def __eq__(self, arg0: Vec3fPrimvarData) -> bool: 
        """
        Check that all data between two `PrimvarData` objects is identical.

        This differs from the equality operator in that it ensures the `Vt.Array` values and indices have not detached.

        Args:
            other: The other `PrimvarData`.

        Returns:
            True if all the member data is equal (but not necessarily identical arrays).
        """
    @typing.overload
    def __init__(self, interpolation: str, values: pxr.Vt.Vec3fArray, elementSize: int = -1) -> None: 
        """
        Construct non-indexed `PrimvarData`.

        Note:
            To avoid immediate array iteration, validation does not occur during construction, and is deferred until `isValid()` is called.
            This may be counter-intuitive as `PrimvarData` provides read-only access, but full validation is often only possible within the context
            of specific surface topology, so premature validation would be redundant.

        Args:
            interpolation: The primvar interpolation. Must match `UsdGeom.Primvar.IsValidInterpolation()` to be considered valid.
            values: Read-only accessor to the values array.
            elementSize: Optional element size. This should be fairly uncommon.
                See [GetElementSize](https://openusd.org/release/api/class_usd_geom_primvar.html#a711c3088ebca00ca75308485151c8590) for details.

        Returns:
            The read-only `PrimvarData`.



        Construct indexed `PrimvarData`.

        Note:
            To avoid immediate array iteration, validation does not occur during construction, and is deferred until `isValid()` is called.
            This may be counter-intuitive as `PrimvarData` provides read-only access, but full validation is often only possible within the context
            of specific surface topology, so premature validation would be redundant.

        Args:
            interpolation: The primvar interpolation. Must match `UsdGeom.Primvar.IsValidInterpolation()` to be considered valid.
            values: Read-only accessor to the values array.
            indices: Read-only accessor to the indices array.
            elementSize: Optional element size. This should be fairly uncommon.
                See [GetElementSize](https://openusd.org/release/api/class_usd_geom_primvar.html#a711c3088ebca00ca75308485151c8590) for details.

        Returns:
            The read-only `PrimvarData`.
        """
    @typing.overload
    def __init__(self, interpolation: str, values: pxr.Vt.Vec3fArray, indices: pxr.Vt.IntArray, elementSize: int = -1) -> None: ...
    def __ne__(self, arg0: Vec3fPrimvarData) -> bool: 
        """
        Check for in-equality between two `PrimvarData` objects.

        Args:
            other: The other `PrimvarData`.

        Returns:
            True if any member data is not equal (but does not guarantee identical arrays).
        """
    def __str__(self) -> str: ...
    def effectiveSize(self) -> int: 
        """
        The effective size of the data, having accounted for values, indices, and element size.

        This is the number of variable values that "really" exist, as far as a consumer is concerned. The indices & elementSize are used as a storage
        optimization, but the consumer should consider the effective size as the number of "deduplicated" individual values.

        Returns:
            The effective size of the data.
        """
    def elementSize(self) -> int: 
        """
        The element size.

        Any value less than 1 is considered "non authored" and indicates no element size. This should be the most common case, as element size is a
        fairly esoteric extension of `UsdGeom.Primvar` data to account for non-typed array strides such as spherical harmonics float[9] arrays.

        See `UsdGeom.Primvar.GetElementSize()` for more details.

        Returns:
            The primvar element size.
        """
    @staticmethod
    def getPrimvarData(primvar: pxr.UsdGeom.Primvar, time: pxr.Usd.TimeCode = nan) -> Vec3fPrimvarData: 
        """
        Construct a `PrimvarData` from a `UsdGeom.Primvar` that has already been authored.

        The primvar may be indexed, non-indexed, with or without elements, or it may not even be validly authored scene description.
        Use `isValid()` to confirm that valid data has been gathered.

        Args:
            primvar: The previously authored `UsdGeom.Primvar`.
            time: The time at which the attribute values are read.

        Returns:
            The read-only `PrimvarData`.
        """
    def hasIndices(self) -> bool: 
        """
        Whether this is indexed or non-indexed `PrimvarData`

        Returns:
            Whether this is indexed or non-indexed `PrimvarData`.
        """
    def index(self) -> bool: 
        """
        Update the values and indices of this `PrimvarData` object to avoid duplicate values.

        Updates will not be made in the following conditions:
            - If element size is greater than one.
            - If the existing indexing is efficient.
            - If there are no duplicate values.
            - If the existing indices are invalid

        Returns:
            True if the values and/or indices were modified.
        """
    def indices(self) -> pxr.Vt.IntArray: 
        """
        Access to the indices array.

        This method throws a runtime error if the `PrimvarData` is not indexed. For exception-free access, check `hasIndices()` before calling this.

        Note:
            It may contain an empty or invalid indices array. Use `PrimvarData.isValid()` to validate that the indices are not out-of-range.

        Returns:
            The primvar indices
        """
    def interpolation(self) -> str: 
        """
        The geometric interpolation.

        It may be an invalid interpolation. Use `PrimvarData.isValid()` or `UsdGeom.Primvar.IsValidInterpolation()` to confirm.

        Returns:
            The geometric interpolation.
        """
    def isIdentical(self, other: Vec3fPrimvarData) -> bool: 
        """
        Check that all data between two `PrimvarData` objects is identical.

        This differs from the equality operator in that it ensures the `Vt.Array` values and indices have not detached.

        Args:
            other: The other `PrimvarData`.

        Returns:
            True if all the member data is equal and arrays are identical.
        """
    def isValid(self) -> bool: 
        """
        Whether the data is valid or invalid.

        This is a validation check with respect to the `PrimvarData` itself & the requirements of `UsdGeom.Prim`. It does not validate with respect to
        specific surface topology data, as no such data is available or consistant across `UsdGeom.PointBased` prim types.

        This validation checks the following, in this order, and returns false if any condition fails:

            - The interpolation matches `UsdGeom.Primvar.IsValidInterpolation()`.
            - The values are not empty. Note that individual values may be invalid (e.g `NaN` values on a `Vt.FloatArray`) but this will not be
              considered a failure, as some workflows allow for `NaN` to indicate non-authored elements or "holes" within the data.
            - If it is non-indexed, and has elements, that the values divide evenly by elementSize.
            - If it is indexed, and has elements, that the indices divide evenly by elementSize.
            - If it is indexed, that the indices are all within the expected range of the values array.

        Returns:
            Whether the data is valid or invalid.
        """
    def setPrimvar(self, primvar: pxr.UsdGeom.Primvar, time: pxr.Usd.TimeCode = nan) -> bool: 
        """
        Set data on an existing `UsdGeom.Primvar` from a `PrimvarData` that has already been authored.

        Any existing authored data on the primvar will be overwritten or blocked with the `PrimvarData` members.

        To copy data from one `UsdGeom.Primvar` to another, use `data: PrimvarData = PrimvarData.get(primvar: UsdGeom.Primvar)` to gather the data,
        then use `set(primvar: UsdGeom.Primvar)` to author it.

        Args:
            primvar: The previously authored `UsdGeom.Primvar`.
            time: The time at which the attribute values are written.

        Returns:
            Whether the `UsdGeom.Primvar` was completely authored from the member data.
            Any failure to author may leave the primvar in an unknown state (e.g. it may have been partially authored).
        """
    def values(self) -> pxr.Vt.Vec3fArray: 
        """
        Access to the values array.

        Bear in mind the values may need to be accessed via `indices()` or using an `elementSize()` stride.

        It may contain an empty or invalid values array.

        Returns:
            The primvar values.
        """
    __hash__ = None
    pass
def addDiffuseTextureToPbrMaterial(material: pxr.UsdShade.Material, texturePath: pxr.Sdf.AssetPath) -> bool:
    """
    Add a diffuse texture to a PBR material

    It is expected that the material was created by the Connect SDK's defineOmniPbrMaterial() function.

    Note:
        The material prim's "Color" input will be removed and replaced with "DiffuseTexture".
        Due to the input removal this function should be used at initial authoring time rather than in a stronger layer.

    Args:
        material: The UsdShade.Material prim to add the texture
        texturePath: The Sdf.AssetPath for the texture

    Returns:
        Whether or not the texture was added to the material
    """
def addLogConsumer(name: str, callback: object) -> None:
    """
    Adds a log consumer.

    The provided callback will be hit when any log within the app's set log level is published.
    Log level is set in the implementer's omni.connect.client.toml file.
    If two consumers with the same name are added the first is removed automatically.
    Callbacks must take the form Callable[str, omni.log.Level, str] where the arguments are the channel,
    log level and message respectively.

    Args:
        name: The name of the consumer. No two log consumers can have the same name.
        callback: The function to be called when a log is published. Callable[str, omni.log.Level, str].
    """
def addMetallicTextureToPbrMaterial(material: pxr.UsdShade.Material, texturePath: pxr.Sdf.AssetPath) -> bool:
    """
    Add a metallic texture to a PBR material

    It is expected that the material was created by the Connect SDK's defineOmniPbrMaterial() function.

    Note:
        The material prim's "Metallic" input will be removed and replaced with "MetallicTexture".
        Due to the input removal this function should be used at initial authoring time rather than in a stronger layer.

    Args:
        material: The UsdShade.Material prim to add the texture
        texturePath: The Sdf.AssetPath for the texture

    Returns:
        Whether or not the texture was added to the material
    """
def addNormalTextureToPbrMaterial(material: pxr.UsdShade.Material, texturePath: pxr.Sdf.AssetPath) -> bool:
    """
    Add a normal texture to a PBR material

    It is expected that the material was created by the Connect SDK's defineOmniPbrMaterial() function.

    Args:
        material: The UsdShade.Material prim to add the texture
        texturePath: The Sdf.AssetPath for the texture

    Returns:
        Whether or not the texture was added to the material
    """
def addOpacityTextureToPbrMaterial(material: pxr.UsdShade.Material, texturePath: pxr.Sdf.AssetPath) -> bool:
    """
    Add an Opacity texture to a PBR material

    It is expected that the material was created by the Connect SDK's defineOmniPbrMaterial() function.

    Note:
        The material prim's "Opacity" input will be removed and replaced with "OpacityTexture".
        Due to the input removal this function should be used at initial authoring time rather than in a stronger layer.

    These shader parameters will be set to produce better masked geometry:
    - MDL OmniPBR: `opacity_threshold = float_epsilon` (just greater than zero)
    - UsdPreviewSurface: `ior = 1.0`
    - UsdPreviewSurface: `opacityThreshold = float_epsilon` (just greater than zero)

    Args:
        material: The UsdShade.Material prim to add the texture
        texturePath: The Sdf.AssetPath for the texture

    Returns:
        Whether or not the texture was added to the material
    """
def addOrmTextureToPbrMaterial(material: pxr.UsdShade.Material, texturePath: pxr.Sdf.AssetPath) -> bool:
    """
    Add an ORM texture to a PBR material

    It is expected that the material was created by the Connect SDK's defineOmniPbrMaterial() function.

    Note:
        The material prim's "Roughness" and "Metallic" inputs will be removed and replaced with "ORMTexture".
        Due to the input removal this function should be used at initial authoring time rather than in a stronger layer.

    Args:
        material: The UsdShade.Material prim to add the texture
        texturePath: The Sdf.AssetPath for the texture

    Returns:
        Whether or not the texture was added to the material
    """
def addRoughnessTextureToPbrMaterial(material: pxr.UsdShade.Material, texturePath: pxr.Sdf.AssetPath) -> bool:
    """
    Add a roughness texture to a PBR material

    It is expected that the material was created by the Connect SDK's defineOmniPbrMaterial() function.

    Note:
        The material prim's "Roughness" input will be removed and replaced with "RoughnessTexture".
        Due to the input removal this function should be used at initial authoring time rather than in a stronger layer.

    Args:
        material: The UsdShade.Material prim to add the texture
        texturePath: The Sdf.AssetPath for the texture

    Returns:
        Whether or not the texture was added to the material
    """
def bindMaterial(prim: pxr.Usd.Prim, material: pxr.UsdShade.Material) -> None:
    """
    Binds a UsdShade.Material to a Usd.Prim

    Args:
        prim: Usd.Prim to hind the material to
        material: UsdShade.Material to bind to the prim
    """
def blockDisplayName(prim: pxr.Usd.Prim) -> bool:
    """
    Block this prim's display name (metadata)

    The fallback value will be explicitly authored to cause the value to resolve as if there were no authored value opinions in weaker layers

    Args:
        prim: The prim to block the display name for

    Returns:
        True on success, otherwise false
    """
def canRemovePrim(prim: pxr.Usd.Prim) -> bool:
    """
    Determines if the given `Usd.Prim` can be removed safely.

    Multi-layer editing and Omniverse Live editing present challenges when trying to remove prims.
    We cannot always safely delete prims, sometimes they must must be deactivated instead.
    Use `canRemovePrim` to determine if a prim can be removed via the current `Usd.EditTarget`,
    and if so, use `removeOrDeactivatePrim` to do it safely.

    Note:
        Nucleus is an optional feature which is required when using Omniverse Live editing.
        This function will work without Nucleus, but the logic may be overly complicated for simpler
        single layer or "static" composition use cases.

    Args:
        prim: The prim to be removed.

    Returns:
        A bool indicating if the prim can be removed.
    """
def clearDisplayName(prim: pxr.Usd.Prim) -> bool:
    """
    Clears this prim's display name (metadata) in the current EditTarget (only)

    Args:
        prim: The prim to clear the display name for

    Returns:
        True on success, otherwise false
    """
def clientVersion() -> str:
    """
    Verify the expected Omniverse Client Library version is being loaded at runtime.

    Returns:
        A human-readable version string for the Omniverse Client Library.
    """
def computeEffectiveDisplayName(prim: pxr.Usd.Prim) -> str:
    """
    Calculate the effective display name of this prim

    If the display name is un-authored or empty then the prim's name is returned

    Args:
        prim: The prim to compute the display name for

    Returns:
        The effective display name
    """
def computeEffectiveMdlSurfaceShader(material: pxr.UsdShade.Material) -> pxr.UsdShade.Shader:
    """
    Get the effective surface Shader of a Material for the MDL render context.

    If no valid Shader is connected to the MDL render context then the universal render context will be considered.

    Args:
        material: The Material to consider

    Returns:
        The connected Shader. Returns an invalid object on error.
    """
def computeEffectivePreviewSurfaceShader(material: pxr.UsdShade.Material) -> pxr.UsdShade.Shader:
    """
    Get the effective surface Shader of a Material for the universal render context.

    Args:
        material: The Material to consider

    Returns:
        The connected Shader. Returns an invalid object on error.
    """
def configureStage(stage: pxr.Usd.Stage, defaultPrimName: str, upAxis: str, linearUnits: float) -> bool:
    """
    Configure a stage so that the defining metadata is explicitly authored

    The default prim will be used as the target of a reference or payload to this layer that doesn't specify a prim path.
    A root prim with the given `defaultPrimName` will be defined on the stage.

    The stage metrics of [Up Axis](https://openusd.org/release/api/group___usd_geom_up_axis__group.html#details) and
    [Linear Units](https://openusd.org/release/api/group___usd_geom_linear_units__group.html#details) will be authored.

    Args:
        stage: The stage to be configured.
        defaultPrimName: Name of the default root prim.
        upAxis: The up axis for all the geometry contained in the stage.
        linearUnits: The meters per unit for all linear measurements in the stage.

    Returns:
        A bool indicating if the metadata was successfully authored.
    """
def copyPrim(prim: pxr.Usd.Prim, destination: pxr.Sdf.Path) -> bool:
    """
    Copy the given `Usd.Prim` to a new location.

    Multi-layer editing and Omniverse Live editing present challenges when trying to copy prims.
    We cannot necessarily perform a simple copy of the `Sdf.PrimSpec` on the current `Usd.EditTarget`,
    but may need to account for the full layer stack and opinions.

    Note:
        Nucleus is an optional feature which is required when using Omniverse Live editing.
        This function will work without Nucleus, but the logic may be overly complicated for simpler
        single layer or "static" composition use cases.

    Args:
        prim: The prim to be copied.
        destination: The path of the new copy.

    Returns:
        A bool indicating if the copy was successful.
    """
def createColorAttr(prim: pxr.UsdLux.LightAPI, value: pxr.Gf.Vec3f, time: pxr.Usd.TimeCode = nan) -> None:
    """
    Author the color attribute for a prim with UsdLux.Light[API] applied

    Args:
        prim: A prim from a UsdLux.Light[API]
        value: The Gf.Vec3f color value to set both old and new USD schema properties
        time: The time at which the attribute value is written
    """
def createColorTemperatureAttr(prim: pxr.UsdLux.LightAPI, value: float, time: pxr.Usd.TimeCode = nan) -> None:
    """
    Author the color temperature attribute for a prim with UsdLux.Light[API] applied

    Args:
        prim: A prim from a UsdLux.Light[API]
        value: The float value to set both old and new USD schema properties
        time: The time at which the attribute value is written
    """
def createDistantAngleAttr(prim: pxr.UsdLux.DistantLight, value: float, time: pxr.Usd.TimeCode = nan) -> None:
    """
    Author the distant angle attribute for a UsdLux.DistantLight prim

    Args:
        prim: A prim from a UsdLux.DistantLight
        value: The float value to set both old and new USD schema properties
        time: The time at which the attribute value is written
    """
def createDomeTextureFileAttr(prim: pxr.UsdLux.DomeLight, value: pxr.Sdf.AssetPath, time: pxr.Usd.TimeCode = nan) -> None:
    """
    Author the dome texture file attribute for a UsdLux.DomeLight prim

    Args:
        prim: A prim from a UsdLux.DomeLight
        value: The string path value to set both old and new USD schema properties
        time: The time at which the attribute value is written
    """
def createDomeTextureFormatAttr(prim: pxr.UsdLux.DomeLight, value: str, time: pxr.Usd.TimeCode = nan) -> None:
    """
    Author the dome texture format attribute for a UsdLux.DomeLight prim

    Args:
        prim: A prim from a UsdLux.DomeLight
        value: The UsdLux.Tokens format value to set both old and new USD schema properties
        time: The time at which the attribute value is written
    """
def createEnableColorTemperatureAttr(prim: pxr.UsdLux.LightAPI, value: bool, time: pxr.Usd.TimeCode = nan) -> None:
    """
    Author the "enable color temperature" attribute for a prim with UsdLux.Light[API] applied

    Args:
        prim: A prim from a UsdLux.Light[API]
        value: The boolean value to set both old and new USD schema properties
        time: The time at which the attribute value is written
    """
def createIntensityAttr(prim: pxr.UsdLux.LightAPI, value: float, time: pxr.Usd.TimeCode = nan) -> None:
    """
    Author the intensity attribute for a prim with UsdLux.Light[API] applied

    Args:
        prim: A prim from a UsdLux.Light[API]
        value: The float value to set both old and new USD schema properties
        time: The time at which the attribute value is written
    """
def createLightExtentAttr(prim: pxr.Usd.Prim, time: pxr.Usd.TimeCode = nan) -> None:
    """
    Author the extent attribute for a UsdLuxCylinderLight, UsdLuxDiskLight,
    UsdLuxRectLight, UsdLuxSphereLight, or UsdLuxPortalLight.

    Setting this attribute improves performance by negating the need to compute it on load.

    Args:
        prim: The prim to author the attribute
        time: The time at which the attribute value is written
    """
def createLiveSessionConfigFile(uri: str, config: typing.Dict[LiveSessionConfig, str]) -> bool:
    """
    Create a Live Session configuration file

    The current serialization for these config files is TOML.

    Args:
        uri: The location of the new session config file
        config: A dictionary of LiveSessionConfig-value pairs

    Returns:
        Whether the session config file was created successfully
    """
def createMaterial(parent: pxr.Usd.Prim, name: str) -> pxr.UsdShade.Material:
    """
    Create a UsdShade.Material as the child of the Usd.Prim argument

    Args:
        parent: Parent Usd.Prim for the material to be created
        name: Name of the material to be created
    Returns:
        The newly created UsdShade.Material. Returns an Invalid prim on error.
    """
def createMdlShader(material: pxr.UsdShade.Material, name: str, mdlPath: pxr.Sdf.AssetPath, module: str, connectMaterialOutputs: bool = True) -> pxr.UsdShade.Shader:
    """
    Create a UsdShade.Shader as a child of the UsdShade.Material argument with the specified MDL

    Args:
        material: Parent UsdShade.Material for the shader to be created
        name: Name of the shader to be created
        mdlPath: Absolute or relative path to the MDL asset
        module: Name of the MDL module to set as source asset sub-identifier for the shader
        connectMaterialOutputs: If true, it creates the surface, volume and displacement outputs of the material and connects them to the shader output
    Returns:
        the newly created UsdShade.Shader. Returns an Invalid prim on error.
    """
def createMdlShaderInput(material: pxr.UsdShade.Material, name: str, value: pxr.Vt.Value, typeName: pxr.Sdf.ValueTypeName, colorSpace: typing.Optional[ColorSpace] = None) -> pxr.UsdShade.Input:
    """
    Create an MDL shader input

    If the shader input already exists and is a different type, defined in the current edit target layer -> it will be removed and recreated

    If the shader input already exists and has a connected source -> the source will be disconnected before being set

    Note:
        When creating texture asset inputs (diffuse, normal, roughness, etc.) it is important to set the colorSpace parameter so that
        the textures are sampled correctly.  Typically, diffuse is "auto", which resolves to "sRGB".  Normal, roughness, and other textures
        should be "raw".

    Args:
        material: The UsdShade.Material prim that contains the MDL shader
        name: Name of the input to be created
        value: The value assigned to the input
        typeName: The Sdf.ValueTypeName of the input
        colorSpace: If set, the newly created input's colorSpace attribute

    Returns:
        The newly created Usd.Shade.Input input.  Returns an Invalid Usd.Shade.Input on error.
    """
def createRectHeightAttr(prim: pxr.UsdLux.RectLight, value: float, time: pxr.Usd.TimeCode = nan) -> None:
    """
    Author the height attribute for a UsdLux.RectLight prim

    Args:
        prim: A prim from a UsdLux.RectLight
        value: The float value to set both old and new USD schema properties
        time: The time at which the attribute value is written
    """
def createRectTextureFileAttr(prim: pxr.UsdLux.RectLight, value: pxr.Sdf.AssetPath, time: pxr.Usd.TimeCode = nan) -> None:
    """
    Author the texture file attribute for a UsdLux.RectLight prim

    Args:
        prim: A prim from a UsdLux.RectLight
        value: The string value to set both old and new USD schema properties
        time: The time at which the attribute value is written
    """
def createRectWidthAttr(prim: pxr.UsdLux.RectLight, value: float, time: pxr.Usd.TimeCode = nan) -> None:
    """
    Author the width attribute for a UsdLux.RectLight prim

    Args:
        prim: A prim from a UsdLux.RectLight
        value: The float value to set both old and new USD schema properties
        time: The time at which the attribute value is written
    """
def createShapingConeAngleAttr(prim: pxr.UsdLux.ShapingAPI, value: float, time: pxr.Usd.TimeCode = nan) -> None:
    """
    Author the cone angle attribute for a prim with UsdLux.ShapingAPI applied

    Args:
        prim: A prim to apply UsdLux.ShapingAPI
        value: The float value to set both old and new USD schema properties
        time: The time at which the attribute value is written
    """
def createShapingConeSoftnessAttr(prim: pxr.UsdLux.ShapingAPI, value: float, time: pxr.Usd.TimeCode = nan) -> None:
    """
    Author the cone softness attribute for a prim with UsdLux.ShapingAPI applied

    Args:
        prim: A prim to apply UsdLux.ShapingAPI
        value: The float value to set both old and new USD schema properties
        time: The time at which the attribute value is written
    """
def createSphereRadiusAttr(prim: pxr.UsdLux.SphereLight, value: float, time: pxr.Usd.TimeCode = nan) -> None:
    """
    Author the sphere radius attribute for a UsdLux.SphereLight prim

    Args:
        prim: A prim from a UsdLux.SphereLight
        value: The float radius value to set both old and new USD schema properties
        time: The time at which the attribute value is written
    """
def createUriCheckpoint(uri: str, comment: str = None) -> bool:
    """
    Add a commented checkpoint for given uri in Nucleus server if the Nucleus server supports checkpoint

    Args:
        uri: The uri of the file to add checkpoint.
        comment: The checkpoints comment.

    Returns:
        A bool indicating if the commented checkpoint was added successfully.
    """
@typing.overload
def defineCamera(stage: pxr.Usd.Stage, path: pxr.Sdf.Path, cameraData: pxr.Gf.Camera) -> pxr.UsdGeom.Camera:
    """
    Defines a basic 3d camera on the stage.

    Note that `Gf.Camera` is a simplified form of 3d camera data that does not account for time-sampled data, shutter window,
    stereo role, or exposure. If you need to author those properties, do so after defining the `UsdGeom.Camera`.

    An invalid UsdGeomCamera will be returned if camera attributes could not be authored successfully.

    Parameters:
        - **stage** - The stage on which to define the camera
        - **path** - The absolute prim path at which to define the camera
        - **cameraData** - The camera data to set, including the world space transform matrix

    Returns:
        A `UsdGeom.Camera` schema wrapping the defined `Usd.Prim`.




    Defines a basic 3d camera on the stage.

    This is an overloaded member function, provided for convenience. It differs from the above function only in what arguments it accepts.

    Parameters:
        - **parent** - Prim below which to define the camera
        - **name** - Name of the camera
        - **cameraData** - The camera data to set, including the world space transform matrix

    Returns:
        A `UsdGeom.Camera` schema wrapping the defined `Usd.Prim`.
    """
@typing.overload
def defineCamera(parent: pxr.Usd.Prim, name: str, cameraData: pxr.Gf.Camera) -> pxr.UsdGeom.Camera:
    pass
@typing.overload
def defineCubicBasisCurves(stage: pxr.Usd.Stage, path: pxr.Sdf.Path, curveVertexCounts: pxr.Vt.IntArray, points: pxr.Vt.Vec3fArray, basis: str = 'bezier', wrap: str = 'nonperiodic', widths: typing.Optional[FloatPrimvarData] = None, normals: typing.Optional[Vec3fPrimvarData] = None, displayColor: typing.Optional[Vec3fPrimvarData] = None, displayOpacity: typing.Optional[FloatPrimvarData] = None) -> pxr.UsdGeom.BasisCurves:
    """
    Defines a batched Cubic `UsdGeom.BasisCurves` prim on the stage.

    Attribute values will be validated and in the case of invalid data the Curves will not be defined. An invalid `UsdGeom.BasisCurves`
    object will be returned in this case.

    Values will be authored for all attributes required to completely describe the Curves, even if weaker matching opinions already exist.

        - Curve Vertex Counts
        - Points
        - Type
        - Basis
        - Wrap
        - Extent

    The "extent" of the Curves will be computed and authored based on the `points` and `widths` provided.

    The following common primvars can optionally be authored at the same time using a `PrimvarData` to specify interpolation, data,
    and optionally indices or elementSize.

        - Widths
        - Normals
        - Display Color
        - Display Opacity

    For both widths and normals, if they are provided, they are authored as `primvars:widths` and `primvars:normals`, so that indexing is
    possible and to ensure that the value takes precedence in cases where both the non-primvar and primvar attributes are authored.

    Parameters:
        - **stage** The stage on which to define the curves.
        - **path** The absolute prim path at which to define the curves.
        - **curveVertexCounts** The number of vertices in each independent curve. The length of this array determines the number of curves.
        - **points** Vertex/CV positions for the curves described in local space.
        - **basis** The basis specifies the vstep and matrix used for cubic interpolation. Accepted values for cubic curves are
            `UsdGeom.Tokens.bezier`, `UsdGeom.Tokens.bspline`, or `UsdGeom.Tokens.catmullRom`.
        - **wrap** Determines how the start and end points of the curve behave. Accepted values are `UsdGeom.Tokens.nonperiodic`,
            `UsdGeom.Tokens.periodic`, and `UsdGeom.Tokens.pinned` (bspline and catmullRom only).
        - **widths** Values for the width specification for the curves.
        - **normals** Values for the normals primvar for the curves. If authored, the curves are considered oriented ribbons rather than tubes.
        - **displayColor** Values to be authored for the display color primvar.
        - **displayOpacity** Values to be authored for the display opacity primvar.

    Returns
        `UsdGeom.BasisCurves` schema wrapping the defined `Usd.Prim`



    Defines a batched Cubic `UsdGeom.BasisCurves` prim on the stage.

    This is an overloaded member function, provided for convenience. It differs from the above function only in what arguments it accepts.

    Parameters:
        - **prim** The stage on which to define the curves.
        - **name** The absolute prim path at which to define the curves.
        - **curveVertexCounts** The number of vertices in each independent curve. The length of this array determines the number of curves.
        - **points** Vertex/CV positions for the curves described in local space.
        - **basis** The basis specifies the vstep and matrix used for cubic interpolation. Accepted values for cubic curves are
            `UsdGeom.Tokens.bezier`, `UsdGeom.Tokens.bspline`, or `UsdGeom.Tokens.catmullRom`.
        - **wrap** Determines how the start and end points of the curve behave. Accepted values are `UsdGeom.Tokens.nonperiodic`,
            `UsdGeom.Tokens.periodic`, and `UsdGeom.Tokens.pinned` (bspline and catmullRom only).
        - **widths** Values for the width specification for the curves.
        - **normals** Values for the normals primvar for the curves. If authored, the curves are considered oriented ribbons rather than tubes.
        - **displayColor** Values to be authored for the display color primvar.
        - **displayOpacity** Values to be authored for the display opacity primvar.

    Returns
        `UsdGeom.BasisCurves` schema wrapping the defined `Usd.Prim`
    """
@typing.overload
def defineCubicBasisCurves(prim: pxr.Usd.Prim, name: str, curveVertexCounts: pxr.Vt.IntArray, points: pxr.Vt.Vec3fArray, basis: str = 'bezier', wrap: str = 'nonperiodic', widths: typing.Optional[FloatPrimvarData] = None, normals: typing.Optional[Vec3fPrimvarData] = None, displayColor: typing.Optional[Vec3fPrimvarData] = None, displayOpacity: typing.Optional[FloatPrimvarData] = None) -> pxr.UsdGeom.BasisCurves:
    pass
@typing.overload
def defineDomeLight(stage: pxr.Usd.Stage, path: pxr.Sdf.Path, intensity: float = 1.0, texturePath: str = None, textureFormat: str = 'automatic') -> pxr.UsdLux.DomeLight:
    """
    Creates a dome light with an optional texture.

    A dome light represents light emitted inward from a distant external environment, such as a sky or IBL light probe.

    Texture Format values:

        - `automatic` - Tries to determine the layout from the file itself.
        - `latlong` - Latitude as X, longitude as Y.
        - `mirroredBall` - An image of the environment reflected in a sphere, using an implicitly orthogonal projection.
        - `angular` - Similar to mirroredBall but the radial dimension is mapped linearly to the angle, for better sampling at the edges.
        - `cubeMapVerticalCross` - Set to "automatic" by default.

    Parameters:
        - **stage** - The stage in which the light should be authored
        - **path** - The path which the light prim should be written to
        - **intensity** - The intensity value of the dome light
        - **texturePath** - The path to the texture file to use on the dome light.
        - **textureFormat** - How the texture should be mapped on the dome light.

    Returns:
        The dome light if created successfully.



    Creates a dome light with an optional texture.

    This is an overloaded member function, provided for convenience. It differs from the above function only in what arguments it accepts.

    Parameters:
        - **parent** - Prim below which to define the light
        - **name** - Name of the light
        - **intensity** - The intensity value of the dome light
        - **texturePath** - The path to the texture file to use on the dome light.
        - **textureFormat** - How the texture should be mapped on the dome light.

    Returns:
        The dome light if created successfully.
    """
@typing.overload
def defineDomeLight(parent: pxr.Usd.Prim, name: str, intensity: float = 1.0, texturePath: str = None, textureFormat: str = 'automatic') -> pxr.UsdLux.DomeLight:
    pass
@typing.overload
def defineLinearBasisCurves(stage: pxr.Usd.Stage, path: pxr.Sdf.Path, curveVertexCounts: pxr.Vt.IntArray, points: pxr.Vt.Vec3fArray, wrap: str = 'nonperiodic', widths: typing.Optional[FloatPrimvarData] = None, normals: typing.Optional[Vec3fPrimvarData] = None, displayColor: typing.Optional[Vec3fPrimvarData] = None, displayOpacity: typing.Optional[FloatPrimvarData] = None) -> pxr.UsdGeom.BasisCurves:
    """
    Defines a batched Linear `UsdGeom.BasisCurves` prim on the stage.

    Attribute values will be validated and in the case of invalid data the Curves will not be defined. An invalid `UsdGeom.BasisCurves`
    object will be returned in this case.

    Values will be authored for all attributes required to completely describe the Curves, even if weaker matching opinions already exist.

        - Curve Vertex Counts
        - Points
        - Type
        - Wrap
        - Extent

    The "extent" of the Curves will be computed and authored based on the `points` and `widths` provided.

    The following common primvars can optionally be authored at the same time using a `PrimvarData` to specify interpolation, data,
    and optionally indices or elementSize.

        - Widths
        - Normals
        - Display Color
        - Display Opacity

    For both widths and normals, if they are provided, they are authored as `primvars:widths` and `primvars:normals`, so that indexing is
    possible and to ensure that the value takes precedence in cases where both the non-primvar and primvar attributes are authored.

    Parameters:
        - **stage** The stage on which to define the curves.
        - **path** The absolute prim path at which to define the curves.
        - **curveVertexCounts** The number of vertices in each independent curve. The length of this array determines the number of curves.
        - **points** Vertex/CV positions for the curves described in local space.
        - **wrap** Determines how the start and end points of the curve behave. Accepted values for linear curves are
            `UsdGeom.Tokens.nonperiodic` and `UsdGeom.Tokens.periodic`.
        - **widths** Values for the width specification for the curves.
        - **normals** Values for the normals primvar for the curves. If authored, the curves are considered oriented ribbons rather than tubes.
        - **displayColor** Values to be authored for the display color primvar.
        - **displayOpacity** Values to be authored for the display opacity primvar.

    Returns
        `UsdGeom.BasisCurves` schema wrapping the defined `Usd.Prim`



    Defines a batched Linear `UsdGeom.BasisCurves` prim on the stage.

    This is an overloaded member function, provided for convenience. It differs from the above function only in what arguments it accepts.

    Parameters:
        - **prim** The stage on which to define the curves.
        - **name** The absolute prim path at which to define the curves.
        - **curveVertexCounts** The number of vertices in each independent curve. The length of this array determines the number of curves.
        - **points** Vertex/CV positions for the curves described in local space.
        - **wrap** Determines how the start and end points of the curve behave. Accepted values for linear curves are
            `UsdGeom.Tokens.nonperiodic` and `UsdGeom.Tokens.periodic`.
        - **widths** Values for the width specification for the curves.
        - **normals** Values for the normals primvar for the curves. If authored, the curves are considered oriented ribbons rather than tubes.
        - **displayColor** Values to be authored for the display color primvar.
        - **displayOpacity** Values to be authored for the display opacity primvar.

    Returns
        `UsdGeom.BasisCurves` schema wrapping the defined `Usd.Prim`
    """
@typing.overload
def defineLinearBasisCurves(prim: pxr.Usd.Prim, name: str, curveVertexCounts: pxr.Vt.IntArray, points: pxr.Vt.Vec3fArray, wrap: str = 'nonperiodic', widths: typing.Optional[FloatPrimvarData] = None, normals: typing.Optional[Vec3fPrimvarData] = None, displayColor: typing.Optional[Vec3fPrimvarData] = None, displayOpacity: typing.Optional[FloatPrimvarData] = None) -> pxr.UsdGeom.BasisCurves:
    pass
@typing.overload
def defineOmniGlassMaterial(stage: pxr.Usd.Stage, path: pxr.Sdf.Path, color: pxr.Gf.Vec3f, indexOfRefraction: float = 1.4910000562667847) -> pxr.UsdShade.Material:
    """
    Defines an OmniGlass `UsdShade.Material` interface that drives both an RTX render context and a UsdPreviewSurface context

    MDL and UsdPreviewSurface use a linear color space, please convert RGB and sRGB values to linear

    Note:
        The use of MDL shaders inside this Material interface is considered an implementation detail of the RTX Renderer.
        Once the RTX Renderer supports OpenPBR or MaterialX shaders we may change the implementation to author those shaders instead of MDL.

    Parameters:
        - **stage** - The stage on which to define the Material
        - **path** - The absolute prim path at which to define the Material
        - **color** - The color of the Material
        - **indexOfRefraction** - The Index of Refraction to set, 1.0-4.0 range

    Returns:
        The newly defined UsdShade.Material. Returns an Invalid prim on error



    Defines an OmniGlass `UsdShade.Material` interface that drives both an RTX render context and a UsdPreviewSurface context

    This is an overloaded member function, provided for convenience. It differs from the above function only in what arguments it accepts.

    Parameters:
        - **parent** - Prim below which to define the Material
        - **name** - Name of the Material
        - **color** - The color of the Material
        - **indexOfRefraction** - The Index of Refraction to set, 1.0-4.0 range

    Returns:
        The newly defined UsdShade.Material. Returns an Invalid prim on error
    """
@typing.overload
def defineOmniGlassMaterial(parent: pxr.Usd.Prim, name: str, color: pxr.Gf.Vec3f, indexOfRefraction: float = 1.4910000562667847) -> pxr.UsdShade.Material:
    pass
@typing.overload
def defineOmniPbrMaterial(stage: pxr.Usd.Stage, path: pxr.Sdf.Path, color: pxr.Gf.Vec3f, opacity: float = 1.0, roughness: float = 0.5, metallic: float = 0.0) -> pxr.UsdShade.Material:
    """
    Defines an OmniPBR `UsdShade.Material` interface that drives both an RTX render context and a UsdPreviewSurface context

    MDL and UsdPreviewSurface use a linear color space, please convert RGB and sRGB values to linear

    Note:
        The use of MDL shaders inside this Material interface is considered an implementation detail of the RTX Renderer.
        Once the RTX Renderer supports OpenPBR or MaterialX shaders we may change the implementation to author those shaders instead of MDL.

    Parameters:
        - **stage** - The stage on which to define the Material
        - **path** - The absolute prim path at which to define the Material
        - **color** - The diffuse color of the Material
        - **opacity** - The Opacity Amount to set. When less than 1.0, Enable Opacity is set to true and Fractional Opacity is enabled in the RT renderer
        - **roughness** - The Roughness Amount to set, 0.0-1.0 range where 1.0 = flat and 0.0 = glossy
        - **metallic** - The Metallic Amount to set, 0.0-1.0 range where 1.0 = max metallic and 0.0 = no metallic

    Returns:
        The newly defined UsdShade.Material. Returns an Invalid prim on error



    Defines an OmniPBR `UsdShade.Material` interface that drives both an RTX render context and a UsdPreviewSurface context

    This is an overloaded member function, provided for convenience. It differs from the above function only in what arguments it accepts.

    Parameters:
        - **parent** - Prim below which to define the Material
        - **name** - Name of the Material
        - **color** - The diffuse color of the Material
        - **opacity** - The Opacity Amount to set. When less than 1.0, Enable Opacity is set to true and Fractional Opacity is enabled in the RT renderer
        - **roughness** - The Roughness Amount to set, 0.0-1.0 range where 1.0 = flat and 0.0 = glossy
        - **metallic** - The Metallic Amount to set, 0.0-1.0 range where 1.0 = max metallic and 0.0 = no metallic

    Returns:
        The newly defined UsdShade.Material. Returns an Invalid prim on error
    """
@typing.overload
def defineOmniPbrMaterial(parent: pxr.Usd.Prim, name: str, color: pxr.Gf.Vec3f, opacity: float = 1.0, roughness: float = 0.5, metallic: float = 0.0) -> pxr.UsdShade.Material:
    pass
@typing.overload
def definePointCloud(stage: pxr.Usd.Stage, path: pxr.Sdf.Path, points: pxr.Vt.Vec3fArray, ids: typing.Optional[pxr.Vt.Int64Array] = None, widths: typing.Optional[FloatPrimvarData] = None, normals: typing.Optional[Vec3fPrimvarData] = None, displayColor: typing.Optional[Vec3fPrimvarData] = None, displayOpacity: typing.Optional[FloatPrimvarData] = None) -> pxr.UsdGeom.Points:
    """
    Defines a `UsdGeom.Points` prim on the stage.

    Attribute values will be validated and in the case of invalid data the Points will not be defined. An invalid `UsdGeom.Points`
    object will be returned in this case.

    Values will be authored for all attributes required to completely describe the Points, even if weaker matching opinions already exist.

        - Point Count
        - Points
        - Extent

    The "extent" of the Points will be computed and authored based on the `points` and `widths` provided.

    The following common primvars can optionally be authored at the same time using a `PrimvarData` to specify interpolation, data,
    and optionally indices or elementSize.

        - Ids
        - Widths
        - Normals
        - Display Color
        - Display Opacity

    For both widths and normals, if they are provided, they are authored as `primvars:widths` and `primvars:normals`, so that indexing is
    possible and to ensure that the value takes precedence in cases where both the non-primvar and primvar attributes are authored.

    Parameters:
        - **stage** The stage on which to define the points.
        - **path** The absolute prim path at which to define the points.
        - **points** Vertex/CV positions for the points described in local space.
        - **ids** Values for the id specification for the points.
        - **widths** Values for the width specification for the points.
        - **normals** Values for the normals primvar for the points. Only Vertex normals are considered valid.
        - **displayColor** Values to be authored for the display color primvar.
        - **displayOpacity** Values to be authored for the display opacity primvar.

    Returns
        `UsdGeom.Points` schema wrapping the defined `Usd.Prim`



    Defines a `UsdGeom.Points` prim on the stage.

    This is an overloaded member function, provided for convenience. It differs from the above function only in what arguments it accepts.

    Parameters:
        - **prim** The stage on which to define the points.
        - **name** The absolute prim path at which to define the points.
        - **points** Vertex/CV positions for the points described in local space.
        - **ids** Values for the id specification for the points.
        - **widths** Values for the width specification for the points.
        - **normals** Values for the normals primvar for the points. Only Vertex normals are considered valid.
        - **displayColor** Values to be authored for the display color primvar.
        - **displayOpacity** Values to be authored for the display opacity primvar.

    Returns
        `UsdGeom.Points` schema wrapping the defined `Usd.Prim`
    """
@typing.overload
def definePointCloud(prim: pxr.Usd.Prim, name: str, points: pxr.Vt.Vec3fArray, ids: typing.Optional[pxr.Vt.Int64Array] = None, widths: typing.Optional[FloatPrimvarData] = None, normals: typing.Optional[Vec3fPrimvarData] = None, displayColor: typing.Optional[Vec3fPrimvarData] = None, displayOpacity: typing.Optional[FloatPrimvarData] = None) -> pxr.UsdGeom.Points:
    pass
@typing.overload
def definePolyMesh(stage: pxr.Usd.Stage, path: pxr.Sdf.Path, faceVertexCounts: pxr.Vt.IntArray, faceVertexIndices: pxr.Vt.IntArray, points: pxr.Vt.Vec3fArray, normals: typing.Optional[Vec3fPrimvarData] = None, uvs: typing.Optional[Vec2fPrimvarData] = None, displayColor: typing.Optional[Vec3fPrimvarData] = None, displayOpacity: typing.Optional[FloatPrimvarData] = None) -> pxr.UsdGeom.Mesh:
    """
    Defines a basic polygon mesh on the stage.

    All interrelated attribute values will be authored, even if weaker matching opinions already exist.

    The following common primvars can optionally be authored at the same time.

        - Normals
        - Primary UV Set
        - Display Color
        - Display Opacity

    Parameters:
        - **stage** - The stage on which to define the mesh
        - **path** - The absolute prim path at which to define the mesh
        - **faceVertexCounts** - The number of vertices in each face of the mesh
        - **faceVertexIndices** - Indices of the positions from the `points` to use for each face vertex
        - **points** - Vertex positions for the mesh described points in local space
        - **normals** - Values to be authored for the normals primvar
        - **uvs** - Values to be authored for the uv primvar
        - **displayColor** - Value to be authored for the display color primvar
        - **displayOpacity** - Value to be authored for the display opacity primvar

    Returns:
        UsdGeomMesh schema wrapping the defined UsdPrim.




    Defines a basic polygon mesh on the stage.

    All interrelated attribute values will be authored, even if weaker matching opinions already exist.

    This is an overloaded member function, provided for convenience. It differs from the above function only in what arguments it accepts.

    Parameters:
        - **parent** - Prim below which to define the mesh
        - **name** - Name of the mesh
        - **faceVertexCounts** - The number of vertices in each face of the mesh
        - **faceVertexIndices** - Indices of the positions from the `points` to use for each face vertex
        - **points** - Vertex positions for the mesh described points in local space
        - **normals** - Values to be authored for the normals primvar
        - **uvs** - Values to be authored for the uv primvar
        - **displayColor** - Value to be authored for the display color primvar
        - **displayOpacity** - Value to be authored for the display opacity primvar

    Returns:
        UsdGeomMesh schema wrapping the defined UsdPrim.
    """
@typing.overload
def definePolyMesh(stage: pxr.Usd.Prim, path: str, faceVertexCounts: pxr.Vt.IntArray, faceVertexIndices: pxr.Vt.IntArray, points: pxr.Vt.Vec3fArray, normals: typing.Optional[Vec3fPrimvarData] = None, uvs: typing.Optional[Vec2fPrimvarData] = None, displayColor: typing.Optional[Vec3fPrimvarData] = None, displayOpacity: typing.Optional[FloatPrimvarData] = None) -> pxr.UsdGeom.Mesh:
    pass
@typing.overload
def defineRectLight(stage: pxr.Usd.Stage, path: pxr.Sdf.Path, width: float, height: float, intensity: float = 1.0, texturePath: str = None) -> pxr.UsdLux.RectLight:
    """
    Creates a rectangular (rect) light with an optional texture.

    A rect light represents light emitted from one side of a rectangle.

    Parameters:
        - **stage** - The stage in which the light should be authored
        - **path** - The path which the light prim should be written to
        - **width** - The width of the rectangular light, in the local X axis.
        - **height** - The height of the rectangular light, in the local Y axis.
        - **intensity** - The intensity value of the rectangular light
        - **texturePath** - Optional - The path to the texture file to use on the rectangular light.

    Returns:
        The rect light if created successfully.



    Creates a rectangular (rect) light with an optional texture.

    This is an overloaded member function, provided for convenience. It differs from the above function only in what arguments it accepts.

    Parameters:
        - **parent** - Prim below which to define the light
        - **name** - Name of the light
        - **width** - The width of the rectangular light, in the local X axis.
        - **height** - The height of the rectangular light, in the local Y axis.
        - **intensity** - The intensity value of the rectangular light
        - **texturePath** - Optional - The path to the texture file to use on the rectangular light.

    Returns:
        The rect light if created successfully.
    """
@typing.overload
def defineRectLight(parent: pxr.Usd.Prim, name: str, width: float, height: float, intensity: float = 1.0, texturePath: str = None) -> pxr.UsdLux.RectLight:
    pass
@typing.overload
def defineXform(stage: pxr.Usd.Stage, path: pxr.Sdf.Path, transform: typing.Optional[pxr.Gf.Transform] = None) -> pxr.UsdGeom.Xform:
    """
    Defines an xform on the stage.

    Parameters:
        - **stage** - The stage on which to define the xform
        - **path** - The absolute prim path at which to define the xform
        - **transform** - Optional local transform to set

    Returns:
        UsdGeom.Xform schema wrapping the defined Usd.Prim. Returns an invalid schema on error.



    Defines an xform on the stage.

    Parameters:
        - **parent** - Prim below which to define the xform
        - **name** - Name of the xform
        - **transform** - Optional local transform to set

    Returns:
        UsdGeom.Xform schema wrapping the defined Usd.Prim. Returns an invalid schema on error.
    """
@typing.overload
def defineXform(parent: pxr.Usd.Prim, name: str, transform: typing.Optional[pxr.Gf.Transform] = None) -> pxr.UsdGeom.Xform:
    pass
def doesUriExist(uri: str) -> bool:
    """
    Determine if the URI exists and is accessible via the Omniverse Client Library.

    Note this function respects user level access. If the connected user does not have
    read permissions for the URI (via `omni.client.AccessFlags`), then it will be reported
    as not existing.

    Returns:
        A bool indicating if the URI exists.
    """
def enableStandardOutputStream(enabled: bool) -> None:
    """
    Enables and disables logging to the standard output stream.

    This is a convenience around Carbonite's ILogging.

    Args:
        enabled: Determine if the output stream should be enabled or disabled
    """
def exportLayer(layer: pxr.Sdf.Layer, identifier: str, comment: str = None, fileFormatArgs: typing.Dict[str, str] = {}) -> bool:
    """
    Export the given `SdfLayer` to an identifier with an optional comment.

    Note this does not impact sublayers or any layers that this layer may be contributing to.

    The comment will be authored in the layer as the SdfLayer comment.

    If the layer is being exported to an Omniverse Nucleus server with checkpoints enabled, then the comment will be added to the checkpoint.

    Args:
        layer: The layer to be exported.
        identifier: The identifier to be used for the new layer.
        comment: The comment.
        fileFormatArgs: Additional file format-specific arguments to be supplied during layer export.

    Returns:
        A bool indicating if the export was successfully.
    """
def getDisplayName(prim: pxr.Usd.Prim) -> str:
    """
    Return this prim's display name (metadata).

    Args:
        prim: The prim to get the display name from

    Returns:
        Authored value, or an empty string if no display name has been set.
    """
def getDistantLightAttrNames() -> list(str):
    """
    Get a list of both current version and forward/reverse compatible UsdLux.DistantLightAPI attribute names

    The new attribute names have "inputs:" prepended to the names to make them connectable,
    this function will return both so that a USD object change notice could filter on light attributes.

    Returns:
        A list that includes both old and new schema attribute names
    """
def getDomeLightAttrNames() -> list(str):
    """
    Get a list of both current version and forward/reverse compatible UsdLux.DomeLightAPI attribute names

    The new attribute names have "inputs:" prepended to the names to make them connectable,
    this function will return both so that a USD object change notice could filter on light attributes.

    Returns:
        A list that includes both old and new schema attribute names
    """
def getExportOptions() -> object:
    """
    Get the export option settings.

    Returns:
        Option settings in dictionary.
    """
def getExportOptionsAsFileFormatArguments() -> typing.Dict[str, str]:
    """
    Get the export option settings.
    The returned values are converted to strings. Array items will be converted to a space separated string.
    The returned key "usdEncoding" is mapping to "format".

    Returns:
        Option settings in dictionary.
    """
def getImportOptions() -> object:
    """
    Get the import option settings.

    Returns:
        Option settings in dictionary.
    """
def getImportOptionsAsFileFormatArguments() -> typing.Dict[str, str]:
    """
    Get the import option settings.
    The returned values are converted to strings. Array items will be converted to space separated string.

    Returns:
        Option settings in dictionary.
    """
def getLightAPIAttrNames() -> list(str):
    """
    Get a list of both current version and forward/reverse compatible UsdLux.Light[API] attribute names

    The new attribute names have "inputs:" prepended to the names to make them connectable,
    this function will return both so that a USD object change notice could filter on light attributes.

    Returns:
        A list that includes both old and new schema attribute names
    """
def getLightAttr(defaultAttr: pxr.Usd.Attribute, PreferNewSchema: bool = True) -> pxr.Usd.Attribute:
    """
    Get the "correct" light attribute for a light that could have any combination of authored old and new UsdLux schema attributes

    The new attribute names have "inputs:" prepended to the names to make them connectable.

        - Light has only "intensity" authored: return "intensity" attribute

        - Light has only "inputs:intensity" authored: return "inputs:intensity" attribute

        - Light has both "inputs:intensity" and "intensity" authored: depends on the `preferNewSchema` argument

    Args:
        defaultAttr: The attribute from the light schema for the attribute to be read: eg. UsdLux.RectLight.GetHeightAttr()
        preferNewSchema: If true and both old and new UsdLux schema attributes are authored on a light prim, the new schema attribute is returned

    Returns:
        The attribute from which the light value should be read
    """
def getLiveSessionConfig(uri: str) -> typing.Dict[LiveSessionConfig, str]:
    """
    Get a configuration value from an existing Live Session configuration file

    This function requires that the session config already exists, otherwise it will fail

    Args:
        uri: The location of the existing session config file

    Returns:
        All configuration values in the live settings config (LiveSessionConfig-value pairs)
    """
def getLocalTransform(prim: pxr.Usd.Prim, time: pxr.Usd.TimeCode = nan) -> pxr.Gf.Transform:
    """
    Get the local transform of a prim at a given time.

    Args:
        prim: The prim to get local transform from.
        time: Time at which to query the value.

    Returns:
        Transform value as a transform.
    """
def getLocalTransformComponents(prim: pxr.Usd.Prim, time: pxr.Usd.TimeCode = nan) -> tuple:
    """
    Get the local transform of a prim at a given time in the form of common transform components.

    Args:
        prim: The prim to get local transform from.
        time: Time at which to query the value.

    Returns:
        Transform value as a tuple of translation, pivot, rotation, rotation order, scale.
    """
def getLocalTransformMatrix(prim: pxr.Usd.Prim, time: pxr.Usd.TimeCode = nan) -> pxr.Gf.Matrix4d:
    """
    Get the local transform of a prim at a given time in the form of a 4x4 matrix.

    Args:
        prim: The prim to get local transform from.
        time: Time at which to query the value.

    Returns:
        Transform value as a 4x4 matrix.
    """
def getRectLightAttrNames() -> list(str):
    """
    Get a list of both current version and forward/reverse compatible UsdLux.RectLight attribute names

    The new attribute names have "inputs:" prepended to the names to make them connectable,
    this function will return both so that a USD object change notice could filter on light attributes.

    Returns:
        A list that includes both old and new schema attribute names
    """
def getShapingAPIAttrNames() -> list(str):
    """
    Get a list of both current version and forward/reverse compatible UsdLux.ShapingAPI attribute names

    The new attribute names have "inputs:" prepended to the names to make them connectable,
    this function will return both so that a USD object change notice could filter on light attributes.

    Returns:
        A list that includes both old and new schema attribute names
    """
def getSphereLightAttrNames() -> list(str):
    """
    Get a list of both current version and forward/reverse compatible UsdLux.SphereLight attribute names

    The new attribute names have "inputs:" prepended to the names to make them connectable,
    this function will return both so that a USD object change notice could filter on light attributes.

    Returns:
        A list that includes both old and new schema attribute names
    """
def getUser(uri: str) -> str:
    """
    Determine the current username on a given Omniverse server.

    If the URI points to a valid Omniverse server, it will be queried to find the associated username.
    If the server connection cannot be established, an empty string will be returned. This does not indicate
    whether the server exists, just that no connection was made.
    If the URI is a local file the OS username will be returned.

    Returns:
        The current username.
    """
def getValidChildNames(prim: pxr.Usd.Prim, names: typing.List[str]) -> list(str):
    """
    Take a prim and a vector of the preferred names. Return a matching vector of valid and unique names as the child names of the given prim.

    Args:
        prim: The USD prim where the given prim names should live under.
        names: A vector of preferred prim names.

    Returns:
        A vector of valid and unique names.
    """
def getValidPrimName(name: str) -> str:
    """
    Produce a valid prim name from the input name

    Args:
        name: The input name

    Returns:
        A string that is considered valid for use as a prim name.
    """
def getValidPrimNames(names: typing.List[str], reservedNames: list(str) = []) -> list(str):
    """
    Take a vector of the preferred names and return a matching vector of valid and unique names.

    Args:
        names: A vector of preferred prim names.
        reservedNames: A vector of reserved prim names. Names in the vector will not be included in the returns.

    Returns:
        A vector of valid and unique names.
    """
def getValidPropertyName(name: str) -> str:
    """
    Produce a valid property name using the Bootstring algorithm.

    Args:
        name: The input name

    Returns:
        A string that is considered valid for use as a property name.
    """
def getValidPropertyNames(names: typing.List[str], reservedNames: list(str) = []) -> list(str):
    """
    Take a vector of the preferred names and return a matching vector of valid and unique names.

    Args:
        names: A vector of preferred property names.
        reservedNames: A vector of reserved prim names. Names in the vector will not be included in the return.

    Returns:
        A vector of valid and unique names.
    """
def hasLayerAuthoringMetadata(layer: pxr.Sdf.Layer) -> bool:
    """
    Check if the `Sdf.Layer` has metadata indicating the provenance of the data.

    Important: this metadata is strictly informational, it is not advisable to key runtime behavior off of this metadata.

    Args:
        layer: The layer to modify

    Returns:
        A bool indicating if the metadata exists
    """
def initialized() -> bool:
    """
    Determine if initialization was successful.

    Returns:
        A bool indicating if initialization was successful.
    """
def isLight(prim: pxr.Usd.Prim) -> bool:
    """
    Determines if a UsdPrim is a UsdLuxLight[API]

    Args:
        prim: The prim to check for a light API

    Returns:
        True if the prim is a UsdLuxLight[API]
    """
def isLiveSessionVersionCompatible(uri: str) -> bool:
    """
    Check that the session config version is compatible [major.minor]

    If major is the same, return true, else return false.
    This works under the assumption that future minor versions will still work.

    Args:
        uri: The location of the existing session config file

    Returns:
        Whether the session config file version is compatible with this API
    """
def isLocalUri(uri: str) -> bool:
    """
    Determine the URI refers to a local file rather than on an Omniverse server.

    Note: This does not indicate whether the URI actually exists locally.

    Returns:
        A bool indicating if the URI refers to a local file.
    """
def isOmniUri(uri: str) -> bool:
    """
    Determine the URI points to an Omniverse server.

    Note: This does not indicate whether the URI actually exists, just if it is formatted correctly.

    Returns:
        A bool indicating if the URI refers to an Omniverse server.
    """
def isUriWritable(uri: str) -> bool:
    """
    Determine if the user has write access to the file or directory identified by the URI

    Returns:
        A bool indicating if the user can write to the URI.
    """
def linearToSrgb(color: pxr.Gf.Vec3f) -> pxr.Gf.Vec3f:
    """
    Translate a linear color value to sRGB color space

    Many 3D modeling applications define colors in RGB (0-255) or sRGB (0-1) color space
    MDL uses a linear color space that aligns with how light and color behave in the natural world

    Args:
        color: linear representation of a color to be translated to sRGB color space
    Returns:
        The translated color in sRGB color space
    """
def loadSettings() -> bool:
    """
    Initialize the Connect SDK & Connector Settings.

    Client Connectors may add or override core configuration via a toml file
    located at `${CARB_APP_PATH}/config/omni.connect.client.toml`

    Note that `loadSettings` may be called multiple times, to reset settings
    back to the default configuration.

    Returns:
        Whether the required settings were loaded successfully.
    """
def loadSettingsFromFile(arg0: str) -> bool:
    """
    Load additional settings from the provided toml file and perform token resolution.

    Note that subsequent calls the the default `loadSettings()` may reset any common settings loaded by this function.

    Returns:
        Whether the required settings were loaded successfully.
    """
def logChannel() -> str:
    """
    Get the main log channel name for the Connect SDK.

    Note : Client code should not use this channel to emit messages. Create your own channel instead.

    Returns:
        The main log channel name for the Connect SDK.
    """
def registerOmniUsdResolverPlugin() -> bool:
    """
    Register the Omniverse USD Resolver plugin from the configured directory path.

    Note:
        Nucleus is a compile-time optional feature which the Omniverse USD Resolver requires.
        This function is only available if Nucleus was enabled at compile time.

    The setting `/omni.connect.core/usd/resolverPath` will be used to locate
    the resolver plugin. This setting must be configured to point to a local
    filesystem directory containing a `plugInfo.json` file. It can be specified
    relative to `$CARB_APP_PATH` or as an absolute filesystem path.

    If `/omni.connect.core/usd/resolverPath` is not set, the client connector must
    load the Omniverse USD Resolver Plugin another way (eg using the `$PXR_PLUGINPATH_NAME`
    environment variable). This function can then be used to determine if the Omniverse
    USD Resolver Plugin was loaded successfully, but will not attempt to load it.

    Note that all USD plugins in `plugInfo.json` in the directory the will be registered when calling
    this function, not just the Omniverse USD Resolver plugin.

    Note that while this function can be called outside of `startup()`, doing so strictly requires
    that `startup()` be called first.

    Returns:
        A bool indicating if the Omniverse USD Resolver plugin has been registered.
    """
def removeLogConsumer(name: str) -> None:
    """
    Removes a log consumer.

    The callback will no longer be hit when a log is published.

    Args:
        name: The name of the consumer to remove.
    """
def removeOrDeactivatePrim(prim: pxr.Usd.Prim) -> bool:
    """
    Removes the given `Usd.Prim` if it can be removed safely, otherwise deactivates it.

    Multi-layer editing and Omniverse Live editing present challenges when trying to remove prims.
    We cannot always safely delete prims, sometimes they must must be deactivated instead.
    Use `removeOrDeactivatePrim` to attempt a full removal. If this is not possible, the prim will
    be deactivated, using an override on the current `Usd.EditTarget`.

    Note:
        Nucleus is an optional feature which is required when using Omniverse Live editing.
        This function will work without Nucleus, but the logic may be overly complicated for simpler
        single layer or "static" composition use cases.

    Args:
        prim: The prim to be removed.

    Returns:
        A bool indicating if the process was successful.
    """
def renamePrim(prim: pxr.Usd.Prim, name: str) -> bool:
    """
    Rename the given `Usd.Prim` if it can be renamed safely.

    Multi-layer editing and Omniverse Live editing present challenges when trying to rename prims.
    We cannot always safely delete prims, sometimes they must must be deactivated instead.
    Use `renamePrim` to simulate a rename by copying the prim and then attempting a full removal.
    If this is not possible, the original prim will be deactivated, using an override on the
    current `Usd.EditTarget`.

    Note:
        Nucleus is an optional feature which is required when using Omniverse Live editing.
        This function will work without Nucleus, but the logic may be overly complicated for simpler
        single layer or "static" composition use cases.

    Args:
        prim: The prim to be renamed.
        name: The new name.

    Returns:
        A bool indicating if the rename was successful.
    """
def sRgbToLinear(color: pxr.Gf.Vec3f) -> pxr.Gf.Vec3f:
    """
    Translate an sRGB color value to linear color space

    Many 3D modeling applications define colors in RGB (0-255) or sRGB (0-1) color space
    MDL uses a linear color space that aligns with how light and color behave in the natural world

    Args:
        color: sRGB representation of a color to be translated to linear color space
    Returns:
        The translated color in linear color space
    """
def saveExportPreferences() -> bool:
    """
    Save the current Export Preferences to the persistent user config file.

    The serialized values will be restored across application processes when calling `omni::connect::core::loadSettings`.

    Use the "storePreference" setting to indicate which settings should be persistent preferences.

    Example:

        ["omni.connect.core".exportOptions.myBool]
        value = false
        storePreference = true

        ["omni.connect.core".exportOptions.myColor]
        value = [10.0, 2.0, 100.0]
        storePreference = true

        ["omni.connect.core".exportOptions.myFloat]
        value = 9.9
        storePreference = true
    """
def saveImportPreferences() -> bool:
    """
    Save the current Import Preferences to the persistent user config file.

    The serialized values will be restored across application processes when calling `omni::connect::core::loadSettings`.

    Use the "storePreference" setting to indicate which settings should be persistent preferences.

    Example:

        ["omni.connect.core".importOptions.myBool]
        value = false
        storePreference = true

        ["omni.connect.core".importOptions.myColor]
        value = [10.0, 2.0, 100.0]
        storePreference = true

        ["omni.connect.core".importOptions.myFloat]
        value = 9.9
        storePreference = true
    """
def saveLayer(layer: pxr.Sdf.Layer, comment: str = None) -> None:
    """
    Save the given `Sdf.Layer` with an optional comment

    Note this does not impact sublayers or any stages that this layer may be contributing to. This is to
    preserve authoring metadata on referenced layers that came from other applications.

    The comment will be authored in the layer as the SdfLayer comment.

    If the layer is being exported to an Omniverse Nucleus server with checkpoints enabled, then the comment will be added to the checkpoint.

    Args:
        layer: The stage to be saved.
        comment: The comment.
    """
def saveStage(stage: pxr.Usd.Stage, comment: str = None) -> None:
    """
    Save the given `Usd.Stage` with an optional checkpoint comment.

    Save all dirty session layers and sublayers of session layers contributing to this stage.

    All dirty layers will be annotated with authoring metadata, unless previously annotated. This is to preserve
    authoring metadata on referenced layers that came from other applications.

    The comment will be authored in all layers as the SdfLayer comment.

    If the layers are being exported to an Omniverse Nucleus server with checkpoints enabled, then the comment will be added to the checkpoints.

    Args:
        stage: The stage to be saved.
        comment: The checkpoints comment.
    """
def setDisplayName(prim: pxr.Usd.Prim, name: str) -> bool:
    """
    Sets this prim's display name (metadata)

    DisplayName is meant to be a descriptive label, not necessarily an alternate identifier; therefore there is no restriction on which
    characters can appear in it

    Args:
        prim: The prim to set the display name for
        name: The value to set

    Returns:
        True on success, otherwise false
    """
def setExportOptions(arg0: dict) -> None:
    """
    Set the export option settings.
    """
def setExportOptionsFromFileFormatArguments(arg0: typing.Dict[str, str]) -> None:
    """
    Set the export option settings.
    Input arguments is type of dict[str, str] - keys as strings and values as strings.
    Values will be converted to the proper type for existing options before set. New options will be set as string.
    The key "format" is mapping to "usdEncoding".
    """
def setImportOptions(arg0: dict) -> None:
    """
    Set the import option settings.
    """
def setImportOptionsFromFileFormatArguments(arg0: typing.Dict[str, str]) -> None:
    """
    Set the import option settings.
    Input arguments is type of dict[str, str] - keys as strings and values as strings.
    Values will be converted to the proper type for existing options before set. New options will be set as string.
    The key "format" is mapping to "usdEncoding".
    """
def setLayerAuthoringMetadata(layer: pxr.Sdf.Layer) -> None:
    """
    Set metadata on the `Sdf.Layer` indicating the provenance of the data.

    Important: this metadata is strictly informational, it is not advisable to key runtime behavior off of this metadata.

    This will add information to the layer that can be used to track it back to its product of origin.
    The mandatory settings `/app/name`, `/app/version`, `/omni.connect.core/client/name`, and
    `/omni.connect.core/client/version` are used to format the metadata.

    Note `startup()` must be called before calling this function.

    Args:
        layer: The layer to modify
    """
def setLiveSessionConfigValues(uri: str, config: typing.Dict[LiveSessionConfig, str]) -> bool:
    """
    Set configuration values in an existing Live Session configuration file

    This function requires that the session config already exists, otherwise it will fail

    Args:
        uri: The location of the existing session config file
        config: A dictionary of LiveSessionConfig-value pairs

    Returns:
        Whether the session config file was updated successfully
    """
@typing.overload
def setLocalTransform(prim: pxr.Usd.Prim, transform: pxr.Gf.Transform, time: pxr.Usd.TimeCode = nan) -> bool:
    """
    Set the local transform of a prim.

    Args:
        prim: The prim to set local transform on.
        transform: The transform value to set.
        time: Time at which to write the value.

    Returns:
        A bool indicating if the local transform was set.




    Set the local transform of a prim from a 4x4 matrix.

    Args:
        prim: The prim to set local transform on.
        matrix: The matrix value to set.
        time: Time at which to write the value.

    Returns:
        A bool indicating if the local transform was set.




    Set the local transform of a prim from common transform components.

    Args:
        prim: The prim to set local transform on.
        translation: The translation value to set.
        pivot: The pivot position value to set.
        rotation: The rotation value to set in degrees.
        rotationOrder: The rotation order of the rotation value.
        scale: The scale value to set.
        time: Time at which to write the value.

    Returns:
        A bool indicating if the local transform was set.
    """
@typing.overload
def setLocalTransform(prim: pxr.Usd.Prim, matrix: pxr.Gf.Matrix4d, time: pxr.Usd.TimeCode = nan) -> bool:
    pass
@typing.overload
def setLocalTransform(prim: pxr.Usd.Prim, translation: pxr.Gf.Vec3d, pivot: pxr.Gf.Vec3d, rotation: pxr.Gf.Vec3f, rotationOrder: RotationOrder, scale: pxr.Gf.Vec3f, time: pxr.Usd.TimeCode = nan) -> bool:
    pass
def startup() -> bool:
    """
    Perform some one-time initialization.

    This initializes the carb Framework and required carb plugins, sets up default logging, and initializes any optional features
    that have been enabled.

        - If Nucleus features have been enabled and configured, the Omniverse Client Library and Omniverse USD Resolver will be initialized.
        - If Python features have been enabled, and the Python interpreter has been configured, it will be initialized.

    Returns:
        A bool indicating if startup was successful.
    """
def startupLog() -> None:
    """
    Initialize the Omniverse logging system.

    This enables the logging system, sets the log levels for the channels, and forwards
    Omniverse Client Library messages to the default Connect SDK channel.
    """
def version() -> str:
    """
    Verify the expected Omniverse Connect SDK version is being loaded at runtime.

    Returns:
        A human-readable version string for the Omniverse Connect SDK.
    """
def withNucleus() -> bool:
    """
    Verify whether Nucleus support is available via the Omniverse Client Library.

    Returns:
        A bool indicating whether Nucleus support is available.
    """
kAppNameSetting = '/app/name'
kAppNameToken = 'app_name'
kAppVersionSetting = '/app/version'
kAppVersionToken = 'app_version'
kBuildConfigToken = 'config'
kCacheFolderToken = 'cache'
kClientNameSetting = '/omni.connect.core/client/name'
kClientNameToken = 'client_name'
kClientVersionSetting = '/omni.connect.core/client/version'
kClientVersionToken = 'client_version'
kConnectSdkVersionFullToken = 'connect_sdk_version_full'
kConnectSdkVersionToken = 'connect_sdk_version'
kCoreSettings = 'omni.connect.core'
kDataFolderToken = 'data'
kExportOptionsSetting = '/omni.connect.core/exportOptions'
kImportOptionsSetting = '/omni.connect.core/importOptions'
kLiveSessionConfigVersion = '1.0'
kLogConsumerLevelSettingParentPath = '/omni.connect.core/log/consumerLevel/'
kLogFolderToken = 'logs'
kOmniClientLibVersionFullToken = 'omni_client_lib_version_full'
kPluginPathsSetting = '/app/plugins/extraPaths'
kPythonPathsSetting = '/app/python/extraPaths'
kStartTimeToken = 'omni_connect_core_start_time'
kUsdResolverPathSetting = '/omni.connect.core/usd/resolverPath'
kUsdVersionToken = 'usd_version'
