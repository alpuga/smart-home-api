# Smart Home API

## Usage

All responses will have the form

```json
{
  "data": "Mixed type holding the content of the response",
  "message": "Description of what happened"
}
```

Subsequent response definitions will only detail the expected value of the `data field`

### List All Devices

**Definition**

`GET /devices`

**Response**

- `200 OK` on success

```json
[
  {
    "identifier": "kitchen-lights",
    "name": "Kitchen Lights",
    "device_type": "switch",
    "controller_gateway": "192.168.0.2"
  },
  {
    "identifier": "main-door-lock",
    "name": "Main Door Lock",
    "device_type": "switch",
    "controller_gateway": "192.168.0.3"
  }
]
```

### Registering A New Device

**Definition**

`POST /devices`

**Arguments**

- `"identifier":string` a globally unique identifier for this device
- `"name":string` a friendly name for this device -`"device_type":string` the type of the device as understood by the client
- `"controller_gateway":string` the IP address of the device's controller

If a device already exists it will just be overwritten.

**Response**

- `201 Created` on success

```json
{
  "identifier": "kitchen-lights",
  "name": "Kitchen Lights",
  "device_type": "switch",
  "controller_gateway": "192.168.0.2"
}
```

### Lookup Device Details

`GET /device/<identifier>`

**Response**

- `404 Not Found` if the device does not exist
- `200 OK` on success

```json
{
  "identifier": "kitchen-lights",
  "name": "Kitchen Lights",
  "device_type": "switch",
  "controller_gateway": "192.168.0.2"
}
```

### Delete A Device

**Definition**

`DELETE /devices/<identifier>`

**Response**

- `404 Not Found` if the device does not exist
- `204 No Content` on success
