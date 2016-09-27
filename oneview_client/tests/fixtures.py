# -*- encoding: utf-8 -*-
#
# (c) Copyright 2015 Hewlett Packard Enterprise Development LP
# Copyright 2015 Universidade Federal de Campina Grande
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

import json


SERVER_HARDWARE_JSON = {
    "type": "server-hardware-1",
    "name": "Encl2, bay 16",
    "state": "NoProfileApplied",
    "stateReason": "NotApplicable",
    "assetTag": "[Unknown]",
    "category": "server-hardware",
    "created": "2016-01-07T21:31:24.571Z",
    "description": None,
    "eTag": "1455803026048",
    "formFactor": "HalfHeight",
    "licensingIntent": "OneView",
    "locationUri": "/rest/enclosures/09SGH102X6J1",
    "memoryMb": 8192,
    "model": "ProLiant BL460c Gen9",
    "modified": "2016-02-18T13:43:46.048Z",
    "mpDnsName": "172.18.6.30",
    "mpFirmwareVersion": "2.20 Nov 01 2014",
    "mpIpAddress": "172.18.6.30",
    "mpModel": "iLO4",
    "partNumber": "740039-001",
    "portMap": {
        "deviceSlots": [
            {
                "deviceName":
                    "HP FlexFabric 10Gb 2-port 536FLB Adapter",
                "deviceNumber": 9,
                "location": "Flb",
                "physicalPorts": [
                    {
                        "interconnectPort": 16,
                        "interconnectUri": "/rest/interconnects/f78826b8-31a4-"
                                           "495d-a569-52bb9c024645",
                        "mac": "02:23:13:25:22:86",
                        "portNumber": 1,
                        "type": "Ethernet",
                        "virtualPorts": []
                    },
                    {
                        "interconnectPort": 16,
                        "interconnectUri": "/rest/interconnects/d1f57a93-fe5a-"
                                           "43e0-80fa-eaa23ebdae2b",
                        "mac": "02:23:13:25:22:8A",
                        "portNumber": 2,
                        "type": "Ethernet",
                        "virtualPorts": []
                    }
                ],
                "slotNumber": 1
            },
            {
                "deviceName": "",
                "deviceNumber": 1,
                "location": "Mezz",
                "physicalPorts": [],
                "slotNumber": 1
            },
            {
                "deviceName": "",
                "deviceNumber": 2,
                "location": "Mezz",
                "physicalPorts": [],
                "slotNumber": 2
            }
        ]
    },
    "position": 16,
    "powerLock": False,
    "powerState": "Off",
    "processorCoreCount": 4,
    "processorCount": 2,
    "processorSpeedMhz": 2400,
    "processorType": "12-Core Intel(R) Corporation Xeon @ 2.4GHz",
    "refreshState": "NotRefreshing",
    "romVersion": "I36 v1.30 08/26/2014",
    "serialNumber": "SGH111X5RN",
    "serverGroupUri": "/rest/enclosure-groups/c02d2e96-6142-49d6-bd38-0ce9d371"
                      "e94f",
    "serverHardwareTypeUri": "/rest/server-hardware-types/D30D027D-FEB9-46C7-A"
                             "96A-C8B063AD09F2",
    "serverProfileUri": None,
    "shortModel": "BL460c Gen9",
    "signature": {
        "personalityChecksum": 0,
        "serverHwChecksum": 0
    },
    "status": "OK",
    "uri": "/rest/server-hardware/30303437-3933-4753-4831-31315835524E",
    "uuid": "30303437-3933-4753-4831-31315835524E",
    "virtualSerialNumber": "",
    "virtualUuid": None
}

SERVER_HARDWARE_LIST_JSON = {
    "type": "server-hardware-list-1",
    "category": "server-hardware",
    "count": 32,
    "created": "2016-02-26T20:20:15.511Z",
    "eTag": "1456518015511",
    "members": [
        {
            "type": "server-hardware-1",
            "name": "LSD-enl, bay 3",
            "state": "ProfileApplied",
            "stateReason": "NotApplicable",
            "assetTag": "[Unknown]",
            "category": "server-hardware",
            "created": "2015-12-13T11:28:03.234Z",
            "description": None,
            "eTag": "1455801906215",
            "formFactor": "HalfHeight",
            "licensingIntent": "OneView",
            "locationUri": "/rest/enclosures/09BRC3203AFD",
            "memoryMb": 81920,
            "model": "ProLiant BL460c Gen8",
            "modified": "2016-02-18T13:25:06.215Z",
            "mpDnsName": "ILOBRC3062TC3",
            "mpFirmwareVersion": "2.03 Nov 07 2014",
            "mpIpAddress": "10.5.0.203",
            "mpModel": "iLO4",
            "partNumber": "641016-B21",
            "portMap": {
                "deviceSlots": [
                    {
                        "deviceName":
                            "HP FlexFabric 10Gb 2-port 554FLB Adapter",
                        "deviceNumber": 9,
                        "location": "Flb",
                        "physicalPorts": [
                            {
                                "interconnectPort": 3,
                                "interconnectUri": "/rest/interconnects/d6793c"
                                                   "22-ded7-44b7-bdad-5416d853"
                                                   "4c39",
                                "mac": "6C:3B:E5:BA:BB:20",
                                "portNumber": 1,
                                "type": "Ethernet",
                                "virtualPorts": []
                            },
                            {
                                "interconnectPort": 3,
                                "interconnectUri": "/rest/interconnects/52cbe2"
                                                   "87-7de2-4488-8073-6fcf65ea"
                                                   "71e7",
                                "mac": "6C:3B:E5:BA:BB:24",
                                "portNumber": 2,
                                "type": "Ethernet",
                                "virtualPorts": []
                            }
                        ],
                        "slotNumber": 1
                    },
                    {
                        "deviceName": "HP LPe1205A 8Gb FC HBA for BladeSystem "
                                      "c-Class",
                        "deviceNumber": 1,
                        "location": "Mezz",
                        "physicalPorts": [
                            {
                                "interconnectPort": 3,
                                "interconnectUri": "/rest/interconnects/e2f2e1"
                                                   "ed-b92c-4913-add6-52ee17ae"
                                                   "0919",
                                "mac": "10:00:6C:3B:E5:C1:86:8A",
                                "portNumber": 1,
                                "type": "FibreChannel",
                                "virtualPorts": []
                            },
                            {
                                "interconnectPort": 3,
                                "interconnectUri": "/rest/interconnects/ffff79"
                                                   "f4-914c-4ba4-97ef-7e9c0ae2"
                                                   "2921",
                                "mac": "10:00:6C:3B:E5:C1:86:8B",
                                "portNumber": 2,
                                "type": "FibreChannel",
                                "virtualPorts": []
                            }
                        ],
                        "slotNumber": 1
                    },
                    {
                        "deviceName": "",
                        "deviceNumber": 2,
                        "location": "Mezz",
                        "physicalPorts": [],
                        "slotNumber": 2
                    }
                ]
            },
            "position": 3,
            "powerLock": False,
            "powerState": "On",
            "processorCoreCount": 4,
            "processorCount": 2,
            "processorSpeedMhz": 2400,
            "processorType": "Intel(R) Xeon(R) CPU E5-2609 0 @ 2.40GHz",
            "refreshState": "NotRefreshing",
            "romVersion": "I31 08/02/2014",
            "serialNumber": "BRC3062TC3",
            "serverGroupUri": "/rest/enclosure-groups/9869a2ea-55ef-4f1f-90a3-"
                              "8fbf71c0ad12",
            "serverHardwareTypeUri": "/rest/server-hardware-types/CB2ECE5C-C05"
                                     "3-4288-86FE-A65B565BCAA4",
            "serverProfileUri": "/rest/server-profiles/f2160e28-8107-45f9-b4b2"
                                "-3119a622a3a1",
            "shortModel": "BL460c Gen8",
            "signature": {
                "personalityChecksum": 1621528660,
                "serverHwChecksum": 1317121403
            },
            "status": "Warning",
            "uri":
                "/rest/server-hardware/30313436-3631-5242-4333-303632544333",
            "uuid": "30313436-3631-5242-4333-303632544333",
            "virtualSerialNumber": "VCGLPM4001",
            "virtualUuid": "f2160e28-8107-45f9-b4b2-3119a622a3a1"
        },
        {
            "type": "server-hardware-1",
            "name": "LSD-enl, bay 1",
            "state": "ProfileApplied",
            "stateReason": "NotApplicable",
            "assetTag": "\n      ",
            "category": "server-hardware",
            "created": "2015-12-13T11:28:03.456Z",
            "description": None,
            "eTag": "1455801906217",
            "formFactor": "HalfHeight",
            "licensingIntent": "OneView",
            "locationUri": "/rest/enclosures/09BRC3203AFD",
            "memoryMb": 57344,
            "model": "ProLiant BL460c Gen8",
            "modified": "2016-02-18T13:25:06.217Z",
            "mpDnsName": "ILOBRC3203AFK",
            "mpFirmwareVersion": "2.03 Nov 07 2014",
            "mpIpAddress": "10.5.0.201",
            "mpModel": "iLO4",
            "partNumber": "641016-B21",
            "portMap": {
                "deviceSlots": [
                    {
                        "deviceName":
                            "HP FlexFabric 10Gb 2-port 554FLB Adapter",
                        "deviceNumber": 9,
                        "location": "Flb",
                        "physicalPorts": [
                            {
                                "interconnectPort": 1,
                                "interconnectUri": "/rest/interconnects/d6793c"
                                                   "22-ded7-44b7-bdad-5416d853"
                                                   "4c39",
                                "mac": "D8:9D:67:73:54:00",
                                "portNumber": 1,
                                "type": "Ethernet",
                                "virtualPorts": []
                            },
                            {
                                "interconnectPort": 1,
                                "interconnectUri": "/rest/interconnects/52cbe2"
                                                   "87-7de2-4488-8073-6fcf65ea"
                                                   "71e7",
                                "mac": "D8:9D:67:73:54:04",
                                "portNumber": 2,
                                "type": "Ethernet",
                                "virtualPorts": []
                            }
                        ],
                        "slotNumber": 1
                    },
                    {
                        "deviceName": "HP LPe1205A 8Gb FC HBA for BladeSystem "
                                      "c-Class",
                        "deviceNumber": 1,
                        "location": "Mezz",
                        "physicalPorts": [
                            {
                                "interconnectPort": 1,
                                "interconnectUri": "/rest/interconnects/e2f2e1"
                                                   "ed-b92c-4913-add6-52ee17ae"
                                                   "0919",
                                "mac": "10:00:38:EA:A7:D3:E4:40",
                                "portNumber": 1,
                                "type": "FibreChannel",
                                "virtualPorts": []
                            },
                            {
                                "interconnectPort": 1,
                                "interconnectUri": "/rest/interconnects/ffff79"
                                                   "f4-914c-4ba4-97ef-7e9c0ae2"
                                                   "2921",
                                "mac": "10:00:38:EA:A7:D3:E4:41",
                                "portNumber": 2,
                                "type": "FibreChannel",
                                "virtualPorts": []
                            }
                        ],
                        "slotNumber": 1
                    },
                    {
                        "deviceName": "",
                        "deviceNumber": 2,
                        "location": "Mezz",
                        "physicalPorts": [],
                        "slotNumber": 2
                    }
                ]
            },
            "position": 1,
            "powerLock": False,
            "powerState": "On",
            "processorCoreCount": 6,
            "processorCount": 2,
            "processorSpeedMhz": 2000,
            "processorType": "Intel(R) Xeon(R) CPU E5-2630L 0 @ 2.00GHz",
            "refreshState": "NotRefreshing",
            "romVersion": "I31 08/02/2014",
            "serialNumber": "BRC3203AFK",
            "serverGroupUri": "/rest/enclosure-groups/9869a2ea-55ef-4f1f-90a3-"
                              "8fbf71c0ad12",
            "serverHardwareTypeUri": "/rest/server-hardware-types/CB2ECE5C-C05"
                                     "3-4288-86FE-A65B565BCAA4",
            "serverProfileUri": "/rest/server-profiles/cbf35416-6d1b-418a-8cb8"
                                "-6eb449781a4c",
            "shortModel": "BL460c Gen8",
            "signature": {
                "personalityChecksum": 1540468867,
                "serverHwChecksum": 545262956
            },
            "status": "OK",
            "uri":
                "/rest/server-hardware/30313436-3631-5242-4333-32303341464B",
            "uuid": "30313436-3631-5242-4333-32303341464B",
            "virtualSerialNumber": "VCGLPM4000",
            "virtualUuid": "cbf35416-6d1b-418a-8cb8-6eb449781a4c"
        },
        {
            "type": "server-hardware-1",
            "name": "LSD-enl, bay 4",
            "state": "ProfileApplied",
            "stateReason": "NotApplicable",
            "assetTag": "[Unknown]",
            "category": "server-hardware",
            "created": "2015-12-13T11:28:03.721Z",
            "description": None,
            "eTag": "1455801906238",
            "formFactor": "HalfHeight",
            "licensingIntent": "OneView",
            "locationUri": "/rest/enclosures/09BRC3203AFD",
            "memoryMb": 32768,
            "model": "ProLiant BL460c Gen8",
            "modified": "2016-02-18T13:25:06.238Z",
            "mpDnsName": "ILOBRC3203AFN",
            "mpFirmwareVersion": "2.03 Nov 07 2014",
            "mpIpAddress": "10.5.0.204",
            "mpModel": "iLO4",
            "partNumber": "641016-B21",
            "portMap": {
                "deviceSlots": [
                    {
                        "deviceName":
                            "HP FlexFabric 10Gb 2-port 554FLB Adapter",
                        "deviceNumber": 9,
                        "location": "Flb",
                        "physicalPorts": [
                            {
                                "interconnectPort": 4,
                                "interconnectUri": "/rest/interconnects/d6793c"
                                                   "22-ded7-44b7-bdad-5416d853"
                                                   "4c39",
                                "mac": "D8:9D:67:6A:94:F0",
                                "portNumber": 1,
                                "type": "Ethernet",
                                "virtualPorts": []
                            },
                            {
                                "interconnectPort": 4,
                                "interconnectUri": "/rest/interconnects/52cbe2"
                                                   "87-7de2-4488-8073-6fcf65ea"
                                                   "71e7",
                                "mac": "D8:9D:67:6A:94:F4",
                                "portNumber": 2,
                                "type": "Ethernet",
                                "virtualPorts": []
                            }
                        ],
                        "slotNumber": 1
                    },
                    {
                        "deviceName": "HP LPe1205A 8Gb FC HBA for BladeSystem "
                                      "c-Class",
                        "deviceNumber": 1,
                        "location": "Mezz",
                        "physicalPorts": [
                            {
                                "interconnectPort": 4,
                                "interconnectUri": "/rest/interconnects/e2f2e1"
                                                   "ed-b92c-4913-add6-52ee17ae"
                                                   "0919",
                                "mac": "10:00:6C:3B:E5:C1:D5:F6",
                                "portNumber": 1,
                                "type": "FibreChannel",
                                "virtualPorts": []
                            },
                            {
                                "interconnectPort": 4,
                                "interconnectUri": "/rest/interconnects/ffff79"
                                                   "f4-914c-4ba4-97ef-7e9c0ae2"
                                                   "2921",
                                "mac": "10:00:6C:3B:E5:C1:D5:F7",
                                "portNumber": 2,
                                "type": "FibreChannel",
                                "virtualPorts": []
                            }
                        ],
                        "slotNumber": 1
                    },
                    {
                        "deviceName": "",
                        "deviceNumber": 2,
                        "location": "Mezz",
                        "physicalPorts": [],
                        "slotNumber": 2
                    }
                ]
            },
            "position": 4,
            "powerLock": False,
            "powerState": "On",
            "processorCoreCount": 6,
            "processorCount": 2,
            "processorSpeedMhz": 2000,
            "processorType": "Intel(R) Xeon(R) CPU E5-2630L 0 @ 2.00GHz",
            "refreshState": "NotRefreshing",
            "romVersion": "I31 08/02/2014",
            "serialNumber": "BRC3203AFN",
            "serverGroupUri": "/rest/enclosure-groups/9869a2ea-55ef-4f1f-90a3-"
                              "8fbf71c0ad12",
            "serverHardwareTypeUri": "/rest/server-hardware-types/CB2ECE5C-C05"
                                     "3-4288-86FE-A65B565BCAA4",
            "serverProfileUri": "/rest/server-profiles/0cccd18d-df97-4414-a7d3"
                                "-a0183607c612",
            "shortModel": "BL460c Gen8",
            "signature": {
                "personalityChecksum": 1645468957,
                "serverHwChecksum": 1221121145
            },
            "status": "Warning",
            "uri":
                "/rest/server-hardware/30313436-3631-5242-4333-32303341464E",
            "uuid": "30313436-3631-5242-4333-32303341464E",
            "virtualSerialNumber": "VCGLPM4003",
            "virtualUuid": "0cccd18d-df97-4414-a7d3-a0183607c612"
        },
        {
            "type": "server-hardware-1",
            "name": "LSD-enl, bay 5",
            "state": "ProfileApplied",
            "stateReason": "NotApplicable",
            "assetTag": "\n      ",
            "category": "server-hardware",
            "created": "2015-12-13T11:28:04.606Z",
            "description": None,
            "eTag": "1455801906163",
            "formFactor": "HalfHeight",
            "licensingIntent": "OneView",
            "locationUri": "/rest/enclosures/09BRC3203AFD",
            "memoryMb": 57344,
            "model": "ProLiant BL460c Gen8",
            "modified": "2016-02-18T13:25:06.163Z",
            "mpDnsName": "ILOBRC3203AFS",
            "mpFirmwareVersion": "2.03 Nov 07 2014",
            "mpIpAddress": "10.5.0.205",
            "mpModel": "iLO4",
            "partNumber": "641016-B21",
            "portMap": {
                "deviceSlots": [
                    {
                        "deviceName":
                            "HP FlexFabric 10Gb 2-port 554FLB Adapter",
                        "deviceNumber": 9,
                        "location": "Flb",
                        "physicalPorts": [
                            {
                                "interconnectPort": 5,
                                "interconnectUri": "/rest/interconnects/d6793c"
                                                   "22-ded7-44b7-bdad-5416d853"
                                                   "4c39",
                                "mac": "D8:9D:67:6A:25:88",
                                "portNumber": 1,
                                "type": "Ethernet",
                                "virtualPorts": []
                            },
                            {
                                "interconnectPort": 5,
                                "interconnectUri": "/rest/interconnects/52cbe2"
                                                   "87-7de2-4488-8073-6fcf65ea"
                                                   "71e7",
                                "mac": "D8:9D:67:6A:25:8C",
                                "portNumber": 2,
                                "type": "Ethernet",
                                "virtualPorts": []
                            }
                        ],
                        "slotNumber": 1
                    },
                    {
                        "deviceName": "HP LPe1205A 8Gb FC HBA for BladeSystem "
                                      "c-Class",
                        "deviceNumber": 1,
                        "location": "Mezz",
                        "physicalPorts": [
                            {
                                "interconnectPort": 5,
                                "interconnectUri": "/rest/interconnects/e2f2e1"
                                                   "ed-b92c-4913-add6-52ee17ae"
                                                   "0919",
                                "mac": "10:00:6C:3B:E5:C1:B5:82",
                                "portNumber": 1,
                                "type": "FibreChannel",
                                "virtualPorts": []
                            },
                            {
                                "interconnectPort": 5,
                                "interconnectUri": "/rest/interconnects/ffff79"
                                                   "f4-914c-4ba4-97ef-7e9c0ae2"
                                                   "2921",
                                "mac": "10:00:6C:3B:E5:C1:B5:83",
                                "portNumber": 2,
                                "type": "FibreChannel",
                                "virtualPorts": []
                            }
                        ],
                        "slotNumber": 1
                    },
                    {
                        "deviceName": "",
                        "deviceNumber": 2,
                        "location": "Mezz",
                        "physicalPorts": [],
                        "slotNumber": 2
                    }
                ]
            },
            "position": 5,
            "powerLock": False,
            "powerState": "On",
            "processorCoreCount": 6,
            "processorCount": 2,
            "processorSpeedMhz": 2000,
            "processorType": "Intel(R) Xeon(R) CPU E5-2630L 0 @ 2.00GHz",
            "refreshState": "NotRefreshing",
            "romVersion": "I31 08/02/2014",
            "serialNumber": "BRC3203AFS",
            "serverGroupUri": "/rest/enclosure-groups/9869a2ea-55ef-4f1f-90a3-"
                              "8fbf71c0ad12",
            "serverHardwareTypeUri": "/rest/server-hardware-types/CB2ECE5C-C05"
                                     "3-4288-86FE-A65B565BCAA4",
            "serverProfileUri": "/rest/server-profiles/b1f92e8d-d7e9-4f7c-84f4"
                                "-7c732d43a962",
            "shortModel": "BL460c Gen8",
            "signature": {
                "personalityChecksum": 2006829509,
                "serverHwChecksum": 892342425
            },
            "status": "OK",
            "uri":
                "/rest/server-hardware/30313436-3631-5242-4333-323033414653",
            "uuid": "30313436-3631-5242-4333-323033414653",
            "virtualSerialNumber": "",
            "virtualUuid": None
        },
        {
            "type": "server-hardware-1",
            "name": "LSD-enl, bay 2",
            "state": "ProfileApplied",
            "stateReason": "NotApplicable",
            "assetTag": "[Unknown]",
            "category": "server-hardware",
            "created": "2015-12-13T11:28:04.945Z",
            "description": None,
            "eTag": "1455801906258",
            "formFactor": "HalfHeight",
            "licensingIntent": "OneViewNoiLO",
            "locationUri": "/rest/enclosures/09BRC3203AFD",
            "memoryMb": 40960,
            "model": "ProLiant BL460c Gen8",
            "modified": "2016-02-18T13:25:06.258Z",
            "mpDnsName": "ILOBRC3203AFE",
            "mpFirmwareVersion": "2.03 Nov 07 2014",
            "mpIpAddress": "10.5.0.202",
            "mpModel": "iLO4",
            "partNumber": "641016-B21",
            "portMap": {
                "deviceSlots": [
                    {
                        "deviceName":
                            "HP FlexFabric 10Gb 2-port 554FLB Adapter",
                        "deviceNumber": 9,
                        "location": "Flb",
                        "physicalPorts": [
                            {
                                "interconnectPort": 2,
                                "interconnectUri": "/rest/interconnects/d6793c"
                                                   "22-ded7-44b7-bdad-5416d853"
                                                   "4c39",
                                "mac": "D8:9D:67:6A:C4:98",
                                "portNumber": 1,
                                "type": "Ethernet",
                                "virtualPorts": []
                            },
                            {
                                "interconnectPort": 2,
                                "interconnectUri": "/rest/interconnects/52cbe2"
                                                   "87-7de2-4488-8073-6fcf65ea"
                                                   "71e7",
                                "mac": "D8:9D:67:6A:C4:9C",
                                "portNumber": 2,
                                "type": "Ethernet",
                                "virtualPorts": []
                            }
                        ],
                        "slotNumber": 1
                    },
                    {
                        "deviceName": "HP LPe1205A 8Gb FC HBA for BladeSystem"
                                      "c-Class",
                        "deviceNumber": 1,
                        "location": "Mezz",
                        "physicalPorts": [
                            {
                                "interconnectPort": 2,
                                "interconnectUri": "/rest/interconnects/e2f2e1"
                                                   "ed-b92c-4913-add6-52ee17ae"
                                                   "0919",
                                "mac": "10:00:6C:3B:E5:C1:C5:F8",
                                "portNumber": 1,
                                "type": "FibreChannel",
                                "virtualPorts": []
                            },
                            {
                                "interconnectPort": 2,
                                "interconnectUri": "/rest/interconnects/ffff79"
                                                   "f4-914c-4ba4-97ef-7e9c0ae2"
                                                   "2921",
                                "mac": "10:00:6C:3B:E5:C1:C5:F9",
                                "portNumber": 2,
                                "type": "FibreChannel",
                                "virtualPorts": []
                            }
                        ],
                        "slotNumber": 1
                    },
                    {
                        "deviceName": "",
                        "deviceNumber": 2,
                        "location": "Mezz",
                        "physicalPorts": [],
                        "slotNumber": 2
                    }
                ]
            },
            "position": 2,
            "powerLock": False,
            "powerState": "On",
            "processorCoreCount": 6,
            "processorCount": 2,
            "processorSpeedMhz": 2000,
            "processorType": "Intel(R) Xeon(R) CPU E5-2630L 0 @ 2.00GHz",
            "refreshState": "NotRefreshing",
            "romVersion": "I31 08/02/2014",
            "serialNumber": "BRC3203AFE",
            "serverGroupUri": "/rest/enclosure-groups/9869a2ea-55ef-4f1f-90a3-"
                              "8fbf71c0ad12",
            "serverHardwareTypeUri": "/rest/server-hardware-types/CB2ECE5C-C05"
                                     "3-4288-86FE-A65B565BCAA4",
            "serverProfileUri": "/rest/server-profiles/6db42da4-219d-4d02-aef7"
                                "-67bc17726e6b",
            "shortModel": "BL460c Gen8",
            "signature": {
                "personalityChecksum": 1031235135,
                "serverHwChecksum": 2111405204
            },
            "status": "Warning",
            "uri":
                "/rest/server-hardware/30313436-3631-5242-4333-323033414645",
            "uuid": "30313436-3631-5242-4333-323033414645",
            "virtualSerialNumber": "VCGLPM4002",
            "virtualUuid": "6db42da4-219d-4d02-aef7-67bc17726e6b"
        },
        {
            "type": "server-hardware-1",
            "name": "LSD-enl, bay 8",
            "state": "ProfileApplied",
            "stateReason": "NotApplicable",
            "assetTag": "\n      ",
            "category": "server-hardware",
            "created": "2015-12-13T11:28:05.136Z",
            "description": None,
            "eTag": "1456516181679",
            "formFactor": "HalfHeight",
            "licensingIntent": "OneView",
            "locationUri": "/rest/enclosures/09BRC3203AFD",
            "memoryMb": 32768,
            "model": "ProLiant BL460c Gen8",
            "modified": "2016-02-26T19:49:41.679Z",
            "mpDnsName": "ILOBRC3203AFH",
            "mpFirmwareVersion": "2.03 Nov 07 2014",
            "mpIpAddress": "10.5.0.208",
            "mpModel": "iLO4",
            "partNumber": "641016-B21",
            "portMap": {
                "deviceSlots": [
                    {
                        "deviceName":
                            "HP FlexFabric 10Gb 2-port 554FLB Adapter",
                        "deviceNumber": 9,
                        "location": "Flb",
                        "physicalPorts": [
                            {
                                "interconnectPort": 8,
                                "interconnectUri": "/rest/interconnects/d6793c"
                                                   "22-ded7-44b7-bdad-5416d853"
                                                   "4c39",
                                "mac": "D8:9D:67:6A:C5:40",
                                "portNumber": 1,
                                "type": "Ethernet",
                                "virtualPorts": []
                            },
                            {
                                "interconnectPort": 8,
                                "interconnectUri": "/rest/interconnects/52cbe2"
                                                   "87-7de2-4488-8073-6fcf65ea"
                                                   "71e7",
                                "mac": "D8:9D:67:6A:C5:44",
                                "portNumber": 2,
                                "type": "Ethernet",
                                "virtualPorts": []
                            }
                        ],
                        "slotNumber": 1
                    },
                    {
                        "deviceName": "",
                        "deviceNumber": 1,
                        "location": "Mezz",
                        "physicalPorts": [],
                        "slotNumber": 1
                    },
                    {
                        "deviceName": "HP LPe1205A 8Gb FC HBA for BladeSystem "
                                      "c-Class",
                        "deviceNumber": 2,
                        "location": "Mezz",
                        "physicalPorts": [
                            {
                                "interconnectPort": 0,
                                "interconnectUri": None,
                                "mac": "10:00:6C:3B:E5:C1:B6:CE",
                                "portNumber": 1,
                                "type": "FibreChannel",
                                "virtualPorts": []
                            },
                            {
                                "interconnectPort": 0,
                                "interconnectUri": None,
                                "mac": "10:00:6C:3B:E5:C1:B6:CF",
                                "portNumber": 2,
                                "type": "FibreChannel",
                                "virtualPorts": []
                            }
                        ],
                        "slotNumber": 2
                    }
                ]
            },
            "position": 8,
            "powerLock": False,
            "powerState": "On",
            "processorCoreCount": 6,
            "processorCount": 2,
            "processorSpeedMhz": 2000,
            "processorType": "Intel(R) Xeon(R) CPU E5-2630L 0 @ 2.00GHz",
            "refreshState": "NotRefreshing",
            "romVersion": "I31 08/02/2014",
            "serialNumber": "BRC3203AFH",
            "serverGroupUri": "/rest/enclosure-groups/9869a2ea-55ef-4f1f-90a3-"
                              "8fbf71c0ad12",
            "serverHardwareTypeUri": "/rest/server-hardware-types/150A6FA0-CB8"
                                     "3-4899-97A1-AA09F45F0D32",
            "serverProfileUri": "/rest/server-profiles/3c8394d5-ff5f-4893-8603"
                                "-0d7a98939ab1",
            "shortModel": "BL460c Gen8",
            "signature": {
                "personalityChecksum": 1066954895,
                "serverHwChecksum": 546679022
            },
            "status": "OK",
            "uri":
                "/rest/server-hardware/30313436-3631-5242-4333-323033414648",
            "uuid": "30313436-3631-5242-4333-323033414648",
            "virtualSerialNumber": None,
            "virtualUuid": None
        },
        {
            "type": "server-hardware-1",
            "name": "LSD-enl, bay 7",
            "state": "ProfileApplied",
            "stateReason": "NotApplicable",
            "assetTag": "\n      ",
            "category": "server-hardware",
            "created": "2015-12-13T11:28:06.261Z",
            "description": None,
            "eTag": "1455801906243",
            "formFactor": "HalfHeight",
            "licensingIntent": "OneViewNoiLO",
            "locationUri": "/rest/enclosures/09BRC3203AFD",
            "memoryMb": 16384,
            "model": "ProLiant BL460c Gen8",
            "modified": "2016-02-18T13:25:06.243Z",
            "mpDnsName": "ILOBRC3203AFR",
            "mpFirmwareVersion": "2.03 Nov 07 2014",
            "mpIpAddress": "10.5.0.207",
            "mpModel": "iLO4",
            "partNumber": "641016-B21",
            "portMap": {
                "deviceSlots": [
                    {
                        "deviceName":
                            "HP FlexFabric 10Gb 2-port 554FLB Adapter",
                        "deviceNumber": 9,
                        "location": "Flb",
                        "physicalPorts": [
                            {
                                "interconnectPort": 7,
                                "interconnectUri": "/rest/interconnects/d6793c"
                                                   "22-ded7-44b7-bdad-5416d853"
                                                   "4c39",
                                "mac": "D8:9D:67:69:2C:30",
                                "portNumber": 1,
                                "type": "Ethernet",
                                "virtualPorts": []
                            },
                            {
                                "interconnectPort": 7,
                                "interconnectUri": "/rest/interconnects/52cbe2"
                                                   "87-7de2-4488-8073-6fcf65ea"
                                                   "71e7",
                                "mac": "D8:9D:67:69:2C:34",
                                "portNumber": 2,
                                "type": "Ethernet",
                                "virtualPorts": []
                            }
                        ],
                        "slotNumber": 1
                    },
                    {
                        "deviceName": "HP LPe1205A 8Gb FC HBA for BladeSystem "
                                      "c-Class",
                        "deviceNumber": 1,
                        "location": "Mezz",
                        "physicalPorts": [
                            {
                                "interconnectPort": 7,
                                "interconnectUri": "/rest/interconnects/e2f2e1"
                                                   "ed-b92c-4913-add6-52ee17ae"
                                                   "0919",
                                "mac": "10:00:6C:3B:E5:C1:D5:A0",
                                "portNumber": 1,
                                "type": "FibreChannel",
                                "virtualPorts": []
                            },
                            {
                                "interconnectPort": 7,
                                "interconnectUri": "/rest/interconnects/ffff79"
                                                   "f4-914c-4ba4-97ef-7e9c0ae2"
                                                   "2921",
                                "mac": "10:00:6C:3B:E5:C1:D5:A1",
                                "portNumber": 2,
                                "type": "FibreChannel",
                                "virtualPorts": []
                            }
                        ],
                        "slotNumber": 1
                    },
                    {
                        "deviceName": "",
                        "deviceNumber": 2,
                        "location": "Mezz",
                        "physicalPorts": [],
                        "slotNumber": 2
                    }
                ]
            },
            "position": 7,
            "powerLock": False,
            "powerState": "On",
            "processorCoreCount": 6,
            "processorCount": 2,
            "processorSpeedMhz": 2000,
            "processorType": "Intel(R) Xeon(R) CPU E5-2630L 0 @ 2.00GHz",
            "refreshState": "NotRefreshing",
            "romVersion": "I31 08/02/2014",
            "serialNumber": "BRC3203AFR",
            "serverGroupUri": "/rest/enclosure-groups/9869a2ea-55ef-4f1f-90a3-"
                              "8fbf71c0ad12",
            "serverHardwareTypeUri": "/rest/server-hardware-types/CB2ECE5C-C05"
                                     "3-4288-86FE-A65B565BCAA4",
            "serverProfileUri": "/rest/server-profiles/b7e78617-9678-43c5-8085"
                                "-a47e03aa93e0",
            "shortModel": "BL460c Gen8",
            "signature": {
                "personalityChecksum": 566691619,
                "serverHwChecksum": 1898565611
            },
            "status": "OK",
            "uri":
                "/rest/server-hardware/30313436-3631-5242-4333-323033414652",
            "uuid": "30313436-3631-5242-4333-323033414652",
            "virtualSerialNumber": "",
            "virtualUuid": None
        },
        {
            "type": "server-hardware-1",
            "name": "LSD-enl, bay 6",
            "state": "ProfileApplied",
            "stateReason": "NotApplicable",
            "assetTag": "[Unknown]",
            "category": "server-hardware",
            "created": "2015-12-13T11:28:07.615Z",
            "description": None,
            "eTag": "1455801906183",
            "formFactor": "HalfHeight",
            "licensingIntent": "OneView",
            "locationUri": "/rest/enclosures/09BRC3203AFD",
            "memoryMb": 16384,
            "model": "ProLiant BL465c Gen8",
            "modified": "2016-02-18T13:25:06.183Z",
            "mpDnsName": "ILOBRC3092WK1",
            "mpFirmwareVersion": "2.03 Nov 07 2014",
            "mpIpAddress": "10.5.0.206",
            "mpModel": "iLO4",
            "partNumber": "634975-B21",
            "portMap": {
                "deviceSlots": [
                    {
                        "deviceName":
                            "HP FlexFabric 10Gb 2-port 554FLB Adapter",
                        "deviceNumber": 9,
                        "location": "Flb",
                        "physicalPorts": [
                            {
                                "interconnectPort": 6,
                                "interconnectUri": "/rest/interconnects/d6793c"
                                                   "22-ded7-44b7-bdad-5416d853"
                                                   "4c39",
                                "mac": "6C:3B:E5:BB:C0:B0",
                                "portNumber": 1,
                                "type": "Ethernet",
                                "virtualPorts": []
                            },
                            {
                                "interconnectPort": 6,
                                "interconnectUri": "/rest/interconnects/52cbe2"
                                                   "87-7de2-4488-8073-6fcf65ea"
                                                   "71e7",
                                "mac": "6C:3B:E5:BB:C0:B4",
                                "portNumber": 2,
                                "type": "Ethernet",
                                "virtualPorts": []
                            }
                        ],
                        "slotNumber": 1
                    },
                    {
                        "deviceName": "",
                        "deviceNumber": 1,
                        "location": "Mezz",
                        "physicalPorts": [],
                        "slotNumber": 1
                    },
                    {
                        "deviceName": "HP LPe1205A 8Gb FC HBA for BladeSystem "
                                      "c-Class",
                        "deviceNumber": 2,
                        "location": "Mezz",
                        "physicalPorts": [
                            {
                                "interconnectPort": 0,
                                "interconnectUri": None,
                                "mac": "10:00:6C:3B:E5:C1:A5:B2",
                                "portNumber": 1,
                                "type": "FibreChannel",
                                "virtualPorts": []
                            },
                            {
                                "interconnectPort": 0,
                                "interconnectUri": None,
                                "mac": "10:00:6C:3B:E5:C1:A5:B3",
                                "portNumber": 2,
                                "type": "FibreChannel",
                                "virtualPorts": []
                            }
                        ],
                        "slotNumber": 2
                    }
                ]
            },
            "position": 6,
            "powerLock": False,
            "powerState": "On",
            "processorCoreCount": 4,
            "processorCount": 2,
            "processorSpeedMhz": 3300,
            "processorType": "AMD Opteron(tm) Processor 6204",
            "refreshState": "NotRefreshing",
            "romVersion": "A26 09/03/2014",
            "serialNumber": "BRC3092WK1",
            "serverGroupUri": "/rest/enclosure-groups/9869a2ea-55ef-4f1f-90a3-"
                              "8fbf71c0ad12",
            "serverHardwareTypeUri": "/rest/server-hardware-types/8BE70066-9CE"
                                     "9-4007-986E-1B774146E0AA",
            "serverProfileUri": "/rest/server-profiles/48ccb56d-5db4-4454-8b7c"
                                "-19208fcb3785",
            "shortModel": "BL465c Gen8",
            "signature": {
                "personalityChecksum": 2068029009,
                "serverHwChecksum": 459966055
            },
            "status": "OK",
            "uri":
                "/rest/server-hardware/39343336-3537-5242-4333-303932574B31",
            "uuid": "39343336-3537-5242-4333-303932574B31",
            "virtualSerialNumber": "",
            "virtualUuid": None
        },
        {
            "type": "server-hardware-1",
            "name": "Encl1, bay 3",
            "state": "NoProfileApplied",
            "stateReason": "NotApplicable",
            "assetTag": "[Unknown]",
            "category": "server-hardware",
            "created": "2016-01-07T19:56:02.718Z",
            "description": None,
            "eTag": "1455802931889",
            "formFactor": "HalfHeight",
            "licensingIntent": "OneView",
            "locationUri": "/rest/enclosures/09SGH100X6J1",
            "memoryMb": 32768,
            "model": "ProLiant BL460c Gen8",
            "modified": "2016-02-18T13:42:11.889Z",
            "mpDnsName": "172.18.6.3",
            "mpFirmwareVersion": "2.20 Nov 01 2014",
            "mpIpAddress": "172.18.6.3",
            "mpModel": "iLO4",
            "partNumber": "603718-C21",
            "portMap": {
                "deviceSlots": [
                    {
                        "deviceName":
                            "HP FlexFabric 10Gb 2-port 554FLB Adapter",
                        "deviceNumber": 9,
                        "location": "Flb",
                        "physicalPorts": [
                            {
                                "interconnectPort": 3,
                                "interconnectUri": "/rest/interconnects/19501e"
                                                   "ba-53d4-4aa2-9e02-0c1ab031"
                                                   "2ce7",
                                "mac": "02:23:13:25:22:A8",
                                "portNumber": 1,
                                "type": "Ethernet",
                                "virtualPorts": []
                            },
                            {
                                "interconnectPort": 3,
                                "interconnectUri": "/rest/interconnects/242ce6"
                                                   "60-4b8a-46ca-9e77-79bfe960"
                                                   "06e2",
                                "mac": "02:23:13:25:22:AC",
                                "portNumber": 2,
                                "type": "Ethernet",
                                "virtualPorts": []
                            }
                        ],
                        "slotNumber": 1
                    },
                    {
                        "deviceName": "",
                        "deviceNumber": 1,
                        "location": "Mezz",
                        "physicalPorts": [],
                        "slotNumber": 1
                    },
                    {
                        "deviceName": "",
                        "deviceNumber": 2,
                        "location": "Mezz",
                        "physicalPorts": [],
                        "slotNumber": 2
                    }
                ]
            },
            "position": 3,
            "powerLock": False,
            "powerState": "Off",
            "processorCoreCount": 4,
            "processorCount": 2,
            "processorSpeedMhz": 2400,
            "processorType": "Intel(R) Xeon(R) Processor E5620 @ 2.4GHz",
            "refreshState": "NotRefreshing",
            "romVersion": "I31 09/30/2011",
            "serialNumber": "SGH100X8RN",
            "serverGroupUri": "/rest/enclosure-groups/c02d2e96-6142-49d6-bd38-"
                              "0ce9d371e94f",
            "serverHardwareTypeUri": "/rest/server-hardware-types/61720699-7D8"
                                     "9-4E3E-BFC4-32FB9BBE2E71",
            "serverProfileUri": None,
            "shortModel": "BL460c Gen8",
            "signature": {
                "personalityChecksum": 0,
                "serverHwChecksum": 0
            },
            "status": "OK",
            "uri":
                "/rest/server-hardware/37333036-3831-4753-4831-30305838524E",
            "uuid": "37333036-3831-4753-4831-30305838524E",
            "virtualSerialNumber": "",
            "virtualUuid": None
        },
        {
            "type": "server-hardware-1",
            "name": "Encl1, bay 1",
            "state": "NoProfileApplied",
            "stateReason": "NotApplicable",
            "assetTag": "[Unknown]",
            "category": "server-hardware",
            "created": "2016-01-07T19:56:03.256Z",
            "description": None,
            "eTag": "1455802949926",
            "formFactor": "FullHeight",
            "licensingIntent": "OneView",
            "locationUri": "/rest/enclosures/09SGH100X6J1",
            "memoryMb": 16384,
            "model": "ProLiant BL660c Gen9",
            "modified": "2016-02-18T13:42:29.926Z",
            "mpDnsName": "172.18.6.1",
            "mpFirmwareVersion": "2.20 Nov 01 2014",
            "mpIpAddress": "172.18.6.1",
            "mpModel": "iLO4",
            "partNumber": "679118-B21",
            "portMap": {
                "deviceSlots": [
                    {
                        "deviceName":
                            "HP FlexFabric 10Gb 2-port 536FLB Adapter",
                        "deviceNumber": 9,
                        "location": "Flb",
                        "physicalPorts": [
                            {
                                "interconnectPort": 9,
                                "interconnectUri": "/rest/interconnects/19501e"
                                                   "ba-53d4-4aa2-9e02-0c1ab031"
                                                   "2ce7",
                                "mac": "02:23:13:25:23:43",
                                "portNumber": 1,
                                "type": "Ethernet",
                                "virtualPorts": []
                            },
                            {
                                "interconnectPort": 9,
                                "interconnectUri": "/rest/interconnects/242ce6"
                                                   "60-4b8a-46ca-9e77-79bfe960"
                                                   "06e2",
                                "mac": "02:23:13:25:23:47",
                                "portNumber": 2,
                                "type": "Ethernet",
                                "virtualPorts": []
                            }
                        ],
                        "slotNumber": 1
                    },
                    {
                        "deviceName": "",
                        "deviceNumber": 10,
                        "location": "Flb",
                        "physicalPorts": [],
                        "slotNumber": 2
                    },
                    {
                        "deviceName": "",
                        "deviceNumber": 1,
                        "location": "Mezz",
                        "physicalPorts": [],
                        "slotNumber": 1
                    },
                    {
                        "deviceName": "",
                        "deviceNumber": 2,
                        "location": "Mezz",
                        "physicalPorts": [],
                        "slotNumber": 2
                    },
                    {
                        "deviceName": "",
                        "deviceNumber": 3,
                        "location": "Mezz",
                        "physicalPorts": [],
                        "slotNumber": 3
                    }
                ]
            },
            "position": 1,
            "powerLock": False,
            "powerState": "Off",
            "processorCoreCount": 8,
            "processorCount": 4,
            "processorSpeedMhz": 2000,
            "processorType": "Quad-Core Intel Xeon @ 2.0GHz",
            "refreshState": "NotRefreshing",
            "romVersion": "I38 v1.30 08/03/2014",
            "serialNumber": "SGH100X7RN",
            "serverGroupUri": "/rest/enclosure-groups/c02d2e96-6142-49d6-bd38-"
                              "0ce9d371e94f",
            "serverHardwareTypeUri": "/rest/server-hardware-types/934E00C0-45F"
                                     "0-4329-AA8C-A0864E834ED4",
            "serverProfileUri": None,
            "shortModel": "BL660c Gen9",
            "signature": {
                "personalityChecksum": 0,
                "serverHwChecksum": 0
            },
            "status": "OK",
            "uri":
                "/rest/server-hardware/31393736-3831-4753-4831-30305837524E",
            "uuid": "31393736-3831-4753-4831-30305837524E",
            "virtualSerialNumber": "",
            "virtualUuid": None
        },
        {
            "type": "server-hardware-1",
            "name": "Encl1, bay 2",
            "state": "NoProfileApplied",
            "stateReason": "NotApplicable",
            "assetTag": "[Unknown]",
            "category": "server-hardware",
            "created": "2016-01-07T19:56:03.599Z",
            "description": None,
            "eTag": "1455802925147",
            "formFactor": "FullHeight",
            "licensingIntent": "OneView",
            "locationUri": "/rest/enclosures/09SGH100X6J1",
            "memoryMb": 16384,
            "model": "ProLiant BL660c Gen9",
            "modified": "2016-02-18T13:42:05.147Z",
            "mpDnsName": "172.18.6.2",
            "mpFirmwareVersion": "2.20 Nov 01 2014",
            "mpIpAddress": "172.18.6.2",
            "mpModel": "iLO4",
            "partNumber": "679118-B21",
            "portMap": {
                "deviceSlots": [
                    {
                        "deviceName":
                            "HP FlexFabric 10Gb 2-port 536FLB Adapter",
                        "deviceNumber": 9,
                        "location": "Flb",
                        "physicalPorts": [
                            {
                                "interconnectPort": 10,
                                "interconnectUri": "/rest/interconnects/19501e"
                                                   "ba-53d4-4aa2-9e02-0c1ab031"
                                                   "2ce7",
                                "mac": "02:23:13:25:23:4B",
                                "portNumber": 1,
                                "type": "Ethernet",
                                "virtualPorts": []
                            },
                            {
                                "interconnectPort": 10,
                                "interconnectUri": "/rest/interconnects/242ce6"
                                                   "60-4b8a-46ca-9e77-79bfe960"
                                                   "06e2",
                                "mac": "02:23:13:25:23:4F",
                                "portNumber": 2,
                                "type": "Ethernet",
                                "virtualPorts": []
                            }
                        ],
                        "slotNumber": 1
                    },
                    {
                        "deviceName": "",
                        "deviceNumber": 10,
                        "location": "Flb",
                        "physicalPorts": [],
                        "slotNumber": 2
                    },
                    {
                        "deviceName": "",
                        "deviceNumber": 1,
                        "location": "Mezz",
                        "physicalPorts": [],
                        "slotNumber": 1
                    },
                    {
                        "deviceName": "",
                        "deviceNumber": 2,
                        "location": "Mezz",
                        "physicalPorts": [],
                        "slotNumber": 2
                    },
                    {
                        "deviceName": "",
                        "deviceNumber": 3,
                        "location": "Mezz",
                        "physicalPorts": [],
                        "slotNumber": 3
                    }
                ]
            },
            "position": 2,
            "powerLock": False,
            "powerState": "Off",
            "processorCoreCount": 8,
            "processorCount": 4,
            "processorSpeedMhz": 2000,
            "processorType": "Quad-Core Intel Xeon @ 2.0GHz",
            "refreshState": "NotRefreshing",
            "romVersion": "I38 v1.30 08/03/2014",
            "serialNumber": "SGH101X7RN",
            "serverGroupUri": "/rest/enclosure-groups/c02d2e96-6142-49d6-bd38-"
                              "0ce9d371e94f",
            "serverHardwareTypeUri": "/rest/server-hardware-types/934E00C0-45F"
                                     "0-4329-AA8C-A0864E834ED4",
            "serverProfileUri": None,
            "shortModel": "BL660c Gen9",
            "signature": {
                "personalityChecksum": 0,
                "serverHwChecksum": 0
            },
            "status": "OK",
            "uri":
                "/rest/server-hardware/31393736-3831-4753-4831-30315837524E",
            "uuid": "31393736-3831-4753-4831-30315837524E",
            "virtualSerialNumber": "",
            "virtualUuid": None
        },
        {
            "type": "server-hardware-1",
            "name": "Encl1, bay 11",
            "state": "NoProfileApplied",
            "stateReason": "NotApplicable",
            "assetTag": "[Unknown]",
            "category": "server-hardware",
            "created": "2016-01-07T19:56:03.789Z",
            "description": None,
            "eTag": "1455802922842",
            "formFactor": "HalfHeight",
            "licensingIntent": "OneView",
            "locationUri": "/rest/enclosures/09SGH100X6J1",
            "memoryMb": 8192,
            "model": "ProLiant BL460c Gen9",
            "modified": "2016-02-18T13:42:02.842Z",
            "mpDnsName": "172.18.6.9",
            "mpFirmwareVersion": "2.20 Nov 01 2014",
            "mpIpAddress": "172.18.6.9",
            "mpModel": "iLO4",
            "partNumber": "740039-001",
            "portMap": {
                "deviceSlots": [
                    {
                        "deviceName":
                            "HP FlexFabric 10Gb 2-port 536FLB Adapter",
                        "deviceNumber": 9,
                        "location": "Flb",
                        "physicalPorts": [
                            {
                                "interconnectPort": 11,
                                "interconnectUri": "/rest/interconnects/19501e"
                                                   "ba-53d4-4aa2-9e02-0c1ab031"
                                                   "2ce7",
                                "mac": "02:23:13:25:22:2E",
                                "portNumber": 1,
                                "type": "Ethernet",
                                "virtualPorts": []
                            },
                            {
                                "interconnectPort": 11,
                                "interconnectUri": "/rest/interconnects/242ce6"
                                                   "60-4b8a-46ca-9e77-79bfe960"
                                                   "06e2",
                                "mac": "02:23:13:25:22:32",
                                "portNumber": 2,
                                "type": "Ethernet",
                                "virtualPorts": []
                            }
                        ],
                        "slotNumber": 1
                    },
                    {
                        "deviceName": "",
                        "deviceNumber": 1,
                        "location": "Mezz",
                        "physicalPorts": [],
                        "slotNumber": 1
                    },
                    {
                        "deviceName": "",
                        "deviceNumber": 2,
                        "location": "Mezz",
                        "physicalPorts": [],
                        "slotNumber": 2
                    }
                ]
            },
            "position": 11,
            "powerLock": False,
            "powerState": "Off",
            "processorCoreCount": 4,
            "processorCount": 2,
            "processorSpeedMhz": 2400,
            "processorType": "12-Core Intel(R) Corporation Xeon @ 2.4GHz",
            "refreshState": "NotRefreshing",
            "romVersion": "I36 v1.30 08/26/2014",
            "serialNumber": "SGH100X5RN",
            "serverGroupUri": "/rest/enclosure-groups/c02d2e96-6142-49d6-bd38-"
                              "0ce9d371e94f",
            "serverHardwareTypeUri": "/rest/server-hardware-types/D30D027D-FEB"
                                     "9-46C7-A96A-C8B063AD09F2",
            "serverProfileUri": None,
            "shortModel": "BL460c Gen9",
            "signature": {
                "personalityChecksum": 0,
                "serverHwChecksum": 0
            },
            "status": "OK",
            "uri":
                "/rest/server-hardware/30303437-3933-4753-4831-30305835524E",
            "uuid": "30303437-3933-4753-4831-30305835524E",
            "virtualSerialNumber": "",
            "virtualUuid": None
        },
        {
            "type": "server-hardware-1",
            "name": "Encl1, bay 4",
            "state": "NoProfileApplied",
            "stateReason": "NotApplicable",
            "assetTag": "[Unknown]",
            "category": "server-hardware",
            "created": "2016-01-07T19:56:04.029Z",
            "description": None,
            "eTag": "1455802946738",
            "formFactor": "HalfHeight",
            "licensingIntent": "OneView",
            "locationUri": "/rest/enclosures/09SGH100X6J1",
            "memoryMb": 32768,
            "model": "ProLiant BL460c Gen8",
            "modified": "2016-02-18T13:42:26.738Z",
            "mpDnsName": "172.18.6.4",
            "mpFirmwareVersion": "2.20 Nov 01 2014",
            "mpIpAddress": "172.18.6.4",
            "mpModel": "iLO4",
            "partNumber": "603718-C21",
            "portMap": {
                "deviceSlots": [
                    {
                        "deviceName":
                            "HP FlexFabric 10Gb 2-port 554FLB Adapter",
                        "deviceNumber": 9,
                        "location": "Flb",
                        "physicalPorts": [
                            {
                                "interconnectPort": 4,
                                "interconnectUri": "/rest/interconnects/19501e"
                                                   "ba-53d4-4aa2-9e02-0c1ab031"
                                                   "2ce7",
                                "mac": "02:23:13:25:22:B0",
                                "portNumber": 1,
                                "type": "Ethernet",
                                "virtualPorts": []
                            },
                            {
                                "interconnectPort": 4,
                                "interconnectUri": "/rest/interconnects/242ce6"
                                                   "60-4b8a-46ca-9e77-79bfe960"
                                                   "06e2",
                                "mac": "02:23:13:25:22:B4",
                                "portNumber": 2,
                                "type": "Ethernet",
                                "virtualPorts": []
                            }
                        ],
                        "slotNumber": 1
                    },
                    {
                        "deviceName": "",
                        "deviceNumber": 1,
                        "location": "Mezz",
                        "physicalPorts": [],
                        "slotNumber": 1
                    },
                    {
                        "deviceName": "",
                        "deviceNumber": 2,
                        "location": "Mezz",
                        "physicalPorts": [],
                        "slotNumber": 2
                    }
                ]
            },
            "position": 4,
            "powerLock": False,
            "powerState": "Off",
            "processorCoreCount": 4,
            "processorCount": 2,
            "processorSpeedMhz": 2400,
            "processorType": "Intel(R) Xeon(R) Processor E5620 @ 2.4GHz",
            "refreshState": "NotRefreshing",
            "romVersion": "I31 09/30/2011",
            "serialNumber": "SGH101X8RN",
            "serverGroupUri": "/rest/enclosure-groups/c02d2e96-6142-49d6-bd38-"
                              "0ce9d371e94f",
            "serverHardwareTypeUri": "/rest/server-hardware-types/61720699-7D8"
                                     "9-4E3E-BFC4-32FB9BBE2E71",
            "serverProfileUri": None,
            "shortModel": "BL460c Gen8",
            "signature": {
                "personalityChecksum": 0,
                "serverHwChecksum": 0
            },
            "status": "OK",
            "uri":
                "/rest/server-hardware/37333036-3831-4753-4831-30315838524E",
            "uuid": "37333036-3831-4753-4831-30315838524E",
            "virtualSerialNumber": "",
            "virtualUuid": None
        },
        {
            "type": "server-hardware-1",
            "name": "Encl1, bay 5",
            "state": "NoProfileApplied",
            "stateReason": "NotApplicable",
            "assetTag": "[Unknown]",
            "category": "server-hardware",
            "created": "2016-01-07T19:56:04.246Z",
            "description": None,
            "eTag": "1455802931931",
            "formFactor": "HalfHeight",
            "licensingIntent": "OneView",
            "locationUri": "/rest/enclosures/09SGH100X6J1",
            "memoryMb": 32768,
            "model": "ProLiant BL460c Gen8",
            "modified": "2016-02-18T13:42:11.931Z",
            "mpDnsName": "172.18.6.5",
            "mpFirmwareVersion": "2.20 Nov 01 2014",
            "mpIpAddress": "172.18.6.5",
            "mpModel": "iLO4",
            "partNumber": "603718-C21",
            "portMap": {
                "deviceSlots": [
                    {
                        "deviceName":
                            "HP FlexFabric 10Gb 2-port 554FLB Adapter",
                        "deviceNumber": 9,
                        "location": "Flb",
                        "physicalPorts": [
                            {
                                "interconnectPort": 5,
                                "interconnectUri": "/rest/interconnects/19501e"
                                                   "ba-53d4-4aa2-9e02-0c1ab031"
                                                   "2ce7",
                                "mac": "02:23:13:25:22:B8",
                                "portNumber": 1,
                                "type": "Ethernet",
                                "virtualPorts": []
                            },
                            {
                                "interconnectPort": 5,
                                "interconnectUri": "/rest/interconnects/242ce6"
                                                   "60-4b8a-46ca-9e77-79bfe960"
                                                   "06e2",
                                "mac": "02:23:13:25:22:BC",
                                "portNumber": 2,
                                "type": "Ethernet",
                                "virtualPorts": []
                            }
                        ],
                        "slotNumber": 1
                    },
                    {
                        "deviceName": "",
                        "deviceNumber": 1,
                        "location": "Mezz",
                        "physicalPorts": [],
                        "slotNumber": 1
                    },
                    {
                        "deviceName": "",
                        "deviceNumber": 2,
                        "location": "Mezz",
                        "physicalPorts": [],
                        "slotNumber": 2
                    }
                ]
            },
            "position": 5,
            "powerLock": False,
            "powerState": "Off",
            "processorCoreCount": 4,
            "processorCount": 2,
            "processorSpeedMhz": 2400,
            "processorType": "Intel(R) Xeon(R) Processor E5620 @ 2.4GHz",
            "refreshState": "NotRefreshing",
            "romVersion": "I31 09/30/2011",
            "serialNumber": "SGH102X8RN",
            "serverGroupUri": "/rest/enclosure-groups/c02d2e96-6142-49d6-bd38-"
                              "0ce9d371e94f",
            "serverHardwareTypeUri": "/rest/server-hardware-types/61720699-7D8"
                                     "9-4E3E-BFC4-32FB9BBE2E71",
            "serverProfileUri": None,
            "shortModel": "BL460c Gen8",
            "signature": {
                "personalityChecksum": 0,
                "serverHwChecksum": 0
            },
            "status": "OK",
            "uri":
                "/rest/server-hardware/37333036-3831-4753-4831-30325838524E",
            "uuid": "37333036-3831-4753-4831-30325838524E",
            "virtualSerialNumber": "",
            "virtualUuid": None
        },
        {
            "type": "server-hardware-1",
            "name": "Encl1, bay 6",
            "state": "NoProfileApplied",
            "stateReason": "NotApplicable",
            "assetTag": "[Unknown]",
            "category": "server-hardware",
            "created": "2016-01-07T19:56:04.353Z",
            "description": None,
            "eTag": "1455802949160",
            "formFactor": "HalfHeight",
            "licensingIntent": "OneView",
            "locationUri": "/rest/enclosures/09SGH100X6J1",
            "memoryMb": 32768,
            "model": "ProLiant BL460c Gen8",
            "modified": "2016-02-18T13:42:29.160Z",
            "mpDnsName": "172.18.6.6",
            "mpFirmwareVersion": "2.20 Nov 01 2014",
            "mpIpAddress": "172.18.6.6",
            "mpModel": "iLO4",
            "partNumber": "603718-C21",
            "portMap": {
                "deviceSlots": [
                    {
                        "deviceName":
                            "HP FlexFabric 10Gb 2-port 554FLB Adapter",
                        "deviceNumber": 9,
                        "location": "Flb",
                        "physicalPorts": [
                            {
                                "interconnectPort": 6,
                                "interconnectUri": "/rest/interconnects/19501e"
                                                   "ba-53d4-4aa2-9e02-0c1ab031"
                                                   "2ce7",
                                "mac": "02:23:13:25:22:C0",
                                "portNumber": 1,
                                "type": "Ethernet",
                                "virtualPorts": []
                            },
                            {
                                "interconnectPort": 6,
                                "interconnectUri": "/rest/interconnects/242ce6"
                                                   "60-4b8a-46ca-9e77-79bfe960"
                                                   "06e2",
                                "mac": "02:23:13:25:22:C4",
                                "portNumber": 2,
                                "type": "Ethernet",
                                "virtualPorts": []
                            }
                        ],
                        "slotNumber": 1
                    },
                    {
                        "deviceName": "",
                        "deviceNumber": 1,
                        "location": "Mezz",
                        "physicalPorts": [],
                        "slotNumber": 1
                    },
                    {
                        "deviceName": "",
                        "deviceNumber": 2,
                        "location": "Mezz",
                        "physicalPorts": [],
                        "slotNumber": 2
                    }
                ]
            },
            "position": 6,
            "powerLock": False,
            "powerState": "Off",
            "processorCoreCount": 4,
            "processorCount": 2,
            "processorSpeedMhz": 2400,
            "processorType": "Intel(R) Xeon(R) Processor E5620 @ 2.4GHz",
            "refreshState": "NotRefreshing",
            "romVersion": "I31 09/30/2011",
            "serialNumber": "SGH103X8RN",
            "serverGroupUri": "/rest/enclosure-groups/c02d2e96-6142-49d6-bd38-"
                              "0ce9d371e94f",
            "serverHardwareTypeUri": "/rest/server-hardware-types/61720699-7D8"
                                     "9-4E3E-BFC4-32FB9BBE2E71",
            "serverProfileUri": None,
            "shortModel": "BL460c Gen8",
            "signature": {
                "personalityChecksum": 0,
                "serverHwChecksum": 0
            },
            "status": "OK",
            "uri":
                "/rest/server-hardware/37333036-3831-4753-4831-30335838524E",
            "uuid": "37333036-3831-4753-4831-30335838524E",
            "virtualSerialNumber": "",
            "virtualUuid": None
        },
        {
            "type": "server-hardware-1",
            "name": "Encl1, bay 7",
            "state": "NoProfileApplied",
            "stateReason": "NotApplicable",
            "assetTag": "[Unknown]",
            "category": "server-hardware",
            "created": "2016-01-07T19:56:04.459Z",
            "description": None,
            "eTag": "1455802942624",
            "formFactor": "HalfHeight",
            "licensingIntent": "OneView",
            "locationUri": "/rest/enclosures/09SGH100X6J1",
            "memoryMb": 32768,
            "model": "ProLiant BL460c Gen8",
            "modified": "2016-02-18T13:42:22.624Z",
            "mpDnsName": "172.18.6.7",
            "mpFirmwareVersion": "2.20 Nov 01 2014",
            "mpIpAddress": "172.18.6.7",
            "mpModel": "iLO4",
            "partNumber": "603718-C21",
            "portMap": {
                "deviceSlots": [
                    {
                        "deviceName":
                            "HP FlexFabric 10Gb 2-port 554FLB Adapter",
                        "deviceNumber": 9,
                        "location": "Flb",
                        "physicalPorts": [
                            {
                                "interconnectPort": 7,
                                "interconnectUri": "/rest/interconnects/19501e"
                                                   "ba-53d4-4aa2-9e02-0c1ab031"
                                                   "2ce7",
                                "mac": "02:23:13:25:22:C8",
                                "portNumber": 1,
                                "type": "Ethernet",
                                "virtualPorts": []
                            },
                            {
                                "interconnectPort": 7,
                                "interconnectUri": "/rest/interconnects/242ce6"
                                                   "60-4b8a-46ca-9e77-79bfe960"
                                                   "06e2",
                                "mac": "02:23:13:25:22:CC",
                                "portNumber": 2,
                                "type": "Ethernet",
                                "virtualPorts": []
                            }
                        ],
                        "slotNumber": 1
                    },
                    {
                        "deviceName": "",
                        "deviceNumber": 1,
                        "location": "Mezz",
                        "physicalPorts": [],
                        "slotNumber": 1
                    },
                    {
                        "deviceName": "",
                        "deviceNumber": 2,
                        "location": "Mezz",
                        "physicalPorts": [],
                        "slotNumber": 2
                    }
                ]
            },
            "position": 7,
            "powerLock": False,
            "powerState": "Off",
            "processorCoreCount": 4,
            "processorCount": 2,
            "processorSpeedMhz": 2400,
            "processorType": "Intel(R) Xeon(R) Processor E5620 @ 2.4GHz",
            "refreshState": "NotRefreshing",
            "romVersion": "I31 09/30/2011",
            "serialNumber": "SGH104X8RN",
            "serverGroupUri": "/rest/enclosure-groups/c02d2e96-6142-49d6-bd38-"
                              "0ce9d371e94f",
            "serverHardwareTypeUri": "/rest/server-hardware-types/61720699-7D8"
                                     "9-4E3E-BFC4-32FB9BBE2E71",
            "serverProfileUri": None,
            "shortModel": "BL460c Gen8",
            "signature": {
                "personalityChecksum": 0,
                "serverHwChecksum": 0
            },
            "status": "OK",
            "uri":
                "/rest/server-hardware/37333036-3831-4753-4831-30345838524E",
            "uuid": "37333036-3831-4753-4831-30345838524E",
            "virtualSerialNumber": "",
            "virtualUuid": None
        },
        {
            "type": "server-hardware-1",
            "name": "Encl1, bay 8",
            "state": "NoProfileApplied",
            "stateReason": "NotApplicable",
            "assetTag": "[Unknown]",
            "category": "server-hardware",
            "created": "2016-01-07T19:56:04.701Z",
            "description": None,
            "eTag": "1455802949308",
            "formFactor": "HalfHeight",
            "licensingIntent": "OneView",
            "locationUri": "/rest/enclosures/09SGH100X6J1",
            "memoryMb": 32768,
            "model": "ProLiant BL460c Gen8",
            "modified": "2016-02-18T13:42:29.308Z",
            "mpDnsName": "172.18.6.8",
            "mpFirmwareVersion": "2.20 Nov 01 2014",
            "mpIpAddress": "172.18.6.8",
            "mpModel": "iLO4",
            "partNumber": "603718-C21",
            "portMap": {
                "deviceSlots": [
                    {
                        "deviceName":
                            "HP FlexFabric 10Gb 2-port 554FLB Adapter",
                        "deviceNumber": 9,
                        "location": "Flb",
                        "physicalPorts": [
                            {
                                "interconnectPort": 8,
                                "interconnectUri": "/rest/interconnects/19501e"
                                                   "ba-53d4-4aa2-9e02-0c1ab031"
                                                   "2ce7",
                                "mac": "02:23:13:25:22:D0",
                                "portNumber": 1,
                                "type": "Ethernet",
                                "virtualPorts": []
                            },
                            {
                                "interconnectPort": 8,
                                "interconnectUri": "/rest/interconnects/242ce6"
                                                   "60-4b8a-46ca-9e77-79bfe960"
                                                   "06e2",
                                "mac": "02:23:13:25:22:D4",
                                "portNumber": 2,
                                "type": "Ethernet",
                                "virtualPorts": []
                            }
                        ],
                        "slotNumber": 1
                    },
                    {
                        "deviceName": "",
                        "deviceNumber": 1,
                        "location": "Mezz",
                        "physicalPorts": [],
                        "slotNumber": 1
                    },
                    {
                        "deviceName": "",
                        "deviceNumber": 2,
                        "location": "Mezz",
                        "physicalPorts": [],
                        "slotNumber": 2
                    }
                ]
            },
            "position": 8,
            "powerLock": False,
            "powerState": "Off",
            "processorCoreCount": 4,
            "processorCount": 2,
            "processorSpeedMhz": 2400,
            "processorType": "Intel(R) Xeon(R) Processor E5620 @ 2.4GHz",
            "refreshState": "NotRefreshing",
            "romVersion": "I31 09/30/2011",
            "serialNumber": "SGH105X8RN",
            "serverGroupUri": "/rest/enclosure-groups/c02d2e96-6142-49d6-bd38-"
                              "0ce9d371e94f",
            "serverHardwareTypeUri": "/rest/server-hardware-types/61720699-7D8"
                                     "9-4E3E-BFC4-32FB9BBE2E71",
            "serverProfileUri": None,
            "shortModel": "BL460c Gen8",
            "signature": {
                "personalityChecksum": 0,
                "serverHwChecksum": 0
            },
            "status": "OK",
            "uri":
                "/rest/server-hardware/37333036-3831-4753-4831-30355838524E",
            "uuid": "37333036-3831-4753-4831-30355838524E",
            "virtualSerialNumber": "",
            "virtualUuid": None
        },
        {
            "type": "server-hardware-1",
            "name": "Encl1, bay 12",
            "state": "NoProfileApplied",
            "stateReason": "NotApplicable",
            "assetTag": "[Unknown]",
            "category": "server-hardware",
            "created": "2016-01-07T19:56:04.907Z",
            "description": None,
            "eTag": "1455802951452",
            "formFactor": "HalfHeight",
            "licensingIntent": "OneView",
            "locationUri": "/rest/enclosures/09SGH100X6J1",
            "memoryMb": 8192,
            "model": "ProLiant BL460c Gen9",
            "modified": "2016-02-18T13:42:31.452Z",
            "mpDnsName": "172.18.6.10",
            "mpFirmwareVersion": "2.20 Nov 01 2014",
            "mpIpAddress": "172.18.6.10",
            "mpModel": "iLO4",
            "partNumber": "740039-001",
            "portMap": {
                "deviceSlots": [
                    {
                        "deviceName":
                            "HP FlexFabric 10Gb 2-port 536FLB Adapter",
                        "deviceNumber": 9,
                        "location": "Flb",
                        "physicalPorts": [
                            {
                                "interconnectPort": 12,
                                "interconnectUri": "/rest/interconnects/19501e"
                                                   "ba-53d4-4aa2-9e02-0c1ab031"
                                                   "2ce7",
                                "mac": "02:23:13:25:22:36",
                                "portNumber": 1,
                                "type": "Ethernet",
                                "virtualPorts": []
                            },
                            {
                                "interconnectPort": 12,
                                "interconnectUri": "/rest/interconnects/242ce6"
                                                   "60-4b8a-46ca-9e77-79bfe960"
                                                   "06e2",
                                "mac": "02:23:13:25:22:3A",
                                "portNumber": 2,
                                "type": "Ethernet",
                                "virtualPorts": []
                            }
                        ],
                        "slotNumber": 1
                    },
                    {
                        "deviceName": "",
                        "deviceNumber": 1,
                        "location": "Mezz",
                        "physicalPorts": [],
                        "slotNumber": 1
                    },
                    {
                        "deviceName": "",
                        "deviceNumber": 2,
                        "location": "Mezz",
                        "physicalPorts": [],
                        "slotNumber": 2
                    }
                ]
            },
            "position": 12,
            "powerLock": False,
            "powerState": "Off",
            "processorCoreCount": 4,
            "processorCount": 2,
            "processorSpeedMhz": 2400,
            "processorType": "12-Core Intel(R) Corporation Xeon @ 2.4GHz",
            "refreshState": "NotRefreshing",
            "romVersion": "I36 v1.30 08/26/2014",
            "serialNumber": "SGH101X5RN",
            "serverGroupUri": "/rest/enclosure-groups/c02d2e96-6142-49d6-bd38-"
                              "0ce9d371e94f",
            "serverHardwareTypeUri": "/rest/server-hardware-types/D30D027D-FEB"
                                     "9-46C7-A96A-C8B063AD09F2",
            "serverProfileUri": None,
            "shortModel": "BL460c Gen9",
            "signature": {
                "personalityChecksum": 0,
                "serverHwChecksum": 0
            },
            "status": "OK",
            "uri":
                "/rest/server-hardware/30303437-3933-4753-4831-30315835524E",
            "uuid": "30303437-3933-4753-4831-30315835524E",
            "virtualSerialNumber": "",
            "virtualUuid": None
        },
        {
            "type": "server-hardware-1",
            "name": "Encl1, bay 13",
            "state": "NoProfileApplied",
            "stateReason": "NotApplicable",
            "assetTag": "[Unknown]",
            "category": "server-hardware",
            "created": "2016-01-07T19:56:05.242Z",
            "description": None,
            "eTag": "1455802943067",
            "formFactor": "HalfHeight",
            "licensingIntent": "OneView",
            "locationUri": "/rest/enclosures/09SGH100X6J1",
            "memoryMb": 8192,
            "model": "ProLiant BL460c Gen9",
            "modified": "2016-02-18T13:42:23.067Z",
            "mpDnsName": "172.18.6.11",
            "mpFirmwareVersion": "2.20 Nov 01 2014",
            "mpIpAddress": "172.18.6.11",
            "mpModel": "iLO4",
            "partNumber": "740039-001",
            "portMap": {
                "deviceSlots": [
                    {
                        "deviceName":
                            "HP FlexFabric 10Gb 2-port 536FLB Adapter",
                        "deviceNumber": 9,
                        "location": "Flb",
                        "physicalPorts": [
                            {
                                "interconnectPort": 13,
                                "interconnectUri": "/rest/interconnects/19501e"
                                                   "ba-53d4-4aa2-9e02-0c1ab031"
                                                   "2ce7",
                                "mac": "02:23:13:25:22:3E",
                                "portNumber": 1,
                                "type": "Ethernet",
                                "virtualPorts": []
                            },
                            {
                                "interconnectPort": 13,
                                "interconnectUri": "/rest/interconnects/242ce6"
                                                   "60-4b8a-46ca-9e77-79bfe960"
                                                   "06e2",
                                "mac": "02:23:13:25:22:42",
                                "portNumber": 2,
                                "type": "Ethernet",
                                "virtualPorts": []
                            }
                        ],
                        "slotNumber": 1
                    },
                    {
                        "deviceName": "",
                        "deviceNumber": 1,
                        "location": "Mezz",
                        "physicalPorts": [],
                        "slotNumber": 1
                    },
                    {
                        "deviceName": "",
                        "deviceNumber": 2,
                        "location": "Mezz",
                        "physicalPorts": [],
                        "slotNumber": 2
                    }
                ]
            },
            "position": 13,
            "powerLock": False,
            "powerState": "Off",
            "processorCoreCount": 4,
            "processorCount": 2,
            "processorSpeedMhz": 2400,
            "processorType": "12-Core Intel(R) Corporation Xeon @ 2.4GHz",
            "refreshState": "NotRefreshing",
            "romVersion": "I36 v1.30 08/26/2014",
            "serialNumber": "SGH102X5RN",
            "serverGroupUri": "/rest/enclosure-groups/c02d2e96-6142-49d6-bd38-"
                              "0ce9d371e94f",
            "serverHardwareTypeUri": "/rest/server-hardware-types/D30D027D-FEB"
                                     "9-46C7-A96A-C8B063AD09F2",
            "serverProfileUri": None,
            "shortModel": "BL460c Gen9",
            "signature": {
                "personalityChecksum": 0,
                "serverHwChecksum": 0
            },
            "status": "OK",
            "uri":
                "/rest/server-hardware/30303437-3933-4753-4831-30325835524E",
            "uuid": "30303437-3933-4753-4831-30325835524E",
            "virtualSerialNumber": "",
            "virtualUuid": None
        },
        {
            "type": "server-hardware-1",
            "name": "Encl1, bay 14",
            "state": "NoProfileApplied",
            "stateReason": "NotApplicable",
            "assetTag": "[Unknown]",
            "category": "server-hardware",
            "created": "2016-01-07T19:56:05.302Z",
            "description": None,
            "eTag": "1455802942888",
            "formFactor": "HalfHeight",
            "licensingIntent": "OneView",
            "locationUri": "/rest/enclosures/09SGH100X6J1",
            "memoryMb": 8192,
            "model": "ProLiant BL460c Gen9",
            "modified": "2016-02-18T13:42:22.888Z",
            "mpDnsName": "172.18.6.12",
            "mpFirmwareVersion": "2.20 Nov 01 2014",
            "mpIpAddress": "172.18.6.12",
            "mpModel": "iLO4",
            "partNumber": "740039-001",
            "portMap": {
                "deviceSlots": [
                    {
                        "deviceName":
                            "HP FlexFabric 10Gb 2-port 536FLB Adapter",
                        "deviceNumber": 9,
                        "location": "Flb",
                        "physicalPorts": [
                            {
                                "interconnectPort": 14,
                                "interconnectUri": "/rest/interconnects/19501e"
                                                   "ba-53d4-4aa2-9e02-0c1ab031"
                                                   "2ce7",
                                "mac": "02:23:13:25:22:46",
                                "portNumber": 1,
                                "type": "Ethernet",
                                "virtualPorts": []
                            },
                            {
                                "interconnectPort": 14,
                                "interconnectUri": "/rest/interconnects/242ce6"
                                                   "60-4b8a-46ca-9e77-79bfe960"
                                                   "06e2",
                                "mac": "02:23:13:25:22:4A",
                                "portNumber": 2,
                                "type": "Ethernet",
                                "virtualPorts": []
                            }
                        ],
                        "slotNumber": 1
                    },
                    {
                        "deviceName": "",
                        "deviceNumber": 1,
                        "location": "Mezz",
                        "physicalPorts": [],
                        "slotNumber": 1
                    },
                    {
                        "deviceName": "",
                        "deviceNumber": 2,
                        "location": "Mezz",
                        "physicalPorts": [],
                        "slotNumber": 2
                    }
                ]
            },
            "position": 14,
            "powerLock": False,
            "powerState": "Off",
            "processorCoreCount": 4,
            "processorCount": 2,
            "processorSpeedMhz": 2400,
            "processorType": "12-Core Intel(R) Corporation Xeon @ 2.4GHz",
            "refreshState": "NotRefreshing",
            "romVersion": "I36 v1.30 08/26/2014",
            "serialNumber": "SGH103X5RN",
            "serverGroupUri": "/rest/enclosure-groups/c02d2e96-6142-49d6-bd38-"
                              "0ce9d371e94f",
            "serverHardwareTypeUri": "/rest/server-hardware-types/D30D027D-FEB"
                                     "9-46C7-A96A-C8B063AD09F2",
            "serverProfileUri": None,
            "shortModel": "BL460c Gen9",
            "signature": {
                "personalityChecksum": 0,
                "serverHwChecksum": 0
            },
            "status": "OK",
            "uri":
                "/rest/server-hardware/30303437-3933-4753-4831-30335835524E",
            "uuid": "30303437-3933-4753-4831-30335835524E",
            "virtualSerialNumber": "",
            "virtualUuid": None
        },
        {
            "type": "server-hardware-1",
            "name": "Encl1, bay 15",
            "state": "NoProfileApplied",
            "stateReason": "NotApplicable",
            "assetTag": "[Unknown]",
            "category": "server-hardware",
            "created": "2016-01-07T19:56:05.518Z",
            "description": None,
            "eTag": "1455802949317",
            "formFactor": "HalfHeight",
            "licensingIntent": "OneView",
            "locationUri": "/rest/enclosures/09SGH100X6J1",
            "memoryMb": 8192,
            "model": "ProLiant BL460c Gen9",
            "modified": "2016-02-18T13:42:29.317Z",
            "mpDnsName": "172.18.6.13",
            "mpFirmwareVersion": "2.20 Nov 01 2014",
            "mpIpAddress": "172.18.6.13",
            "mpModel": "iLO4",
            "partNumber": "740039-001",
            "portMap": {
                "deviceSlots": [
                    {
                        "deviceName":
                            "HP FlexFabric 10Gb 2-port 536FLB Adapter",
                        "deviceNumber": 9,
                        "location": "Flb",
                        "physicalPorts": [
                            {
                                "interconnectPort": 15,
                                "interconnectUri": "/rest/interconnects/19501e"
                                                   "ba-53d4-4aa2-9e02-0c1ab031"
                                                   "2ce7",
                                "mac": "02:23:13:25:22:4E",
                                "portNumber": 1,
                                "type": "Ethernet",
                                "virtualPorts": []
                            },
                            {
                                "interconnectPort": 15,
                                "interconnectUri": "/rest/interconnects/242ce6"
                                                   "60-4b8a-46ca-9e77-79bfe960"
                                                   "06e2",
                                "mac": "02:23:13:25:22:52",
                                "portNumber": 2,
                                "type": "Ethernet",
                                "virtualPorts": []
                            }
                        ],
                        "slotNumber": 1
                    },
                    {
                        "deviceName": "",
                        "deviceNumber": 1,
                        "location": "Mezz",
                        "physicalPorts": [],
                        "slotNumber": 1
                    },
                    {
                        "deviceName": "",
                        "deviceNumber": 2,
                        "location": "Mezz",
                        "physicalPorts": [],
                        "slotNumber": 2
                    }
                ]
            },
            "position": 15,
            "powerLock": False,
            "powerState": "Off",
            "processorCoreCount": 4,
            "processorCount": 2,
            "processorSpeedMhz": 2400,
            "processorType": "12-Core Intel(R) Corporation Xeon @ 2.4GHz",
            "refreshState": "NotRefreshing",
            "romVersion": "I36 v1.30 08/26/2014",
            "serialNumber": "SGH104X5RN",
            "serverGroupUri": "/rest/enclosure-groups/c02d2e96-6142-49d6-bd38-"
                              "0ce9d371e94f",
            "serverHardwareTypeUri": "/rest/server-hardware-types/D30D027D-FEB"
                                     "9-46C7-A96A-C8B063AD09F2",
            "serverProfileUri": None,
            "shortModel": "BL460c Gen9",
            "signature": {
                "personalityChecksum": 0,
                "serverHwChecksum": 0
            },
            "status": "OK",
            "uri":
                "/rest/server-hardware/30303437-3933-4753-4831-30345835524E",
            "uuid": "30303437-3933-4753-4831-30345835524E",
            "virtualSerialNumber": "",
            "virtualUuid": None
        },
        {
            "type": "server-hardware-1",
            "name": "Encl1, bay 16",
            "state": "NoProfileApplied",
            "stateReason": "NotApplicable",
            "assetTag": "[Unknown]",
            "category": "server-hardware",
            "created": "2016-01-07T19:56:05.590Z",
            "description": None,
            "eTag": "1455802942799",
            "formFactor": "HalfHeight",
            "licensingIntent": "OneView",
            "locationUri": "/rest/enclosures/09SGH100X6J1",
            "memoryMb": 8192,
            "model": "ProLiant BL460c Gen9",
            "modified": "2016-02-18T13:42:22.799Z",
            "mpDnsName": "172.18.6.14",
            "mpFirmwareVersion": "2.20 Nov 01 2014",
            "mpIpAddress": "172.18.6.14",
            "mpModel": "iLO4",
            "partNumber": "740039-001",
            "portMap": {
                "deviceSlots": [
                    {
                        "deviceName":
                            "HP FlexFabric 10Gb 2-port 536FLB Adapter",
                        "deviceNumber": 9,
                        "location": "Flb",
                        "physicalPorts": [
                            {
                                "interconnectPort": 16,
                                "interconnectUri": "/rest/interconnects/19501e"
                                                   "ba-53d4-4aa2-9e02-0c1ab031"
                                                   "2ce7",
                                "mac": "02:23:13:25:22:56",
                                "portNumber": 1,
                                "type": "Ethernet",
                                "virtualPorts": []
                            },
                            {
                                "interconnectPort": 16,
                                "interconnectUri": "/rest/interconnects/242ce6"
                                                   "60-4b8a-46ca-9e77-79bfe960"
                                                   "06e2",
                                "mac": "02:23:13:25:22:5A",
                                "portNumber": 2,
                                "type": "Ethernet",
                                "virtualPorts": []
                            }
                        ],
                        "slotNumber": 1
                    },
                    {
                        "deviceName": "",
                        "deviceNumber": 1,
                        "location": "Mezz",
                        "physicalPorts": [],
                        "slotNumber": 1
                    },
                    {
                        "deviceName": "",
                        "deviceNumber": 2,
                        "location": "Mezz",
                        "physicalPorts": [],
                        "slotNumber": 2
                    }
                ]
            },
            "position": 16,
            "powerLock": False,
            "powerState": "Off",
            "processorCoreCount": 4,
            "processorCount": 2,
            "processorSpeedMhz": 2400,
            "processorType": "12-Core Intel(R) Corporation Xeon @ 2.4GHz",
            "refreshState": "NotRefreshing",
            "romVersion": "I36 v1.30 08/26/2014",
            "serialNumber": "SGH105X5RN",
            "serverGroupUri": "/rest/enclosure-groups/c02d2e96-6142-49d6-bd38-"
                              "0ce9d371e94f",
            "serverHardwareTypeUri": "/rest/server-hardware-types/D30D027D-FEB"
                                     "9-46C7-A96A-C8B063AD09F2",
            "serverProfileUri": None,
            "shortModel": "BL460c Gen9",
            "signature": {
                "personalityChecksum": 0,
                "serverHwChecksum": 0
            },
            "status": "OK",
            "uri":
                "/rest/server-hardware/30303437-3933-4753-4831-30355835524E",
            "uuid": "30303437-3933-4753-4831-30355835524E",
            "virtualSerialNumber": "",
            "virtualUuid": None
        },
        {
            "type": "server-hardware-1",
            "name": "Encl2, bay 3",
            "state": "NoProfileApplied",
            "stateReason": "NotApplicable",
            "assetTag": "[Unknown]",
            "category": "server-hardware",
            "created": "2016-01-07T21:31:22.326Z",
            "description": None,
            "eTag": "1455803002804",
            "formFactor": "HalfHeight",
            "licensingIntent": "OneView",
            "locationUri": "/rest/enclosures/09SGH102X6J1",
            "memoryMb": 32768,
            "model": "ProLiant BL460c Gen8",
            "modified": "2016-02-18T13:43:22.804Z",
            "mpDnsName": "172.18.6.19",
            "mpFirmwareVersion": "2.20 Nov 01 2014",
            "mpIpAddress": "172.18.6.19",
            "mpModel": "iLO4",
            "partNumber": "603718-C21",
            "portMap": {
                "deviceSlots": [
                    {
                        "deviceName":
                            "HP FlexFabric 10Gb 2-port 554FLB Adapter",
                        "deviceNumber": 9,
                        "location": "Flb",
                        "physicalPorts": [
                            {
                                "interconnectPort": 3,
                                "interconnectUri": "/rest/interconnects/f78826"
                                                   "b8-31a4-495d-a569-52bb9c02"
                                                   "4645",
                                "mac": "02:23:13:25:22:D8",
                                "portNumber": 1,
                                "type": "Ethernet",
                                "virtualPorts": []
                            },
                            {
                                "interconnectPort": 3,
                                "interconnectUri": "/rest/interconnects/d1f57a"
                                                   "93-fe5a-43e0-80fa-eaa23ebd"
                                                   "ae2b",
                                "mac": "02:23:13:25:22:DC",
                                "portNumber": 2,
                                "type": "Ethernet",
                                "virtualPorts": []
                            }
                        ],
                        "slotNumber": 1
                    },
                    {
                        "deviceName": "",
                        "deviceNumber": 1,
                        "location": "Mezz",
                        "physicalPorts": [],
                        "slotNumber": 1
                    },
                    {
                        "deviceName": "",
                        "deviceNumber": 2,
                        "location": "Mezz",
                        "physicalPorts": [],
                        "slotNumber": 2
                    }
                ]
            },
            "position": 3,
            "powerLock": False,
            "powerState": "Off",
            "processorCoreCount": 4,
            "processorCount": 2,
            "processorSpeedMhz": 2400,
            "processorType": "Intel(R) Xeon(R) Processor E5620 @ 2.4GHz",
            "refreshState": "NotRefreshing",
            "romVersion": "I31 09/30/2011",
            "serialNumber": "SGH106X8RN",
            "serverGroupUri": "/rest/enclosure-groups/c02d2e96-6142-49d6-bd38-"
                              "0ce9d371e94f",
            "serverHardwareTypeUri": "/rest/server-hardware-types/61720699-7D8"
                                     "9-4E3E-BFC4-32FB9BBE2E71",
            "serverProfileUri": None,
            "shortModel": "BL460c Gen8",
            "signature": {
                "personalityChecksum": 0,
                "serverHwChecksum": 0
            },
            "status": "OK",
            "uri":
                "/rest/server-hardware/37333036-3831-4753-4831-30365838524E",
            "uuid": "37333036-3831-4753-4831-30365838524E",
            "virtualSerialNumber": "",
            "virtualUuid": None
        },
        {
            "type": "server-hardware-1",
            "name": "Encl2, bay 1",
            "state": "NoProfileApplied",
            "stateReason": "NotApplicable",
            "assetTag": "[Unknown]",
            "category": "server-hardware",
            "created": "2016-01-07T21:31:22.757Z",
            "description": None,
            "eTag": "1455803009287",
            "formFactor": "FullHeight",
            "licensingIntent": "OneView",
            "locationUri": "/rest/enclosures/09SGH102X6J1",
            "memoryMb": 16384,
            "model": "ProLiant BL660c Gen9",
            "modified": "2016-02-18T13:43:29.287Z",
            "mpDnsName": "172.18.6.17",
            "mpFirmwareVersion": "2.20 Nov 01 2014",
            "mpIpAddress": "172.18.6.17",
            "mpModel": "iLO4",
            "partNumber": "679118-B21",
            "portMap": {
                "deviceSlots": [
                    {
                        "deviceName":
                            "HP FlexFabric 10Gb 2-port 536FLB Adapter",
                        "deviceNumber": 9,
                        "location": "Flb",
                        "physicalPorts": [
                            {
                                "interconnectPort": 9,
                                "interconnectUri": "/rest/interconnects/f78826"
                                                   "b8-31a4-495d-a569-52bb9c02"
                                                   "4645",
                                "mac": "02:23:13:25:23:53",
                                "portNumber": 1,
                                "type": "Ethernet",
                                "virtualPorts": []
                            },
                            {
                                "interconnectPort": 9,
                                "interconnectUri": "/rest/interconnects/d1f57a"
                                                   "93-fe5a-43e0-80fa-eaa23ebd"
                                                   "ae2b",
                                "mac": "02:23:13:25:23:57",
                                "portNumber": 2,
                                "type": "Ethernet",
                                "virtualPorts": []
                            }
                        ],
                        "slotNumber": 1
                    },
                    {
                        "deviceName": "",
                        "deviceNumber": 10,
                        "location": "Flb",
                        "physicalPorts": [],
                        "slotNumber": 2
                    },
                    {
                        "deviceName": "",
                        "deviceNumber": 1,
                        "location": "Mezz",
                        "physicalPorts": [],
                        "slotNumber": 1
                    },
                    {
                        "deviceName": "",
                        "deviceNumber": 2,
                        "location": "Mezz",
                        "physicalPorts": [],
                        "slotNumber": 2
                    },
                    {
                        "deviceName": "",
                        "deviceNumber": 3,
                        "location": "Mezz",
                        "physicalPorts": [],
                        "slotNumber": 3
                    }
                ]
            },
            "position": 1,
            "powerLock": False,
            "powerState": "Off",
            "processorCoreCount": 8,
            "processorCount": 4,
            "processorSpeedMhz": 2000,
            "processorType": "Quad-Core Intel Xeon @ 2.0GHz",
            "refreshState": "NotRefreshing",
            "romVersion": "I38 v1.30 08/03/2014",
            "serialNumber": "SGH102X7RN",
            "serverGroupUri": "/rest/enclosure-groups/c02d2e96-6142-49d6-bd38-"
                              "0ce9d371e94f",
            "serverHardwareTypeUri": "/rest/server-hardware-types/934E00C0-45F"
                                     "0-4329-AA8C-A0864E834ED4",
            "serverProfileUri": None,
            "shortModel": "BL660c Gen9",
            "signature": {
                "personalityChecksum": 0,
                "serverHwChecksum": 0
            },
            "status": "OK",
            "uri":
                "/rest/server-hardware/31393736-3831-4753-4831-30325837524E",
            "uuid": "31393736-3831-4753-4831-30325837524E",
            "virtualSerialNumber": "",
            "virtualUuid": None
        },
        {
            "type": "server-hardware-1",
            "name": "Encl2, bay 5",
            "state": "NoProfileApplied",
            "stateReason": "NotApplicable",
            "assetTag": "[Unknown]",
            "category": "server-hardware",
            "created": "2016-01-07T21:31:23.082Z",
            "description": None,
            "eTag": "1455803021924",
            "formFactor": "HalfHeight",
            "licensingIntent": "OneView",
            "locationUri": "/rest/enclosures/09SGH102X6J1",
            "memoryMb": 32768,
            "model": "ProLiant BL460c Gen8",
            "modified": "2016-02-18T13:43:41.924Z",
            "mpDnsName": "172.18.6.21",
            "mpFirmwareVersion": "2.20 Nov 01 2014",
            "mpIpAddress": "172.18.6.21",
            "mpModel": "iLO4",
            "partNumber": "603718-C21",
            "portMap": {
                "deviceSlots": [
                    {
                        "deviceName":
                            "HP FlexFabric 10Gb 2-port 554FLB Adapter",
                        "deviceNumber": 9,
                        "location": "Flb",
                        "physicalPorts": [
                            {
                                "interconnectPort": 5,
                                "interconnectUri": "/rest/interconnects/f78826"
                                                   "b8-31a4-495d-a569-52bb9c02"
                                                   "4645",
                                "mac": "02:23:13:25:22:E8",
                                "portNumber": 1,
                                "type": "Ethernet",
                                "virtualPorts": []
                            },
                            {
                                "interconnectPort": 5,
                                "interconnectUri": "/rest/interconnects/d1f57a"
                                                   "93-fe5a-43e0-80fa-eaa23ebd"
                                                   "ae2b",
                                "mac": "02:23:13:25:22:EC",
                                "portNumber": 2,
                                "type": "Ethernet",
                                "virtualPorts": []
                            }
                        ],
                        "slotNumber": 1
                    },
                    {
                        "deviceName": "",
                        "deviceNumber": 1,
                        "location": "Mezz",
                        "physicalPorts": [],
                        "slotNumber": 1
                    },
                    {
                        "deviceName": "",
                        "deviceNumber": 2,
                        "location": "Mezz",
                        "physicalPorts": [],
                        "slotNumber": 2
                    }
                ]
            },
            "position": 5,
            "powerLock": False,
            "powerState": "Off",
            "processorCoreCount": 4,
            "processorCount": 2,
            "processorSpeedMhz": 2400,
            "processorType": "Intel(R) Xeon(R) Processor E5620 @ 2.4GHz",
            "refreshState": "NotRefreshing",
            "romVersion": "I31 09/30/2011",
            "serialNumber": "SGH108X8RN",
            "serverGroupUri": "/rest/enclosure-groups/c02d2e96-6142-49d6-bd38-"
                              "0ce9d371e94f",
            "serverHardwareTypeUri": "/rest/server-hardware-types/61720699-7D8"
                                     "9-4E3E-BFC4-32FB9BBE2E71",
            "serverProfileUri": None,
            "shortModel": "BL460c Gen8",
            "signature": {
                "personalityChecksum": 0,
                "serverHwChecksum": 0
            },
            "status": "OK",
            "uri":
                "/rest/server-hardware/37333036-3831-4753-4831-30385838524E",
            "uuid": "37333036-3831-4753-4831-30385838524E",
            "virtualSerialNumber": "",
            "virtualUuid": None
        },
        {
            "type": "server-hardware-1",
            "name": "Encl2, bay 2",
            "state": "NoProfileApplied",
            "stateReason": "NotApplicable",
            "assetTag": "[Unknown]",
            "category": "server-hardware",
            "created": "2016-01-07T21:31:23.134Z",
            "description": None,
            "eTag": "1455803016561",
            "formFactor": "FullHeight",
            "licensingIntent": "OneView",
            "locationUri": "/rest/enclosures/09SGH102X6J1",
            "memoryMb": 16384,
            "model": "ProLiant BL660c Gen9",
            "modified": "2016-02-18T13:43:36.561Z",
            "mpDnsName": "172.18.6.18",
            "mpFirmwareVersion": "2.20 Nov 01 2014",
            "mpIpAddress": "172.18.6.18",
            "mpModel": "iLO4",
            "partNumber": "679118-B21",
            "portMap": {
                "deviceSlots": [
                    {
                        "deviceName":
                            "HP FlexFabric 10Gb 2-port 536FLB Adapter",
                        "deviceNumber": 9,
                        "location": "Flb",
                        "physicalPorts": [
                            {
                                "interconnectPort": 10,
                                "interconnectUri": "/rest/interconnects/f78826"
                                                   "b8-31a4-495d-a569-52bb9c02"
                                                   "4645",
                                "mac": "02:23:13:25:23:5B",
                                "portNumber": 1,
                                "type": "Ethernet",
                                "virtualPorts": []
                            },
                            {
                                "interconnectPort": 10,
                                "interconnectUri": "/rest/interconnects/d1f57a"
                                                   "93-fe5a-43e0-80fa-eaa23ebd"
                                                   "ae2b",
                                "mac": "02:23:13:25:23:5F",
                                "portNumber": 2,
                                "type": "Ethernet",
                                "virtualPorts": []
                            }
                        ],
                        "slotNumber": 1
                    },
                    {
                        "deviceName": "",
                        "deviceNumber": 10,
                        "location": "Flb",
                        "physicalPorts": [],
                        "slotNumber": 2
                    },
                    {
                        "deviceName": "",
                        "deviceNumber": 1,
                        "location": "Mezz",
                        "physicalPorts": [],
                        "slotNumber": 1
                    },
                    {
                        "deviceName": "",
                        "deviceNumber": 2,
                        "location": "Mezz",
                        "physicalPorts": [],
                        "slotNumber": 2
                    },
                    {
                        "deviceName": "",
                        "deviceNumber": 3,
                        "location": "Mezz",
                        "physicalPorts": [],
                        "slotNumber": 3
                    }
                ]
            },
            "position": 2,
            "powerLock": False,
            "powerState": "Off",
            "processorCoreCount": 8,
            "processorCount": 4,
            "processorSpeedMhz": 2000,
            "processorType": "Quad-Core Intel Xeon @ 2.0GHz",
            "refreshState": "NotRefreshing",
            "romVersion": "I38 v1.30 08/03/2014",
            "serialNumber": "SGH103X7RN",
            "serverGroupUri": "/rest/enclosure-groups/c02d2e96-6142-49d6-bd38-"
                              "0ce9d371e94f",
            "serverHardwareTypeUri": "/rest/server-hardware-types/934E00C0-45F"
                                     "0-4329-AA8C-A0864E834ED4",
            "serverProfileUri": None,
            "shortModel": "BL660c Gen9",
            "signature": {
                "personalityChecksum": 0,
                "serverHwChecksum": 0
            },
            "status": "OK",
            "uri":
                "/rest/server-hardware/31393736-3831-4753-4831-30335837524E",
            "uuid": "31393736-3831-4753-4831-30335837524E",
            "virtualSerialNumber": "",
            "virtualUuid": None
        },
        {
            "type": "server-hardware-1",
            "name": "Encl2, bay 4",
            "state": "NoProfileApplied",
            "stateReason": "NotApplicable",
            "assetTag": "[Unknown]",
            "category": "server-hardware",
            "created": "2016-01-07T21:31:23.393Z",
            "description": None,
            "eTag": "1455803026429",
            "formFactor": "HalfHeight",
            "licensingIntent": "OneView",
            "locationUri": "/rest/enclosures/09SGH102X6J1",
            "memoryMb": 32768,
            "model": "ProLiant BL460c Gen8",
            "modified": "2016-02-18T13:43:46.429Z",
            "mpDnsName": "172.18.6.20",
            "mpFirmwareVersion": "2.20 Nov 01 2014",
            "mpIpAddress": "172.18.6.20",
            "mpModel": "iLO4",
            "partNumber": "603718-C21",
            "portMap": {
                "deviceSlots": [
                    {
                        "deviceName":
                            "HP FlexFabric 10Gb 2-port 554FLB Adapter",
                        "deviceNumber": 9,
                        "location": "Flb",
                        "physicalPorts": [
                            {
                                "interconnectPort": 4,
                                "interconnectUri": "/rest/interconnects/f78826"
                                                   "b8-31a4-495d-a569-52bb9c02"
                                                   "4645",
                                "mac": "02:23:13:25:22:E0",
                                "portNumber": 1,
                                "type": "Ethernet",
                                "virtualPorts": []
                            },
                            {
                                "interconnectPort": 4,
                                "interconnectUri": "/rest/interconnects/d1f57a"
                                                   "93-fe5a-43e0-80fa-eaa23ebd"
                                                   "ae2b",
                                "mac": "02:23:13:25:22:E4",
                                "portNumber": 2,
                                "type": "Ethernet",
                                "virtualPorts": []
                            }
                        ],
                        "slotNumber": 1
                    },
                    {
                        "deviceName": "",
                        "deviceNumber": 1,
                        "location": "Mezz",
                        "physicalPorts": [],
                        "slotNumber": 1
                    },
                    {
                        "deviceName": "",
                        "deviceNumber": 2,
                        "location": "Mezz",
                        "physicalPorts": [],
                        "slotNumber": 2
                    }
                ]
            },
            "position": 4,
            "powerLock": False,
            "powerState": "Off",
            "processorCoreCount": 4,
            "processorCount": 2,
            "processorSpeedMhz": 2400,
            "processorType": "Intel(R) Xeon(R) Processor E5620 @ 2.4GHz",
            "refreshState": "NotRefreshing",
            "romVersion": "I31 09/30/2011",
            "serialNumber": "SGH107X8RN",
            "serverGroupUri": "/rest/enclosure-groups/c02d2e96-6142-49d6-bd38-"
                              "0ce9d371e94f",
            "serverHardwareTypeUri": "/rest/server-hardware-types/61720699-7D8"
                                     "9-4E3E-BFC4-32FB9BBE2E71",
            "serverProfileUri": None,
            "shortModel": "BL460c Gen8",
            "signature": {
                "personalityChecksum": 0,
                "serverHwChecksum": 0
            },
            "status": "OK",
            "uri":
                "/rest/server-hardware/37333036-3831-4753-4831-30375838524E",
            "uuid": "37333036-3831-4753-4831-30375838524E",
            "virtualSerialNumber": "",
            "virtualUuid": None
        },
        {
            "type": "server-hardware-1",
            "name": "Encl2, bay 6",
            "state": "NoProfileApplied",
            "stateReason": "NotApplicable",
            "assetTag": "[Unknown]",
            "category": "server-hardware",
            "created": "2016-01-07T21:31:23.805Z",
            "description": None,
            "eTag": "1455803020658",
            "formFactor": "HalfHeight",
            "licensingIntent": "OneView",
            "locationUri": "/rest/enclosures/09SGH102X6J1",
            "memoryMb": 32768,
            "model": "ProLiant BL460c Gen8",
            "modified": "2016-02-18T13:43:40.658Z",
            "mpDnsName": "172.18.6.22",
            "mpFirmwareVersion": "2.20 Nov 01 2014",
            "mpIpAddress": "172.18.6.22",
            "mpModel": "iLO4",
            "partNumber": "603718-C21",
            "portMap": {
                "deviceSlots": [
                    {
                        "deviceName":
                            "HP FlexFabric 10Gb 2-port 554FLB Adapter",
                        "deviceNumber": 9,
                        "location": "Flb",
                        "physicalPorts": [
                            {
                                "interconnectPort": 6,
                                "interconnectUri": "/rest/interconnects/f78826"
                                                   "b8-31a4-495d-a569-52bb9c02"
                                                   "4645",
                                "mac": "02:23:13:25:22:F0",
                                "portNumber": 1,
                                "type": "Ethernet",
                                "virtualPorts": []
                            },
                            {
                                "interconnectPort": 6,
                                "interconnectUri": "/rest/interconnects/d1f57a"
                                                   "93-fe5a-43e0-80fa-eaa23ebd"
                                                   "ae2b",
                                "mac": "02:23:13:25:22:F4",
                                "portNumber": 2,
                                "type": "Ethernet",
                                "virtualPorts": []
                            }
                        ],
                        "slotNumber": 1
                    },
                    {
                        "deviceName": "",
                        "deviceNumber": 1,
                        "location": "Mezz",
                        "physicalPorts": [],
                        "slotNumber": 1
                    },
                    {
                        "deviceName": "",
                        "deviceNumber": 2,
                        "location": "Mezz",
                        "physicalPorts": [],
                        "slotNumber": 2
                    }
                ]
            },
            "position": 6,
            "powerLock": False,
            "powerState": "Off",
            "processorCoreCount": 4,
            "processorCount": 2,
            "processorSpeedMhz": 2400,
            "processorType": "Intel(R) Xeon(R) Processor E5620 @ 2.4GHz",
            "refreshState": "NotRefreshing",
            "romVersion": "I31 09/30/2011",
            "serialNumber": "SGH109X8RN",
            "serverGroupUri": "/rest/enclosure-groups/c02d2e96-6142-49d6-bd38-"
                              "0ce9d371e94f",
            "serverHardwareTypeUri": "/rest/server-hardware-types/61720699-7D8"
                                     "9-4E3E-BFC4-32FB9BBE2E71",
            "serverProfileUri": None,
            "shortModel": "BL460c Gen8",
            "signature": {
                "personalityChecksum": 0,
                "serverHwChecksum": 0
            },
            "status": "OK",
            "uri":
                "/rest/server-hardware/37333036-3831-4753-4831-30395838524E",
            "uuid": "37333036-3831-4753-4831-30395838524E",
            "virtualSerialNumber": "",
            "virtualUuid": None
        },
        {
            "type": "server-hardware-1",
            "name": "Encl2, bay 8",
            "state": "NoProfileApplied",
            "stateReason": "NotApplicable",
            "assetTag": "[Unknown]",
            "category": "server-hardware",
            "created": "2016-01-07T21:31:24.106Z",
            "description": None,
            "eTag": "1455803021927",
            "formFactor": "HalfHeight",
            "licensingIntent": "OneView",
            "locationUri": "/rest/enclosures/09SGH102X6J1",
            "memoryMb": 32768,
            "model": "ProLiant BL460c Gen8",
            "modified": "2016-02-18T13:43:41.927Z",
            "mpDnsName": "172.18.6.24",
            "mpFirmwareVersion": "2.20 Nov 01 2014",
            "mpIpAddress": "172.18.6.24",
            "mpModel": "iLO4",
            "partNumber": "603718-C21",
            "portMap": {
                "deviceSlots": [
                    {
                        "deviceName":
                            "HP FlexFabric 10Gb 2-port 554FLB Adapter",
                        "deviceNumber": 9,
                        "location": "Flb",
                        "physicalPorts": [
                            {
                                "interconnectPort": 8,
                                "interconnectUri": "/rest/interconnects/f78826"
                                                   "b8-31a4-495d-a569-52bb9c02"
                                                   "4645",
                                "mac": "02:23:13:25:23:00",
                                "portNumber": 1,
                                "type": "Ethernet",
                                "virtualPorts": []
                            },
                            {
                                "interconnectPort": 8,
                                "interconnectUri": "/rest/interconnects/d1f57a"
                                                   "93-fe5a-43e0-80fa-eaa23ebd"
                                                   "ae2b",
                                "mac": "02:23:13:25:23:04",
                                "portNumber": 2,
                                "type": "Ethernet",
                                "virtualPorts": []
                            }
                        ],
                        "slotNumber": 1
                    },
                    {
                        "deviceName": "",
                        "deviceNumber": 1,
                        "location": "Mezz",
                        "physicalPorts": [],
                        "slotNumber": 1
                    },
                    {
                        "deviceName": "",
                        "deviceNumber": 2,
                        "location": "Mezz",
                        "physicalPorts": [],
                        "slotNumber": 2
                    }
                ]
            },
            "position": 8,
            "powerLock": False,
            "powerState": "Off",
            "processorCoreCount": 4,
            "processorCount": 2,
            "processorSpeedMhz": 2400,
            "processorType": "Intel(R) Xeon(R) Processor E5620 @ 2.4GHz",
            "refreshState": "NotRefreshing",
            "romVersion": "I31 09/30/2011",
            "serialNumber": "SGH111X8RN",
            "serverGroupUri": "/rest/enclosure-groups/c02d2e96-6142-49d6-bd38-"
                              "0ce9d371e94f",
            "serverHardwareTypeUri": "/rest/server-hardware-types/61720699-7D8"
                                     "9-4E3E-BFC4-32FB9BBE2E71",
            "serverProfileUri": None,
            "shortModel": "BL460c Gen8",
            "signature": {
                "personalityChecksum": 0,
                "serverHwChecksum": 0
            },
            "status": "OK",
            "uri":
                "/rest/server-hardware/37333036-3831-4753-4831-31315838524E",
            "uuid": "37333036-3831-4753-4831-31315838524E",
            "virtualSerialNumber": "",
            "virtualUuid": None
        },
        {
            "type": "server-hardware-1",
            "name": "Encl2, bay 16",
            "state": "NoProfileApplied",
            "stateReason": "NotApplicable",
            "assetTag": "[Unknown]",
            "category": "server-hardware",
            "created": "2016-01-07T21:31:24.571Z",
            "description": None,
            "eTag": "1455803026048",
            "formFactor": "HalfHeight",
            "licensingIntent": "OneView",
            "locationUri": "/rest/enclosures/09SGH102X6J1",
            "memoryMb": 8192,
            "model": "ProLiant BL460c Gen9",
            "modified": "2016-02-18T13:43:46.048Z",
            "mpDnsName": "172.18.6.30",
            "mpFirmwareVersion": "2.20 Nov 01 2014",
            "mpIpAddress": "172.18.6.30",
            "mpModel": "iLO4",
            "partNumber": "740039-001",
            "portMap": {
                "deviceSlots": [
                    {
                        "deviceName":
                            "HP FlexFabric 10Gb 2-port 536FLB Adapter",
                        "deviceNumber": 9,
                        "location": "Flb",
                        "physicalPorts": [
                            {
                                "interconnectPort": 16,
                                "interconnectUri": "/rest/interconnects/f78826"
                                                   "b8-31a4-495d-a569-52bb9c02"
                                                   "4645",
                                "mac": "02:23:13:25:22:86",
                                "portNumber": 1,
                                "type": "Ethernet",
                                "virtualPorts": []
                            },
                            {
                                "interconnectPort": 16,
                                "interconnectUri": "/rest/interconnects/d1f57a"
                                                   "93-fe5a-43e0-80fa-eaa23ebd"
                                                   "ae2b",
                                "mac": "02:23:13:25:22:8A",
                                "portNumber": 2,
                                "type": "Ethernet",
                                "virtualPorts": []
                            }
                        ],
                        "slotNumber": 1
                    },
                    {
                        "deviceName": "",
                        "deviceNumber": 1,
                        "location": "Mezz",
                        "physicalPorts": [],
                        "slotNumber": 1
                    },
                    {
                        "deviceName": "",
                        "deviceNumber": 2,
                        "location": "Mezz",
                        "physicalPorts": [],
                        "slotNumber": 2
                    }
                ]
            },
            "position": 16,
            "powerLock": False,
            "powerState": "Off",
            "processorCoreCount": 4,
            "processorCount": 2,
            "processorSpeedMhz": 2400,
            "processorType": "12-Core Intel(R) Corporation Xeon @ 2.4GHz",
            "refreshState": "NotRefreshing",
            "romVersion": "I36 v1.30 08/26/2014",
            "serialNumber": "SGH111X5RN",
            "serverGroupUri": "/rest/enclosure-groups/c02d2e96-6142-49d6-bd38-"
                              "0ce9d371e94f",
            "serverHardwareTypeUri": "/rest/server-hardware-types/D30D027D-FEB"
                                     "9-46C7-A96A-C8B063AD09F2",
            "serverProfileUri": None,
            "shortModel": "BL460c Gen9",
            "signature": {
                "personalityChecksum": 0,
                "serverHwChecksum": 0
            },
            "status": "OK",
            "uri":
                "/rest/server-hardware/30303437-3933-4753-4831-31315835524E",
            "uuid": "30303437-3933-4753-4831-31315835524E",
            "virtualSerialNumber": "",
            "virtualUuid": None
        },
        {
            "type": "server-hardware-1",
            "name": "Encl2, bay 7",
            "state": "NoProfileApplied",
            "stateReason": "NotApplicable",
            "assetTag": "[Unknown]",
            "category": "server-hardware",
            "created": "2016-01-07T21:31:24.769Z",
            "description": None,
            "eTag": "1455803020877",
            "formFactor": "HalfHeight",
            "licensingIntent": "OneView",
            "locationUri": "/rest/enclosures/09SGH102X6J1",
            "memoryMb": 32768,
            "model": "ProLiant BL460c Gen8",
            "modified": "2016-02-18T13:43:40.877Z",
            "mpDnsName": "172.18.6.23",
            "mpFirmwareVersion": "2.20 Nov 01 2014",
            "mpIpAddress": "172.18.6.23",
            "mpModel": "iLO4",
            "partNumber": "603718-C21",
            "portMap": {
                "deviceSlots": [
                    {
                        "deviceName":
                            "HP FlexFabric 10Gb 2-port 554FLB Adapter",
                        "deviceNumber": 9,
                        "location": "Flb",
                        "physicalPorts": [
                            {
                                "interconnectPort": 7,
                                "interconnectUri": "/rest/interconnects/f78826"
                                                   "b8-31a4-495d-a569-52bb9c02"
                                                   "4645",
                                "mac": "02:23:13:25:22:F8",
                                "portNumber": 1,
                                "type": "Ethernet",
                                "virtualPorts": []
                            },
                            {
                                "interconnectPort": 7,
                                "interconnectUri": "/rest/interconnects/d1f57a"
                                                   "93-fe5a-43e0-80fa-eaa23ebd"
                                                   "ae2b",
                                "mac": "02:23:13:25:22:FC",
                                "portNumber": 2,
                                "type": "Ethernet",
                                "virtualPorts": []
                            }
                        ],
                        "slotNumber": 1
                    },
                    {
                        "deviceName": "",
                        "deviceNumber": 1,
                        "location": "Mezz",
                        "physicalPorts": [],
                        "slotNumber": 1
                    },
                    {
                        "deviceName": "",
                        "deviceNumber": 2,
                        "location": "Mezz",
                        "physicalPorts": [],
                        "slotNumber": 2
                    }
                ]
            },
            "position": 7,
            "powerLock": False,
            "powerState": "Off",
            "processorCoreCount": 4,
            "processorCount": 2,
            "processorSpeedMhz": 2400,
            "processorType": "Intel(R) Xeon(R) Processor E5620 @ 2.4GHz",
            "refreshState": "NotRefreshing",
            "romVersion": "I31 09/30/2011",
            "serialNumber": "SGH110X8RN",
            "serverGroupUri": "/rest/enclosure-groups/c02d2e96-6142-49d6-bd38-"
                              "0ce9d371e94f",
            "serverHardwareTypeUri": "/rest/server-hardware-types/61720699-7D8"
                                     "9-4E3E-BFC4-32FB9BBE2E71",
            "serverProfileUri": None,
            "shortModel": "BL460c Gen8",
            "signature": {
                "personalityChecksum": 0,
                "serverHwChecksum": 0
            },
            "status": "OK",
            "uri":
                "/rest/server-hardware/37333036-3831-4753-4831-31305838524E",
            "uuid": "37333036-3831-4753-4831-31305838524E",
            "virtualSerialNumber": "",
            "virtualUuid": None
        },
        {
            "type": "server-hardware-1",
            "name": "Encl2, bay 11",
            "state": "NoProfileApplied",
            "stateReason": "NotApplicable",
            "assetTag": "[Unknown]",
            "category": "server-hardware",
            "created": "2016-01-07T21:31:25.008Z",
            "description": None,
            "eTag": "1455803022503",
            "formFactor": "HalfHeight",
            "licensingIntent": "OneView",
            "locationUri": "/rest/enclosures/09SGH102X6J1",
            "memoryMb": 8192,
            "model": "ProLiant BL460c Gen9",
            "modified": "2016-02-18T13:43:42.503Z",
            "mpDnsName": "172.18.6.25",
            "mpFirmwareVersion": "2.20 Nov 01 2014",
            "mpIpAddress": "172.18.6.25",
            "mpModel": "iLO4",
            "partNumber": "740039-001",
            "portMap": {
                "deviceSlots": [
                    {
                        "deviceName":
                            "HP FlexFabric 10Gb 2-port 536FLB Adapter",
                        "deviceNumber": 9,
                        "location": "Flb",
                        "physicalPorts": [
                            {
                                "interconnectPort": 11,
                                "interconnectUri": "/rest/interconnects/f78826"
                                                   "b8-31a4-495d-a569-52bb9c02"
                                                   "4645",
                                "mac": "02:23:13:25:22:5E",
                                "portNumber": 1,
                                "type": "Ethernet",
                                "virtualPorts": []
                            },
                            {
                                "interconnectPort": 11,
                                "interconnectUri": "/rest/interconnects/d1f57a"
                                                   "93-fe5a-43e0-80fa-eaa23ebd"
                                                   "ae2b",
                                "mac": "02:23:13:25:22:62",
                                "portNumber": 2,
                                "type": "Ethernet",
                                "virtualPorts": []
                            }
                        ],
                        "slotNumber": 1
                    },
                    {
                        "deviceName": "",
                        "deviceNumber": 1,
                        "location": "Mezz",
                        "physicalPorts": [],
                        "slotNumber": 1
                    },
                    {
                        "deviceName": "",
                        "deviceNumber": 2,
                        "location": "Mezz",
                        "physicalPorts": [],
                        "slotNumber": 2
                    }
                ]
            },
            "position": 11,
            "powerLock": False,
            "powerState": "Off",
            "processorCoreCount": 4,
            "processorCount": 2,
            "processorSpeedMhz": 2400,
            "processorType": "12-Core Intel(R) Corporation Xeon @ 2.4GHz",
            "refreshState": "NotRefreshing",
            "romVersion": "I36 v1.30 08/26/2014",
            "serialNumber": "SGH106X5RN",
            "serverGroupUri": "/rest/enclosure-groups/c02d2e96-6142-49d6-bd38-"
                              "0ce9d371e94f",
            "serverHardwareTypeUri": "/rest/server-hardware-types/D30D027D-FEB"
                                     "9-46C7-A96A-C8B063AD09F2",
            "serverProfileUri": None,
            "shortModel": "BL460c Gen9",
            "signature": {
                "personalityChecksum": 0,
                "serverHwChecksum": 0
            },
            "status": "OK",
            "uri":
                "/rest/server-hardware/30303437-3933-4753-4831-30365835524E",
            "uuid": "30303437-3933-4753-4831-30365835524E",
            "virtualSerialNumber": "",
            "virtualUuid": None
        }
    ],
    "modified": "2016-02-26T20:20:15.511Z",
    "nextPageUri": "/rest/server-hardware?start=32&count=32",
    "prevPageUri": None,
    "start": 0,
    "total": 38,
    "uri": "/rest/server-hardware?start=0&count=32"
}

SERVER_PROFILE_TEMPLATE_JSON = {
    "type": "ServerProfileTemplateV1",
    "uri":
        "/rest/server-profile-templates/1597face-5ef4-40a5-b677-24e1b63697f6",
    "name": "encl1-blade1-spt-test",
    "description": "",
    "serverProfileDescription": "",
    "serverHardwareTypeUri": "/rest/server-hardware-types/934E00C0-45F0-4329-A"
                             "A8C-A0864E834ED4",
    "enclosureGroupUri": "/rest/enclosure-groups/c02d2e96-6142-49d6-bd38-0ce9d"
                         "371e94f",
    "affinity": "Bay",
    "hideUnusedFlexNics": True,
    "macType": "Virtual",
    "wwnType": "Virtual",
    "serialNumberType": "Virtual",
    "firmware": {
        "manageFirmware": False,
        "firmwareInstallType": None,
        "forceInstallFirmware": False,
        "firmwareBaselineUri": None
    },
    "connections": [
        {
            "id": 1,
            "name": "encl1-blade1",
            "functionType": "Ethernet",
            "networkUri": "/rest/ethernet-networks/b4a0663d-9160-4566-96b3-1b0"
                          "0745c8115",
            "portId": "Flb 1:1-a",
            "requestedVFs": "Auto",
            "requestedMbps": "2500",
            "boot": {
                "priority": "Primary"
            }
        }
    ],
    "bootMode": {
        "manageMode": True,
        "mode": "BIOS",
        "pxeBootPolicy": None
    },
    "boot": {
        "manageBoot": True,
        "order": [
            "CD",
            "USB",
            "HardDisk",
            "PXE"
        ]
    },
    "bios": {
        "manageBios": False,
        "overriddenSettings": []
    },
    "localStorage": {
        "controllers": []
    },
    "sanStorage": {
        "manageSanStorage": False,
        "volumeAttachments": []
    },
    "category": "server-profile-templates",
    "created": "2016-01-12T20:40:33.342Z",
    "modified": "2016-01-12T20:40:33.382Z",
    "status": "OK",
    "state": None,
    "eTag": "1452631233382/1"
}

SERVER_PROFILE_TEMPLATE_LIST_JSON = {
    "type": "ServerProfileTemplateListV1",
    "members": [
        {
            "type": "ServerProfileTemplateV1",
            "uri": "/rest/server-profile-templates/1597face-5ef4-40a5-b677-24e"
                   "1b63697f6",
            "name": "encl1-blade1-spt-test",
            "description": "",
            "serverProfileDescription": "",
            "serverHardwareTypeUri": "/rest/server-hardware-types/934E00C0-45F"
                                     "0-4329-AA8C-A0864E834ED4",
            "enclosureGroupUri": "/rest/enclosure-groups/c02d2e96-6142-49d6-bd"
                                 "38-0ce9d371e94f",
            "affinity": "Bay",
            "hideUnusedFlexNics": True,
            "macType": "Virtual",
            "wwnType": "Virtual",
            "serialNumberType": "Virtual",
            "firmware": {
                "manageFirmware": False,
                "firmwareInstallType": None,
                "forceInstallFirmware": False,
                "firmwareBaselineUri": None
            },
            "connections": [
                {
                    "id": 1,
                    "name": "encl1-blade1",
                    "functionType": "Ethernet",
                    "networkUri": "/rest/ethernet-networks/b4a0663d-9160-4566-"
                                  "96b3-1b00745c8115",
                    "portId": "Flb 1:1-a",
                    "requestedVFs": "Auto",
                    "requestedMbps": "2500",
                    "boot": {
                        "priority": "Primary"
                    }
                }
            ],
            "bootMode": {
                "manageMode": True,
                "mode": "BIOS",
                "pxeBootPolicy": None
            },
            "boot": {
                "manageBoot": True,
                "order": [
                    "CD",
                    "USB",
                    "HardDisk",
                    "PXE"
                ]
            },
            "bios": {
                "manageBios": False,
                "overriddenSettings": []
            },
            "localStorage": {
                "controllers": []
            },
            "sanStorage": {
                "manageSanStorage": False,
                "volumeAttachments": []
            },
            "category": "server-profile-templates",
            "created": "2016-01-12T20:40:33.342Z",
            "modified": "2016-01-12T20:40:33.382Z",
            "status": "OK",
            "state": None,
            "eTag": "1452631233382/1"
        },
        {
            "type": "ServerProfileTemplateV1",
            "uri": "/rest/server-profile-templates/1e805804-93f8-4ca9-9fce-067"
                   "5d1db9a1d",
            "name": "SPT-oneviewd-multi-thread-2",
            "description": "",
            "serverProfileDescription": "",
            "serverHardwareTypeUri": "/rest/server-hardware-types/CB2ECE5C-C05"
                                     "3-4288-86FE-A65B565BCAA4",
            "enclosureGroupUri": "/rest/enclosure-groups/c02d2e96-6142-49d6-bd"
                                 "38-0ce9d371e94f",
            "affinity": "Bay",
            "hideUnusedFlexNics": True,
            "macType": "Virtual",
            "wwnType": "Virtual",
            "serialNumberType": "Virtual",
            "firmware": {
                "manageFirmware": False,
                "firmwareInstallType": None,
                "forceInstallFirmware": False,
                "firmwareBaselineUri": None
            },
            "connections": [
                {
                    "id": 1,
                    "name": "encl1-blade1",
                    "functionType": "Ethernet",
                    "networkUri": "/rest/ethernet-networks/b4a0663d-9160-4566-"
                                  "96b3-1b00745c8115",
                    "portId": "Flb 1:1-a",
                    "requestedVFs": "Auto",
                    "requestedMbps": "2500",
                    "boot": {
                        "priority": "NotBootable"
                    }
                }
            ],
            "bootMode": None,
            "boot": {
                "manageBoot": True,
                "order": [
                    "CD",
                    "Floppy",
                    "USB",
                    "HardDisk",
                    "PXE"
                ]
            },
            "bios": {
                "manageBios": False,
                "overriddenSettings": []
            },
            "localStorage": {
                "controllers": []
            },
            "sanStorage": {
                "manageSanStorage": False,
                "volumeAttachments": []
            },
            "category": "server-profile-templates",
            "created": "2016-01-26T12:14:08.554Z",
            "modified": "2016-01-26T12:14:08.563Z",
            "status": "OK",
            "state": None,
            "eTag": "1453810448563/1"
        },
        {
            "type": "ServerProfileTemplateV1",
            "uri": "/rest/server-profile-templates/3d2b3833-c911-45ff-81e3-03f"
                   "81cc8730c",
            "name": "SPT-oneviewd-multi-thread-1",
            "description": "",
            "serverProfileDescription": "",
            "serverHardwareTypeUri": "/rest/server-hardware-types/61720699-7D8"
                                     "9-4E3E-BFC4-32FB9BBE2E71",
            "enclosureGroupUri": "/rest/enclosure-groups/c02d2e96-6142-49d6-bd"
                                 "38-0ce9d371e94f",
            "affinity": "Bay",
            "hideUnusedFlexNics": True,
            "macType": "Virtual",
            "wwnType": "Virtual",
            "serialNumberType": "Virtual",
            "firmware": {
                "manageFirmware": False,
                "firmwareInstallType": None,
                "forceInstallFirmware": False,
                "firmwareBaselineUri": None
            },
            "connections": [
                {
                    "id": 1,
                    "name": "internal-net-dcs-connection",
                    "functionType": "Ethernet",
                    "networkUri": "/rest/ethernet-networks/b4a0663d-9160-4566-"
                                  "96b3-1b00745c8115",
                    "portId": "Flb 1:1-a",
                    "requestedVFs": "Auto",
                    "requestedMbps": "2500",
                    "boot": {
                        "priority": "Primary"
                    }
                },
                {
                    "id": 2,
                    "name": "internal-net-dcs-connection",
                    "functionType": "Ethernet",
                    "networkUri": "/rest/ethernet-networks/b4a0663d-9160-4566-"
                                  "96b3-1b00745c8115",
                    "portId": "Flb 1:1-a",
                    "requestedVFs": "Auto",
                    "requestedMbps": "2500",
                    "boot": {
                        "priority": "NotBootable"
                    }
                }
            ],
            "bootMode": None,
            "boot": {
                "manageBoot": True,
                "order": [
                    "CD",
                    "Floppy",
                    "USB",
                    "HardDisk",
                    "PXE"
                ]
            },
            "bios": {
                "manageBios": False,
                "overriddenSettings": []
            },
            "localStorage": {
                "controllers": []
            },
            "sanStorage": {
                "manageSanStorage": False,
                "volumeAttachments": []
            },
            "category": "server-profile-templates",
            "created": "2016-01-26T12:13:46.585Z",
            "modified": "2016-01-26T14:48:13.486Z",
            "status": "OK",
            "state": None,
            "eTag": "1453819693486/2"
        },
        {
            "type": "ServerProfileTemplateV1",
            "uri": "/rest/server-profile-templates/4b120330-1c9c-4641-8aa6-bf0"
                   "626839ce1",
            "name": "Integration-Tests-Blade-8-Template",
            "description": "",
            "serverProfileDescription": "",
            "serverHardwareTypeUri": "/rest/server-hardware-types/CB2ECE5C-C05"
                                     "3-4288-86FE-A65B565BCAA4",
            "enclosureGroupUri": "/rest/enclosure-groups/9869a2ea-55ef-4f1f-90"
                                 "a3-8fbf71c0ad12",
            "affinity": "Bay",
            "hideUnusedFlexNics": True,
            "macType": "Physical",
            "wwnType": "Physical",
            "serialNumberType": "Physical",
            "firmware": {
                "manageFirmware": False,
                "firmwareInstallType": None,
                "forceInstallFirmware": False,
                "firmwareBaselineUri": None
            },
            "connections": [
                {
                    "id": 1,
                    "name": "Devstack Blade 7",
                    "functionType": "Ethernet",
                    "networkUri": "/rest/ethernet-networks/f676ffc9-d2c3-499e-"
                                  "b616-265708f34216",
                    "portId": "Flb 1:1-a",
                    "requestedVFs": "Auto",
                    "requestedMbps": "2500",
                    "boot": {
                        "priority": "NotBootable"
                    }
                },
                {
                    "id": 1,
                    "name": "internal-net-dcs-connection",
                    "functionType": "Ethernet",
                    "networkUri": "/rest/ethernet-networks/b4a0663d-9160-4566-"
                                  "96b3-1b00745c8115",
                    "portId": "Flb 1:1-a",
                    "requestedVFs": "Auto",
                    "requestedMbps": "2500",
                    "boot": {
                        "priority": "Primary"
                    }
                }

            ],
            "bootMode": None,
            "boot": {
                "manageBoot": True,
                "order": [
                    "CD",
                    "Floppy",
                    "USB",
                    "HardDisk",
                    "PXE"
                ]
            },
            "bios": {
                "manageBios": False,
                "overriddenSettings": []
            },
            "localStorage": {
                "controllers": []
            },
            "sanStorage": {
                "manageSanStorage": False,
                "volumeAttachments": []
            },
            "category": "server-profile-templates",
            "created": "2015-12-13T12:10:29.485Z",
            "modified": "2015-12-13T12:10:29.495Z",
            "status": "OK",
            "state": None,
            "eTag": "1450008629495/1"
        },
        {
            "type": "ServerProfileTemplateV1",
            "uri": "/rest/server-profile-templates/502aa84a-1bf1-408e-9247-825"
                   "3b4c2c914",
            "name": "ServerProfileTemplate-Blade8-AlocacaoDinamica",
            "description": "",
            "serverProfileDescription": "",
            "serverHardwareTypeUri": "/rest/server-hardware-types/150A6FA0-CB8"
                                     "3-4899-97A1-AA09F45F0D32",
            "enclosureGroupUri": "/rest/enclosure-groups/9869a2ea-55ef-4f1f-90"
                                 "a3-8fbf71c0ad12",
            "affinity": "Bay",
            "hideUnusedFlexNics": True,
            "macType": "Physical",
            "wwnType": "Physical",
            "serialNumberType": "Physical",
            "firmware": {
                "manageFirmware": False,
                "firmwareInstallType": None,
                "forceInstallFirmware": False,
                "firmwareBaselineUri": None
            },
            "connections": [
                {
                    "id": 1,
                    "name": "Devstack-blade7",
                    "functionType": "Ethernet",
                    "networkUri": "/rest/ethernet-networks/f676ffc9-d2c3-499e-"
                                  "b616-265708f34216",
                    "portId": "Flb 1:1-a",
                    "requestedVFs": "Auto",
                    "requestedMbps": "2500",
                    "boot": {
                        "priority": "NotBootable"
                    }
                },
                {
                    "id": 2,
                    "name": "Devstack-blade7",
                    "functionType": "Ethernet",
                    "networkUri": "/rest/ethernet-networks/f676ffc9-d2c3-499e-"
                                  "b616-265708f34216",
                    "portId": "Flb 1:1-a",
                    "requestedVFs": "Auto",
                    "requestedMbps": "2500",
                    "boot": {
                        "priority": "NotBootable"
                    }
                }
            ],
            "bootMode": None,
            "boot": {
                "manageBoot": True,
                "order": [
                    "CD",
                    "Floppy",
                    "USB",
                    "HardDisk",
                    "PXE"
                ]
            },
            "bios": {
                "manageBios": False,
                "overriddenSettings": []
            },
            "localStorage": {
                "controllers": []
            },
            "sanStorage": {
                "manageSanStorage": False,
                "volumeAttachments": []
            },
            "category": "server-profile-templates",
            "created": "2015-12-14T14:21:46.831Z",
            "modified": "2015-12-16T11:00:04.786Z",
            "status": "OK",
            "state": None,
            "eTag": "1450263604786/3"
        },
        {
            "type": "ServerProfileTemplateV1",
            "uri": "/rest/server-profile-templates/583d5d63-3d01-4622-aa20-4d4"
                   "926eb1c48",
            "name": "Integration Tests - Power and Management - DCS 4",
            "description": "",
            "serverProfileDescription": "",
            "serverHardwareTypeUri": "/rest/server-hardware-types/150A6FA0-CB8"
                                     "3-4899-97A1-AA09F45F0D32",
            "enclosureGroupUri": "/rest/enclosure-groups/c02d2e96-6142-49d6-bd"
                                 "38-0ce9d371e94f",
            "affinity": "Bay",
            "hideUnusedFlexNics": True,
            "macType": "Virtual",
            "wwnType": "Virtual",
            "serialNumberType": "Virtual",
            "firmware": {
                "manageFirmware": False,
                "firmwareInstallType": None,
                "forceInstallFirmware": False,
                "firmwareBaselineUri": None
            },
            "connections": [
                {
                    "id": 1,
                    "name": "DCS-Virt4-Net",
                    "functionType": "Ethernet",
                    "networkUri": "/rest/ethernet-networks/b4a0663d-9160-4566-"
                                  "96b3-1b00745c8115",
                    "portId": "Flb 1:1-a",
                    "requestedVFs": "Auto",
                    "requestedMbps": "2500",
                    "boot": {
                        "priority": "Primary"
                    }
                }
            ],
            "bootMode": None,
            "boot": {
                "manageBoot": False,
            },
            "bios": {
                "manageBios": False,
                "overriddenSettings": []
            },
            "localStorage": {
                "controllers": []
            },
            "sanStorage": {
                "manageSanStorage": False,
                "volumeAttachments": []
            },
            "category": "server-profile-templates",
            "created": "2015-12-13T12:19:52.242Z",
            "modified": "2015-12-13T12:19:52.247Z",
            "status": "OK",
            "state": None,
            "eTag": "1450009192247/1"
        },
        {
            "type": "ServerProfileTemplateV1",
            "uri": "/rest/server-profile-templates/8b60b11c-93dc-401a-9f88-0c1"
                   "4ee8a825b",
            "name": "Blade 6 Template",
            "description": "",
            "serverProfileDescription": "",
            "serverHardwareTypeUri": "/rest/server-hardware-types/8BE70066-9CE"
                                     "9-4007-986E-1B774146E0AA",
            "enclosureGroupUri": "/rest/enclosure-groups/9869a2ea-55ef-4f1f-90"
                                 "a3-8fbf71c0ad12",
            "affinity": "Bay",
            "hideUnusedFlexNics": True,
            "macType": "Physical",
            "wwnType": "Physical",
            "serialNumberType": "Physical",
            "firmware": {
                "manageFirmware": False,
                "firmwareInstallType": None,
                "forceInstallFirmware": False,
                "firmwareBaselineUri": None
            },
            "connections": [
                {
                    "id": 1,
                    "name": "Devstack - Integration Test",
                    "functionType": "Ethernet",
                    "networkUri": "/rest/ethernet-networks/326cb391-59ee-4cbd-"
                                  "ab12-505eed1488d9",
                    "portId": "Flb 1:1-a",
                    "requestedVFs": "Auto",
                    "requestedMbps": "2500",
                    "boot": {
                        "priority": "Primary"
                    }
                },
                {
                    "id": 2,
                    "name": "Rede 15",
                    "functionType": "Ethernet",
                    "networkUri": "/rest/ethernet-networks/45fa5da5-151b-46a4-"
                                  "b999-38d62f87cb6d",
                    "portId": "Flb 1:2-a",
                    "requestedVFs": "Auto",
                    "requestedMbps": "2500",
                    "boot": {
                        "priority": "NotBootable"
                    }
                }
            ],
            "bootMode": None,
            "boot": {
                "manageBoot": False,
                "order": [
                    "CD",
                    "Floppy",
                    "USB",
                    "HardDisk",
                    "PXE"
                ]
            },
            "bios": {
                "manageBios": False,
                "overriddenSettings": []
            },
            "localStorage": {
                "controllers": []
            },
            "sanStorage": {
                "manageSanStorage": False,
                "volumeAttachments": []
            },
            "category": "server-profile-templates",
            "created": "2015-12-13T11:50:14.656Z",
            "modified": "2015-12-13T11:50:14.683Z",
            "status": "OK",
            "state": None,
            "eTag": "1450007414683/1"
        },
        {
            "type": "ServerProfileTemplateV1",
            "uri": "/rest/server-profile-templates/939aa615-a74b-474c-af65-5f6"
                   "950f07e9e",
            "name": "Integration Tests - Power and Management - DCS 1",
            "description": "",
            "serverProfileDescription": "",
            "serverHardwareTypeUri": "/rest/server-hardware-types/934E00C0-45F"
                                     "0-4329-AA8C-A0864E834ED4",
            "enclosureGroupUri": "/rest/enclosure-groups/c02d2e96-6142-49d6-bd"
                                 "38-0ce9d371e94f",
            "affinity": "Bay",
            "hideUnusedFlexNics": True,
            "macType": "Virtual",
            "wwnType": "Virtual",
            "serialNumberType": "Virtual",
            "firmware": {
                "manageFirmware": False,
                "firmwareInstallType": None,
                "forceInstallFirmware": False,
                "firmwareBaselineUri": None
            },
            "connections": [
                {
                    "id": 1,
                    "name": "internal net dcs",
                    "functionType": "Ethernet",
                    "networkUri": "/rest/ethernet-networks/b4a0663d-9160-4566-"
                                  "96b3-1b00745c8115",
                    "portId": "Flb 1:1-a",
                    "requestedVFs": "Auto",
                    "requestedMbps": "2500",
                    "boot": {
                        "priority": "Primary"
                    }
                }
            ],
            "bootMode": {
                "manageMode": True,
                "mode": "BIOS",
                "pxeBootPolicy": None
            },
            "boot": {
                "manageBoot": False,
            },
            "bios": {
                "manageBios": False,
                "overriddenSettings": []
            },
            "localStorage": {
                "controllers": []
            },
            "sanStorage": {
                "manageSanStorage": False,
                "volumeAttachments": []
            },
            "category": "server-profile-templates",
            "created": "2015-12-13T12:18:40.189Z",
            "modified": "2015-12-13T12:18:40.192Z",
            "status": "OK",
            "state": None,
            "eTag": "1450009120192/1"
        },
        {
            "type": "ServerProfileTemplateV1",
            "uri": "/rest/server-profile-templates/c3446877-371b-4636-a007-c0c"
                   "07d7872c6",
            "name": "Integration-Tests-Blade-7-Template",
            "description": "",
            "serverProfileDescription": "",
            "serverHardwareTypeUri": "/rest/server-hardware-types/CB2ECE5C-C05"
                                     "3-4288-86FE-A65B565BCAA4",
            "enclosureGroupUri": "/rest/enclosure-groups/9869a2ea-55ef-4f1f-90"
                                 "a3-8fbf71c0ad12",
            "affinity": "Bay",
            "hideUnusedFlexNics": True,
            "macType": "Physical",
            "wwnType": "Physical",
            "serialNumberType": "Physical",
            "firmware": {
                "manageFirmware": False,
                "firmwareInstallType": None,
                "forceInstallFirmware": False,
                "firmwareBaselineUri": None
            },
            "connections": [
                {
                    "id": 1,
                    "name": "Devstack Blade 7",
                    "functionType": "Ethernet",
                    "networkUri": "/rest/ethernet-networks/f676ffc9-d2c3-499e-"
                                  "b616-265708f34216",
                    "portId": "Flb 1:1-a",
                    "requestedVFs": "Auto",
                    "requestedMbps": "2500",
                    "boot": {
                        "priority": "NotBootable"
                    }
                },
                {
                    "id": 2,
                    "name": "Rede 15",
                    "functionType": "Ethernet",
                    "networkUri": "/rest/ethernet-networks/45fa5da5-151b-46a4-"
                                  "b999-38d62f87cb6d",
                    "portId": "Flb 1:2-a",
                    "requestedVFs": "Auto",
                    "requestedMbps": "2500",
                    "boot": {
                        "priority": "NotBootable"
                    }
                }
            ],
            "bootMode": None,
            "boot": {
                "manageBoot": True,
                "order": [
                    "CD",
                    "Floppy",
                    "USB",
                    "HardDisk",
                    "PXE"
                ]
            },
            "bios": {
                "manageBios": False,
                "overriddenSettings": []
            },
            "localStorage": {
                "controllers": []
            },
            "sanStorage": {
                "manageSanStorage": False,
                "volumeAttachments": []
            },
            "category": "server-profile-templates",
            "created": "2015-12-13T12:07:34.250Z",
            "modified": "2015-12-13T12:07:34.257Z",
            "status": "OK",
            "state": None,
            "eTag": "1450008454257/1"
        },
        {
            "type": "ServerProfileTemplateV1",
            "uri": "/rest/server-profile-templates/ce100056-c928-4593-9118-7a8"
                   "c7317a02d",
            "name": "spt-DL-test-delete-it",
            "description": "",
            "serverProfileDescription": "",
            "serverHardwareTypeUri": "/rest/server-hardware-types/D2F405E3-24F"
                                     "9-4F25-9524-9818E21AF6D6",
            "enclosureGroupUri": None,
            "affinity": None,
            "hideUnusedFlexNics": None,
            "macType": "Physical",
            "wwnType": "Physical",
            "serialNumberType": "Physical",
            "firmware": {
                "manageFirmware": False,
                "firmwareInstallType": None,
                "forceInstallFirmware": False,
                "firmwareBaselineUri": None
            },
            "connections": [],
            "bootMode": {
                "manageMode": True,
                "mode": "BIOS",
                "pxeBootPolicy": None
            },
            "boot": {
                "manageBoot": True,
                "order": [
                    "CD",
                    "USB",
                    "HardDisk",
                    "PXE"
                ]
            },
            "bios": {
                "manageBios": False,
                "overriddenSettings": []
            },
            "localStorage": {
                "controllers": []
            },
            "sanStorage": {
                "manageSanStorage": False,
                "volumeAttachments": []
            },
            "category": "server-profile-templates",
            "created": "2016-02-15T20:27:16.165Z",
            "modified": "2016-02-15T20:27:16.225Z",
            "status": "OK",
            "state": None,
            "eTag": "1455568036225/1"
        }
    ],
    "start": 0,
    "prevPageUri": None,
    "nextPageUri": None,
    "count": 10,
    "total": 10,
    "created": "2016-02-26T21:16:32.003Z",
    "eTag": "2016-02-26T21:16:32.003Z",
    "modified": "2016-02-26T21:16:32.003Z",
    "category": "server-profile-templates",
    "uri": "/rest/server-profile-templates?start=0&count=64"
}

SERVER_PROFILE_JSON = {
    "type": "ServerProfileV1",
    "uri": "/rest/server-profiles/f2160e28-8107-45f9-b4b2-3119a622a3a1",
    "name": "blade3",
    "description": "compute node kilocloud2",
    "serialNumber": "VCGLPM4001",
    "uuid": "f2160e28-8107-45f9-b4b2-3119a622a3a1",
    "serverHardwareUri": "/rest/server-hardware/30313436-3631-5242-4333-303632"
                         "544333",
    "serverHardwareTypeUri": "/rest/server-hardware-types/CB2ECE5C-C053-4288-8"
                             "6FE-A65B565BCAA4",
    "enclosureGroupUri": "/rest/enclosure-groups/9869a2ea-55ef-4f1f-90a3-8fbf7"
                         "1c0ad12",
    "enclosureUri": "/rest/enclosures/09BRC3203AFD",
    "enclosureBay": 3,
    "firmware": {
        "manageFirmware": False,
        "firmwareBaselineUri": None
    },
    "macType": "Virtual",
    "wwnType": "Virtual",
    "serialNumberType": "Virtual",
    "category": "server-profiles",
    "created": "20151213T114910.008Z",
    "modified": "20160118T141346.473Z",
    "status": "OK",
    "state": "Normal",
    "inProgress": False,
    "taskUri": "/rest/tasks/81CECBC2-AAFD-4FB3-8E20-9F14579D3E0D",
    "connections": [
        {
            "id": 1,
            "functionType": "Ethernet",
            "deploymentStatus": "Deployed",
            "networkUri": "/rest/ethernet-networks/850cb594-9c6c-4c61-b4eb-d47"
                          "75859c4c7",
            "portId": "Flb 1:1-a",
            "interconnectUri": "/rest/interconnects/d6793c22-ded7-44b7-bdad-54"
                               "16d8534c39",
            "macType": "Virtual",
            "wwpnType": "Virtual",
            "mac": "F6:08:CF:00:00:01",
            "wwnn": None,
            "wwpn": None,
            "requestedMbps": 2500,
            "allocatedMbps": 2500,
            "maximumMbps": 10000,
            "boot": {
                "priority": "NotBootable"
            }
        }
    ],
    "boot": {
        "order": [
            "CD",
            "Floppy",
            "USB",
            "HardDisk",
            "PXE"
        ],
        "manageBoot": True
    },
    "bios": {
        "overriddenSettings": [],
        "manageBios": False
    },
    "eTag": "1450007350645/7"
}

SERVER_PROFILE_LIST_JSON = {
    "type": "ServerProfileListV1",
    "members": [
        {
            "type": "ServerProfileV1",
            "uri":
                "/rest/server-profiles/0cccd18d-df97-4414-a7d3-a0183607c612",
            "name": "blade4",
            "description": "compute node kilocloud2",
            "serialNumber": "VCGLPM4003",
            "uuid": "0cccd18d-df97-4414-a7d3-a0183607c612",
            "serverHardwareUri": "/rest/server-hardware/30313436-3631-5242-433"
                                 "3-32303341464E",
            "serverHardwareTypeUri": "/rest/server-hardware-types/CB2ECE5C-C05"
                                     "3-4288-86FE-A65B565BCAA4",
            "enclosureGroupUri": "/rest/enclosure-groups/9869a2ea-55ef-4f1f-90"
                                 "a3-8fbf71c0ad12",
            "enclosureUri": "/rest/enclosures/09BRC3203AFD",
            "enclosureBay": 4,
            "firmware": {
                "manageFirmware": False,
                "firmwareBaselineUri": None
            },
            "macType": "Virtual",
            "wwnType": "Virtual",
            "serialNumberType": "Virtual",
            "category": "server-profiles",
            "created": "20151213T115653.697Z",
            "modified": "20160118T141350.483Z",
            "status": "Critical",
            "state": "Normal",
            "inProgress": False,
            "taskUri": "/rest/tasks/38DF8FEE-FE85-4408-B131-31BEC0D89FCA",
            "connections": [
                {
                    "id": 1,
                    "functionType": "Ethernet",
                    "deploymentStatus": "Deployed",
                    "networkUri": "/rest/ethernet-networks/850cb594-9c6c-4c61-"
                                  "b4eb-d4775859c4c7",
                    "portId": "Flb 1:1-a",
                    "interconnectUri": "/rest/interconnects/d6793c22-ded7-44b7"
                                       "-bdad-5416d8534c39",
                    "macType": "Virtual",
                    "wwpnType": "Virtual",
                    "mac": "F6:08:CF:00:00:03",
                    "wwnn": None,
                    "wwpn": None,
                    "requestedMbps": 2500,
                    "allocatedMbps": 2500,
                    "maximumMbps": 10000,
                    "boot": {
                        "priority": "NotBootable"
                    }
                }
            ],
            "boot": {
                "order": [
                    "CD",
                    "Floppy",
                    "USB",
                    "HardDisk",
                    "PXE"
                ],
                "manageBoot": True
            },
            "bios": {
                "overriddenSettings": [],
                "manageBios": False
            },
            "eTag": "1450007813991/10"
        },
        {
            "type": "ServerProfileV1",
            "uri":
                "/rest/server-profiles/3c8394d5-ff5f-4893-8603-0d7a98939ab1",
            "name": "dyn-test [ff1224c0-7c58-4cea-b762-e6f61e061980]",
            "description": "",
            "serialNumber": "BRC3203AFH",
            "uuid": "30313436-3631-5242-4333-323033414648",
            "serverHardwareUri": "/rest/server-hardware/30313436-3631-5242-433"
                                 "3-323033414648",
            "serverHardwareTypeUri": "/rest/server-hardware-types/150A6FA0-CB8"
                                     "3-4899-97A1-AA09F45F0D32",
            "enclosureGroupUri": "/rest/enclosure-groups/9869a2ea-55ef-4f1f-90"
                                 "a3-8fbf71c0ad12",
            "enclosureUri": "/rest/enclosures/09BRC3203AFD",
            "enclosureBay": 8,
            "firmware": {
                "manageFirmware": False,
                "firmwareBaselineUri": None
            },
            "macType": "Physical",
            "wwnType": "Physical",
            "serialNumberType": "Physical",
            "category": "server-profiles",
            "created": "20160226T194834.708Z",
            "modified": "20160226T194925.133Z",
            "status": "Warning",
            "state": "Normal",
            "inProgress": False,
            "taskUri": "/rest/tasks/13ADD3C6-9B0E-4273-B125-E671A8824976",
            "connections": [
                {
                    "id": 1,
                    "functionType": "Ethernet",
                    "deploymentStatus": "Deployed",
                    "networkUri": "/rest/ethernet-networks/f676ffc9-d2c3-499e-"
                                  "b616-265708f34216",
                    "portId": "Flb 1:1-a",
                    "interconnectUri": "/rest/interconnects/d6793c22-ded7-44b7"
                                       "-bdad-5416d8534c39",
                    "macType": "Physical",
                    "wwpnType": "Physical",
                    "mac": "D8:9D:67:6A:C5:40",
                    "wwnn": None,
                    "wwpn": None,
                    "requestedMbps": 2500,
                    "allocatedMbps": 2500,
                    "maximumMbps": 10000,
                    "boot": {
                        "priority": "Primary"
                    }
                }
            ],
            "boot": {
                "order": [
                    "PXE",
                    "CD",
                    "Floppy",
                    "USB",
                    "HardDisk"
                ],
                "manageBoot": True
            },
            "bios": {
                "overriddenSettings": [],
                "manageBios": False
            },
            "eTag": "1456516144590/13"
        },
        {
            "type": "ServerProfileV1",
            "uri":
                "/rest/server-profiles/48ccb56d-5db4-4454-8b7c-19208fcb3785",
            "name": "Blade 6",
            "description": "",
            "serialNumber": "BRC3092WK1",
            "uuid": "39343336-3537-5242-4333-303932574B31",
            "serverHardwareUri": "/rest/server-hardware/39343336-3537-5242-433"
                                 "3-303932574B31",
            "serverHardwareTypeUri": "/rest/server-hardware-types/8BE70066-9CE"
                                     "9-4007-986E-1B774146E0AA",
            "enclosureGroupUri": "/rest/enclosure-groups/9869a2ea-55ef-4f1f-90"
                                 "a3-8fbf71c0ad12",
            "enclosureUri": "/rest/enclosures/09BRC3203AFD",
            "enclosureBay": 6,
            "firmware": {
                "manageFirmware": False,
                "firmwareBaselineUri": None
            },
            "macType": "Physical",
            "wwnType": "Physical",
            "serialNumberType": "Physical",
            "category": "server-profiles",
            "created": "20151213T120611.193Z",
            "modified": "20160218T132430.725Z",
            "status": "Warning",
            "state": "Normal",
            "inProgress": False,
            "taskUri": "/rest/tasks/1B3F2E82-5E6D-4CBB-B371-B136DBECD9B1",
            "connections": [
                {
                    "id": 1,
                    "functionType": "Ethernet",
                    "deploymentStatus": "Deployed",
                    "networkUri": "/rest/ethernet-networks/326cb391-59ee-4cbd-"
                                  "ab12-505eed1488d9",
                    "portId": "Flb 1:1-a",
                    "interconnectUri": "/rest/interconnects/d6793c22-ded7-44b7"
                                       "-bdad-5416d8534c39",
                    "macType": "Physical",
                    "wwpnType": "Physical",
                    "mac": "6C:3B:E5:BB:C0:B0",
                    "wwnn": None,
                    "wwpn": None,
                    "requestedMbps": 2500,
                    "allocatedMbps": 2500,
                    "maximumMbps": 10000,
                    "boot": {
                        "priority": "Primary"
                    }
                },
                {
                    "id": 2,
                    "functionType": "Ethernet",
                    "deploymentStatus": "Deployed",
                    "networkUri": "/rest/ethernet-networks/45fa5da5-151b-46a4-"
                                  "b999-38d62f87cb6d",
                    "portId": "Flb 1:2-a",
                    "interconnectUri": "/rest/interconnects/52cbe287-7de2-4488"
                                       "-8073-6fcf65ea71e7",
                    "macType": "Physical",
                    "wwpnType": "Physical",
                    "mac": "6C:3B:E5:BB:C0:B4",
                    "wwnn": None,
                    "wwpn": None,
                    "requestedMbps": 2500,
                    "allocatedMbps": 2500,
                    "maximumMbps": 10000,
                    "boot": {
                        "priority": "NotBootable"
                    }
                }
            ],
            "boot": {
                "order": [
                    "PXE",
                    "CD",
                    "Floppy",
                    "USB",
                    "HardDisk"
                ],
                "manageBoot": True
            },
            "bios": {
                "overriddenSettings": [],
                "manageBios": False
            },
            "eTag": "1452623152390/79"
        },
        {
            "type": "ServerProfileV1",
            "uri":
                "/rest/server-profiles/6db42da4-219d-4d02-aef7-67bc17726e6b",
            "name": "blade2",
            "description": "compute node kilocloud2",
            "serialNumber": "VCGLPM4002",
            "uuid": "6db42da4-219d-4d02-aef7-67bc17726e6b",
            "serverHardwareUri": "/rest/server-hardware/30313436-3631-5242-433"
                                 "3-323033414645",
            "serverHardwareTypeUri": "/rest/server-hardware-types/CB2ECE5C-C05"
                                     "3-4288-86FE-A65B565BCAA4",
            "enclosureGroupUri": "/rest/enclosure-groups/9869a2ea-55ef-4f1f-90"
                                 "a3-8fbf71c0ad12",
            "enclosureUri": "/rest/enclosures/09BRC3203AFD",
            "enclosureBay": 2,
            "firmware": {
                "manageFirmware": False,
                "firmwareBaselineUri": None
            },
            "macType": "Virtual",
            "wwnType": "Virtual",
            "serialNumberType": "Virtual",
            "category": "server-profiles",
            "created": "20151213T115144.584Z",
            "modified": "20160118T141343.104Z",
            "status": "Critical",
            "state": "Normal",
            "inProgress": False,
            "taskUri": "/rest/tasks/1E3468E8-FA6E-4D53-92E1-2C9709DA6229",
            "connections": [
                {
                    "id": 1,
                    "functionType": "Ethernet",
                    "deploymentStatus": "Deployed",
                    "networkUri": "/rest/ethernet-networks/850cb594-9c6c-4c61-"
                                  "b4eb-d4775859c4c7",
                    "portId": "Flb 1:1-a",
                    "interconnectUri": "/rest/interconnects/d6793c22-ded7-44b7"
                                       "-bdad-5416d8534c39",
                    "macType": "Virtual",
                    "wwpnType": "Virtual",
                    "mac": "F6:08:CF:00:00:02",
                    "wwnn": None,
                    "wwpn": None,
                    "requestedMbps": 2500,
                    "allocatedMbps": 2500,
                    "maximumMbps": 10000,
                    "boot": {
                        "priority": "NotBootable"
                    }
                }
            ],
            "boot": {
                "order": [
                    "CD",
                    "Floppy",
                    "USB",
                    "HardDisk",
                    "PXE"
                ],
                "manageBoot": True
            },
            "bios": {
                "overriddenSettings": [],
                "manageBios": False
            },
            "eTag": "1450007505057/10"
        },
        {
            "type": "ServerProfileV1",
            "uri":
                "/rest/server-profiles/b1f92e8d-d7e9-4f7c-84f4-7c732d43a962",
            "name": "Blade 5",
            "description": "",
            "serialNumber": "BRC3203AFS",
            "uuid": "30313436-3631-5242-4333-323033414653",
            "serverHardwareUri": "/rest/server-hardware/30313436-3631-5242-433"
                                 "3-323033414653",
            "serverHardwareTypeUri": "/rest/server-hardware-types/CB2ECE5C-C05"
                                     "3-4288-86FE-A65B565BCAA4",
            "enclosureGroupUri": "/rest/enclosure-groups/9869a2ea-55ef-4f1f-90"
                                 "a3-8fbf71c0ad12",
            "enclosureUri": "/rest/enclosures/09BRC3203AFD",
            "enclosureBay": 5,
            "firmware": {
                "manageFirmware": False,
                "firmwareBaselineUri": None
            },
            "macType": "Physical",
            "wwnType": "Physical",
            "serialNumberType": "Physical",
            "category": "server-profiles",
            "created": "20151213T120147.820Z",
            "modified": "20160218T132429.368Z",
            "status": "OK",
            "state": "Normal",
            "inProgress": False,
            "taskUri": "/rest/tasks/C8DB5F0E-211F-47BC-8328-A6189D2185F4",
            "connections": [
                {
                    "id": 1,
                    "functionType": "Ethernet",
                    "deploymentStatus": "Deployed",
                    "networkUri": "/rest/ethernet-networks/326cb391-59ee-4cbd-"
                                  "ab12-505eed1488d9",
                    "portId": "Flb 1:1-a",
                    "interconnectUri": "/rest/interconnects/d6793c22-ded7-44b7"
                                       "-bdad-5416d8534c39",
                    "macType": "Physical",
                    "wwpnType": "Physical",
                    "mac": "D8:9D:67:6A:25:88",
                    "wwnn": None,
                    "wwpn": None,
                    "requestedMbps": 2500,
                    "allocatedMbps": 2500,
                    "maximumMbps": 10000,
                    "boot": {
                        "priority": "NotBootable"
                    }
                },
                {
                    "id": 2,
                    "functionType": "Ethernet",
                    "deploymentStatus": "Deployed",
                    "networkUri": "/rest/ethernet-networks/45fa5da5-151b-46a4-"
                                  "b999-38d62f87cb6d",
                    "portId": "Flb 1:2-a",
                    "interconnectUri": "/rest/interconnects/52cbe287-7de2-4488"
                                       "-8073-6fcf65ea71e7",
                    "macType": "Physical",
                    "wwpnType": "Physical",
                    "mac": "D8:9D:67:6A:25:8C",
                    "wwnn": None,
                    "wwpn": None,
                    "requestedMbps": 2500,
                    "allocatedMbps": 2500,
                    "maximumMbps": 10000,
                    "boot": {
                        "priority": "NotBootable"
                    }
                }
            ],
            "boot": {
                "order": [
                    "CD",
                    "Floppy",
                    "USB",
                    "HardDisk",
                    "PXE"
                ],
                "manageBoot": True
            },
            "bios": {
                "overriddenSettings": [],
                "manageBios": False
            },
            "eTag": "1452078206847/40"
        },
        {
            "type": "ServerProfileV1",
            "uri":
                "/rest/server-profiles/b5cf9298-6226-49dc-aca0-44bcae20a01f",
            "name": "Ironic [0dc0c4a8-69ce-4fe3-8a70-cb326714e0d2]",
            "description": "",
            "serialNumber": "BRC513695W",
            "uuid": "32353537-3835-5242-4335-313336393557",
            "serverHardwareUri": "/rest/server-hardware/32353537-3835-5242-433"
                                 "5-313336393557",
            "serverHardwareTypeUri": "/rest/server-hardware-types/D2F405E3-24F"
                                     "9-4F25-9524-9818E21AF6D6",
            "enclosureGroupUri": None,
            "enclosureUri": None,
            "enclosureBay": None,
            "firmware": {
                "manageFirmware": False,
                "firmwareBaselineUri": None
            },
            "macType": "Physical",
            "wwnType": "Physical",
            "serialNumberType": "Physical",
            "category": "server-profiles",
            "created": "20160218T234841.743Z",
            "modified": "20160218T234932.964Z",
            "status": "Warning",
            "state": "Normal",
            "inProgress": False,
            "taskUri": "/rest/tasks/D6BD00A7-5892-44EC-BF73-49B04BF7A5B3",
            "connections": [],
            "boot": None,
            "bios": {
                "overriddenSettings": [],
                "manageBios": False
            },
            "eTag": "1455839356607/12"
        },
        {
            "type": "ServerProfileV1",
            "uri":
                "/rest/server-profiles/b7e78617-9678-43c5-8085-a47e03aa93e0",
            "name": "Integration-Tests-Blade-7",
            "description": "",
            "serialNumber": "BRC3203AFR",
            "uuid": "30313436-3631-5242-4333-323033414652",
            "serverHardwareUri": "/rest/server-hardware/30313436-3631-5242-433"
                                 "3-323033414652",
            "serverHardwareTypeUri": "/rest/server-hardware-types/CB2ECE5C-C05"
                                     "3-4288-86FE-A65B565BCAA4",
            "enclosureGroupUri": "/rest/enclosure-groups/9869a2ea-55ef-4f1f-90"
                                 "a3-8fbf71c0ad12",
            "enclosureUri": "/rest/enclosures/09BRC3203AFD",
            "enclosureBay": 7,
            "firmware": {
                "manageFirmware": False,
                "firmwareBaselineUri": None
            },
            "macType": "Physical",
            "wwnType": "Physical",
            "serialNumberType": "Physical",
            "category": "server-profiles",
            "created": "20151213T121416.426Z",
            "modified": "20160218T132427.372Z",
            "status": "OK",
            "state": "Normal",
            "inProgress": False,
            "taskUri": "/rest/tasks/997C5593-F21A-4FC0-80A9-4BA88EEE5B26",
            "connections": [
                {
                    "id": 1,
                    "functionType": "Ethernet",
                    "deploymentStatus": "Deployed",
                    "networkUri": "/rest/ethernet-networks/f676ffc9-d2c3-499e-"
                                  "b616-265708f34216",
                    "portId": "Flb 1:1-a",
                    "interconnectUri": "/rest/interconnects/d6793c22-ded7-44b7"
                                       "-bdad-5416d8534c39",
                    "macType": "Physical",
                    "wwpnType": "Physical",
                    "mac": "D8:9D:67:69:2C:30",
                    "wwnn": None,
                    "wwpn": None,
                    "requestedMbps": 2500,
                    "allocatedMbps": 2500,
                    "maximumMbps": 10000,
                    "boot": {
                        "priority": "NotBootable"
                    }
                },
                {
                    "id": 2,
                    "functionType": "Ethernet",
                    "deploymentStatus": "Deployed",
                    "networkUri": "/rest/ethernet-networks/45fa5da5-151b-46a4-"
                                  "b999-38d62f87cb6d",
                    "portId": "Flb 1:2-a",
                    "interconnectUri": "/rest/interconnects/52cbe287-7de2-4488"
                                       "-8073-6fcf65ea71e7",
                    "macType": "Physical",
                    "wwpnType": "Physical",
                    "mac": "D8:9D:67:69:2C:34",
                    "wwnn": None,
                    "wwpn": None,
                    "requestedMbps": 2500,
                    "allocatedMbps": 2500,
                    "maximumMbps": 10000,
                    "boot": {
                        "priority": "NotBootable"
                    }
                }
            ],
            "boot": {
                "order": [
                    "CD",
                    "Floppy",
                    "USB",
                    "HardDisk",
                    "PXE"
                ],
                "manageBoot": True
            },
            "bios": {
                "overriddenSettings": [],
                "manageBios": False
            },
            "eTag": "1452077182665/41"
        },
        {
            "type": "ServerProfileV1",
            "uri":
                "/rest/server-profiles/c1b9a029-328a-482a-be47-8be6c3741567",
            "name": "Integration Tests - Power and Management - DCS 2",
            "description": "",
            "serialNumber": "VCGLPM4004",
            "uuid": "c1b9a029-328a-482a-be47-8be6c3741567",
            "serverHardwareUri": None,
            "serverHardwareTypeUri": "/rest/server-hardware-types/934E00C0-45F"
                                     "0-4329-AA8C-A0864E834ED4",
            "enclosureGroupUri": "/rest/enclosure-groups/c02d2e96-6142-49d6-bd"
                                 "38-0ce9d371e94f",
            "enclosureUri": None,
            "enclosureBay": None,
            "firmware": {
                "manageFirmware": False,
                "firmwareBaselineUri": None
            },
            "macType": "Virtual",
            "wwnType": "Virtual",
            "serialNumberType": "Virtual",
            "category": "server-profiles",
            "created": "20151214T152031.395Z",
            "modified": "20160107T194900.125Z",
            "status": "OK",
            "state": "Normal",
            "inProgress": False,
            "taskUri": "/rest/tasks/A8DBACD7-DC4B-4052-91CC-925A8ABAF043",
            "connections": [
                {
                    "id": 1,
                    "functionType": "Ethernet",
                    "deploymentStatus": "Reserved",
                    "networkUri": "/rest/ethernet-networks/b4a0663d-9160-4566-"
                                  "96b3-1b00745c8115",
                    "portId": "Flb 1:1-a",
                    "interconnectUri": None,
                    "macType": "Virtual",
                    "wwpnType": "Virtual",
                    "mac": "F6:08:CF:00:00:04",
                    "wwnn": None,
                    "wwpn": None,
                    "requestedMbps": 2500,
                    "allocatedMbps": 2500,
                    "maximumMbps": 10000,
                    "boot": {
                        "priority": "Primary"
                    }
                }
            ],
            "boot": {
                "order": [
                    "CD",
                    "USB",
                    "HardDisk",
                    "PXE"
                ],
                "manageBoot": True
            },
            "bios": {
                "overriddenSettings": [],
                "manageBios": False
            },
            "eTag": "1452196122062/14"
        },
        {
            "type": "ServerProfileV1",
            "uri":
                "/rest/server-profiles/cbf35416-6d1b-418a-8cb8-6eb449781a4c",
            "name": "blade1",
            "description": "compute node kilocloud2",
            "serialNumber": "VCGLPM4000",
            "uuid": "cbf35416-6d1b-418a-8cb8-6eb449781a4c",
            "serverHardwareUri": "/rest/server-hardware/30313436-3631-5242-433"
                                 "3-32303341464B",
            "serverHardwareTypeUri": "/rest/server-hardware-types/CB2ECE5C-C05"
                                     "3-4288-86FE-A65B565BCAA4",
            "enclosureGroupUri": "/rest/enclosure-groups/9869a2ea-55ef-4f1f-90"
                                 "a3-8fbf71c0ad12",
            "enclosureUri": "/rest/enclosures/09BRC3203AFD",
            "enclosureBay": 1,
            "firmware": {
                "manageFirmware": False,
                "firmwareBaselineUri": None
            },
            "macType": "Virtual",
            "wwnType": "Virtual",
            "serialNumberType": "Virtual",
            "category": "server-profiles",
            "created": "20151213T114557.134Z",
            "modified": "20160118T141352.411Z",
            "status": "Critical",
            "state": "Normal",
            "inProgress": False,
            "taskUri": "/rest/tasks/206797BC-2A0F-4845-8370-35227ACF1242",
            "connections": [
                {
                    "id": 1,
                    "functionType": "Ethernet",
                    "deploymentStatus": "Deployed",
                    "networkUri": "/rest/ethernet-networks/850cb594-9c6c-4c61-"
                                  "b4eb-d4775859c4c7",
                    "portId": "Flb 1:1-a",
                    "interconnectUri": "/rest/interconnects/d6793c22-ded7-44b7"
                                       "-bdad-5416d8534c39",
                    "macType": "Virtual",
                    "wwpnType": "Virtual",
                    "mac": "F6:08:CF:00:00:00",
                    "wwnn": None,
                    "wwpn": None,
                    "requestedMbps": 2500,
                    "allocatedMbps": 2500,
                    "maximumMbps": 10000,
                    "boot": {
                        "priority": "NotBootable"
                    }
                }
            ],
            "boot": {
                "order": [
                    "CD",
                    "Floppy",
                    "USB",
                    "HardDisk",
                    "PXE"
                ],
                "manageBoot": True
            },
            "bios": {
                "overriddenSettings": [],
                "manageBios": False
            },
            "eTag": "1450007158282/10"
        },
        {
            "type": "ServerProfileV1",
            "uri":
                "/rest/server-profiles/f1e8c68b-d6b8-4af1-a496-e6a86e7c25db",
            "name": "Integration Tests - Power and Management - DCS 1",
            "description": "",
            "serialNumber": "SGH100X7RN",
            "uuid": "31393736-3831-4753-4831-30305837524E",
            "serverHardwareUri": None,
            "serverHardwareTypeUri": "/rest/server-hardware-types/934E00C0-45F"
                                     "0-4329-AA8C-A0864E834ED4",
            "enclosureGroupUri": "/rest/enclosure-groups/c02d2e96-6142-49d6-bd"
                                 "38-0ce9d371e94f",
            "enclosureUri": None,
            "enclosureBay": None,
            "firmware": {
                "manageFirmware": False,
                "firmwareBaselineUri": None
            },
            "macType": "Physical",
            "wwnType": "Physical",
            "serialNumberType": "Physical",
            "category": "server-profiles",
            "created": "20151214T145605.660Z",
            "modified": "20160107T194937.255Z",
            "status": "OK",
            "state": "Normal",
            "inProgress": False,
            "taskUri": "/rest/tasks/04E06839-2C51-4689-AC5D-6D673D3DD19E",
            "connections": [
                {
                    "id": 1,
                    "functionType": "Ethernet",
                    "deploymentStatus": "Reserved",
                    "networkUri": "/rest/ethernet-networks/b4a0663d-9160-4566-"
                                  "96b3-1b00745c8115",
                    "portId": "Flb 1:1-a",
                    "interconnectUri": None,
                    "macType": "Physical",
                    "wwpnType": "Physical",
                    "mac": None,
                    "wwnn": None,
                    "wwpn": None,
                    "requestedMbps": 2500,
                    "allocatedMbps": 2500,
                    "maximumMbps": 10000,
                    "boot": {
                        "priority": "Primary"
                    }
                }
            ],
            "boot": {
                "order": [
                    "PXE",
                    "HardDisk",
                    "CD",
                    "USB"
                ],
                "manageBoot": True
            },
            "bios": {
                "overriddenSettings": [],
                "manageBios": False
            },
            "eTag": "1452196159433/152"
        },
        {
            "type": "ServerProfileV1",
            "uri":
                "/rest/server-profiles/f2160e28-8107-45f9-b4b2-3119a622a3a1",
            "name": "blade3",
            "description": "compute node kilocloud2",
            "serialNumber": "VCGLPM4001",
            "uuid": "f2160e28-8107-45f9-b4b2-3119a622a3a1",
            "serverHardwareUri": "/rest/server-hardware/30313436-3631-5242-433"
                                 "3-303632544333",
            "serverHardwareTypeUri": "/rest/server-hardware-types/CB2ECE5C-C05"
                                     "3-4288-86FE-A65B565BCAA4",
            "enclosureGroupUri": "/rest/enclosure-groups/9869a2ea-55ef-4f1f-90"
                                 "a3-8fbf71c0ad12",
            "enclosureUri": "/rest/enclosures/09BRC3203AFD",
            "enclosureBay": 3,
            "firmware": {
                "manageFirmware": False,
                "firmwareBaselineUri": None
            },
            "macType": "Virtual",
            "wwnType": "Virtual",
            "serialNumberType": "Virtual",
            "category": "server-profiles",
            "created": "20151213T114910.008Z",
            "modified": "20160118T141346.473Z",
            "status": "OK",
            "state": "Normal",
            "inProgress": False,
            "taskUri": "/rest/tasks/81CECBC2-AAFD-4FB3-8E20-9F14579D3E0D",
            "connections": [
                {
                    "id": 1,
                    "functionType": "Ethernet",
                    "deploymentStatus": "Deployed",
                    "networkUri": "/rest/ethernet-networks/850cb594-9c6c-4c61-"
                                  "b4eb-d4775859c4c7",
                    "portId": "Flb 1:1-a",
                    "interconnectUri": "/rest/interconnects/d6793c22-ded7-44b7"
                                       "bdad-5416d8534c39",
                    "macType": "Virtual",
                    "wwpnType": "Virtual",
                    "mac": "F6:08:CF:00:00:01",
                    "wwnn": None,
                    "wwpn": None,
                    "requestedMbps": 2500,
                    "allocatedMbps": 2500,
                    "maximumMbps": 10000,
                    "boot": {
                        "priority": "NotBootable"
                    }
                }
            ],
            "boot": {
                "order": [
                    "CD",
                    "Floppy",
                    "USB",
                    "HardDisk",
                    "PXE"
                ],
                "manageBoot": True
            },
            "bios": {
                "overriddenSettings": [],
                "manageBios": False
            },
            "eTag": "1450007350645/7"
        }
    ],
    "start": 0,
    "prevPageUri": None,
    "nextPageUri": None,
    "count": 11,
    "total": 11,
    "created": "20160226T211219.135Z",
    "eTag": "20160226T211219.135Z",
    "modified": "20160226T211219.135Z",
    "category": "server-profiles",
    "uri": "/rest/server-profiles"
}

INDEX_SERVER_HARDWARE_LIST_JSON = json.loads("""{
    "type": "IndexPaginatedCollectionV4",
    "category": "resources",
    "members": [{
        "type": "IndexResource",
        "name": "172.18.6.31",
        "description": null,
        "attributes": {
            "mpIpV4Mode": "dhcp",
            "model": "ProLiant DL360 Gen9",
            "uidState": "Unsupported",
            "model_short": "DL360 Gen9",
            "refreshState": "RefreshFailed",
            "mpModel": "iLO4",
            "mpHostName": "172.18.6.31",
            "romVersion": "P89 v1.30",
            "mpFirmwareVersion": "2.20 Nov 01 2014",
            "serial_number": "MXQ1000208",
            "stateReason": "Unconfigured",
            "processorType": "Intel(R) Xeon(R) CPU E5620 @ 2.40GHz",
            "powerState": "Unknown",
            "bay": "0",
            "memoryMb": "32768",
            "uuid": "37333036-3831-584D-5131-303030323038",
            "partNumber": "603718-F21",
            "intelligentProvisioningVersion": "Unknown"
        },
        "multiAttributes": {
            "mpIpAddresses": ["172.18.6.31"],
            "mezzSlots": [],
            "mezzNames": []
        },
        "ownerId": "psrm",
        "state": "Unmanaged",
        "status": "Critical",
        "created": "2016-01-21T14:32:12.210Z",
        "modified": "2016-05-10T19:20:46.981Z",
        "eTag": "2016-05-10T19:20:46.981Z",
        "category": "server-hardware",
        "uri": "/rest/server-hardware/37333036-3831-584D-5131-303030323038"
    }, {
        "type": "IndexResource",
        "name": "DL160Gen9",
        "description": null,
        "attributes": {
            "mpIpV4Mode": "static",
            "model": "ProLiant DL160 Gen9",
            "uidState": "Unsupported",
            "model_short": "DL160 Gen9",
            "refreshState": "NotRefreshing",
            "mpModel": "iLO4",
            "romVersion": "U20 07/20/2015",
            "mpHostName": "DL160Gen9",
            "mpFirmwareVersion": "2.30 Aug 19 2015",
            "serial_number": "BRC549769T",
            "serverProfileUri":
                "/rest/server-profiles/90d7fa54-70b5-44d3-ab3c-eb3a48d02714",
            "stateReason": "NotApplicable",
            "processorType": "Intel(R) Xeon(R) CPU E5-2620 v3 @ 2.40GHz",
            "powerState": "Off",
            "bay": "0",
            "memoryMb": "65536",
            "uuid": "39343837-3239-5242-4335-343937363954",
            "profileName": "SP DL160 - SecureCloud",
            "partNumber": "784992-S05",
            "intelligentProvisioningVersion": "2.30.75"
        },
        "multiAttributes": {
            "mpIpAddresses": ["10.5.0.52"],
            "mezzSlots": [],
            "mezzNames": []
        },
        "ownerId": "psrm",
        "state": "ProfileApplied",
        "status": "Warning",
        "created": "2016-04-19T18:50:15.697Z",
        "modified": "2016-05-10T21:45:03.978Z",
        "eTag": "2016-05-10T21:45:03.978Z",
        "category": "server-hardware",
        "uri": "/rest/server-hardware/39343837-3239-5242-4335-343937363954"
    }, {
        "type": "IndexResource",
        "name": "DL360Gen9",
        "description": null,
        "attributes": {
            "mpIpV4Mode": "static",
            "model": "ProLiant DL360 Gen9",
            "uidState": "Unsupported",
            "model_short": "DL360 Gen9",
            "refreshState": "NotRefreshing",
            "mpModel": "iLO4",
            "romVersion": "P89 03/05/2015",
            "mpHostName": "DL360Gen9",
            "mpFirmwareVersion": "2.10 Jan 15 2015",
            "serial_number": "BRC513695W",
            "serverProfileUri":
                "/rest/server-profiles/f5c58a06-fdab-42e5-ae3e-4ef25b063367",
            "stateReason": "NotApplicable",
            "processorType": "Intel(R) Xeon(R) CPU E5-2603 v3 @ 1.60GHz",
            "powerState": "On",
            "bay": "0",
            "memoryMb": "81920",
            "uuid": "32353537-3835-5242-4335-313336393557",
            "profileName": "SP DL360 - SecureCloud",
            "partNumber": "755258-B21",
            "intelligentProvisioningVersion": "Unknown"
        },
        "multiAttributes": {
            "mpIpAddresses": ["10.5.0.250", "fe80:0:0:0:c634:6bff:febf:69b0"],
            "mezzSlots": [],
            "mezzNames": []
        },
        "ownerId": "psrm",
        "state": "ProfileApplied",
        "status": "Warning",
        "created": "2016-02-18T18:36:32.278Z",
        "modified": "2016-05-10T19:21:07.576Z",
        "eTag": "2016-05-10T19:21:07.576Z",
        "category": "server-hardware",
        "uri": "/rest/server-hardware/32353537-3835-5242-4335-313336393557"
    }, {
        "type": "IndexResource",
        "name": "Encl1, bay 1",
        "description": null,
        "attributes": {
            "mpIpV4Mode": "undefined",
            "model": "ProLiant BL660c Gen9",
            "uidState": "Unsupported",
            "model_short": "BL660c Gen9",
            "refreshState": "NotRefreshing",
            "mpModel": "iLO4",
            "mpHostName": "172.18.6.1",
            "romVersion": "I38 v1.30 08/03/2014",
            "mpFirmwareVersion": "2.20 Nov 01 2014",
            "serial_number": "SGH100X7RN",
            "stateReason": "NotApplicable",
            "processorType": "Quad-Core Intel Xeon @ 2.0GHz",
            "powerState": "Off",
            "bay": "1",
            "memoryMb": "16384",
            "uuid": "31393736-3831-4753-4831-30305837524E",
            "partNumber": "679118-B21",
            "intelligentProvisioningVersion": "Unknown"
        },
        "multiAttributes": {
            "mpIpAddresses": ["172.18.6.1"],
            "mezzSlots": ["1", "2", "3"],
            "mezzNames": ["", "", ""]
        },
        "ownerId": "psrm",
        "state": "NoProfileApplied",
        "status": "Warning",
        "created": "2016-01-07T19:56:03.256Z",
        "modified": "2016-05-10T19:38:42.557Z",
        "eTag": "2016-05-10T19:38:42.557Z",
        "category": "server-hardware",
        "uri": "/rest/server-hardware/31393736-3831-4753-4831-30305837524E"
    }, {
        "type": "IndexResource",
        "name": "Encl1, bay 2",
        "description": null,
        "attributes": {
            "mpIpV4Mode": "undefined",
            "model": "ProLiant BL660c Gen9",
            "uidState": "Unsupported",
            "model_short": "BL660c Gen9",
            "refreshState": "NotRefreshing",
            "mpModel": "iLO4",
            "mpHostName": "172.18.6.2",
            "romVersion": "I38 v1.30 08/03/2014",
            "mpFirmwareVersion": "2.20 Nov 01 2014",
            "serial_number": "SGH101X7RN",
            "stateReason": "NotApplicable",
            "processorType": "Quad-Core Intel Xeon @ 2.0GHz",
            "powerState": "Off",
            "bay": "2",
            "memoryMb": "16384",
            "uuid": "31393736-3831-4753-4831-30315837524E",
            "partNumber": "679118-B21",
            "intelligentProvisioningVersion": "Unknown"
        },
        "multiAttributes": {
            "mpIpAddresses": ["172.18.6.2"],
            "mezzSlots": ["1", "2", "3"],
            "mezzNames": ["", "", ""]
        },
        "ownerId": "psrm",
        "state": "NoProfileApplied",
        "status": "Warning",
        "created": "2016-01-07T19:56:03.599Z",
        "modified": "2016-05-10T19:38:38.829Z",
        "eTag": "2016-05-10T19:38:38.829Z",
        "category": "server-hardware",
        "uri": "/rest/server-hardware/31393736-3831-4753-4831-30315837524E"
    }, {
        "type": "IndexResource",
        "name": "Encl1, bay 3",
        "description": null,
        "attributes": {
            "mpIpV4Mode": "undefined",
            "model": "ProLiant BL460c Gen8",
            "uidState": "Unsupported",
            "model_short": "BL460c Gen8",
            "refreshState": "NotRefreshing",
            "mpModel": "iLO4",
            "mpHostName": "172.18.6.3",
            "romVersion": "I31 09/30/2011",
            "mpFirmwareVersion": "2.20 Nov 01 2014",
            "serial_number": "SGH100X8RN",
            "stateReason": "NotApplicable",
            "processorType": "Intel(R) Xeon(R) Processor E5620 @ 2.4GHz",
            "powerState": "Off",
            "bay": "3",
            "memoryMb": "32768",
            "uuid": "37333036-3831-4753-4831-30305838524E",
            "partNumber": "603718-C21",
            "intelligentProvisioningVersion": "Unknown"
        },
        "multiAttributes": {
            "mpIpAddresses": ["172.18.6.3"],
            "mezzSlots": ["1", "2"],
            "mezzNames": ["", ""]
        },
        "ownerId": "psrm",
        "state": "NoProfileApplied",
        "status": "Warning",
        "created": "2016-01-07T19:56:02.718Z",
        "modified": "2016-05-10T19:38:39.054Z",
        "eTag": "2016-05-10T19:38:39.054Z",
        "category": "server-hardware",
        "uri": "/rest/server-hardware/37333036-3831-4753-4831-30305838524E"
    }, {
        "type": "IndexResource",
        "name": "Encl1, bay 4",
        "description": null,
        "attributes": {
            "mpIpV4Mode": "undefined",
            "model": "ProLiant BL460c Gen8",
            "uidState": "Unsupported",
            "model_short": "BL460c Gen8",
            "refreshState": "NotRefreshing",
            "mpModel": "iLO4",
            "mpHostName": "172.18.6.4",
            "romVersion": "I31 09/30/2011",
            "mpFirmwareVersion": "2.20 Nov 01 2014",
            "serial_number": "SGH101X8RN",
            "stateReason": "NotApplicable",
            "processorType": "Intel(R) Xeon(R) Processor E5620 @ 2.4GHz",
            "powerState": "Off",
            "bay": "4",
            "memoryMb": "32768",
            "uuid": "37333036-3831-4753-4831-30315838524E",
            "partNumber": "603718-C21",
            "intelligentProvisioningVersion": "Unknown"
        },
        "multiAttributes": {
            "mpIpAddresses": ["172.18.6.4"],
            "mezzSlots": ["1", "2"],
            "mezzNames": ["", ""]
        },
        "ownerId": "psrm",
        "state": "NoProfileApplied",
        "status": "Warning",
        "created": "2016-01-07T19:56:04.029Z",
        "modified": "2016-05-10T19:38:39.868Z",
        "eTag": "2016-05-10T19:38:39.868Z",
        "category": "server-hardware",
        "uri": "/rest/server-hardware/37333036-3831-4753-4831-30315838524E"
    }, {
        "type": "IndexResource",
        "name": "Encl1, bay 5",
        "description": null,
        "attributes": {
            "mpIpV4Mode": "undefined",
            "model": "ProLiant BL460c Gen8",
            "uidState": "Unsupported",
            "model_short": "BL460c Gen8",
            "refreshState": "NotRefreshing",
            "mpModel": "iLO4",
            "mpHostName": "172.18.6.5",
            "romVersion": "I31 09/30/2011",
            "mpFirmwareVersion": "2.20 Nov 01 2014",
            "serial_number": "SGH102X8RN",
            "stateReason": "NotApplicable",
            "processorType": "Intel(R) Xeon(R) Processor E5620 @ 2.4GHz",
            "powerState": "Off",
            "bay": "5",
            "memoryMb": "32768",
            "uuid": "37333036-3831-4753-4831-30325838524E",
            "partNumber": "603718-C21",
            "intelligentProvisioningVersion": "Unknown"
        },
        "multiAttributes": {
            "mpIpAddresses": ["172.18.6.5"],
            "mezzSlots": ["1", "2"],
            "mezzNames": ["", ""]
        },
        "ownerId": "psrm",
        "state": "NoProfileApplied",
        "status": "Warning",
        "created": "2016-01-07T19:56:04.246Z",
        "modified": "2016-05-10T19:38:38.881Z",
        "eTag": "2016-05-10T19:38:38.881Z",
        "category": "server-hardware",
        "uri": "/rest/server-hardware/37333036-3831-4753-4831-30325838524E"
    }, {
        "type": "IndexResource",
        "name": "Encl1, bay 6",
        "description": null,
        "attributes": {
            "mpIpV4Mode": "undefined",
            "model": "ProLiant BL460c Gen8",
            "uidState": "Unsupported",
            "model_short": "BL460c Gen8",
            "refreshState": "NotRefreshing",
            "mpModel": "iLO4",
            "mpHostName": "172.18.6.6",
            "romVersion": "I31 09/30/2011",
            "mpFirmwareVersion": "2.20 Nov 01 2014",
            "serial_number": "SGH103X8RN",
            "stateReason": "NotApplicable",
            "processorType": "Intel(R) Xeon(R) Processor E5620 @ 2.4GHz",
            "powerState": "Off",
            "bay": "6",
            "memoryMb": "32768",
            "uuid": "37333036-3831-4753-4831-30335838524E",
            "partNumber": "603718-C21",
            "intelligentProvisioningVersion": "Unknown"
        },
        "multiAttributes": {
            "mpIpAddresses": ["172.18.6.6"],
            "mezzSlots": ["1", "2"],
            "mezzNames": ["", ""]
        },
        "ownerId": "psrm",
        "state": "NoProfileApplied",
        "status": "Warning",
        "created": "2016-01-07T19:56:04.353Z",
        "modified": "2016-05-10T19:38:42.546Z",
        "eTag": "2016-05-10T19:38:42.546Z",
        "category": "server-hardware",
        "uri": "/rest/server-hardware/37333036-3831-4753-4831-30335838524E"
    }, {
        "type": "IndexResource",
        "name": "Encl1, bay 7",
        "description": null,
        "attributes": {
            "mpIpV4Mode": "undefined",
            "model": "ProLiant BL460c Gen8",
            "uidState": "Unsupported",
            "model_short": "BL460c Gen8",
            "refreshState": "NotRefreshing",
            "mpModel": "iLO4",
            "mpHostName": "172.18.6.7",
            "romVersion": "I31 09/30/2011",
            "mpFirmwareVersion": "2.20 Nov 01 2014",
            "serial_number": "SGH104X8RN",
            "stateReason": "NotApplicable",
            "processorType": "Intel(R) Xeon(R) Processor E5620 @ 2.4GHz",
            "powerState": "Off",
            "bay": "7",
            "memoryMb": "32768",
            "uuid": "37333036-3831-4753-4831-30345838524E",
            "partNumber": "603718-C21",
            "intelligentProvisioningVersion": "Unknown"
        },
        "multiAttributes": {
            "mpIpAddresses": ["172.18.6.7"],
            "mezzSlots": ["1", "2"],
            "mezzNames": ["", ""]
        },
        "ownerId": "psrm",
        "state": "NoProfileApplied",
        "status": "Warning",
        "created": "2016-01-07T19:56:04.459Z",
        "modified": "2016-05-10T19:38:49.439Z",
        "eTag": "2016-05-10T19:38:49.439Z",
        "category": "server-hardware",
        "uri": "/rest/server-hardware/37333036-3831-4753-4831-30345838524E"
    }, {
        "type": "IndexResource",
        "name": "Encl1, bay 8",
        "description": null,
        "attributes": {
            "mpIpV4Mode": "undefined",
            "model": "ProLiant BL460c Gen8",
            "uidState": "Unsupported",
            "model_short": "BL460c Gen8",
            "refreshState": "NotRefreshing",
            "mpModel": "iLO4",
            "mpHostName": "172.18.6.8",
            "romVersion": "I31 09/30/2011",
            "mpFirmwareVersion": "2.20 Nov 01 2014",
            "serial_number": "SGH105X8RN",
            "stateReason": "NotApplicable",
            "processorType": "Intel(R) Xeon(R) Processor E5620 @ 2.4GHz",
            "powerState": "Off",
            "bay": "8",
            "memoryMb": "32768",
            "uuid": "37333036-3831-4753-4831-30355838524E",
            "partNumber": "603718-C21",
            "intelligentProvisioningVersion": "Unknown"
        },
        "multiAttributes": {
            "mpIpAddresses": ["172.18.6.8"],
            "mezzSlots": ["1", "2"],
            "mezzNames": ["", ""]
        },
        "ownerId": "psrm",
        "state": "NoProfileApplied",
        "status": "Warning",
        "created": "2016-01-07T19:56:04.701Z",
        "modified": "2016-05-10T19:38:47.877Z",
        "eTag": "2016-05-10T19:38:47.877Z",
        "category": "server-hardware",
        "uri": "/rest/server-hardware/37333036-3831-4753-4831-30355838524E"
    }, {
        "type": "IndexResource",
        "name": "Encl1, bay 11",
        "description": null,
        "attributes": {
            "mpIpV4Mode": "undefined",
            "model": "ProLiant BL460c Gen9",
            "uidState": "Unsupported",
            "model_short": "BL460c Gen9",
            "refreshState": "NotRefreshing",
            "mpModel": "iLO4",
            "romVersion": "I36 v1.30 08/26/2014",
            "mpHostName": "172.18.6.9",
            "mpFirmwareVersion": "2.20 Nov 01 2014",
            "serial_number": "SGH100X5RN",
            "serverProfileUri":
                "/rest/server-profiles/fd73eb62-771a-41b2-88c6-6c071c31415f",
            "stateReason": "NotApplicable",
            "processorType": "12-Core Intel(R) Corporation Xeon @ 2.4GHz",
            "powerState": "Off",
            "bay": "11",
            "memoryMb": "8192",
            "uuid": "30303437-3933-4753-4831-30305835524E",
            "profileName": "neutron-test",
            "partNumber": "740039-001",
            "intelligentProvisioningVersion": "Unknown"
        },
        "multiAttributes": {
            "mpIpAddresses": ["172.18.6.9"],
            "mezzSlots": ["1", "2"],
            "mezzNames": ["", ""]
        },
        "ownerId": "psrm",
        "state": "ProfileApplied",
        "status": "Warning",
        "created": "2016-01-07T19:56:03.789Z",
        "modified": "2016-05-10T19:38:50.654Z",
        "eTag": "2016-05-10T19:38:50.654Z",
        "category": "server-hardware",
        "uri": "/rest/server-hardware/30303437-3933-4753-4831-30305835524E"
    }, {
        "type": "IndexResource",
        "name": "Encl1, bay 12",
        "description": null,
        "attributes": {
            "mpIpV4Mode": "undefined",
            "model": "ProLiant BL460c Gen9",
            "uidState": "Unsupported",
            "model_short": "BL460c Gen9",
            "refreshState": "NotRefreshing",
            "mpModel": "iLO4",
            "mpHostName": "172.18.6.10",
            "romVersion": "I36 v1.30 08/26/2014",
            "mpFirmwareVersion": "2.20 Nov 01 2014",
            "serial_number": "SGH101X5RN",
            "stateReason": "NotApplicable",
            "processorType": "12-Core Intel(R) Corporation Xeon @ 2.4GHz",
            "powerState": "Off",
            "bay": "12",
            "memoryMb": "8192",
            "uuid": "30303437-3933-4753-4831-30315835524E",
            "partNumber": "740039-001",
            "intelligentProvisioningVersion": "Unknown"
        },
        "multiAttributes": {
            "mpIpAddresses": ["172.18.6.10"],
            "mezzSlots": ["1", "2"],
            "mezzNames": ["", ""]
        },
        "ownerId": "psrm",
        "state": "NoProfileApplied",
        "status": "Warning",
        "created": "2016-01-07T19:56:04.907Z",
        "modified": "2016-05-10T19:38:46.854Z",
        "eTag": "2016-05-10T19:38:46.854Z",
        "category": "server-hardware",
        "uri": "/rest/server-hardware/30303437-3933-4753-4831-30315835524E"
    }, {
        "type": "IndexResource",
        "name": "Encl1, bay 13",
        "description": null,
        "attributes": {
            "mpIpV4Mode": "undefined",
            "model": "ProLiant BL460c Gen9",
            "uidState": "Unsupported",
            "model_short": "BL460c Gen9",
            "refreshState": "NotRefreshing",
            "mpModel": "iLO4",
            "mpHostName": "172.18.6.11",
            "romVersion": "I36 v1.30 08/26/2014",
            "mpFirmwareVersion": "2.20 Nov 01 2014",
            "serial_number": "SGH102X5RN",
            "stateReason": "NotApplicable",
            "processorType": "12-Core Intel(R) Corporation Xeon @ 2.4GHz",
            "powerState": "Off",
            "bay": "13",
            "memoryMb": "8192",
            "uuid": "30303437-3933-4753-4831-30325835524E",
            "partNumber": "740039-001",
            "intelligentProvisioningVersion": "Unknown"
        },
        "multiAttributes": {
            "mpIpAddresses": ["172.18.6.11"],
            "mezzSlots": ["1", "2"],
            "mezzNames": ["", ""]
        },
        "ownerId": "psrm",
        "state": "NoProfileApplied",
        "status": "Warning",
        "created": "2016-01-07T19:56:05.242Z",
        "modified": "2016-05-10T19:38:42.957Z",
        "eTag": "2016-05-10T19:38:42.957Z",
        "category": "server-hardware",
        "uri": "/rest/server-hardware/30303437-3933-4753-4831-30325835524E"
    }, {
        "type": "IndexResource",
        "name": "Encl1, bay 14",
        "description": null,
        "attributes": {
            "mpIpV4Mode": "undefined",
            "model": "ProLiant BL460c Gen9",
            "uidState": "Unsupported",
            "model_short": "BL460c Gen9",
            "refreshState": "NotRefreshing",
            "mpModel": "iLO4",
            "mpHostName": "172.18.6.12",
            "romVersion": "I36 v1.30 08/26/2014",
            "mpFirmwareVersion": "2.20 Nov 01 2014",
            "serial_number": "SGH103X5RN",
            "stateReason": "NotApplicable",
            "processorType": "12-Core Intel(R) Corporation Xeon @ 2.4GHz",
            "powerState": "Off",
            "bay": "14",
            "memoryMb": "8192",
            "uuid": "30303437-3933-4753-4831-30335835524E",
            "partNumber": "740039-001",
            "intelligentProvisioningVersion": "Unknown"
        },
        "multiAttributes": {
            "mpIpAddresses": ["172.18.6.12"],
            "mezzSlots": ["1", "2"],
            "mezzNames": ["", ""]
        },
        "ownerId": "psrm",
        "state": "NoProfileApplied",
        "status": "Warning",
        "created": "2016-01-07T19:56:05.302Z",
        "modified": "2016-05-10T19:38:49.461Z",
        "eTag": "2016-05-10T19:38:49.461Z",
        "category": "server-hardware",
        "uri": "/rest/server-hardware/30303437-3933-4753-4831-30335835524E"
    }, {
        "type": "IndexResource",
        "name": "Encl1, bay 15",
        "description": null,
        "attributes": {
            "mpIpV4Mode": "undefined",
            "model": "ProLiant BL460c Gen9",
            "uidState": "Unsupported",
            "model_short": "BL460c Gen9",
            "refreshState": "NotRefreshing",
            "mpModel": "iLO4",
            "mpHostName": "172.18.6.13",
            "romVersion": "I36 v1.30 08/26/2014",
            "mpFirmwareVersion": "2.20 Nov 01 2014",
            "serial_number": "SGH104X5RN",
            "stateReason": "NotApplicable",
            "processorType": "12-Core Intel(R) Corporation Xeon @ 2.4GHz",
            "powerState": "Off",
            "bay": "15",
            "memoryMb": "8192",
            "uuid": "30303437-3933-4753-4831-30345835524E",
            "partNumber": "740039-001",
            "intelligentProvisioningVersion": "Unknown"
        },
        "multiAttributes": {
            "mpIpAddresses": ["172.18.6.13"],
            "mezzSlots": ["1", "2"],
            "mezzNames": ["", ""]
        },
        "ownerId": "psrm",
        "state": "NoProfileApplied",
        "status": "Warning",
        "created": "2016-01-07T19:56:05.518Z",
        "modified": "2016-05-10T19:38:49.031Z",
        "eTag": "2016-05-10T19:38:49.031Z",
        "category": "server-hardware",
        "uri": "/rest/server-hardware/30303437-3933-4753-4831-30345835524E"
    }, {
        "type": "IndexResource",
        "name": "Encl1, bay 16",
        "description": null,
        "attributes": {
            "mpIpV4Mode": "undefined",
            "model": "ProLiant BL460c Gen9",
            "uidState": "Unsupported",
            "model_short": "BL460c Gen9",
            "refreshState": "NotRefreshing",
            "mpModel": "iLO4",
            "mpHostName": "172.18.6.14",
            "romVersion": "I36 v1.30 08/26/2014",
            "mpFirmwareVersion": "2.20 Nov 01 2014",
            "serial_number": "SGH105X5RN",
            "stateReason": "NotApplicable",
            "processorType": "12-Core Intel(R) Corporation Xeon @ 2.4GHz",
            "powerState": "Off",
            "bay": "16",
            "memoryMb": "8192",
            "uuid": "30303437-3933-4753-4831-30355835524E",
            "partNumber": "740039-001",
            "intelligentProvisioningVersion": "Unknown"
        },
        "multiAttributes": {
            "mpIpAddresses": ["172.18.6.14"],
            "mezzSlots": ["1", "2"],
            "mezzNames": ["", ""]
        },
        "ownerId": "psrm",
        "state": "NoProfileApplied",
        "status": "Warning",
        "created": "2016-01-07T19:56:05.590Z",
        "modified": "2016-05-10T19:38:49.459Z",
        "eTag": "2016-05-10T19:38:49.459Z",
        "category": "server-hardware",
        "uri": "/rest/server-hardware/30303437-3933-4753-4831-30355835524E"
    }, {
        "type": "IndexResource",
        "name": "Encl2, bay 1",
        "description": null,
        "attributes": {
            "mpIpV4Mode": "undefined",
            "model": "ProLiant BL660c Gen9",
            "uidState": "Unsupported",
            "model_short": "BL660c Gen9",
            "refreshState": "NotRefreshing",
            "mpModel": "iLO4",
            "mpHostName": "172.18.6.17",
            "romVersion": "I38 v1.30 08/03/2014",
            "mpFirmwareVersion": "2.20 Nov 01 2014",
            "serial_number": "SGH102X7RN",
            "stateReason": "NotApplicable",
            "processorType": "Quad-Core Intel Xeon @ 2.0GHz",
            "powerState": "Off",
            "bay": "1",
            "memoryMb": "16384",
            "uuid": "31393736-3831-4753-4831-30325837524E",
            "partNumber": "679118-B21",
            "intelligentProvisioningVersion": "Unknown"
        },
        "multiAttributes": {
            "mpIpAddresses": ["172.18.6.17"],
            "mezzSlots": ["1", "2", "3"],
            "mezzNames": ["", "", ""]
        },
        "ownerId": "psrm",
        "state": "NoProfileApplied",
        "status": "Warning",
        "created": "2016-01-07T21:31:22.757Z",
        "modified": "2016-05-10T19:44:59.032Z",
        "eTag": "2016-05-10T19:44:59.032Z",
        "category": "server-hardware",
        "uri": "/rest/server-hardware/31393736-3831-4753-4831-30325837524E"
    }, {
        "type": "IndexResource",
        "name": "Encl2, bay 2",
        "description": null,
        "attributes": {
            "mpIpV4Mode": "undefined",
            "model": "ProLiant BL660c Gen9",
            "uidState": "Unsupported",
            "model_short": "BL660c Gen9",
            "refreshState": "NotRefreshing",
            "mpModel": "iLO4",
            "mpHostName": "172.18.6.18",
            "romVersion": "I38 v1.30 08/03/2014",
            "mpFirmwareVersion": "2.20 Nov 01 2014",
            "serial_number": "SGH103X7RN",
            "stateReason": "NotApplicable",
            "processorType": "Quad-Core Intel Xeon @ 2.0GHz",
            "powerState": "Off",
            "bay": "2",
            "memoryMb": "16384",
            "uuid": "31393736-3831-4753-4831-30335837524E",
            "partNumber": "679118-B21",
            "intelligentProvisioningVersion": "Unknown"
        },
        "multiAttributes": {
            "mpIpAddresses": ["172.18.6.18"],
            "mezzSlots": ["1", "2", "3"],
            "mezzNames": ["", "", ""]
        },
        "ownerId": "psrm",
        "state": "NoProfileApplied",
        "status": "Warning",
        "created": "2016-01-07T21:31:23.134Z",
        "modified": "2016-05-10T19:45:03.630Z",
        "eTag": "2016-05-10T19:45:03.630Z",
        "category": "server-hardware",
        "uri": "/rest/server-hardware/31393736-3831-4753-4831-30335837524E"
    }, {
        "type": "IndexResource",
        "name": "Encl2, bay 3",
        "description": null,
        "attributes": {
            "mpIpV4Mode": "undefined",
            "model": "ProLiant BL460c Gen8",
            "uidState": "Unsupported",
            "model_short": "BL460c Gen8",
            "refreshState": "NotRefreshing",
            "mpModel": "iLO4",
            "romVersion": "I31 09/30/2011",
            "mpHostName": "172.18.6.19",
            "mpFirmwareVersion": "2.20 Nov 01 2014",
            "serial_number": "SGH106X8RN",
            "serverProfileUri":
                "/rest/server-profiles/e473df8e-ed42-4f67-96f2-677c75d3b502",
            "stateReason": "NotApplicable",
            "processorType": "Intel(R) Xeon(R) Processor E5620 @ 2.4GHz",
            "powerState": "Off",
            "bay": "3",
            "memoryMb": "32768",
            "uuid": "37333036-3831-4753-4831-30365838524E",
            "profileName": "Integration Tests - Power and Management - DCS3",
            "partNumber": "603718-C21",
            "intelligentProvisioningVersion": "Unknown"
        },
        "multiAttributes": {
            "mpIpAddresses": ["172.18.6.19"],
            "mezzSlots": ["1", "2"],
            "mezzNames": ["", ""]
        },
        "ownerId": "psrm",
        "state": "ProfileApplied",
        "status": "Warning",
        "created": "2016-01-07T21:31:22.326Z",
        "modified": "2016-05-10T19:45:04.975Z",
        "eTag": "2016-05-10T19:45:04.975Z",
        "category": "server-hardware",
        "uri": "/rest/server-hardware/37333036-3831-4753-4831-30365838524E"
    }, {
        "type": "IndexResource",
        "name": "Encl2, bay 4",
        "description": null,
        "attributes": {
            "mpIpV4Mode": "undefined",
            "model": "ProLiant BL460c Gen8",
            "uidState": "Unsupported",
            "model_short": "BL460c Gen8",
            "refreshState": "NotRefreshing",
            "mpModel": "iLO4",
            "mpHostName": "172.18.6.20",
            "romVersion": "I31 09/30/2011",
            "mpFirmwareVersion": "2.20 Nov 01 2014",
            "serial_number": "SGH107X8RN",
            "stateReason": "NotApplicable",
            "processorType": "Intel(R) Xeon(R) Processor E5620 @ 2.4GHz",
            "powerState": "Off",
            "bay": "4",
            "memoryMb": "32768",
            "uuid": "37333036-3831-4753-4831-30375838524E",
            "partNumber": "603718-C21",
            "intelligentProvisioningVersion": "Unknown"
        },
        "multiAttributes": {
            "mpIpAddresses": ["172.18.6.20"],
            "mezzSlots": ["1", "2"],
            "mezzNames": ["", ""]
        },
        "ownerId": "psrm",
        "state": "NoProfileApplied",
        "status": "Warning",
        "created": "2016-01-07T21:31:23.393Z",
        "modified": "2016-05-10T19:45:01.857Z",
        "eTag": "2016-05-10T19:45:01.857Z",
        "category": "server-hardware",
        "uri": "/rest/server-hardware/37333036-3831-4753-4831-30375838524E"
    }, {
        "type": "IndexResource",
        "name": "Encl2, bay 5",
        "description": null,
        "attributes": {
            "mpIpV4Mode": "undefined",
            "model": "ProLiant BL460c Gen8",
            "uidState": "Unsupported",
            "model_short": "BL460c Gen8",
            "refreshState": "NotRefreshing",
            "mpModel": "iLO4",
            "mpHostName": "172.18.6.21",
            "romVersion": "I31 09/30/2011",
            "mpFirmwareVersion": "2.20 Nov 01 2014",
            "serial_number": "SGH108X8RN",
            "stateReason": "NotApplicable",
            "processorType": "Intel(R) Xeon(R) Processor E5620 @ 2.4GHz",
            "powerState": "Off",
            "bay": "5",
            "memoryMb": "32768",
            "uuid": "37333036-3831-4753-4831-30385838524E",
            "partNumber": "603718-C21",
            "intelligentProvisioningVersion": "Unknown"
        },
        "multiAttributes": {
            "mpIpAddresses": ["172.18.6.21"],
            "mezzSlots": ["1", "2"],
            "mezzNames": ["", ""]
        },
        "ownerId": "psrm",
        "state": "NoProfileApplied",
        "status": "Warning",
        "created": "2016-01-07T21:31:23.082Z",
        "modified": "2016-05-10T19:44:58.749Z",
        "eTag": "2016-05-10T19:44:58.749Z",
        "category": "server-hardware",
        "uri": "/rest/server-hardware/37333036-3831-4753-4831-30385838524E"
    }, {
        "type": "IndexResource",
        "name": "Encl2, bay 6",
        "description": null,
        "attributes": {
            "mpIpV4Mode": "undefined",
            "model": "ProLiant BL460c Gen8",
            "uidState": "Unsupported",
            "model_short": "BL460c Gen8",
            "refreshState": "NotRefreshing",
            "mpModel": "iLO4",
            "mpHostName": "172.18.6.22",
            "romVersion": "I31 09/30/2011",
            "mpFirmwareVersion": "2.20 Nov 01 2014",
            "serial_number": "SGH109X8RN",
            "stateReason": "NotApplicable",
            "processorType": "Intel(R) Xeon(R) Processor E5620 @ 2.4GHz",
            "powerState": "Off",
            "bay": "6",
            "memoryMb": "32768",
            "uuid": "37333036-3831-4753-4831-30395838524E",
            "partNumber": "603718-C21",
            "intelligentProvisioningVersion": "Unknown"
        },
        "multiAttributes": {
            "mpIpAddresses": ["172.18.6.22"],
            "mezzSlots": ["1", "2"],
            "mezzNames": ["", ""]
        },
        "ownerId": "psrm",
        "state": "NoProfileApplied",
        "status": "Warning",
        "created": "2016-01-07T21:31:23.805Z",
        "modified": "2016-05-10T19:45:02.257Z",
        "eTag": "2016-05-10T19:45:02.257Z",
        "category": "server-hardware",
        "uri": "/rest/server-hardware/37333036-3831-4753-4831-30395838524E"
    }, {
        "type": "IndexResource",
        "name": "Encl2, bay 7",
        "description": null,
        "attributes": {
            "mpIpV4Mode": "undefined",
            "model": "ProLiant BL460c Gen8",
            "uidState": "Unsupported",
            "model_short": "BL460c Gen8",
            "refreshState": "NotRefreshing",
            "mpModel": "iLO4",
            "mpHostName": "172.18.6.23",
            "romVersion": "I31 09/30/2011",
            "mpFirmwareVersion": "2.20 Nov 01 2014",
            "serial_number": "SGH110X8RN",
            "stateReason": "NotApplicable",
            "processorType": "Intel(R) Xeon(R) Processor E5620 @ 2.4GHz",
            "powerState": "Off",
            "bay": "7",
            "memoryMb": "32768",
            "uuid": "37333036-3831-4753-4831-31305838524E",
            "partNumber": "603718-C21",
            "intelligentProvisioningVersion": "Unknown"
        },
        "multiAttributes": {
            "mpIpAddresses": ["172.18.6.23"],
            "mezzSlots": ["1", "2"],
            "mezzNames": ["", ""]
        },
        "ownerId": "psrm",
        "state": "NoProfileApplied",
        "status": "Warning",
        "created": "2016-01-07T21:31:24.769Z",
        "modified": "2016-05-10T19:45:03.542Z",
        "eTag": "2016-05-10T19:45:03.542Z",
        "category": "server-hardware",
        "uri": "/rest/server-hardware/37333036-3831-4753-4831-31305838524E"
    }, {
        "type": "IndexResource",
        "name": "Encl2, bay 8",
        "description": null,
        "attributes": {
            "mpIpV4Mode": "undefined",
            "model": "ProLiant BL460c Gen8",
            "uidState": "Unsupported",
            "model_short": "BL460c Gen8",
            "refreshState": "NotRefreshing",
            "mpModel": "iLO4",
            "mpHostName": "172.18.6.24",
            "romVersion": "I31 09/30/2011",
            "mpFirmwareVersion": "2.20 Nov 01 2014",
            "serial_number": "SGH111X8RN",
            "stateReason": "NotApplicable",
            "processorType": "Intel(R) Xeon(R) Processor E5620 @ 2.4GHz",
            "powerState": "Off",
            "bay": "8",
            "memoryMb": "32768",
            "uuid": "37333036-3831-4753-4831-31315838524E",
            "partNumber": "603718-C21",
            "intelligentProvisioningVersion": "Unknown"
        },
        "multiAttributes": {
            "mpIpAddresses": ["172.18.6.24"],
            "mezzSlots": ["1", "2"],
            "mezzNames": ["", ""]
        },
        "ownerId": "psrm",
        "state": "NoProfileApplied",
        "status": "Warning",
        "created": "2016-01-07T21:31:24.106Z",
        "modified": "2016-05-10T19:45:01.867Z",
        "eTag": "2016-05-10T19:45:01.867Z",
        "category": "server-hardware",
        "uri": "/rest/server-hardware/37333036-3831-4753-4831-31315838524E"
    }, {
        "type": "IndexResource",
        "name": "Encl2, bay 11",
        "description": null,
        "attributes": {
            "mpIpV4Mode": "undefined",
            "model": "ProLiant BL460c Gen9",
            "uidState": "Unsupported",
            "model_short": "BL460c Gen9",
            "refreshState": "NotRefreshing",
            "mpModel": "iLO4",
            "mpHostName": "172.18.6.25",
            "romVersion": "I36 v1.30 08/26/2014",
            "mpFirmwareVersion": "2.20 Nov 01 2014",
            "serial_number": "SGH106X5RN",
            "stateReason": "NotApplicable",
            "processorType": "12-Core Intel(R) Corporation Xeon @ 2.4GHz",
            "powerState": "Off",
            "bay": "11",
            "memoryMb": "8192",
            "uuid": "30303437-3933-4753-4831-30365835524E",
            "partNumber": "740039-001",
            "intelligentProvisioningVersion": "Unknown"
        },
        "multiAttributes": {
            "mpIpAddresses": ["172.18.6.25"],
            "mezzSlots": ["1", "2"],
            "mezzNames": ["", ""]
        },
        "ownerId": "psrm",
        "state": "NoProfileApplied",
        "status": "Warning",
        "created": "2016-01-07T21:31:25.008Z",
        "modified": "2016-05-10T19:44:58.991Z",
        "eTag": "2016-05-10T19:44:58.991Z",
        "category": "server-hardware",
        "uri": "/rest/server-hardware/30303437-3933-4753-4831-30365835524E"
    }, {
        "type": "IndexResource",
        "name": "Encl2, bay 12",
        "description": null,
        "attributes": {
            "mpIpV4Mode": "undefined",
            "model": "ProLiant BL460c Gen9",
            "uidState": "Unsupported",
            "model_short": "BL460c Gen9",
            "refreshState": "NotRefreshing",
            "mpModel": "iLO4",
            "mpHostName": "172.18.6.26",
            "romVersion": "I36 v1.30 08/26/2014",
            "mpFirmwareVersion": "2.20 Nov 01 2014",
            "serial_number": "SGH107X5RN",
            "stateReason": "NotApplicable",
            "processorType": "12-Core Intel(R) Corporation Xeon @ 2.4GHz",
            "powerState": "Off",
            "bay": "12",
            "memoryMb": "8192",
            "uuid": "30303437-3933-4753-4831-30375835524E",
            "partNumber": "740039-001",
            "intelligentProvisioningVersion": "Unknown"
        },
        "multiAttributes": {
            "mpIpAddresses": ["172.18.6.26"],
            "mezzSlots": ["1", "2"],
            "mezzNames": ["", ""]
        },
        "ownerId": "psrm",
        "state": "NoProfileApplied",
        "status": "Warning",
        "created": "2016-01-07T21:31:25.174Z",
        "modified": "2016-05-10T19:45:03.844Z",
        "eTag": "2016-05-10T19:45:03.844Z",
        "category": "server-hardware",
        "uri": "/rest/server-hardware/30303437-3933-4753-4831-30375835524E"
    }, {
        "type": "IndexResource",
        "name": "Encl2, bay 13",
        "description": null,
        "attributes": {
            "mpIpV4Mode": "undefined",
            "model": "ProLiant BL460c Gen9",
            "uidState": "Unsupported",
            "model_short": "BL460c Gen9",
            "refreshState": "NotRefreshing",
            "mpModel": "iLO4",
            "mpHostName": "172.18.6.27",
            "romVersion": "I36 v1.30 08/26/2014",
            "mpFirmwareVersion": "2.20 Nov 01 2014",
            "serial_number": "SGH108X5RN",
            "stateReason": "NotApplicable",
            "processorType": "12-Core Intel(R) Corporation Xeon @ 2.4GHz",
            "powerState": "Off",
            "bay": "13",
            "memoryMb": "8192",
            "uuid": "30303437-3933-4753-4831-30385835524E",
            "partNumber": "740039-001",
            "intelligentProvisioningVersion": "Unknown"
        },
        "multiAttributes": {
            "mpIpAddresses": ["172.18.6.27"],
            "mezzSlots": ["1", "2"],
            "mezzNames": ["", ""]
        },
        "ownerId": "psrm",
        "state": "NoProfileApplied",
        "status": "Warning",
        "created": "2016-01-07T21:31:25.405Z",
        "modified": "2016-05-10T19:45:04.437Z",
        "eTag": "2016-05-10T19:45:04.437Z",
        "category": "server-hardware",
        "uri": "/rest/server-hardware/30303437-3933-4753-4831-30385835524E"
    }, {
        "type": "IndexResource",
        "name": "Encl2, bay 14",
        "description": null,
        "attributes": {
            "mpIpV4Mode": "undefined",
            "model": "ProLiant BL460c Gen9",
            "uidState": "Unsupported",
            "model_short": "BL460c Gen9",
            "refreshState": "NotRefreshing",
            "mpModel": "iLO4",
            "mpHostName": "172.18.6.28",
            "romVersion": "I36 v1.30 08/26/2014",
            "mpFirmwareVersion": "2.20 Nov 01 2014",
            "serial_number": "SGH109X5RN",
            "stateReason": "NotApplicable",
            "processorType": "12-Core Intel(R) Corporation Xeon @ 2.4GHz",
            "powerState": "Off",
            "bay": "14",
            "memoryMb": "8192",
            "uuid": "30303437-3933-4753-4831-30395835524E",
            "partNumber": "740039-001",
            "intelligentProvisioningVersion": "Unknown"
        },
        "multiAttributes": {
            "mpIpAddresses": ["172.18.6.28"],
            "mezzSlots": ["1", "2"],
            "mezzNames": ["", ""]
        },
        "ownerId": "psrm",
        "state": "NoProfileApplied",
        "status": "Warning",
        "created": "2016-01-07T21:31:25.561Z",
        "modified": "2016-05-10T19:45:04.987Z",
        "eTag": "2016-05-10T19:45:04.987Z",
        "category": "server-hardware",
        "uri": "/rest/server-hardware/30303437-3933-4753-4831-30395835524E"
    }, {
        "type": "IndexResource",
        "name": "Encl2, bay 15",
        "description": null,
        "attributes": {
            "mpIpV4Mode": "undefined",
            "model": "ProLiant BL460c Gen9",
            "uidState": "Unsupported",
            "model_short": "BL460c Gen9",
            "refreshState": "NotRefreshing",
            "mpModel": "iLO4",
            "mpHostName": "172.18.6.29",
            "romVersion": "I36 v1.30 08/26/2014",
            "mpFirmwareVersion": "2.20 Nov 01 2014",
            "serial_number": "SGH110X5RN",
            "stateReason": "NotApplicable",
            "processorType": "12-Core Intel(R) Corporation Xeon @ 2.4GHz",
            "powerState": "Off",
            "bay": "15",
            "memoryMb": "8192",
            "uuid": "30303437-3933-4753-4831-31305835524E",
            "partNumber": "740039-001",
            "intelligentProvisioningVersion": "Unknown"
        },
        "multiAttributes": {
            "mpIpAddresses": ["172.18.6.29"],
            "mezzSlots": ["1", "2"],
            "mezzNames": ["", ""]
        },
        "ownerId": "psrm",
        "state": "NoProfileApplied",
        "status": "Warning",
        "created": "2016-01-07T21:31:25.788Z",
        "modified": "2016-05-10T19:45:04.595Z",
        "eTag": "2016-05-10T19:45:04.595Z",
        "category": "server-hardware",
        "uri": "/rest/server-hardware/30303437-3933-4753-4831-31305835524E"
    }, {
        "type": "IndexResource",
        "name": "Encl2, bay 16",
        "description": null,
        "attributes": {
            "mpIpV4Mode": "undefined",
            "model": "ProLiant BL460c Gen9",
            "uidState": "Unsupported",
            "model_short": "BL460c Gen9",
            "refreshState": "NotRefreshing",
            "mpModel": "iLO4",
            "mpHostName": "172.18.6.30",
            "romVersion": "I36 v1.30 08/26/2014",
            "mpFirmwareVersion": "2.20 Nov 01 2014",
            "serial_number": "SGH111X5RN",
            "stateReason": "NotApplicable",
            "processorType": "12-Core Intel(R) Corporation Xeon @ 2.4GHz",
            "powerState": "Off",
            "bay": "16",
            "memoryMb": "8192",
            "uuid": "30303437-3933-4753-4831-31315835524E",
            "partNumber": "740039-001",
            "intelligentProvisioningVersion": "Unknown"
        },
        "multiAttributes": {
            "mpIpAddresses": ["172.18.6.30"],
            "mezzSlots": ["1", "2"],
            "mezzNames": ["", ""]
        },
        "ownerId": "psrm",
        "state": "NoProfileApplied",
        "status": "Warning",
        "created": "2016-01-07T21:31:24.571Z",
        "modified": "2016-05-10T19:45:04.799Z",
        "eTag": "2016-05-10T19:45:04.799Z",
        "category": "server-hardware",
        "uri": "/rest/server-hardware/30303437-3933-4753-4831-31315835524E"
    }, {
        "type": "IndexResource",
        "name": "LSD-enl, bay 1",
        "description": null,
        "attributes": {
            "mpIpV4Mode": "undefined",
            "model": "ProLiant BL460c Gen8",
            "uidState": "Unsupported",
            "model_short": "BL460c Gen8",
            "refreshState": "NotRefreshing",
            "mpModel": "iLO4",
            "romVersion": "I31 08/02/2014",
            "mpHostName": "ILOBRC3203AFK",
            "mpFirmwareVersion": "2.03 Nov 07 2014",
            "serial_number": "BRC3203AFK",
            "serverProfileUri":
                "/rest/server-profiles/cbf35416-6d1b-418a-8cb8-6eb449781a4c",
            "stateReason": "NotApplicable",
            "processorType": "Intel(R) Xeon(R) CPU E5-2630L 0 @ 2.00GHz",
            "powerState": "On",
            "bay": "1",
            "memoryMb": "57344",
            "uuid": "30313436-3631-5242-4333-32303341464B",
            "profileName": "blade1",
            "partNumber": "641016-B21",
            "intelligentProvisioningVersion": "1.40.88"
        },
        "multiAttributes": {
            "mpIpAddresses": ["10.5.0.201"],
            "mezzSlots": ["1", "2"],
            "mezzNames": ["HP LPe1205A 8Gb FC HBA for BladeSystem c-Class", ""]
        },
        "ownerId": "psrm",
        "state": "ProfileApplied",
        "status": "Warning",
        "created": "2015-12-13T11:28:03.456Z",
        "modified": "2016-05-10T19:24:48.805Z",
        "eTag": "2016-05-10T19:24:48.805Z",
        "category": "server-hardware",
        "uri": "/rest/server-hardware/30313436-3631-5242-4333-32303341464B"
    }, {
        "type": "IndexResource",
        "name": "LSD-enl, bay 2",
        "description": null,
        "attributes": {
            "mpIpV4Mode": "undefined",
            "model": "ProLiant BL460c Gen8",
            "uidState": "Unsupported",
            "model_short": "BL460c Gen8",
            "refreshState": "NotRefreshing",
            "mpModel": "iLO4",
            "romVersion": "I31 08/02/2014",
            "mpHostName": "ILOBRC3203AFE",
            "mpFirmwareVersion": "2.03 Nov 07 2014",
            "serial_number": "BRC3203AFE",
            "serverProfileUri":
                "/rest/server-profiles/6db42da4-219d-4d02-aef7-67bc17726e6b",
            "stateReason": "NotApplicable",
            "processorType": "Intel(R) Xeon(R) CPU E5-2630L 0 @ 2.00GHz",
            "powerState": "On",
            "bay": "2",
            "memoryMb": "40960",
            "uuid": "30313436-3631-5242-4333-323033414645",
            "profileName": "blade2",
            "partNumber": "641016-B21",
            "intelligentProvisioningVersion": "1.60.143"
        },
        "multiAttributes": {
            "mpIpAddresses": ["10.5.0.202"],
            "mezzSlots": ["1", "2"],
            "mezzNames": ["HP LPe1205A 8Gb FC HBA for BladeSystem c-Class", ""]
        },
        "ownerId": "psrm",
        "state": "ProfileApplied",
        "status": "Warning",
        "created": "2015-12-13T11:28:04.945Z",
        "modified": "2016-05-10T19:24:48.874Z",
        "eTag": "2016-05-10T19:24:48.874Z",
        "category": "server-hardware",
        "uri": "/rest/server-hardware/30313436-3631-5242-4333-323033414645"
    }, {
        "type": "IndexResource",
        "name": "LSD-enl, bay 3",
        "description": null,
        "attributes": {
            "mpIpV4Mode": "undefined",
            "model": "ProLiant BL460c Gen8",
            "uidState": "Unsupported",
            "model_short": "BL460c Gen8",
            "refreshState": "NotRefreshing",
            "mpModel": "iLO4",
            "romVersion": "I31 08/02/2014",
            "mpHostName": "ILOBRC3062TC3",
            "mpFirmwareVersion": "2.03 Nov 07 2014",
            "serial_number": "BRC3062TC3",
            "serverProfileUri":
                "/rest/server-profiles/f2160e28-8107-45f9-b4b2-3119a622a3a1",
            "stateReason": "NotApplicable",
            "processorType": "Intel(R) Xeon(R) CPU E5-2609 0 @ 2.40GHz",
            "powerState": "On",
            "bay": "3",
            "memoryMb": "81920",
            "uuid": "30313436-3631-5242-4333-303632544333",
            "profileName": "blade3",
            "partNumber": "641016-B21",
            "intelligentProvisioningVersion": "1.60.200"
        },
        "multiAttributes": {
            "mpIpAddresses": ["10.5.0.203"],
            "mezzSlots": ["1", "2"],
            "mezzNames": ["HP LPe1205A 8Gb FC HBA for BladeSystem c-Class", ""]
        },
        "ownerId": "psrm",
        "state": "ProfileApplied",
        "status": "Warning",
        "created": "2016-03-18T17:18:40.588Z",
        "modified": "2016-05-10T19:24:48.898Z",
        "eTag": "2016-05-10T19:24:48.898Z",
        "category": "server-hardware",
        "uri": "/rest/server-hardware/30313436-3631-5242-4333-303632544333"
    }, {
        "type": "IndexResource",
        "name": "LSD-enl, bay 4",
        "description": null,
        "attributes": {
            "mpIpV4Mode": "undefined",
            "model": "ProLiant BL460c Gen8",
            "uidState": "Unsupported",
            "model_short": "BL460c Gen8",
            "refreshState": "NotRefreshing",
            "mpModel": "iLO4",
            "romVersion": "I31 08/02/2014",
            "mpHostName": "ILOBRC3203AFN",
            "mpFirmwareVersion": "2.03 Nov 07 2014",
            "serial_number": "BRC3203AFN",
            "serverProfileUri":
                "/rest/server-profiles/0cccd18d-df97-4414-a7d3-a0183607c612",
            "stateReason": "NotApplicable",
            "processorType": "Intel(R) Xeon(R) CPU E5-2630L 0 @ 2.00GHz",
            "powerState": "On",
            "bay": "4",
            "memoryMb": "32768",
            "uuid": "30313436-3631-5242-4333-32303341464E",
            "profileName": "blade4",
            "partNumber": "641016-B21",
            "intelligentProvisioningVersion": "1.40.88"
        },
        "multiAttributes": {
            "mpIpAddresses": ["10.5.0.204"],
            "mezzSlots": ["1", "2"],
            "mezzNames": ["HP LPe1205A 8Gb FC HBA for BladeSystem c-Class", ""]
        },
        "ownerId": "psrm",
        "state": "ProfileApplied",
        "status": "Warning",
        "created": "2015-12-13T11:28:03.721Z",
        "modified": "2016-05-10T19:24:48.694Z",
        "eTag": "2016-05-10T19:24:48.694Z",
        "category": "server-hardware",
        "uri": "/rest/server-hardware/30313436-3631-5242-4333-32303341464E"
    }, {
        "type": "IndexResource",
        "name": "LSD-enl, bay 5",
        "description": null,
        "attributes": {
            "mpIpV4Mode": "undefined",
            "model": "ProLiant BL460c Gen8",
            "uidState": "Unsupported",
            "model_short": "BL460c Gen8",
            "refreshState": "NotRefreshing",
            "mpModel": "iLO4",
            "romVersion": "I31 08/02/2014",
            "mpHostName": "ILOBRC3203AFS",
            "mpFirmwareVersion": "2.03 Nov 07 2014",
            "serial_number": "BRC3203AFS",
            "serverProfileUri":
                "/rest/server-profiles/b1f92e8d-d7e9-4f7c-84f4-7c732d43a962",
            "stateReason": "NotApplicable",
            "processorType": "Intel(R) Xeon(R) CPU E5-2630L 0 @ 2.00GHz",
            "powerState": "On",
            "bay": "5",
            "memoryMb": "57344",
            "uuid": "30313436-3631-5242-4333-323033414653",
            "profileName": "Blade 5",
            "partNumber": "641016-B21",
            "intelligentProvisioningVersion": "1.40.88"
        },
        "multiAttributes": {
            "mpIpAddresses": ["10.5.0.205"],
            "mezzSlots": ["1", "2"],
            "mezzNames": ["HP LPe1205A 8Gb FC HBA for BladeSystem c-Class", ""]
        },
        "ownerId": "psrm",
        "state": "ProfileApplied",
        "status": "Warning",
        "created": "2015-12-13T11:28:04.606Z",
        "modified": "2016-05-10T19:24:48.968Z",
        "eTag": "2016-05-10T19:24:48.968Z",
        "category": "server-hardware",
        "uri": "/rest/server-hardware/30313436-3631-5242-4333-323033414653"
    }, {
        "type": "IndexResource",
        "name": "LSD-enl, bay 6",
        "description": null,
        "attributes": {
            "mpIpV4Mode": "undefined",
            "model": "ProLiant BL465c Gen8",
            "uidState": "Unsupported",
            "model_short": "BL465c Gen8",
            "refreshState": "NotRefreshing",
            "mpModel": "iLO4",
            "romVersion": "A26 09/03/2014",
            "mpHostName": "ILOBRC3092WK1",
            "mpFirmwareVersion": "2.03 Nov 07 2014",
            "serial_number": "BRC3092WK1",
            "serverProfileUri":
                "/rest/server-profiles/48ccb56d-5db4-4454-8b7c-19208fcb3785",
            "stateReason": "NotApplicable",
            "processorType": "AMD Opteron(tm) Processor 6204",
            "powerState": "Off",
            "bay": "6",
            "memoryMb": "16384",
            "uuid": "39343336-3537-5242-4333-303932574B31",
            "profileName": "Blade 6",
            "partNumber": "634975-B21",
            "intelligentProvisioningVersion": "1.30.113"
        },
        "multiAttributes": {
            "mpIpAddresses": ["10.5.0.206"],
            "mezzSlots": ["1", "2"],
            "mezzNames": ["", "HP LPe1205A 8Gb FC HBA for BladeSystem c-Class"]
        },
        "ownerId": "psrm",
        "state": "ProfileApplied",
        "status": "Warning",
        "created": "2015-12-13T11:28:07.615Z",
        "modified": "2016-05-10T19:24:48.874Z",
        "eTag": "2016-05-10T19:24:48.874Z",
        "category": "server-hardware",
        "uri": "/rest/server-hardware/39343336-3537-5242-4333-303932574B31"
    }, {
        "type": "IndexResource",
        "name": "LSD-enl, bay 7",
        "description": null,
        "attributes": {
            "mpIpV4Mode": "undefined",
            "model": "ProLiant BL460c Gen8",
            "uidState": "Unsupported",
            "model_short": "BL460c Gen8",
            "refreshState": "NotRefreshing",
            "mpModel": "iLO4",
            "romVersion": "I31 08/02/2014",
            "mpHostName": "ILOBRC3203AFR",
            "mpFirmwareVersion": "2.03 Nov 07 2014",
            "serial_number": "BRC3203AFR",
            "serverProfileUri":
                "/rest/server-profiles/b7e78617-9678-43c5-8085-a47e03aa93e0",
            "stateReason": "NotApplicable",
            "processorType": "Intel(R) Xeon(R) CPU E5-2630L 0 @ 2.00GHz",
            "powerState": "On",
            "bay": "7",
            "memoryMb": "16384",
            "uuid": "30313436-3631-5242-4333-323033414652",
            "profileName": "Integration-Tests-Blade-7",
            "partNumber": "641016-B21",
            "intelligentProvisioningVersion": "1.40.88"
        },
        "multiAttributes": {
            "mpIpAddresses": ["10.5.0.207"],
            "mezzSlots": ["1", "2"],
            "mezzNames": ["HP LPe1205A 8Gb FC HBA for BladeSystem c-Class", ""]
        },
        "ownerId": "psrm",
        "state": "ProfileApplied",
        "status": "OK",
        "created": "2015-12-13T11:28:06.261Z",
        "modified": "2016-05-10T19:25:16.098Z",
        "eTag": "2016-05-10T19:25:16.098Z",
        "category": "server-hardware",
        "uri": "/rest/server-hardware/30313436-3631-5242-4333-323033414652"
    }],
    "created": null,
    "modified": null,
    "uri": "<removed>",
    "prevPageUri": null,
    "nextPageUri": null,
    "start": 0,
    "count": 39,
    "total": 39,
    "unFilteredTotal": 39,
    "eTag": null
}""")

INDEX_SERVER_HARDWARE_JSON = json.loads("""{
    "type": "IndexPaginatedCollectionV4",
    "category": "resources",
    "members": [{
        "type": "IndexResource",
        "name": "172.18.6.31",
        "description": null,
        "attributes": {
            "mpIpV4Mode": "dhcp",
            "model": "ProLiant DL360 Gen9",
            "uidState": "Unsupported",
            "model_short": "DL360 Gen9",
            "refreshState": "RefreshFailed",
            "mpModel": "iLO4",
            "mpHostName": "172.18.6.31",
            "romVersion": "P89 v1.30",
            "mpFirmwareVersion": "2.20 Nov 01 2014",
            "serial_number": "MXQ1000208",
            "stateReason": "Unconfigured",
            "processorType": "Intel(R) Xeon(R) CPU E5620 @ 2.40GHz",
            "powerState": "Unknown",
            "bay": "0",
            "memoryMb": "32768",
            "uuid": "37333036-3831-584D-5131-303030323038",
            "partNumber": "603718-F21",
            "intelligentProvisioningVersion": "Unknown"
        },
        "multiAttributes": {
            "mpIpAddresses": ["172.18.6.31"],
            "mezzSlots": [],
            "mezzNames": []
        },
        "ownerId": "psrm",
        "state": "Unmanaged",
        "status": "Critical",
        "created": "2016-01-21T14:32:12.210Z",
        "modified": "2016-05-10T19:20:46.981Z",
        "eTag": "2016-05-10T19:20:46.981Z",
        "category": "server-hardware",
        "uri": "/rest/server-hardware/37333036-3831-584D-5131-303030323038"
    }],
    "created": null,
    "modified": null,
    "uri": "<removed>",
    "prevPageUri": null,
    "nextPageUri": null,
    "start": 0,
    "count": 1,
    "total": 1,
    "unFilteredTotal": 1,
    "eTag": null
}""")


PORT_MAP = {
    "deviceSlots": [{
        "deviceName": "HP FlexFabric 10Gb 2-port 554FLB Adapter",
        "deviceNumber": 9,
        "location": "Flb",
        "physicalPorts": [{
            "interconnectPort": 1,
            "interconnectUri": ("/rest/interconnects/25352bd0-6a7a-4c1"
                                "d-abe1-268c306c82b8"),
            "mac": "D8:9D:67:73:54:00",
            "physicalInterconnectPort": 1,
            "physicalInterconnectUri": ("/rest/interconnects/25352bd0-"
                                        "6a7a-4c1d-abe1-268c306c82b8"),
            "portNumber": 1,
            "type": "Ethernet",
            "virtualPorts": [{
                "currentAllocatedVirtualFunctionCount": (-1),
                "mac": "EA:EF:C7:70:00:00",
                "portFunction": "a",
                "portNumber": 1,
                "wwnn": None,
                "wwpn": None
            }, {
                "currentAllocatedVirtualFunctionCount": (-1),
                "mac": "D8:9D:67:73:54:01",
                "portFunction": "b",
                "portNumber": 2,
                "wwnn": "20:00:D8:9D:67:73:54:01",
                "wwpn": "10:00:D8:9D:67:73:54:01"
            }, {
                "currentAllocatedVirtualFunctionCount": (-1),
                "mac": "D8:9D:67:73:54:02",
                "portFunction": "c",
                "portNumber": 3,
                "wwnn": None,
                "wwpn": None
            }, {
                "currentAllocatedVirtualFunctionCount": (-1),
                "mac": "D8:9D:67:73:54:03",
                "portFunction": "d",
                "portNumber": 4,
                "wwnn": None,
                "wwpn": None
            }],
            "wwn": None
        }, {
            "interconnectPort": 1,
            "interconnectUri": ("/rest/interconnects/e005478c-8b50-45c"
                                "7-8aae-7239df039078"),
            "mac": "D8:9D:67:73:54:04",
            "physicalInterconnectPort": 1,
            "physicalInterconnectUri": ("/rest/interconnects/e005478c-"
                                        "8b50-45cf-8aae-7239df039078"),
            "portNumber": 2,
            "type": "Ethernet",
            "virtualPorts": [{
                "currentAllocatedVirtualFunctionCount": (-1),
                "mac": "D8:9D:67:73:54:04",
                "portFunction": "a",
                "portNumber": 1,
                "wwnn": None,
                "wwpn": None
            }, {
                "currentAllocatedVirtualFunctionCount": (-1),
                "mac": "D8:9D:67:73:54:05",
                "portFunction": "b",
                "portNumber": 2,
                "wwnn": "20:00:D8:9D:67:73:54:05",
                "wwpn": "10:00:D8:9D:67:73:54:05"
            }, {
                "currentAllocatedVirtualFunctionCount": (-1),
                "mac": "D8:9D:67:73:54:06",
                "portFunction": "c",
                "portNumber": 3,
                "wwnn": None,
                "wwpn": None
            }, {
                "currentAllocatedVirtualFunctionCount": (-1),
                "mac": "D8:9D:67:73:54:07",
                "portFunction": "d",
                "portNumber": 4,
                "wwnn": None,
                "wwpn": None
            }],
            "wwn": None
        }],
        "slotNumber": 1
    }, {
        "deviceName": "HP LPe1205A 8Gb FC HBA for BladeSystem c-Class",
        "deviceNumber": 1,
        "location": "Mezz",
        "physicalPorts": [{
            "interconnectPort": 1,
            "interconnectUri": ("/rest/interconnects/efb60cdf-caf4-438"
                                "2-8419-7ac969504034"),
            "mac": None,
            "physicalInterconnectPort": 1,
            "physicalInterconnectUri": ("/rest/interconnects/efb60cdf-"
                                        "caf4-4382-8419-7ac969504034"),
            "portNumber": 1,
            "type": "FibreChannel",
            "virtualPorts": [],
            "wwn": "10:00:38:EA:A7:D3:E4:40"
        }, {
            "interconnectPort": 1,
            "interconnectUri": ("/rest/interconnects/e4607445-0571-484"
                                "e-8629-8e01bdd1ea9f"),
            "mac": None,
            "physicalInterconnectPort": 1,
            "physicalInterconnectUri": ("/rest/interconnects/e4607445-"
                                        "0571-484e-8629-8e01bdd1ea9f"),
            "portNumber": 2,
            "type": "FibreChannel",
            "virtualPorts": [],
            "wwn": "10:00:38:EA:A7:D3:E4:41"
        }],
        "slotNumber": 1
    }, {
        "deviceName": "",
        "deviceNumber": 2,
        "location": "Mezz",
        "physicalPorts": [],
        "slotNumber": 2
    }]
}

PROPERTIES_DICT = {"cpu_arch": "x86_64",
                   "cpus": "8",
                   "local_gb": "10",
                   "memory_mb": "4096",
                   "capabilities": "server_hardware_type_uri:fake_sht_uri,"
                                   "enclosure_group_uri:fake_eg_uri"}

DRIVER_INFO_DICT = {'server_hardware_uri': 'fake_sh_uri',
                    'server_profile_template_uri': 'fake_spt_uri'}
