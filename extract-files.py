#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

import extract_utils.tools

extract_utils.tools.DEFAULT_PATCHELF_VERSION = '0_17_2'

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

namespace_imports = [
    'hardware/qcom-caf/common/libqti-perfd-client',
    'hardware/qcom-caf/sdm660',
    'hardware/qcom-caf/wlan',
    'hardware/xiaomi',
    'vendor/qcom/opensource/display',
    'vendor/xiaomi/sdm660-common',
]

blob_fixups: blob_fixups_user_type = {
    (
        'vendor/lib/libSonyIMX386PdafLibrary.so',
        'vendor/lib/libarcsoft_dualcam_optical_zoom.so',
        'vendor/lib/libarcsoft_dualcam_optical_zoom_control.so',
        'vendor/lib/libarcsoft_dualcam_refocus.so',
    ): blob_fixup()
        .replace_needed('libstdc++.so', 'libstdc++_vendor.so'),
    'vendor/lib/libmmcamera2_stats_modules.so': blob_fixup()
        .remove_needed('libandroid.so')
        .remove_needed('libgui.so'),
    'vendor/lib/libmmcamera_faceproc.so': blob_fixup()
        .clear_symbol_version('__aeabi_memcpy')
        .clear_symbol_version('__aeabi_memset')
        .clear_symbol_version('__gnu_Unwind_Find_exidx'),
    'vendor/lib/libmmcamera_hdr_gb_lib.so': blob_fixup()
        .add_needed('liblog.so')
        .replace_needed('libstdc++.so', 'libstdc++_vendor.so'),
    'vendor/lib/libmmcamera_jason_s5k3p8sp_sunny.so': blob_fixup()
        .binary_regex_replace(b'\x1e\x40\x9a\x99\x99\x99\x99\x99\x3b\x40\x10', b'\x1e\x40\x9a\x99\x99\x99\x99\x99\x3b\x40\x01'),
    (
     'vendor/lib/libmmcamera_pdaf.so',
     'vendor/lib/libmmcamera_pdafcamif.so',
     'vendor/lib/libmmcamera_tintless_bg_pca_algo.so',
    ): blob_fixup()
        .add_needed('liblog.so'),
    'vendor/lib/libmmcamera_ppeiscore.so': blob_fixup()
        .remove_needed('libgui.so'),
    'vendor/lib/libmmcamera_tuning.so': blob_fixup()
        .remove_needed('libmm-qcamera.so'),
    'vendor/lib/libmpbase.so': blob_fixup()
        .remove_needed('libandroid.so')
        .replace_needed('libstdc++.so', 'libstdc++_vendor.so'),
    'vendor/lib64/libgf_hal.so': blob_fixup()
        .remove_needed('libpowermanager.so'),
}  # fmt: skip

module = ExtractUtilsModule(
    'jason',
    'xiaomi',
    blob_fixups=blob_fixups,
    namespace_imports=namespace_imports,
)

if __name__ == '__main__':
    utils = ExtractUtils.device_with_commons(
        module, [('sdm660-common',)]
    )
    utils.run()
