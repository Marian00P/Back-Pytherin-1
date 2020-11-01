from fastapi import HTTPException
from api.handlers.authentication import *

from classes.room import RoomStatus,Room
from classes.room_hub import RoomHub


def check_game_preconditions(email : str, room_name : str, hub : RoomHub):
    room : Room = hub.get_room_by_name(room_name)
    if room is None:
        raise HTTPException(
            status_code=404, detail="Room not found")
    elif email not in (room.get_user_list()):
        raise HTTPException(
            status_code=403, detail="You're not in this room")
    elif room.status == RoomStatus.PREGAME:
        raise HTTPException(
            status_code=409, detail="The game hasn't started yet")
    elif room.status == RoomStatus.FINISHED:
        raise HTTPException(
            status_code=409, detail="The game is over")
    return room