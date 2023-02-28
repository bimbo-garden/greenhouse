# SPDX-FileCopyrightText: 2023 peepo.world developers
#
# SPDX-License-Identifier: EUPL-1.2

import contextlib

from typing import AsyncIterator

from starlette.applications import Starlette
from starlette.routing import Route, Mount
from starlette.staticfiles import StaticFiles

import greenhouse.web

from greenhouse.web import db, routes


@contextlib.asynccontextmanager
async def lifespan(app) -> AsyncIterator[None]:
    async with db.lifespan(app):
        yield



app = Starlette(
    debug=greenhouse.web.DEBUG,
    routes=[
        Route('/', routes.homepage),
        Route('/dashboard', routes.dashboard),
        Route('/top-emotes', routes.top_emotes),
        Mount('/static', StaticFiles(directory='greenhouse/web/static'), name='static')
    ],
    lifespan=lifespan,
)
