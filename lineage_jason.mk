#
# SPDX-FileCopyrightText: The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

# Inherit from those products. Most specific first.
$(call inherit-product, $(SRC_TARGET_DIR)/product/core_64_bit.mk)
$(call inherit-product, $(SRC_TARGET_DIR)/product/full_base_telephony.mk)
$(call inherit-product, $(SRC_TARGET_DIR)/product/non_ab_device.mk)

# Device was launched with N-MR1
$(call inherit-product, $(SRC_TARGET_DIR)/product/product_launched_with_n_mr1.mk)

# Inherit from jason device
$(call inherit-product, $(LOCAL_PATH)/device.mk)

# Inherit some common Lineage stuff.
$(call inherit-product, vendor/lineage/config/common_full_phone.mk)

PRODUCT_NAME := lineage_jason
PRODUCT_BRAND := Xiaomi
PRODUCT_DEVICE := jason
PRODUCT_MANUFACTURER := Xiaomi
PRODUCT_MODEL := Mi Note 3

PRODUCT_GMS_CLIENTID_BASE := android-xiaomi

PRODUCT_BUILD_PROP_OVERRIDES += \
    BuildDesc="jason-user 9 PKQ1.181007.001 V12.0.1.0.PCHCNXM release-keys" \
    BuildFingerprint=Xiaomi/jason/jason:9/PKQ1.181007.001/V12.0.1.0.PCHCNXM:user/release-keys \
    DeviceName=jason \
    DeviceProduct=jason

TARGET_VENDOR := Xiaomi
