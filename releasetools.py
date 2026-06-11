#
# SPDX-FileCopyrightText: 2009 The Android Open Source Project
# SPDX-FileCopyrightText: 2011 The Linux Foundation. All rights reserved.
# SPDX-FileCopyrightText: The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

import re


def FullOTA_Assertions(info):
    AddModemAssertion(info, info.input_zip)


def IncrementalOTA_Assertions(info):
    AddModemAssertion(info, info.target_zip)


def AddModemAssertion(info, input_zip):
    android_info = input_zip.read("OTA/android-info.txt").decode('UTF-8')
    m = re.search(r'require\s+date-modem\s*=\s*(.+)$', android_info)
    if m:
        modem_version, build_version = m.group(1).split('|')
        if modem_version and '*' not in modem_version:
            cmd = ('assert(jason.verify_modem("{}") == "1" || abort("Modem firmware '
                   'from {} or newer stock ROMs is prerequisite to be compatible '
                   'with this build."););'.format(modem_version, build_version))
            info.script.AppendExtra(cmd)
