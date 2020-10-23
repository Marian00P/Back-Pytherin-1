from pony.orm import db_session, select
from api.models.base import db


async def check_email_status(email: str):
    with db_session:
        try:
            email_confirmed = db.get(
                "select email_confirmed from DB_User where email = $email")
            return email_confirmed
        except BaseException:
            return None
