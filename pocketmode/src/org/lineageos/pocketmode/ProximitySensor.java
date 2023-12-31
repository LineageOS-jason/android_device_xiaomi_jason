/*
 * Copyright (c) 2016 The CyanogenMod Project
 *               2017-2018 The LineageOS Project
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package org.lineageos.pocketmode;

import android.content.Context;
import android.hardware.Sensor;
import android.hardware.SensorEvent;
import android.hardware.SensorEventListener;
import android.hardware.SensorManager;
import android.util.Log;

import org.lineageos.internal.util.FileUtils;

public class ProximitySensor implements SensorEventListener {

    private static final boolean DEBUG = false;
    private static final String TAG = "PocketModeProximity";

    private static final String FPC_PROX_NODE = "/sys/devices/soc/soc:fingerprint_fpc/proximity_state";
    private static final String GOODIX_PROX_NODE = "/sys/devices/soc/soc:fingerprint_goodix/proximity_state";

    private SensorManager mSensorManager;
    private Sensor mSensor;
    private Context mContext;

    public ProximitySensor(Context context) {
        mContext = context;
        mSensorManager = mContext.getSystemService(SensorManager.class);
        mSensor = mSensorManager.getDefaultSensor(Sensor.TYPE_PROXIMITY);
    }

    @Override
    public void onSensorChanged(SensorEvent event) {
        boolean isNear = (int) event.values[0] < (int) mSensor.getMaximumRange();
        if (FileUtils.isFileWritable(FPC_PROX_NODE)) {
            FileUtils.writeLine(FPC_PROX_NODE, isNear ? "1" : "0");
        }
        if (FileUtils.isFileWritable(GOODIX_PROX_NODE)) {
            FileUtils.writeLine(GOODIX_PROX_NODE, isNear ? "1" : "0");
        }
    }

    @Override
    public void onAccuracyChanged(Sensor sensor, int accuracy) {
        /* Empty */
    }

    protected void enable() {
        if (DEBUG) Log.d(TAG, "Enabling");
        mSensorManager.registerListener(this, mSensor,
                SensorManager.SENSOR_DELAY_NORMAL);
    }

    protected void disable() {
        if (DEBUG) Log.d(TAG, "Disabling");
        mSensorManager.unregisterListener(this, mSensor);
    }
}
