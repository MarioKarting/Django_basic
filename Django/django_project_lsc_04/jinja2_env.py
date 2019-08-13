from jinja2 import Environment

def environment(**options):
    env = Environment(**options)#实例化jinja2环境

    env.filters["jinja_filter"] = jinja_filter
    return env




# 1.写函数
def jinja_filter(x):
    return x * 100
