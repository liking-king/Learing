import pandas as pd

# 求大风天停工的概率。大风天停工的概率：是指在天气为大风的这些天里，停工的天数占大风天总天数的比例 公式:古典概率学
data = {
  "日期": ["1号", "2号", "3号", "4号", "5号", "6号", "7号"],
  "天气": ["晴", "大风", "大风", "晴", "雨", "大风", "雨"],
  "停工": [False, True, True, False, True, False, True]
}
df = pd.DataFrame(data)

# 大风天的总天数
windy_day = df[df['天气']=='大风']
windy_days = len(windy_day)

# 大风天且停工的天数
stop_and_windy = windy_day[windy_day['停工']==True]
stop_and_windy_day = len(stop_and_windy)


# 大风天停工的概率
P_stop = stop_and_windy_day / windy_days
print(f"大风天停工的概率: {round(P_stop, 3)}")