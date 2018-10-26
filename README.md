tuboshu项目后端

## 安装依赖项

pip freeze > requirements.txt

## API

##### "create_user": "api/userprofile/create/", method=post

```json
{
    "username": "xxx",  // 用户名不能重复
    "password": "xxxxxx"  // 至少6位
}
```

##### "delete_user": "api/userprofile/edit/{user_id}/", method=delete

```json
{
}
```

##### "update_user": "api/userprofile/edit/{user_id}/", method=put

```json
{
    "email": "test@gmail.com",
    "password": "xxxxxx",
    "profile": {
        "phone": "12345678900",  // 11位
        "gender": "男/女",
        "birthday": 100000000,  // long型
        "address": "成都",
        "avatar": "",  // 未完成
        "bio": "xxx",
        "tags": "xxx"  // 未完成
    }
}
```

##### "retrieve_user": "api/userprofile/edit/{user_id}/", method=get

```json
{
}
```

##### "user_list": "api/userprofile/list/",

```json
{
}
```

##### "create_post": "api/post/create/", method=post

```json
{
    "title": "xxx",
    "content": "xxx",
    // ...
    "point": [
            {
                "longitude": 10,
                "latitude": 10,
                "travel_date_time": 1000000,
                // ...
            },
            {
                "longitude": 10,
                "latitude": 10,
                "travel_date_time": 1000000
                // ...
            }
        ]
}
```

##### "retrive_post": "api/post/edit/{post_id}/", method=get

```json
{
}
```

##### "delete_post": "api/post/edit/{post_id}/", method=delete

```json
{
}
```

##### "update_post": "api/post/edit/{post_id}/", method=put

```json
{
    "title": "xxx",
    "content": "xxx",
    // ...
    "point": [
            // 创建新Point
            {
                "method": "create",
                "longitude": 10,
                "latitude": 10,
                "travel_date_time": 1000000,
                // ...
            },
            // 删除id为"id"的Point
            {
                "method": "delete",
                "id": 10,
            },
            // 更新id为"id"的Point
            {
                "method": "update",
                "id": 10,
                "longitude": 10,
                "latitude": 10,
                "travel_date_time": 1000000,
                // ...
            }
        ]
}
```

##### "post_list": "api/post/list/",

```json
{
}
```

##### "create_point": "api/point/create/", method=post

```json
{
    "longitude": 10,
    "latitude": 10,
    "travel_date_time": 1000000
    // ...
}
```

##### "retrive_point": "api/point/edit/{point_id}/", method=get

```json
{
}
```

##### "delete_point": "api/point/edit/{point_id}/", method=delete

```json
{
}
```

##### "update_point": "api/point/edit/{point_id}/", method=put

```json
{
    "longitude": 10,
    "latitude": 10,
    "travel_date_time": 1000000
    // ...
}
```

##### "point_list": "api/point/list/",

```json
{
}
```

"create_comment": "api/comment/create/", method=post

```json
{
    "post": 1,
    "content": "xxx"
}
```

"retrive_comment": "api/comment/edit/{comment_id}/", method=get

```json
{
}
```

"delete_comment": "api/comment/edit/{comment_id}/", method=delete

```json
{
}
```

"update_comment": "api/comment/edit/{comment_id}/", method=put

```json
{
    "content": "xxx"
}
```

"comment_list": "api/comment/list/",

```json
{
}
```

