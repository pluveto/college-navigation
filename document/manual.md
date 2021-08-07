# 用户手册

## 1 运行系统

Windows 系统

## 2 运行环境

安装.NET Core Runtime 3.1

安装地址：<https://dotnet.microsoft.com/download>

安装vcpkg，指南：<https://github.com/microsoft/vcpkg> 

使用vcpkg安装[jsoncpp](https://github.com/open-source-parsers/jsoncpp)和[restbed](https://github.com/Corvusoft/restbed)包

修改CMakeLists.txt.sample中这两项的路径的前缀为vcpkg的安装路径，并且去除.sample后缀

```
set(INC_DIR ~/vcpkg/installed/x64-osx/include)
set(LINK_DIR ~/vcpkg/installed/x64-osx/lib)

```

之后进入后端目录，运行如下命令

```
mkdir build
cd build
cmake ..
make

```

将数据文件拷贝到build目录内，之后即可运行后端

## 3 运行方法

进入`run`文件夹，双击`WpfNavigation.exe`运行

# 操作手册

## 1 系统介绍

本系统为具有查询导航功能的校园导览系统，用户登录后可以于某一时刻向系统提出导航要求，系统根据要求为其设计一条线路并输出；系统能查询当前时刻用户所处的地点和周围的建筑物等信息。

## 2 操作说明

1. 输入用户名：zzj

   输入密码：111111

   点击登录

![image-20210604154646993](https://gitee.com/sg2019/picgo/raw/master/20210604154647.png)

1. 点击选点后点击地图选点，支持拖动地图。

   ![image-20210604154828164](https://gitee.com/sg2019/picgo/raw/master/20210604154828.png)

   可以在右边栏通过点击选择移动方式、跨校区策略、出发时间和寻路策略。

   可以调节速度倍率和时间流逝，输入步行速度和骑行速度。

   ![image-20210604230331073](https://gitee.com/sg2019/picgo/raw/master/20210604230331.png)

   点击查看路径，显示导航路径。

   可以选择多个途经点，会按照选择途经点的顺序，进行距离优先或者时间有限的导航。

   ![image-20210604230719752](https://gitee.com/sg2019/picgo/raw/master/20210604230719.png)

   点击开始模拟，开始从起始点移动，模拟导航过程。

   ![image-20210604230417283](https://gitee.com/sg2019/picgo/raw/master/20210604230417.png)

   开始模拟后，可以点击暂停。

2. 设置自行车道路导航，并可以设置步行和骑车速度。

   ![image-20210604141722047](https://gitee.com/sg2019/picgo/raw/master/20210604141722.png)

3. 可以跨校区导航，在上方选择不同地图即可，预估时间根据出发时间和跨校区策略而定。

   ![image-20210604143550160](https://gitee.com/sg2019/picgo/raw/master/20210604143550.png)

   ![image-20210604143513159](https://gitee.com/sg2019/picgo/raw/master/20210604143513.png)

4. 可以输入搜索半径，得到附近建筑物搜索结果

   ![image-20210604141546806](https://gitee.com/sg2019/picgo/raw/master/20210604141546.png)

5. 可以搜索逻辑位置，定位到教室

   ![image-20210604144103379](https://gitee.com/sg2019/picgo/raw/master/20210604144103.png)

   输入“食堂”，可以获得由负载均衡算法得出的最优食堂。

6. 可以导航到建筑物内部，并模拟进入建筑物内部

   ![image-20210604144243963](https://gitee.com/sg2019/picgo/raw/master/20210604144244.png)

   ![image-20210604144307554](https://gitee.com/sg2019/picgo/raw/master/20210604144307.png)

# 开发者手册

## 后端

* 通过CMakeList安装依赖
* 依赖库可以通过vcpkg安装管理

## 前端

* 目标框架为.NET Core 3.1


