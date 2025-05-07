
Use the Heltec V3 LoRa Board
 - https://heltec.org/project/wifi-lora-32-v3/#Specifications
 - LoRa
 - Built in OLED screen
 - 2.4GHz Wifi
 - Bluetooth Low Energy v5
 - Can't use Wifi & BLE at the same time
 - USB Type C Interface
     - power
     - programming
 - ESP32 Chip
 - Onboard BMS to switch between battery / USB for power
     - handles charge/discharge management
     - JST1.5 Battery Connector
 - Power input
     - USB (C) >= 500mA, 6V
     - Battery >= 250mA, 4.2V

How to split usb from pc for programming and setup vs usb for power
 - Use a power / data switch
 - connect data D-/D+ to pass through
 - connect VCC/GND to Power
 - Won't get power from PC though
