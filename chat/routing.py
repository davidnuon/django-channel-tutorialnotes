from channels.routing import route

channel_routing = [
    route("http.request", "chat.consumers.http_consumer"),
    route("websocket.receive", "chat.consumers.ws_message"),
    route("websocket.connect", "chat.consumers.ws_add"),
    route("websocket.disconnect", "chat.consumers.ws_disconnect")
]