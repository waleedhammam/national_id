import json
from json.decoder import JSONDecodeError

from bottle import Bottle, HTTPResponse, request, run

from lib.national_id import NationalID

app = Bottle()


@app.route("/get_info", method="POST")
def get_info():
    """Get info method is an endpoint for validating and extracting information
    from the egyptian national id. It expects data to be {"id_number": "<your_id_number"}

    Returns:
        HTTPResponse: - 200 OK, json_info: national id is validated and info extraction ok
                      - 400 Bad Request: Wrong national id number
                      - 500 Internal Server Error: Invalid request from user
    """
    request_body = request.body.read()

    try:
        request_data = json.loads(request_body)
        national_id_number = request_data["id_number"]
    except (JSONDecodeError, KeyError) as e:
        json_error_msg = f"Error parsing input data:\n{str(e)}"
        return HTTPResponse({"error": json_error_msg}, status=500, headers={"Content-Type": "application/json"},)

    national_id_object = NationalID(national_id_number)

    is_valid_id, national_id_information = national_id_object.get_info()

    if is_valid_id:
        return HTTPResponse(
            {"nationl_id_data": national_id_information}, status=200, headers={"Content-Type": "application/json"},
        )
    else:
        return HTTPResponse(national_id_information, status=400, headers={"Content-Type": "application/json"},)


if __name__ == "__main__":
    run(app, host="0.0.0.0", port=8001)

