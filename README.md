# 0、项目简介
实现使用开源的LangFlow框架，零代码实现大模型相关应用如流量包推荐智能客服、RAG应用等，并使用两种方式将创建的工作流集成到自己的项目中                                                   


# 1、基础概念
## 1.1 LangFlow简介  
官方介绍:一种用于构建多智能体和RAG应用的可视化框架                                 
GitHub地址:https://github.com/langflow-ai/langflow                           
开源协议:MIT协议                      


# 2、前期准备工作
## 2.1 anaconda、pycharm 安装   
anaconda:提供python虚拟环境，官网下载对应系统版本的安装包安装即可              
pycharm:提供集成开发环境，官网下载社区版本安装包安装即可            
可参考如下视频进行安装：                                          
https://www.bilibili.com/video/BV1q9HxeEEtT/?vd_source=30acb5331e4f5739ebbad50f7cc6b949                                    
https://youtu.be/myVgyitFzrA                                                             

## 2.2 非GPT大模型(国产大模型)使用方案，OneAPI安装、部署、创建渠道和令牌 
### （1）OneAPI是什么
官方介绍：是OpenAI接口的管理、分发系统             
支持 Azure、Anthropic Claude、Google PaLM 2 & Gemini、智谱 ChatGLM、百度文心一言、讯飞星火认知、阿里通义千问、360 智脑以及腾讯混元             
### (2)安装、部署、创建渠道和令牌   
创建渠道：大模型类型(通义千问)、APIKey(通义千问申请的真实有效的APIKey)                 
创建令牌：创建OneAPI的APIKey，后续代码中直接调用此APIKey                
### (3)详细介绍可以观看这期视频 
【GraphRAG+阿里通义千问大模型】构建+检索全流程实操，打造基于知识图谱的本地知识库，本地搜索、全局搜索二合一          
https://www.bilibili.com/video/BV1yzHxeZEG5/?vd_source=30acb5331e4f5739ebbad50f7cc6b949            
https://youtu.be/w9CRDbafhPI                 

## 2.3 GPT大模型使用方案            
可以使用代理的方式，具体代理方案自己选择                          
可以参考视频《GraphRAG最新版本0.3.0对比实战评测-使用gpt-4o-mini和qwen-plus分别构建近2万字文本知识索引+本地/全局检索对比测试》中推荐的方式：                      
https://www.bilibili.com/video/BV1zkWse9Enb/?vd_source=30acb5331e4f5739ebbad50f7cc6b949                           
                            

# 3、项目初始化
## 3.1 下载源码
GitHub中下载工程文件到本地，下载地址如下：                
https://github.com/NanGePlus/LangFlowTest          
https://gitee.com/NanGePlus/LangFlowTest   

## 3.2 构建项目
使用pycharm构建一个项目，为项目配置虚拟python环境               
项目名称：LangFlowTest                 

## 3.3 将相关代码拷贝到项目工程中           
直接将下载的文件夹中的文件拷贝到新建的项目目录中               

## 3.4 安装项目依赖          
pip install -r requirements.txt            
每个软件包后面都指定了本次视频测试中固定的版本号           

# 4、项目测试          
## 4.1 基础案例:推荐流量包的智能客服测试
### (1)使用LangFlow搭建推荐流量包的智能客服工作流
首先，在终端命令行中启动LangFlow服务，执行 langflow run 命令启动                   
启动成功后，登陆http://127.0.0.1:7860，在服务页面进入store菜单中创建API Key                            
最后进入My Collectio菜单中新建工程进行工作流编排，测试没问题后，导出工作流json文件                     

### （2）通过调用API接口方式使用创建的工作流
进入chatTest文件夹下，在使用python fromApiTest.py命令启动脚本前，需根据自己的实际情况调整代码中的如下参数：                        
**模型相关配置 根据自己的实际情况进行调整:**                            

### （3）通过调用工作流的json文件使用工作流
进入chatTest文件夹下，在使用python fromJsonTest.py命令启动脚本前，需根据自己的实际情况调整代码中的如下参数：                             
**模型相关配置 根据自己的实际情况进行调整:**           
**引入LangFlow的json文件**            
