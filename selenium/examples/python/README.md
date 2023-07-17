```
cd examples/python

#创建虚拟环境
python3 -m venv ./venv

#激活虚拟环境
source ./venv/bin/activate

#安装依赖
pip install -r requirements.txt

#执行
python3 tests/save_screenshot.py

#最后，退出虚拟环境
deactivate
```