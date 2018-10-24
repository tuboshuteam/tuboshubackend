tuboshu项目后端

## 安装依赖项

pip freeze > requirements.txt

## API

[

    "create_user": "api/userprofile/create/", method=post

    "delete_user": "api/userprofile/edit/{user_id}/", method=delete

    "update_user": "api/userprofile/edit/{user_id}/", method=put

    "retrieve_user": "api/userprofile/edit/{user_id}/", method=get

    "user_list": "api/userprofile/list/",
    
    
    
    "create_post": "api/post/create/", method=post
    
    "retrive_post": "api/post/edit/{post_id}/", method=get
    
    "delete_post": "api/post/edit/{post_id}/", method=delete

    "update_post": "api/post/edit/{post_id}/", method=put
    
    "post_list": "api/post/list/",
    
    
    
    "create_point": "api/point/create/", method=post
    
    "retrive_point": "api/point/edit/{point_id}/", method=get
    
    "delete_point": "api/point/edit/{point_id}/", method=delete

    "update_point": "api/point/edit/{point_id}/", method=put
    
    "point_list": "api/point/list/",
]
