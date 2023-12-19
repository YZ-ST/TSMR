from fastapi import Header, HTTPException

# 驗證Token
def verify_token(x_token: str = Header(...)):
    SECRET_TOKEN = "12345"  # 從配置文件或環境變數獲取
    # 403 Forbidden: 這個狀態碼表示伺服器理解請求但拒絕授權。它通常用於已經被伺服器接受的 token，但這個 token 沒有足夠的權限
    if x_token != SECRET_TOKEN:
        raise HTTPException(status_code=403, detail="token is not correct")
    return x_token
