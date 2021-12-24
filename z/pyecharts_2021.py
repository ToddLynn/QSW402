#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Line



df = pd.read_excel('data.xlsx')
df.sort_index(ascending=False,inplace=True)


y_data = []
counter = 0
position = ['left', 'right']
for idx, row in df.iterrows():
    msg = '{bbb|%s}\n{aaa|%s}' % (row['日期'], row['事件'])
    l_item = opts.LineItem(
        name=10,
        value=counter,
        symbol='emptyCircle',
        symbol_size=10,
        label_opts=opts.LabelOpts(
            is_show=True,
            font_size=16,
            position=position[counter%2],
            formatter=msg,
            rich={
                'aaa': {
                    'fontSize': 12,
                    'color': 'FireBrick',
                    'fontWeight':'bold',
                    'align':position[(counter+1)%2],
                    },
                'bbb': {
                    'fontSize': 14,
                    'color': '#000',
                    'align':position[(counter+1)%2]}}
            )
    )
    y_data.append(l_item)
    counter+=1


line = Line(
    init_opts=opts.InitOpts(
        theme='light',
        width='500px',
        height='900px'
    )
)
line.add_xaxis(
    ['']
)
line.add_yaxis(
    '',
    y_data,
    linestyle_opts={
        'normal': {
            'width': 4,  # 设置线宽
            'color':'SteelBlue',
            'shadowColor': 'rgba(155, 18, 184, .3)',  # 阴影颜色
            'shadowBlur': 10,  # 阴影大小
            'shadowOffsetY': 10,  # Y轴方向阴影偏移
            'shadowOffsetX': 10,  # x轴方向阴影偏移
        }
    },
    itemstyle_opts={
        'normal': {
            'color':'red',
            'shadowColor': 'rgba(155, 18, 184, .3)',  # 阴影颜色
            'shadowBlur': 10,  # 阴影大小
            'shadowOffsetY': 10,  # Y轴方向阴影偏移
            'shadowOffsetX': 10,  # x轴方向阴影偏移
        }
    },
    tooltip_opts=opts.TooltipOpts(is_show=False)
)

line.set_global_opts(
    xaxis_opts=opts.AxisOpts(is_show=False, type_='category'),
    yaxis_opts=opts.AxisOpts(is_show=False, type_='value', max_=len(y_data)),
    title_opts=opts.TitleOpts(
        title="盘点2021年娱乐圈大事件", pos_left='center', pos_top='2%',
        subtitle="制图@微信公众号：关于数据分析与可视化",
        title_textstyle_opts=opts.TextStyleOpts(color='BlueViolet', font_size=20)
    ),
    graphic_opts=[
                opts.GraphicGroup(
                            graphic_item=opts.GraphicItem(id_='1',left="center", top="center", z=-1),
                            children=[# tokyo
                                    opts.GraphicImage(graphic_item=opts.GraphicItem(id_="logo",
                                                                                    left='center',
                                                                                    z=-1),
                                                      graphic_imagestyle_opts=opts.GraphicImageStyleOpts(
                                        image="https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fpic.veryhuo.com%2Fupload%2F20201225%2F4a356eba8cdc6b9029ba34d75e08653a.jpg&refer=http%3A%2F%2Fpic.veryhuo.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1642846074&t=af36ced6fff59e6336453380b0bb8344",
                                        width=800,
                                        height=600,
                                        opacity=0.1,)
                                    )])]
)


line.render("test_3.html")