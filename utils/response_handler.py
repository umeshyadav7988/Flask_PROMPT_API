def success_response(data):
    return {"status": "success", "data": data}, 200

def error_response(message, code=400):
    return {"status": "error", "message": message}, code
