import json, re, time


def test_main_route_status_code(client) -> None:
    route = "/"
    rv = client.get(route)
    assert rv.status_code == 200


def test_route_status_code_joinin(client, captured_templates) -> None:
    route = "/joinin/"
    rv = client.get(route)

    assert rv.status_code == 200
    assert len(captured_templates) == 1
    template, context = captured_templates[0]
    assert template.name == "joinin.html"
    assert len(context["subjects_list"]) > 0


def test_route_status_code_contactus(client, captured_templates) -> None:
    route = "/contactus/"
    rv = client.get(route)

    assert rv.status_code == 200
    assert len(captured_templates) == 1
    template, context = captured_templates[0]
    assert template.name == "contactus.html"
    assert len(context["subjects_list"]) > 0

