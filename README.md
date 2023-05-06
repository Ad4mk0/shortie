# plc-communicator

Rewrite of https://gitlab.sanezoo.com/infrastructure/utils-group/acquisition_server
















# T R I G G E R

```
    ___       ___       ___       ___       ___       ___       ___
   /\  \     /\  \     /\  \     /\  \     /\  \     /\  \     /\  \
   \:\  \   /::\  \   _\:\  \   /::\  \   /::\  \   /::\  \   /::\  \
   /::\__\ /::\:\__\ /\/::\__\ /:/\:\__\ /:/\:\__\ /::\:\__\ /::\:\__\
  /:/\/__/ \;:::/  / \::/\/__/ \:\:\/__/ \:\:\/__/ \:\:\/  / \;:::/  /
  \/__/     |:\/__/   \:\__\    \::/  /   \::/  /   \:\/  /   |:\/__/
             \|__|     \/__/     \/__/     \/__/     \/__/     \|__|
```

## Configuration:

Not sure yet.

**This code is part of the Titan principle (lightweight and robust), but deque is stellar**

## API

```
curl -X GET http://localhost:42069
```
implements:
```
curl -X POST -d '{ "views": { "cm01": { "product_code": "AAAA", "serial_number": "69", "metadata": { "view_key": "view01" } }, "cm02": { "product_code": "AAAA", "serial_number": "69", "metadata": { "view_key": "view02" } }, "cm03": { "product_code": "AAAA", "serial_number": "69", "metadata": { "view_key": "view03" } }, "cm04": { "product_code": "AAAA", "serial_number": "69", "metadata": { "view_key": "view04" } }, "cm05": { "product_code": "AAAA", "serial_number": "69", "metadata": { "view_key": "view05" } }, "cm06": { "product_code": "AAAA", "serial_number": "69", "metadata": { "view_key": "view06" } }, "cm08": { "product_code": "AAAA", "serial_number": "69", "metadata": { "view_key": "view08" } }, "cm10": { "product_code": "AAAA", "serial_number": "69", "metadata": { "view_key": "view10" } } } }' localhost:7070/drivers/pd01/trigger
```
