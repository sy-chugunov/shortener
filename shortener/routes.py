def setup_routes(app, handler):
    router = app.router
    router.add_get("/{short_id}", handler.redirect, name="redirect")
    router.add_post("/shortify", handler.shortify, name="shortify")
    router.add_delete("/{short_id}", handler.remove, name="remove")
