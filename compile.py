# coding:utf-8
# 编译靶场平台的docker镜像
import os
CURRENT_DIR = os.getcwd()

for i in os.listdir("vuln"):
    try:
        with open(CURRENT_DIR + "/vuln/" + i + "/README.md", "r") as f:
            desc = eval(f.read())
        os.chdir(CURRENT_DIR + "/vuln/" + i)
        os.system("docker build -t {0} .".format(desc["image"]))
        # 编译依赖的镜像
        if "depends" in desc.keys():
            with open(CURRENT_DIR + "/vuln/{0}/{1}/{1}.json".format(i, desc["depends"]), "r") as f:
                dependsdesc = eval(f.read())
            os.chdir(CURRENT_DIR + "/vuln/{0}/{1}/".format(i, desc["depends"]))
            os.system("docker build -t {0} .".format(dependsdesc["image"]))
    except Exception as e:
        import traceback
        traceback.print_exc()
