from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from .schemas import ORJSONModel
from fastapi import Request
from pydantic import Field


class ErrorResponse(ORJSONModel):
    message: str = Field(example="Example error message")
    code: str = Field(example="example_error")


errors = {
    "auth": {
        "username-required": ["Username is required to do that action", 400],
        "activation-valid": ["Previous activation token still valid", 400],
        "reset-valid": ["Previous password reset token still valid", 400],
        "email-required": ["Email is required to do that action", 400],
        "email-exists": ["User with that email already exists", 400],
        "activation-expired": ["Activation token has expired", 400],
        "activation-invalid": ["Activation token is invalid", 400],
        "oauth-code-required": ["OAuth code required", 400],
        "invalid-provider": ["Invalid OAuth provider", 400],
        "invalid-code": ["Invalid OAuth code", 400],
        "username-taken": ["Username already taken", 400],
        "reset-expired": ["Reset token has expired", 400],
        "reset-invalid": ["Reset token is invalid", 400],
        "already-activated": ["Already activated", 400],
        "invalid-token": ["Auth token is invalid", 400],
        "invalid-password": ["Invalid password", 400],
        "username-set": ["Username already set", 400],
        "not-activated": ["User not activated", 400],
        "token-expired": ["Token has expired", 400],
        "oauth-error": ["Error during OAuth", 400],
        "user-not-found": ["User not found", 404],
        "email-set": ["Email already set", 400],
        "banned": ["Banned", 403],
    },
    "permission": {
        "missing": ["You don't have permission for this action", 401],
    },
    "anime": {
        "no-franchise": ["This anime doesn't have franchise", 400],
        "unknown-producer": ["Unknown producer", 400],
        "unknown-studio": ["Unknown studio", 400],
        "bad-year": ["Invalid years passed", 400],
        "unknown-genre": ["Unknown genre", 400],
        "not-found": ["Anime not found", 404],
    },
    "studio": {
        "not-found": ["Studio not found", 404],
    },
    "genre": {
        "not-found": ["Genre not found", 404],
    },
    "watch": {
        "bad-episodes": ["Bad episodes number provided", 400],
        "not-found": ["Watch record not found", 404],
    },
    "favourite": {
        "exists": ["Favourite record for this anime already exists", 400],
        "not-found": ["Favourite record not found", 404],
    },
    "captcha": {
        "invalid": ["Failed to validate captcha", 401],
    },
    "user": {
        "not-found": ["User not found", 404],
    },
    "follow": {
        "already-following": ["This user is already followed", 400],
        "not-following": ["This user is not followed", 400],
        "invalid-action": ["Invalid action", 401],
        "self": ["Can't follow self", 400],
    },
    "search": {
        "query-down": ["Search by query unavailable at the moment", 400],
    },
    "company": {
        "not-found": ["Company not found", 404],
    },
    "character": {
        "not-found": ["Character not found", 404],
    },
    "person": {
        "not-found": ["Person not found", 404],
    },
}


class Abort(Exception):
    def __init__(self, scope: str, message: str):
        self.scope = scope
        self.message = message


def build_error_code(scope: str, message: str):
    return scope.replace("-", "_") + "_" + message.replace("-", "_")


async def abort_handler(request: Request, exc: Abort):
    error_code = build_error_code(exc.scope, exc.message)

    try:
        error_message = errors[exc.scope][exc.message][0]
        status_code = errors[exc.scope][exc.message][1]
    except Exception:
        error_message = "Unknown error"
        status_code = 400

    return JSONResponse(
        content={"message": error_message, "code": error_code},
        status_code=status_code,
    )


async def validation_handler(request: Request, exc: RequestValidationError):
    exc_str = str(exc).replace("\n", " ").replace("   ", " ")
    return JSONResponse(
        content={"message": exc_str, "code": "validation_error"},
        status_code=422,
    )
