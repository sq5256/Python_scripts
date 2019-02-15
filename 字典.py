city={
    "北京": {
        "东城":"景点",
        "朝阳":"娱乐",
        "海淀":"大学",
    },
    "深圳":{
        "罗湖":"老城区",
        "南山":"IT男聚集",
        "福田":"华强北",
    },
    "上海":{
        "黄埔":"xxxx",
        "徐汇":"xxxx",
        "静安":"xxxx",
    },
}
print(city["北京"]["东城"])
city["北京"]["东城"] = "故宫在这"
print(city["北京"]["东城"])
city["北京"]["昌平"] = "IT"
city["北京"]["海淀"]=["清华","北大","北邮"]
city["北京"]["海淀"].append("北影")
print(city)
for index, i in enumerate(city["北京"].keys()):
    print(index+1, i)
for index, i in enumerate(city["北京"]["海淀"]):
    print(index + 1, i)