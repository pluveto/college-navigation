```js
// [GET] /xxx?p1=v1 表示请求方法 [GET]，路径 /xxx, 参数 p1 值为 v1
/**

Level Flags

转换方法：

 f & o == f 表示存在该值

var flags = Enum.GetValues(typeof(Status))
                .Cast<int>()
                .Where(f=> f & o == f)
                .ToList();
One gotcha with this approach is that it will include aggregate enumeration values. For example:

[Flags]
public enum Status
{
    None = 0,
    One = 1,
    Two = 2,
    All = One | Two,
}

使用 | 来标记 bit

例如 Bicycle + Car = 3 = 0000 0011（注：默认是 Default，用于标记常规道路）

*/
{
    "Default": 0,
    "Bicycle": 1,
    "Car": 2,
    "Bus": 4, // 用于跨校区
    "Subway": 8, // 用于跨校区
    "EnterBuilding": 16, // 用于主图到建筑内，建筑内之间
    "ExitBuilding": 32, // 用于主图到建筑内，建筑内之间
    "DownStair": 64, // 用于主图到建筑内，建筑内之间
    "UpStair": 128 // 用于主图到建筑内，建筑内之间
}
/*

@api {GET} /map_meta 获取地图元数据

返回格式：

*/
{
    "maps": [
        0,
        1,
        2,
        3
    ],
    "ports": [
        {
            "id": 1,
            "level": 12, // Subway + Bus = 4 + 8 = 12
            "sourceMapId": 0,
            "targetMapId": 1,
            "sourceNodeId": 1621873253982,
            "targetNodeId": 1621872829538
        },
        {
            "id": 2,
            "level": 12,
            "sourceMapId": 1,
            "targetMapId": 0,
            "sourceNodeId": 1621872829538,
            "targetNodeId": 1621873253982
        }
    ]
}
/*

@api {GET} /map/:id 获取地图数据

返回格式：

*/
{
    "elements": {
        "nodes": [
            {
                "data": {
                    "id": "6802523324657176576",
                    "title": "",
                    "subtitle": ""
                },
                "position": {
                    "x": 144,
                    "y": 483
                },
            }
        ],
        "edges": [
            {
                "data": {
                    "id": "6802523515032440832",
                    "source": "6802523392281939968",
                    "target": "6802523482799214592",
                    "level": 0
                }
            }
        ]
    }
}

/**
 * @api {POST} /paths?
 * & path_type = 1               // 路径规划类型 0 最短距离 1 最短时间
 * & prefer_transport_type = 1               // 优先交通工具 0 步行 1 强制自行车
 * & depart_at = 1231
 * & cross_type = 1         // 如果跨校区，选择通勤类型 1 班车 2 公交车 3 出租车
 * 获取路径
 * 
 */

// POST SAMPLE:

{
    "nodes": [
        {"nodeId": 123, "mapId": 123}, // 起点
        {"nodeId": 124, "mapId": 123}, // 途径
        {"nodeId": 125, "mapId": 123}, // 途径
        {"nodeId": 126, "mapId": 123}, // 终点
    ],
    "path_type": 1,
    "prefer_transport_type": 1,
    "depart_at": 0,
    "cross_type": 1,
}

// RETURN SAMPLE:

 {
    "time": 89,
    "path": [
        {
            "type": "node",
            "id": 123,
            "mapId": 1,
        },
        {
            "type": "transport",
            "level": 1
        },
        {
            "type": "node",
            "id": 124,
            "mapId": 1,
        },
        {
            "type": "port",
            "id": 123
        }
        {
            "type": "node",
            "id": 333,
            "mapId": 2,
        },
    ]
}
    
/**
 * @api {GET} /path?
 *   source_node_id = xxx
 * & target_node_id = xxx
 * & source_map_id = xxx
 * & target_mop_id = xxx
 * & path_type = 1               // 路径规划类型 0 最短距离 1 最短时间
 * & prefer_transport_type = 1               // 优先交通工具 0 步行 1 强制自行车
 * & depart_at = 1231
 * & cross_type = 1         // 如果跨校区，选择通勤类型 1 班车 2 公交车 3 出租车
 * 获取路径
 * 
 */
 {
    "time": 89,
    "path": [
        {
            "type": "node",
            "id": 123,
            "mapId": 1,
        },
        {
            "type": "transport",
            "level": 1
        },
        {
            "type": "node",
            "id": 124,
            "mapId": 1,
        },
        {
            "type": "port",
            "id": 123
        }
        {
            "type": "node",
            "id": 333,
            "mapId": 2,
        },
    ]
}
/**

关于示例文件

*/
{
    "group": "nodes",
    "removed": false,
    "selected": false,
    "selectable": true,
    "locked": false,
    "grabbable": true,
    "pannable": false,
    "classes": ""
}
/*
这种是编辑器自动生成的，不管就行。
*/

/* port.json */

{
    "maps": [
        0,
        1
    ],
    "ports": [
        {
            "id": 1,
            "level": 12,
            "sourceMapId": 1,
            "targetMapId": 0,
            "sourceNodeId": 1621873253982,
            "targetNodeId": 1621872829538
        },
        {
            "id": 2,
            "level": 12,
            "sourceMapId": 0,
            "targetMapId": 1,
            "sourceNodeId": 1621872829538,
            "targetNodeId": 1621873253982
        },
        {
            "id":3, // 进入教学楼 B2
            "level": 16,
            "sourceMapId": 1,
            "targetMapId": 2,
            "sourceNodeId": 1622019487136,
            "targetNodeId": 1622021008608 // "B2F1 进楼"
        },
        {
            "id":4,// 离开教学楼 B2
            "level": 16,
            "sourceMapId": 2,
            "targetMapId": 1,
            "sourceNodeId": 1622021008608, // "B2F1 进楼"
            "targetNodeId": 1622019487136
        }
    ]
}
```

