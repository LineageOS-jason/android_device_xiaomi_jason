#
# SPDX-FileCopyrightText: The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

#
# This file sets variables that control the way modules are built
# thorughout the system. It should not be used to conditionally
# disable makefiles (the proper mechanism to control what gets
# included in a build is to use PRODUCT_PACKAGES in a product
# definition file).
#

# Inherit from sdm660-common
include device/xiaomi/sdm660-common/BoardConfigCommon.mk

DEVICE_PATH := device/xiaomi/jason

# A/B
AB_OTA_UPDATER := false

# Kernel
TARGET_KERNEL_CONFIG += vendor/xiaomi/jason.config

# Camera
BOARD_QTI_CAMERA_32BIT_ONLY := true
$(call project-set-path,qcom-camera,$(DEVICE_PATH)/camera)

# Display
TARGET_ADDITIONAL_GRALLOC_10_USAGE_BITS := 0x00002000U
TARGET_SCREEN_DENSITY := 420

# Mainfest
DEVICE_MANIFEST_FILE += $(DEVICE_PATH)/configs/manifest.xml

# Partitions
BOARD_SYSTEMIMAGE_PARTITION_SIZE := 5368709120
BOARD_VENDORIMAGE_PARTITION_SIZE := 872415232

# Properties
TARGET_SYSTEM_PROP += $(DEVICE_PATH)/system.prop
TARGET_VENDOR_PROP += $(DEVICE_PATH)/vendor.prop

# Recovery
TARGET_RECOVERY_FSTAB := $(DEVICE_PATH)/rootdir/etc/fstab.qcom

# Releasetools
TARGET_RECOVERY_UPDATER_LIBS := librecovery_updater_jason
TARGET_RELEASETOOLS_EXTENSIONS := $(DEVICE_PATH)

# SELinux
PRODUCT_PRIVATE_SEPOLICY_DIRS += $(DEVICE_PATH)/sepolicy/private
PRODUCT_PUBLIC_SEPOLICY_DIRS += $(DEVICE_PATH)/sepolicy/public
BOARD_VENDOR_SEPOLICY_DIRS += $(DEVICE_PATH)/sepolicy/vendor

# Security patch level
VENDOR_SECURITY_PATCH := 2019-03-01

# Inherit the proprietary files
include vendor/xiaomi/jason/BoardConfigVendor.mk
