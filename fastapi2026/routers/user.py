from fastapi import APIRouter

router = APIRouter(
    prefix="/users",
    tags=["用户管理"]
)

# 定义用户相关路由
@router.get("/")
def get_all_users():
    return {"message": "获取所有用户列表"}

@router.get("/{user_id}")
def get_user(user_id: int):
    return {"message": f"获取ID 为 {user_id} 的用户信息"}

