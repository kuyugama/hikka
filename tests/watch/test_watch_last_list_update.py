from client_requests import request_watch_delete
from client_requests import request_watch_add
from client_requests import request_me
from fastapi import status


async def test_watch_delete(
    client,
    create_test_user,
    aggregator_anime,
    get_test_token,
):
    # For new user last_list_update field is empty
    response = await request_me(client, get_test_token)
    assert response.json()["last_list_update"] is None

    # Add anime to watch list
    await request_watch_add(
        client,
        "bocchi-the-rock-9e172d",
        get_test_token,
        {
            "status": "watching",
            "note": "Test",
            "episodes": 10,
            "score": 8,
        },
    )

    # After adding something to list this field should be updated
    response = await request_me(client, get_test_token)
    assert isinstance(response.json()["last_list_update"], int)

    old_last_list_update = response.json()["last_list_update"]

    # Now remove anime from watch list
    response = await request_watch_delete(
        client, "bocchi-the-rock-9e172d", get_test_token
    )

    # After deleting entry from list it should be updated again
    response = await request_me(client, get_test_token)
    assert isinstance(response.json()["last_list_update"], int)
    assert response.json()["last_list_update"] >= old_last_list_update
