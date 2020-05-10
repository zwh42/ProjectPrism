#!/usr/bin/env python
#! -*- coding: utf-8 -*-
from flask import Flask, request, render_template

from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.commons.utils import JsCode
from pyecharts.globals import ThemeType

app = Flask(__name__)


@app.route("/")
def main_page():
    return render_template("home/insight.html", bar_chart = bar_chart())


@app.route("/notebook")
def notebook_page():
    
    notebook_path = "http://localhost:8889/notebooks/analysis.ipynb"
    return render_template("home/notebook.html", notebook_path = notebook_path)


def bar_chart():
    list2 = [
        {"value": 12, "percent": 12 / (12 + 3)},
        {"value": 23, "percent": 23 / (23 + 21)},
        {"value": 33, "percent": 33 / (33 + 5)},
        {"value": 3, "percent": 3 / (3 + 52)},
        {"value": 33, "percent": 33 / (33 + 43)},
    ]

    list3 = [
        {"value": 3, "percent": 3 / (12 + 3)},
        {"value": 21, "percent": 21 / (23 + 21)},
        {"value": 5, "percent": 5 / (33 + 5)},
        {"value": 52, "percent": 52 / (3 + 52)},
        {"value": 43, "percent": 43 / (33 + 43)},
    ]

    return (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
        .add_xaxis([1, 2, 3, 4, 5])
        .add_yaxis("product1", list2, stack="stack1", category_gap="50%")
        .add_yaxis("product2", list3, stack="stack1", category_gap="50%")
        .set_series_opts(
            label_opts=opts.LabelOpts(
                position="right",
                formatter=JsCode(
                    "function(x){return Number(x.data.percent * 100).toFixed() + '%';}"
                ),
            )
        )).render_embed()


if __name__ == "__main__":
    app.run(debug=True)