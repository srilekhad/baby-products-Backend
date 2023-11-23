from fastapi import APIRouter
from middleware.http_error import Conflict, Unprocessable
from users.models.user import User
from users.utils.password import get_password_hash
from users.validators.register import RegisterRequestFormat, OTPVerificationRequestFormat
from users.utils.send_email import send_email
import pyotp

router = APIRouter()


@router.post("", status_code=200)
async def register(request_body: RegisterRequestFormat):

    request_data = request_body.dict()
    user_data = await User.Model.objects.find_user(email=request_data['email'])

    if user_data:
        raise Conflict()

    if request_data['password'] != request_data['reenteredPassword']:
        raise Unprocessable("Passwords don't match")

    request_data.pop('reenteredPassword')

    request_data['password'] = await get_password_hash(request_data['password'])

    totp = pyotp.TOTP('3SLSWZPQQBB7WBRYDAQZ5J77W5D7I6GU')
    otp = totp.now()

    await send_email(request_data['email'], 'OTP Confirmation', f"Your otp is {otp}")

    request_data['active'] = False
    request_data['otp'] = otp

    await User.Model.objects.add_user(request_data)

    return {'message': 'Please check your email and verify otp'}


@router.put("", status_code=201)
async def register(request_body: OTPVerificationRequestFormat):

    request_data = request_body.dict()

    user_data = await User.Model.objects.find_user(request_data['email'])

    if request_data['otp'] == user_data['otp']:
        await User.Model.objects.update_user(request_data)
    else:
        return {"message": "Invalid otp"}

    return {'message': 'user has been created'}
