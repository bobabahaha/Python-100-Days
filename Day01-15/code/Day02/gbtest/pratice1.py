"""
--将华氏温度转换为摄氏温度
提示：华氏温度到摄氏温度的转换公式为：$C=(F - 32) \div 1.8$。
by gb
date 20240324
"""

wendu = int(input('请输入华式温度：'))
print('摄氏温度为：%0.1f'%((wendu - 32 )/18))
