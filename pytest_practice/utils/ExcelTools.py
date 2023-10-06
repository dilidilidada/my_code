import xlrd

class ExcelTools:
    
    @staticmethod
    def read_excel(excel_path, sheet_name, skip_first=True):
        """
            方法: python读取excel
            参数：
                excel_path: excel的路径
                sheet_name: sheet页面的名字
                skip_first: 是否跳过首行, 默认为True
            返回值：
                [
                    [行1, "查询病例列表", "http://haimo.testgoup.com/haimo/sass/case/sassListCase/10/1", "xxx",,,],
                    [行2],
                    [行3]
                ]
        """
        results = []  # 返回值变量

        datas = xlrd.open_workbook(excel_path)  # 打开excel并且获取操作对象
        table = datas.sheet_by_name(sheet_name)  # 获取每一个页面的操作对象
        if skip_first is True: # is ==
            start_row = 1  # 开始下标为1
        else:
            start_row = 0  # 开始下标为0

        # 循环读取每一行数据
        # table.nrows 自动获取有几行数据
        # range(1, 2) > [1,]
        # table.row_values(1) > [1, "查询病例列表", "/haimo/sass/case/sassListCase/10/1",...],
        for row in range(start_row, table.nrows):
            results.append(table.row_values(row))

        return results

if __name__ == "__main__":
    res = ExcelTools.read_excel(r'C:\Users\Administrator\Desktop\py try again\data\haimo_api.xlsx', '首页')
    print(res)