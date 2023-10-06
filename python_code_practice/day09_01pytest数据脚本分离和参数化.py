# 参数化: 接口信息一致, 参数不一致
# @pytest.mark.parametrize('datas', [{'name':'张三'}, {}]), 数据放代码里维护性差
# 类似于循环, 第一次取{'name':'张三'}, 第二次取{}

# 脚本和数据分离: 数据放excel里面, 可维护性好
# xlrd: python读取excel的第三方包
