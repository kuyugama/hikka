from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, desc, func
from datetime import datetime, timedelta

from app.models import (
    Activity,
    History,
    User,
)


async def get_user_history_count(session: AsyncSession, user: User) -> int:
    return await session.scalar(
        select(func.count(History.id)).filter(History.user == user)
    )


async def get_user_history(
    session: AsyncSession, user: User, limit: int, offset: int
) -> User:
    """Get user history"""

    return await session.scalars(
        select(History)
        .filter(History.user == user)
        .order_by(desc(History.updated), desc(History.created))
        .limit(limit)
        .offset(offset)
    )


async def get_user_activity(session: AsyncSession, user: User) -> User:
    """Get user activity"""

    end = datetime.utcnow()
    start = end - timedelta(weeks=16)

    return await session.scalars(
        select(Activity)
        .filter(
            Activity.user == user,
            Activity.timestamp >= start,
            Activity.timestamp <= end,
        )
        .order_by(desc(Activity.timestamp))
    )
