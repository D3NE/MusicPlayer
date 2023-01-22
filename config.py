"""
Music Player, Telegram Voice Chat Bot
Copyright (c) 2021-present Asm Safone <https://github.com/AsmSafone>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""

import os
from dotenv import load_dotenv


load_dotenv()


class Config:
    def __init__(self) -> None:)
        self.API_ID: str = os.environ.get("API_ID", 29699592)
        self.API_HASH: str = os.environ.get("API_HASH", 36c5d87a0d72b145a014b89def282cbd)
        self.SESSION: str = os.environ.get("SESSION", AgHFLggAPgoxyFOT734qw3Xqxt2GJGYAdsTQ_pn82BhDzEdv2jXytxKS4t6zwEJ7kMKNmFJvQft3qoNQyeaRy62CXRgjE-DSeUogaHf2S2ZfccjpBo6gwiiFL-P_UTaob6WTHIQ-Z2gFYvASkPmaNXZQ2AVigVTaF3M-kg9quaqQheHtBzm9HBsQj0vxGxjFbFhMZ3Q1tXIouj1RDxGf7hCbH8z-fiYVulnymkZmV9eqBbiVZvIHjPQ6Pl6CuwMe5PrtL1s9UJY86xRB2lgVuMTe2FkYRH9L-m9QE1h5ubVOYEtT4ihvslOY0QsHF1ROqVG9e6EUY9Z1f59aZUr6ZiydT54e8wAAAAFR9ZgzAA)
        self.BOT_TOKEN: str = os.environ.get("BOT_TOKEN", 5837427920:AAEHQ8DYhGiTusz2rpz6s_T6BlD9lJKQZ4M)
        self.SUDOERS: list = [
            int(id) for id in os.environ.get("SUDOERS", "5670017075").split() if id.isnumeric()
        ]
        if not self.SESSION or not self.API_ID or not self.API_HASH:
            print("ERROR: SESSION, API_ID and API_HASH is required!")
            quit(0)
        self.SPOTIFY: bool = False
        self.QUALITY: str = os.environ.get("QUALITY", "high").lower()
        self.PREFIXES: list = os.environ.get("PREFIX", "!").split()
        self.LANGUAGE: str = os.environ.get("LANGUAGE", "en").lower()
        self.STREAM_MODE: str = (
            "audio"
            if (os.environ.get("STREAM_MODE", "audio").lower() == "audio")
            else "video"
        )
        self.ADMINS_ONLY: bool = os.environ.get("ADMINS_ONLY", False)
        self.SPOTIFY_CLIENT_ID: str = os.environ.get("SPOTIFY_CLIENT_ID", None)
        self.SPOTIFY_CLIENT_SECRET: str = os.environ.get("SPOTIFY_CLIENT_SECRET", None)


config = Config()
