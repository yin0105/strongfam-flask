import json, re, time




def test_main_route_status_code(client) -> None:
    route = "/"
    rv = client.get(route)
    assert rv.status_code == 200


# def test_route_status_code_joinin(client, captured_templates) -> None:
#     route = "/joinin/"
#     rv = client.get(route)

#     assert rv.status_code == 200
#     assert len(captured_templates) == 1
#     template, context = captured_templates[0]
#     assert template.name == "joinin.html"
#     assert len(context["subjects_list"]) > 0


# def test_route_status_code_contactus(client, captured_templates) -> None:
#     route = "/contactus/"
#     rv = client.get(route)

#     assert rv.status_code == 200
#     assert len(captured_templates) == 1
#     template, context = captured_templates[0]
#     assert template.name == "contactus.html"
#     assert len(context["subjects_list"]) > 0


# def test_route_status_code_send_message_joinin(client, captured_templates) -> None:
#     route = "/ajax/send-message"

#     rv = client.get('/joinin/')
#     m = re.search(b'(<input id="csrf_token" name="csrf_token" type="hidden" value=")([-A-Za-z.0-9]+)', rv.data)
#     token = m.group(2).decode("utf-8")

#     data = {
#         'subject': 'apkas',
#         'visname': 'John Smith',
#         'visemail': 'john@gmail.com',
#         'message': 'Hi, this is testing message',
#         'csrf_token': token
#     }

#     rv = client.post(route, data=data)
    
#     assert rv.status_code == 200
#     assert rv.status == '200 OK'
#     assert rv.json["status"] == 'success'


# def test_route_status_code_send_message_contactus(client, captured_templates) -> None:
#     time.sleep(2)
#     route = "/ajax/send-message"

#     rv = client.get('/contactus/')
#     m = re.search(b'(<input id="csrf_token" name="csrf_token" type="hidden" value=")([-A-Za-z.0-9]+)', rv.data)
#     token = m.group(2).decode("utf-8")

#     data = {
#         'subject': 'apkas',
#         'visname': 'John Smith',
#         'visemail': 'john@gmail.com',
#         'message': 'Hi, this is testing message',
#         'csrf_token': token
#     }

#     rv = client.post(route, data=data)
    
#     assert rv.status_code == 200
#     assert rv.status == '200 OK'
#     assert rv.json["status"] == 'success'

