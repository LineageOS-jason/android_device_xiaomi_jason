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

blob_fixups: blob_fixups_user_type = {
    (
        'vendor/lib/libSonyIMX386PdafLibrary.so',
        'vendor/lib/libarcsoft_dualcam_optical_zoom.so',
        'vendor/lib/libarcsoft_dualcam_optical_zoom_control.so',
        'vendor/lib/libarcsoft_dualcam_refocus.so',
        'vendor/lib/libmmcamera_hdr_gb_lib.so',
    ): blob_fixup()
        .replace_needed('libstdc++.so', 'libstdc++_vendor.so'),
    'vendor/lib/libmmcamera2_stats_modules.so': blob_fixup()
        .remove_needed('libandroid.so')
        .remove_needed('libgui.so'),
    'vendor/lib/libmmcamera_jason_s5k3p8sp_sunny.so': blob_fixup()
        .binary_regex_replace(b'\x1e\x40\x9a\x99\x99\x99\x99\x99\x3b\x40\x10', b'\x1e\x40\x9a\x99\x99\x99\x99\x99\x3b\x40\x01'),
    'vendor/lib/libmmcamera_ppeiscore.so': blob_fixup()
        .remove_needed('libgui.so'),
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
    check_elf=False,
)

if __name__ == '__main__':
    utils = ExtractUtils.device_with_commons(
        module, [('sdm660-common',)]
    )
    utils.run()
