import pdb
from fastapi import APIRouter
from controller.user import User

router = APIRouter()

router.post('/profile')(User.create_user_profile)
router.put('/profile')(User.update_user_profile)
# router.delete('/profile')(user.delete_user_profile)
router.get('/profile')(User.get_user_profile)
# router.get('/list')(user.get_user_list)

