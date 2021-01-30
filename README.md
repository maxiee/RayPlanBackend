# RayPlanBackend

RayPlan 是一款个人管理系统。 RayPlanBackend 是这个系统的后端部分，是一个 RESTful API 服务器。


# 文档

## 项目（Project）

项目表示一件要做的复杂事情，需要通过任务拆分才能够完成。

模型：

|名称|类型|说明|
|---|---|---|
|id |主键|唯一标识|
|name |String|任务名称|
|description |String|任务描述|
|status |String|todo 待开始，doing 进行中，finish 已完成，changed 变更|
|start|date|开始日期|
|deadline|date|截止日期|
|created |datetime|创建时间|
|updated |datetime|更新时间|

## 任务（Task）

任务表示一件要做的事情。是最小粒度的行动，不可拆分。

模型：

|名称|类型|说明|
|---|---|---|
|id |主键|唯一标识|
|name |String|任务名称|
|description |String|任务描述|
|status |String|todo 待开始，doing 进行中，finish 已完成，changed 变更|
|dependency|oneToMany|依赖其他任务|
|created |datetime|创建时间|
|updated |datetime|更新时间|



