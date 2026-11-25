from plotly.offline import get_plotlyjs

with open("plotly-head.html", "w", encoding="utf-8") as f:
    f.write("<script>" + get_plotlyjs() + "</script>")