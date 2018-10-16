tuboshu项目后端

## 安装依赖项

pip freeze > requirements.txt

## API

[

    "create_user": "api/userprofile/create/",

    "delete_user": "api/userprofile/edit/{user_id}/", method=delete

    "update_user": "api/userprofile/edit/{user_id}/", method=put

    "retrieve_user": "api/userprofile/edit/{user_id}/", method=get

    "user_list": "api/userprofile/list/",
    
    "update_profile": "api/userprofile/edit-profile/{user_id}/", method=put
    
    "retrieve_profile": "api/userprofile/edit-profile/{user_id}/", method=get
]
