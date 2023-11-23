from fastapi import APIRouter
from middleware.http_error import Unauthorized
from users.models.user import User
from users.utils.password import verify_password
from users.utils.token import get_access_token
from users.validators.login import LoginRequestFormat
import pyotp
from users.utils.send_email import send_email
from users.validators.register import OTPVerificationRequestFormat

router = APIRouter()


@router.post("", status_code=200)
async def login(request_body: LoginRequestFormat):

    request_data = request_body.dict()
    user = await User.Model.objects.find_user(email=request_data['email'])
    if not user or user['active'] == False:
        raise Unauthorized(message="User does not exist")
    
    plain_password = request_data['password']
    hashed_password = user['password']

    if await verify_password(plain_password, hashed_password):
        totp = pyotp.TOTP('3SLSWZPQQBB7WBRYDAQZ5J77W5D7I6GU')
        otp = totp.now()
        await User.Model.objects.update_user(request_data, otp)
        await send_email(request_data['email'], 'OTP Confirmation', f"Your otp is {otp}")
        # code to store token in db for single login
    else:
        raise Unauthorized(message="Incorrect password")
    
    return {
        "message": "Please check your email and verify otp"
    }


@router.put("", status_code=200)
async def login(request_body: OTPVerificationRequestFormat):

    request_data = request_body.dict()
    user = await User.Model.objects.find_user(email=request_data['email'])

    access_token = ''
    if request_data['otp'] == user['otp']:
        await User.Model.objects.update_user(request_data)
        access_token = await get_access_token(user)
    else:
        return {"message": "Invalid otp"}

    return {
        "token": access_token
    }
