import requests

# 登录
# 构造请求
url = 'http://43.138.178.63:81/haimo/sass/systemUser/release/getLogin'
data = {"userName":"admin","password":"e10adc3949ba59abbe56e057f20f883e"}
res = requests.post(url=url, json=data)

# 判断请求
assert res.status_code == 200  # 接口是正常工作的
assert res.json()['code'] == 1  # 接口的结果码来判断本次请求
print('登录成功')

'''a = {
    "code": 1,
    "msg": "登录成功",
    "data": [
        {
            "status": 0,
            "token": "T9iDoQCHHeH1dmfnJt7CkBBpSw33C1/5yOrVG8FLvB8=",
            "permission": {
                "router": "root",
                "children": [
                    {
                        "menuCode": "10001",
                        "name": "系统首页",
                        "router": "dashboard",
                        "authority": {
                            "role": [
                                "10001"
                            ]
                        },
                        "parentCode": "0"
                    },
                    {
                        "menuCode": "10002",
                        "name": "系统设置",
                        "router": "system",
                        "authority": {
                            "role": [
                                "10002"
                            ]
                        },
                        "children": [
                            {
                                "menuCode": "10003",
                                "name": "报告通用设置",
                                "router": "reportSetting",
                                "authority": {
                                    "role": [
                                        "10003"
                                    ]
                                },
                                "parentCode": "10002"
                            },
                            {
                                "menuCode": "10004",
                                "name": "角色权限",
                                "router": "roleList",
                                "authority": {
                                    "role": [
                                        "10004"
                                    ]
                                },
                                "parentCode": "10002"
                            },
                            {
                                "menuCode": "10005",
                                "name": "用户管理",
                                "router": "user",
                                "authority": {
                                    "role": [
                                        "10005"
                                    ]
                                },
                                "parentCode": "10002"
                            },
                            {
                                "menuCode": "10006",
                                "name": "操作日志",
                                "router": "operationLog",
                                "authority": {
                                    "role": [
                                        "10006"
                                    ]
                                },
                                "parentCode": "10002"
                            },
                            {
                                "menuCode": "10007",
                                "name": "登录日志",
                                "router": "loginLog",
                                "authority": {
                                    "role": [
                                        "10007"
                                    ]
                                },
                                "parentCode": "10002"
                            }
                        ],
                        "parentCode": "0"
                    },
                    {
                        "menuCode": "10008",
                        "name": "检测项目管理",
                        "router": "project",
                        "authority": {
                            "role": [
                                "10008"
                            ]
                        },
                        "children": [
                            {
                                "menuCode": "10009",
                                "name": "检测项目分类",
                                "router": "projectCategory",
                                "authority": {
                                    "role": [
                                        "10009"
                                    ]
                                },
                                "parentCode": "10008"
                            },
                            {
                                "menuCode": "10010",
                                "name": "检测项目列表",
                                "router": "projectList",
                                "authority": {
                                    "role": [
                                        "10010"
                                    ]
                                },
                                "parentCode": "10008"
                            },
                            {
                                "menuCode": "10011",
                                "name": "检测套餐列表",
                                "router": "projectMealList",
                                "authority": {
                                    "role": [
                                        "10011"
                                    ]
                                },
                                "parentCode": "10008"
                            },
                            {
                                "menuCode": "10072",
                                "name": "新增套餐",
                                "router": "addMeal",
                                "authority": {
                                    "role": [
                                        "10072"
                                    ]
                                },
                                "parentCode": "10008"
                            },
                            {
                                "menuCode": "10073",
                                "name": "确认套餐",
                                "router": "confirm",
                                "authority": {
                                    "role": [
                                        "10073"
                                    ]
                                },
                                "parentCode": "10008"
                            },
                            {
                                "menuCode": "10074",
                                "name": "套餐详情",
                                "router": "mealInfo",
                                "authority": {
                                    "role": [
                                        "10074"
                                    ]
                                },
                                "parentCode": "10008"
                            },
                            {
                                "menuCode": "10075",
                                "name": "套餐编辑",
                                "router": "mealEdit",
                                "authority": {
                                    "role": [
                                        "10075"
                                    ]
                                },
                                "parentCode": "10008"
                            }
                        ],
                        "parentCode": "0"
                    },
                    {
                        "menuCode": "10012",
                        "name": "病例管理",
                        "router": "case",
                        "authority": {
                            "role": [
                                "10012"
                            ]
                        },
                        "children": [
                            {
                                "menuCode": "10013",
                                "name": "病例列表",
                                "router": "caseList",
                                "authority": {
                                    "role": [
                                        "10013"
                                    ]
                                },
                                "parentCode": "10012"
                            },
                            {
                                "menuCode": "10078",
                                "name": "新增病例",
                                "router": "addCase",
                                "authority": {
                                    "role": [
                                        "10078"
                                    ]
                                },
                                "parentCode": "10012"
                            },
                            {
                                "menuCode": "10079",
                                "name": "病例详情",
                                "router": "caseDetail",
                                "authority": {
                                    "role": [
                                        "10079"
                                    ]
                                },
                                "parentCode": "10012"
                            },
                            {
                                "menuCode": "10080",
                                "name": "添加检测",
                                "router": "addTest",
                                "authority": {
                                    "role": [
                                        "10080"
                                    ]
                                },
                                "parentCode": "10012"
                            }
                        ],
                        "parentCode": "0"
                    },
                    {
                        "menuCode": "10014",
                        "name": "报告录入",
                        "router": "reportInput",
                        "authority": {
                            "role": [
                                "10014"
                            ]
                        },
                        "children": [
                            {
                                "menuCode": "10015",
                                "name": "报告录入列表",
                                "router": "reportInputList",
                                "authority": {
                                    "role": [
                                        "10015"
                                    ]
                                },
                                "parentCode": "10014"
                            },
                            {
                                "menuCode": "10052",
                                "name": "模板1/4",
                                "router": "templateOne",
                                "authority": {
                                    "role": [
                                        "10052"
                                    ]
                                },
                                "parentCode": "10014"
                            },
                            {
                                "menuCode": "10053",
                                "name": "模板2",
                                "router": "templateTwo",
                                "authority": {
                                    "role": [
                                        "10053"
                                    ]
                                },
                                "parentCode": "10014"
                            },
                            {
                                "menuCode": "10054",
                                "name": "模板3",
                                "router": "templateThree",
                                "authority": {
                                    "role": [
                                        "10054"
                                    ]
                                },
                                "parentCode": "10014"
                            },
                            {
                                "menuCode": "10055",
                                "name": "模板5",
                                "router": "templateFive",
                                "authority": {
                                    "role": [
                                        "10055"
                                    ]
                                },
                                "parentCode": "10014"
                            },
                            {
                                "menuCode": "10056",
                                "name": "模板6",
                                "router": "templateSix",
                                "authority": {
                                    "role": [
                                        "10056"
                                    ]
                                },
                                "parentCode": "10014"
                            },
                            {
                                "menuCode": "10057",
                                "name": "模板7",
                                "router": "templateSeven",
                                "authority": {
                                    "role": [
                                        "10057"
                                    ]
                                },
                                "parentCode": "10014"
                            },
                            {
                                "menuCode": "10058",
                                "name": "模板8",
                                "router": "templateEight",
                                "authority": {
                                    "role": [
                                        "10058"
                                    ]
                                },
                                "parentCode": "10014"
                            },
                            {
                                "menuCode": "10059",
                                "name": "模板9",
                                "router": "templateNine",
                                "authority": {
                                    "role": [
                                        "10059"
                                    ]
                                },
                                "parentCode": "10014"
                            },
                            {
                                "menuCode": "10060",
                                "name": "模板10",
                                "router": "templateTen",
                                "authority": {
                                    "role": [
                                        "10060"
                                    ]
                                },
                                "parentCode": "10014"
                            },
                            {
                                "menuCode": "10061",
                                "name": "模板11",
                                "router": "templateEleven",
                                "authority": {
                                    "role": [
                                        "10061"
                                    ]
                                },
                                "parentCode": "10014"
                            },
                            {
                                "menuCode": "10062",
                                "name": "模板12",
                                "router": "templateTwelve",
                                "authority": {
                                    "role": [
                                        "10062"
                                    ]
                                },
                                "parentCode": "10014"
                            },
                            {
                                "menuCode": "10063",
                                "name": "模板13",
                                "router": "templateThirteen",
                                "authority": {
                                    "role": [
                                        "10063"
                                    ]
                                },
                                "parentCode": "10014"
                            },
                            {
                                "menuCode": "10071",
                                "name": "报告录入详情",
                                "router": "reportInputDetail",
                                "authority": {
                                    "role": [
                                        "10071"
                                    ]
                                },
                                "parentCode": "10014"
                            }
                        ],
                        "parentCode": "0"
                    },
                    {
                        "menuCode": "10018",
                        "name": "报告批准",
                        "router": "reportApproval",
                        "authority": {
                            "role": [
                                "10018"
                            ]
                        },
                        "children": [
                            {
                                "menuCode": "10019",
                                "name": "待批准报告列表",
                                "router": "peddingList",
                                "authority": {
                                    "role": [
                                        "10019"
                                    ]
                                },
                                "parentCode": "10018"
                            },
                            {
                                "menuCode": "10020",
                                "name": "已批准报告列表",
                                "router": "approvalList",
                                "authority": {
                                    "role": [
                                        "10020"
                                    ]
                                },
                                "parentCode": "10018"
                            },
                            {
                                "menuCode": "10021",
                                "name": "报告详情",
                                "router": "reportDetailOne",
                                "authority": {
                                    "role": [
                                        "10021"
                                    ]
                                },
                                "parentCode": "10018"
                            }
                        ],
                        "parentCode": "0"
                    },
                    {
                        "menuCode": "10022",
                        "name": "统计管理",
                        "router": "statistics",
                        "authority": {
                            "role": [
                                "10022"
                            ]
                        },
                        "children": [
                            {
                                "menuCode": "10023",
                                "name": "报告统计",
                                "router": "reportStatistics",
                                "authority": {
                                    "role": [
                                        "10023"
                                    ]
                                },
                                "parentCode": "10022"
                            },
                            {
                                "menuCode": "10024",
                                "name": "病例统计",
                                "router": "caseStatistics",
                                "authority": {
                                    "role": [
                                        "10024"
                                    ]
                                },
                                "parentCode": "10022"
                            }
                        ],
                        "parentCode": "0"
                    },
                    {
                        "menuCode": "10025",
                        "name": "医院管理",
                        "router": "hospital",
                        "authority": {
                            "role": [
                                "10025"
                            ]
                        },
                        "children": [
                            {
                                "menuCode": "10026",
                                "name": "医院列表",
                                "router": "hospitalList",
                                "authority": {
                                    "role": [
                                        "10026"
                                    ]
                                },
                                "parentCode": "10025"
                            }
                        ],
                        "parentCode": "0"
                    },
                    {
                        "menuCode": "10027",
                        "name": "模板管理",
                        "router": "template",
                        "authority": {
                            "role": [
                                "10027"
                            ]
                        },
                        "children": [
                            {
                                "menuCode": "10028",
                                "name": "模板列表",
                                "router": "templateList",
                                "authority": {
                                    "role": [
                                        "10028"
                                    ]
                                },
                                "parentCode": "10027"
                            }
                        ],
                        "parentCode": "0"
                    },
                    {
                        "menuCode": "10029",
                        "name": "素材库管理",
                        "router": "material",
                        "authority": {
                            "role": [
                                "10029"
                            ]
                        },
                        "children": [
                            {
                                "menuCode": "10030",
                                "name": "通用素材库",
                                "router": "universalMaterial",
                                "authority": {
                                    "role": [
                                        "10030"
                                    ]
                                },
                                "parentCode": "10029"
                            },
                            {
                                "menuCode": "10031",
                                "name": "图片素材库",
                                "router": "pictureLibrary",
                                "authority": {
                                    "role": [
                                        "10031"
                                    ]
                                },
                                "parentCode": "10029"
                            },
                            {
                                "menuCode": "10032",
                                "name": "遗传素材库",
                                "router": "geneticMaterial",
                                "authority": {
                                    "role": [
                                        "10032"
                                    ]
                                },
                                "parentCode": "10029"
                            },
                            {
                                "menuCode": "10033",
                                "name": "细菌素材库",
                                "router": "bacterialMaterial",
                                "authority": {
                                    "role": [
                                        "10033"
                                    ]
                                },
                                "parentCode": "10029"
                            },
                            {
                                "menuCode": "10034",
                                "name": "真菌素材库",
                                "router": "fungiLibrary",
                                "authority": {
                                    "role": [
                                        "10034"
                                    ]
                                },
                                "parentCode": "10029"
                            },
                            {
                                "menuCode": "10035",
                                "name": "耐药菌素材库",
                                "router": "drugResistantBacteria",
                                "authority": {
                                    "role": [
                                        "10035"
                                    ]
                                },
                                "parentCode": "10029"
                            },
                            {
                                "menuCode": "10036",
                                "name": "DNA病毒素材库",
                                "router": "DNAVirusLibrary",
                                "authority": {
                                    "role": [
                                        "10036"
                                    ]
                                },
                                "parentCode": "10029"
                            },
                            {
                                "menuCode": "10037",
                                "name": "RNA病毒素材库",
                                "router": "RNAVirusLibrary",
                                "authority": {
                                    "role": [
                                        "10037"
                                    ]
                                },
                                "parentCode": "10029"
                            },
                            {
                                "menuCode": "10038",
                                "name": "寄生虫素材库",
                                "router": "parasiteMaterial",
                                "authority": {
                                    "role": [
                                        "10038"
                                    ]
                                },
                                "parentCode": "10029"
                            },
                            {
                                "menuCode": "10039",
                                "name": "特殊病原体素材库",
                                "router": "specialPathogen",
                                "authority": {
                                    "role": [
                                        "10039"
                                    ]
                                },
                                "parentCode": "10029"
                            },
                            {
                                "menuCode": "10040",
                                "name": "变异来源素材库",
                                "router": "variationSource",
                                "authority": {
                                    "role": [
                                        "10040"
                                    ]
                                },
                                "parentCode": "10029"
                            }
                        ],
                        "parentCode": "0"
                    },
                    {
                        "menuCode": "10066",
                        "name": "个人中心",
                        "router": "userConfig",
                        "authority": {
                            "role": [
                                "10066"
                            ]
                        },
                        "parentCode": "0"
                    },
                    {
                        "menuCode": "10016",
                        "name": "报告审核",
                        "router": "reportAudit",
                        "authority": {
                            "role": [
                                "10016"
                            ]
                        },
                        "children": [
                            {
                                "menuCode": "10017",
                                "name": "报告审核列表",
                                "router": "reportAuditList",
                                "authority": {
                                    "role": [
                                        "10017"
                                    ]
                                },
                                "parentCode": "10016"
                            },
                            {
                                "menuCode": "10076",
                                "name": "报告病例",
                                "router": "reportAuditCase",
                                "authority": {
                                    "role": [
                                        "10076"
                                    ]
                                },
                                "parentCode": "10016"
                            },
                            {
                                "menuCode": "10077",
                                "name": "报告编辑",
                                "router": "reportAuditEdit",
                                "authority": {
                                    "role": [
                                        "10077"
                                    ]
                                },
                                "parentCode": "10016"
                            }
                        ],
                        "parentCode": "0"
                    }
                ]
            },
            "roles": [
                {
                    "id": "10001",
                    "operation": []
                },
                {
                    "id": "10003",
                    "operation": []
                },
                {
                    "id": "10002",
                    "operation": []
                },
                {
                    "id": "10004",
                    "operation": [
                        "add",
                        "assign",
                        "edit",
                        "delete"
                    ]
                },
                {
                    "id": "10005",
                    "operation": [
                        "add",
                        "edit",
                        "assign",
                        "status",
                        "delete"
                    ]
                },
                {
                    "id": "10006",
                    "operation": [
                        "detail",
                        "delete"
                    ]
                },
                {
                    "id": "10007",
                    "operation": []
                },
                {
                    "id": "10009",
                    "operation": []
                },
                {
                    "id": "10008",
                    "operation": []
                },
                {
                    "id": "10010",
                    "operation": []
                },
                {
                    "id": "10011",
                    "operation": []
                },
                {
                    "id": "10013",
                    "operation": []
                },
                {
                    "id": "10012",
                    "operation": []
                },
                {
                    "id": "10078",
                    "operation": []
                },
                {
                    "id": "10079",
                    "operation": []
                },
                {
                    "id": "10080",
                    "operation": []
                },
                {
                    "id": "10015",
                    "operation": []
                },
                {
                    "id": "10014",
                    "operation": []
                },
                {
                    "id": "10052",
                    "operation": []
                },
                {
                    "id": "10053",
                    "operation": []
                },
                {
                    "id": "10054",
                    "operation": []
                },
                {
                    "id": "10055",
                    "operation": []
                },
                {
                    "id": "10056",
                    "operation": []
                },
                {
                    "id": "10057",
                    "operation": []
                },
                {
                    "id": "10058",
                    "operation": []
                },
                {
                    "id": "10059",
                    "operation": []
                },
                {
                    "id": "10060",
                    "operation": []
                },
                {
                    "id": "10061",
                    "operation": []
                },
                {
                    "id": "10062",
                    "operation": []
                },
                {
                    "id": "10063",
                    "operation": []
                },
                {
                    "id": "10071",
                    "operation": []
                },
                {
                    "id": "10017",
                    "operation": [
                        "edit",
                        "edit",
                        "withdraw"
                    ]
                },
                {
                    "id": "10019",
                    "operation": []
                },
                {
                    "id": "10018",
                    "operation": []
                },
                {
                    "id": "10020",
                    "operation": []
                },
                {
                    "id": "10021",
                    "operation": []
                },
                {
                    "id": "10023",
                    "operation": [
                        "detail"
                    ]
                },
                {
                    "id": "10022",
                    "operation": []
                },
                {
                    "id": "10024",
                    "operation": []
                },
                {
                    "id": "10026",
                    "operation": []
                },
                {
                    "id": "10025",
                    "operation": []
                },
                {
                    "id": "10028",
                    "operation": []
                },
                {
                    "id": "10027",
                    "operation": []
                },
                {
                    "id": "10030",
                    "operation": []
                },
                {
                    "id": "10029",
                    "operation": []
                },
                {
                    "id": "10031",
                    "operation": []
                },
                {
                    "id": "10032",
                    "operation": []
                },
                {
                    "id": "10033",
                    "operation": []
                },
                {
                    "id": "10034",
                    "operation": []
                },
                {
                    "id": "10035",
                    "operation": []
                },
                {
                    "id": "10036",
                    "operation": []
                },
                {
                    "id": "10037",
                    "operation": []
                },
                {
                    "id": "10038",
                    "operation": []
                },
                {
                    "id": "10039",
                    "operation": []
                },
                {
                    "id": "10040",
                    "operation": []
                },
                {
                    "id": "10066",
                    "operation": []
                },
                {
                    "id": "10072",
                    "operation": []
                },
                {
                    "id": "10073",
                    "operation": []
                },
                {
                    "id": "10074",
                    "operation": []
                },
                {
                    "id": "10075",
                    "operation": []
                },
                {
                    "id": "10016",
                    "operation": []
                },
                {
                    "id": "10076",
                    "operation": []
                },
                {
                    "id": "10077",
                    "operation": []
                }
            ],
            "userRoleCode": "69IOBJ"
        }
    ]
}
print(a['data'][0]['token'])
'''

# 获取token
user_token = res.json()['data'][0]['token']

# 第二个请求
# 构造请求
url2 = 'http://43.138.178.63:81/haimo/sass/systemUser/getSystemUser'
header2 = {'token': user_token}  # 关联
res= requests.post(url=url2, headers=header2)  # headers=header2, 把请求头带给接口
# 判断结果
assert res.status_code == 200  
assert res.json()['code'] == 1
print('获取系统用户接口正常')
